---
id: go-installation
title: Scope Go Agent instructions
sidebar_label: Installation
---


Installation of the Scope Go agent is done via `go get`:

```bash
go get -u go.undefinedlabs.com/scopeagent
```

## Instrumenting your tests and benchmarks

In order to instrument your tests that use Go's native [`testing`](https://golang.org/pkg/testing/) package, you
have to import `go.undefinedlabs.com/scopeagent/autoinstrument` and all tests and benchmarks in the package will be automatically instrumented through monkey patching.

For example:

```go
import (
    "testing"

    _ "go.undefinedlabs.com/scopeagent/autoinstrument"
)

func TestExample(t *testing.T) {
    // ...
}

func BenchmarkExample(b *testing.B) {
    // ...
}
```

The automatic test instrumentation by imports is achieved using monkey patching. As an alternative, you can call `scopeagent.Run(m)` in your `TestMain` function.

For example:

```go
import (
    "os"
    "testing"

    "go.undefinedlabs.com/scopeagent"
)

func TestMain(m *testing.M) {
    os.Exit(scopeagent.Run(m))
}

func TestExample(t *testing.T) {
    // ...
}

func BenchmarkExample(b *testing.B) {
    // ...
}
```

Note that after this, you can use `scopeagent.GetContextFromTest(t)` to refer to the context of the running test, which has information
about its trace. Use it when you make any external calls, and if you add any custom OpenTracing instrumentation.

Instrumentation for client libraries is done manually. Please check the different sections on the left for more information.

### Instrumenting subtests

Subtests instrumentation is not automatic and it's done by replacing the standard `t.Run` call with the Scope Go agent `test.Run` function, for example:

```go
import (
    "testing"

    "go.undefinedlabs.com/scopeagent"
    _ "go.undefinedlabs.com/scopeagent/autoinstrument"
)

func TestExample(t *testing.T) {
    test := scopeagent.GetTest(t)   // Gets the Scope Go agent representation of test `t`
    test.Run("Sub Test", func(t *testing.T) {
      // ...
    })
    
    // ...	
}
```

## Instrumenting sub benchmarks

Sub benchmarks instrumentation is not automatic and it's done by replacing the standard `b.Run` call with the Scope Go agent `bench.Run` function, for example:

```go
import (
    "testing"

    "go.undefinedlabs.com/scopeagent"
    _ "go.undefinedlabs.com/scopeagent/autoinstrument"
)

func BenchmarkExample(b *testing.B) {
    bench := scopeagent.GetBenchmark(b) // Gets the Scope Go agent representation of benchmark `b`
    bench.Run("Sub Benchmark", func(b *testing.B) {
      // ...
    })
    
    // ...	
}
```


## Runtime instrumentation

In order to install the agent in a runtime process (CLI or server), create an `Agent` instance and make
sure it is stopped cleanly before exiting (in order to flush any pending buffers). For example:

```go
import (
    "go.undefinedlabs.com/scopeagent/agent"
)

func main() {
    scopeAgent, err := agent.NewAgent()
    if err != nil {
        panic(err)
    }
    defer scopeAgent.Stop()

    // ...
}
```

The agent will be automatically configured if the API key was provided via [environment variables](#environment-variables),
or if used locally with _Scope for Mac_ or _Scope for Windows_ installed. Otherwise, you can use the 
[`agent.WithApiKey()`](https://godoc.org/go.undefinedlabs.com/scopeagent/agent#WithApiKey) option
to configure it manually.

The agent will also try to automatically detect git information (repository URL, commit hash and source root path) using
[environment variables](#environment-variables) and the local `.git` folder if available. Otherwise, you can use the 
[`agent.WithGitInfo()`](https://godoc.org/go.undefinedlabs.com/scopeagent/agent#WithGitInfo) option
to configure it manually, for example, if you embed this information in the resulting binary at build time.

Refer to the [`scopeagent` package documentation](https://godoc.org/go.undefinedlabs.com/scopeagent/agent)
for the full list of options available to programmatically configure the agent.

Instrumentation for server and client libraries is done manually. Please check the different sections on the left for more information.


## Custom OpenTracing instrumentation

You can use [OpenTracing's Go API](https://github.com/opentracing/opentracing-go/blob/master/README.md) to add your
own custom spans and events to your code. Always make sure to use a `context.Context` object that comes from Scope's 
instrumentation to extend the traces created by `scopeagent.StartTest`.

In order to capture your custom instrumentation, Scope's agent has to be registered as OpenTracing's global tracer.
There are two options to do this: set the environment variable `SCOPE_SET_GLOBAL_TRACER=true`,
or in code passing the option `WithSetGlobalTracer()`, like in the following example:

```go
import (
    "github.com/opentracing/opentracing-go"

    "go.undefinedlabs.com/scopeagent"
)

func main() {
    scopeAgent, err := agent.NewAgent(agent.WithSetGlobalTracer())
    if err != nil {
        panic(err)
    }
    defer scopeAgent.Stop()

    // ...
}
```

> Note that at the moment it's only possible to register _one_ tracer as global tracer at any given time.

## Environment variables

The following environment variables need to be configured when instrumenting your tests or application:

| Environment variable | Testing mode | Runtime mode | Autodetected |
| -------------------- | ------------ | ------------ | :----------: |
| `SCOPE_DSN`          | Required     | Required     |      ✗       |
| `SCOPE_COMMIT_SHA`   | Required     | Optional     |      ✓       |
| `SCOPE_REPOSITORY`   | Required     | Optional     |      ✓       |
| `SCOPE_SOURCE_ROOT`  | Required     | Optional     |      ✓       |


### SCOPE_DSN

**This is a required setting**. If not set in testing mode, tests will run as usual and an error message pointing to the agent logs for troubleshooting will be printed before the process finishes. If not set in runtime mode, the instrumented process will be executed as usual, a warning message will be printed at the beginning of the execution and no spans will be reported.

`SCOPE_DSN` contains the Data Source Name with connection information about the Scope installation to report to. Specifically, it contains
the hostname of the Scope instance to report to, and the API key to be used for authentication. _`SCOPE_DSN` is considered a secret and should not be checked out in a repository._

Scope DSNs are generated per namespace. You can generate them by clicking on the `API Key` link of the namespace you want to report to in the Scope UI. If running locally using the native apps _Scope for Mac_ or _Scope for Windows_, the DSN will be automatically configured by reading it from `~/.scope/config.json`, which is autogenerated by the native app.

Example value: `https://cbfeff1f5fbf444086c728a096020cad@app.scope.dev/`

### SCOPE_COMMIT_SHA

This is a required setting in testing mode, and optional in runtime mode.

`SCOPE_COMMIT_SHA` contains the commit hash to be used when reporting to Scope.

If not explicitly set, the agent will try to automatically detect it using the following algorithm:

1. If the process is being executed inside a [supported CI provider](go-compatibility.md#ci-providers), it will try
   to read the commit hash from the environment variable set by the CI provider.
2. If not, it will try to extract the current commit from the local git information (if `.git/` is present).

Example value: `974c3566eb8e221d130db86a7ce1f99703fe2e69`

### SCOPE_REPOSITORY

This is a required setting in testing mode, and optional in runtime mode.

`SCOPE_REPOSITORY` contains the repository URL to be used when reporting to Scope.

If not explicitly set, the agent will try to automatically detect it using the following algorithm:

1. If the process is being executed inside a [supported CI provider](go-compatibility.md#ci-providers), it will try to read the repository URL from the environment variables set by the CI provider.
2. If not, it will try to extract the current `origin` remote URL from the local git information (if `.git/` is present).

Examples values: `https://github.com/undefinedlabs/scope-docs.git`, `git@github.com:undefinedlabs/scope-docs.git`

### SCOPE_SOURCE_ROOT

This is a required setting in testing mode, and optional in runtime mode.

`SCOPE_SOURCE_ROOT` contains the absolute path to where the root of the project is located inside the filesystem. This
information is used to automatically show excerpts of source code in the Scope UI in stacktraces, the "Code Path" tab and others.

If not explicitly set, the agent will try to automatically detect it using the following algorithm:

1. If the process is being executed inside a [supported CI provider](go-compatibility.md#ci-providers), it will try
   to read the source root from the environment variable set by the CI provider.
2. If not, it will try to extract the absolute path to the git repository using the local git information (if `.git/` is present).
3. If not, it will be set to the working directory of the command used to launch the application or tests.

Example value: `/home/user/projects/scope-docs`

## Running tests inside a container

If you are running your application or tests inside a container, forward the following environment variables to it so the agent can autodetect the build information. Note that the variables depend on your CI provider.

> Note that you might also need to set `SCOPE_SOURCE_ROOT` manually with the absolute path inside the container where the code is present if it cannot be autodetected by the agent.

<!--DOCUSAURUS_CODE_TABS-->
<!-- Jenkins -->

- `SCOPE_DSN`
- `JENKINS_URL`
- `GIT_URL`
- `GIT_COMMIT`
- `BUILD_ID`
- `BUILD_NUMBER`
- `BUILD_URL`

<!-- CircleCI -->

- `SCOPE_DSN`
- `CIRCLECI`
- `CIRCLE_REPOSITORY_URL`
- `CIRCLE_SHA1`
- `CIRCLE_BUILD_NUM`
- `CIRCLE_BUILD_URL`

<!-- GitLab CI -->

- `SCOPE_DSN`
- `GITLAB_CI`
- `CI_REPOSITORY_URL`
- `CI_COMMIT_SHA`
- `CI_JOB_ID`
- `CI_JOB_URL`

<!-- Travis -->

- `SCOPE_DSN`
- `TRAVIS`
- `TRAVIS_REPO_SLUG`
- `TRAVIS_COMMIT`
- `TRAVIS_BUILD_ID`
- `TRAVIS_BUILD_NUMBER`

<!-- AppVeyor -->

- `SCOPE_DSN`
- `APPVEYOR`
- `APPVEYOR_REPO_NAME`
- `APPVEYOR_REPO_COMMIT`
- `APPVEYOR_BUILD_ID`
- `APPVEYOR_BUILD_NUMBER`
- `APPVEYOR_PROJECT_SLUG`

<!-- Azure Pipelines -->

- `SCOPE_DSN`
- `TF_BUILD`
- `Build.Repository.Uri`
- `Build.SourceVersion`
- `Build.BuildId`
- `Build.BuildNumber`
- `System.TeamFoundationCollectionUri`
- `System.TeamProject`

<!-- Bitbucket Pipelines -->

- `SCOPE_DSN`
- `BITBUCKET_GIT_SSH_ORIGIN`
- `BITBUCKET_COMMIT`
- `BITBUCKET_BUILD_NUMBER`

<!-- GitHub Actions -->

- `SCOPE_DSN`
- `GITHUB_REPOSITORY`
- `GITHUB_SHA`

<!-- TeamCity -->

- `SCOPE_DSN`
- `TEAMCITY_VERSION`
- `BUILD_VCS_URL`
- `BUILD_CHECKOUTDIR`
- `BUILD_ID`
- `BUILD_NUMBER`
- `SERVER_URL`

<!-- Buildkite -->

- `SCOPE_DSN`
- `BUILDKITE`
- `BUILDKITE_REPO`
- `BUILDKITE_COMMIT`
- `BUILDKITE_BUILD_ID`
- `BUILDKITE_BUILD_NUMBER`
- `BUILDKITE_BUILD_URL`

<!--END_DOCUSAURUS_CODE_TABS-->

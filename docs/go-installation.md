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
have to call `scopeagent.Run(m)` in your `TestMain` function, and all tests and benchmarks in the package will be instrumented.

For example:

```go
import (
    "go.undefinedlabs.com/scopeagent"
    "testing"
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
    "go.undefinedlabs.com/scopeagent"
    "testing"
)

func TestMain(m *testing.M) {
    os.Exit(scopeagent.Run(m))
}

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
    "go.undefinedlabs.com/scopeagent"
    "testing"
)

func TestMain(m *testing.M) {
    os.Exit(scopeagent.Run(m))
}

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

| Environment variable  | Default value           | Description                                                       |
|-----------------------|-------------------------|-------------------------------------------------------------------|
| `$SCOPE_DSN`          |                         | Data source name (DSN) of Scope to be used when reporting results |
| `$SCOPE_COMMIT_SHA`   | Autodetected (2)        | Commit hash to use when sending data to Scope                     |
| `$SCOPE_REPOSITORY`   | Autodetected (2)        | Repository URL to use when sending data to Scope                  |
| `$SCOPE_SOURCE_ROOT`  | Autodetected (2)        | Repository root path                                              |

(1) Autodetection of the API key and endpoint is only done if the instrumented process is running on a machine with _Scope for Mac_
or _Scope for Windows_ installed and configured.

(2) Autodetection of git information works if either tests run on a [supported CI provider](go-compatibility.md#ci-providers),
or if the `.git` folder is present locally, and there is an `origin` remote configured pointing to the right repository.

The following optional parameters can also be configured:

| Environment variable | Default value    | Description                                      |
|----------------------|------------------|--------------------------------------------------|
| `$SCOPE_SERVICE`     | `default`        | Service name to use when sending data to Scope   |

The following environment variables are also available to modify the Scope Agent behavior.

| Environment variable  | Default | Description |
|---|---|---|
| `$SCOPE_SET_GLOBAL_TRACER` | `false` | Boolean flag to register `ScopeTracer` as OpenTracing's global tracer |
| `$SCOPE_TESTING_MODE` | Autodetected (*) | Boolean flag to indicate to `ScopeAgent` if it's running tests (`true`), or if it's being used for runtime instrumentation (`false`) |

(*) Autodetection of `$SCOPE_TESTING_MODE` property depends on whether the build has been triggered by a CI server (`true`), or not (`false`),
or if the tests are started using `scopeagent.Run()`.

If these properties are manually configured, they will be `true` only on encountering the string `true` configured on the environment variable. 
Any other value will be considered as `false`.

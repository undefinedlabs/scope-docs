---
id: go-installation
title: Scope Go Agent instructions
sidebar_label: Installation
---


Installation of the Scope Go agent is done via `go get`:

```bash
go get -u go.undefinedlabs.com/scopeagent
```

Importing the package will automatically install the Scope Agent and set it as the [OpenTracing's global tracer](https://github.com/opentracing/opentracing-go#singleton-initialization).


## Instrument your tests

In order to instrument your tests that use Go's native [`testing`](https://golang.org/pkg/testing/) package, you
have to follow these steps:

1. Write a `TestMain` function that calls `scopeagent.GlobalAgent.Run` before exiting (in order to make sure
that we flush any buffers cleanly).
2. Call `scopeagent.StartTest` at the beginning of each test, which will return a `scopeagent.Test` object, and call `test.End` before finishing the test.

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
    test := scopeagent.StartTest(t)
    defer test.End()

    // ...
}
```

Note that after this, you can use `test.Context()` to refer to the context of the running test, which has information
about the currently active span. This will allow the instrumentation to extend the test trace by adding child spans to it (i.e. when calling `opentracing.StartSpanFromContext`)

Check the [process instrumentation](go-process-instrumentation.md) if you plan to launch processes from your tests (for example, to test a CLI tool).

## Runtime instrumentation

In order to install the agent in a runtime process (CLI or server), just import the Scope Go agent package and make
sure it is stopped cleanly before exiting (in order to flush any pending buffers). For example:

```go
import (
    "go.undefinedlabs.com/scopeagent"
)

func main() {
    // Make sure we stop the agent cleanly, flushing the buffer before exiting
    defer scopeagent.Stop()

    // ...
}
```

Instrumentation for client and server libraries in Go is done manually. 
Please check the [HTTP instrumentation](go-http-instrumentation.md) and [gRPC instrumentation](go-grpc-instrumentation.md) 
articles for instructions on how to trace incoming and outgoing requests.


## Custom OpenTracing instrumentation

The agent is automatically installed and set as [OpenTracing's global tracer](https://github.com/opentracing/opentracing-go#singleton-initialization) when imported.

You can use [OpenTracing's Go API](https://github.com/opentracing/opentracing-go/blob/master/README.md) to add your
own custom spans and events to your code. Always make sure to use a `context.Context` object that comes from Scope's 
instrumentation to extend the traces created by `scopeagent.StartTest`.


## Environment variables

The following environment variables need to be configured when instrumenting your tests or application:

| Environment variable  | Default value           | Description                                            |
|-----------------------|-------------------------|--------------------------------------------------------|
| `$SCOPE_APIKEY`       |                         | API key to use when sending data to Scope              |
| `$SCOPE_API_ENDPOINT` | `https://app.scope.dev` | API endpoint of the Scope installation to send data to |
| `$SCOPE_COMMIT_SHA`   | Autodetected (*)        | Commit hash to use when sending data to Scope          |
| `$SCOPE_REPOSITORY`   | Autodetected (*)        | Repository URL to use when sending data to Scope       |
| `$SCOPE_SOURCE_ROOT`  | Autodetected (*)        | Repository root path                                   |

The following optional parameters can also be configured:

| Environment variable | Default value    | Description                                      |
|----------------------|------------------|--------------------------------------------------|
| `$SCOPE_SERVICE`     | `default`        | Service name to use when sending data to Scope   |

(*) Autodetection of git information works if either tests run on a [supported CI provider](go-compatibility.md#ci-providers),
or if the `.git` folder is present locally, and there is an `origin` remote configured pointing to the right repository.

The following environment variables are also available to modify the Scope Agent behavior.

| Environment variable  | Default | Description |
|---|---|---|
| `$SCOPE_AUTO_INSTRUMENT` | `true` | Boolean flag to apply Scope auto instrumentation |
| `$SCOPE_SET_GLOBAL_TRACER` | `true` | Boolean flag to register `ScopeTracer` as OpenTracing's global tracer |
| `$SCOPE_TESTING_MODE` | Autodetected (*) | Boolean flag to indicate to `ScopeAgent` if it's running tests (`true`), or if it's being used for runtime instrumentation (`false`) |

(*) Autodetection of `$SCOPE_TESTING_MODE` property depends on whether the build has been triggered by a CI server (`true`), or not (`false`).

If these properties are manually configured, they will be `true` only on encountering the string `true` configured on the environment variable. Any other value will be considered as `false`.

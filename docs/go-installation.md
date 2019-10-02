---
id: go-installation
title: Scope Go Agent instructions
sidebar_label: Installation
---


Installation of the Scope Go agent is done via `go get`:

```bash
go get -u go.undefinedlabs.com/scopeagent
```

## Instrumenting your tests

In order to instrument your tests that use Go's native [`testing`](https://golang.org/pkg/testing/) package, you
have to call `scopeagent.Run()` before exiting (to gracefully stop the agent),
and call `scopeagent.StartTest(t)` and `defer test.End()` on each test.

For example:

```go
import (
    "go.undefinedlabs.com/scopeagent"
    "testing"
)

func TestMain(m *testing.M) {
    // Make sure we gracefully stop the agent before exiting
    os.Exit(scopeagent.Run(m))
}

func TestExample(t *testing.T) {
    // Instrument the test `t`
    // The method `test.Context()` must be used to extend the trace
    // when creating new spans or when making external requests
    test := scopeagent.StartTest(t)
    defer test.End()

    // ...
}
```

Note that after this, you can use `test.Context()` to refer to the context of the running test, which has information
about its trace. Use it when you make any external calls, and if you add any custom OpenTracing instrumentation.

Check the [process instrumentation](go-process-instrumentation.md) if you plan to launch processes from your tests (for example, to test a CLI tool).

## Runtime instrumentation

In order to install the agent in a runtime process (CLI or server), just import the Scope Go agent package and make
sure it is stopped cleanly before exiting (in order to flush any pending buffers). For example:

```go
import (
    "go.undefinedlabs.com/scopeagent"
)

func main() {
    // Make sure we stop the agent cleanly before exiting
    defer scopeagent.Stop()

    // ...
}
```

The agent will be automatically installed and the instrumentation automatically configured if the API key was provided
via an environment variable, or if used locally with _Scope for Mac_ or _Scope for Windows_ installed. Otherwise, the autoinstallation
process will do nothing. Refer to [Manual installation](#manual-installation) for instructions to programmatically install and configure the agent.

Instrumentation for client and server libraries in Go is done manually. 
Please check the [HTTP instrumentation](go-http-instrumentation.md) and [gRPC instrumentation](go-grpc-instrumentation.md) 
articles for instructions on how to trace incoming and outgoing requests.


### Manual installation

The Scope Agent will automatically be installed if the API key can be autodetected (via environment variable, or via _Scope for Mac_ or _Scope for Windows_ in local development mode).

However, it can also be installed programmatically. In order to do so, you must supply (at least) the API key, and configure the instrumentation library. For example:

```go
import (
	"go.undefinedlabs.com/scopeagent/agent"
	"go.undefinedlabs.com/scopeagent/instrumentation"
)

func main() {
	// Create a custom agent instance
	myAgent, err := agent.NewAgent(agent.WithApiKey("xxxxx"))
	if err != nil {
		panic(err)
	}

	// Make sure we stop the agent cleanly before exiting
	defer myAgent.Stop()

    // Configure the instrumentation library to use the custom agent's tracer
	instrumentation.SetTracer(myAgent.Tracer())
	
	// ...
}
```

Check out the [`scopeagent` package documentation](https://godoc.org/go.undefinedlabs.com/scopeagent/agent) for a full list of options when creating the agent.


## Custom OpenTracing instrumentation

You can use [OpenTracing's Go API](https://github.com/opentracing/opentracing-go/blob/master/README.md) to add your
own custom spans and events to your code. Always make sure to use a `context.Context` object that comes from Scope's 
instrumentation to extend the traces created by `scopeagent.StartTest`.

In order to capture your custom instrumentation, Scope's agent has to be registered as OpenTracing's global tracer.
There are two options to do this: set the environment variable `SCOPE_SET_GLOBAL_TRACER=true`, or in code, like in the following example:

```go
import (
	"github.com/opentracing/opentracing-go"
	"go.undefinedlabs.com/scopeagent"
)

func main() {
	// Register Scope's tracer as OpenTracing's global tracer to capture custom instrumentation
	opentracing.SetGlobalTracer(scopeagent.GlobalAgent().Tracer())

	// ...
}
```

> Note that at the moment it's only possible to register _one_ tracer as global tracer at any given time.

## Environment variables

The following environment variables need to be configured when instrumenting your tests or application:

| Environment variable  | Default value           | Description                                            |
|-----------------------|-------------------------|--------------------------------------------------------|
| `$SCOPE_APIKEY`       | Autodetected (1)        | API key to use when sending data to Scope              |
| `$SCOPE_API_ENDPOINT` | Autodetected (1) or `https://app.scope.dev` | API endpoint of the Scope installation to send data to |
| `$SCOPE_COMMIT_SHA`   | Autodetected (2)        | Commit hash to use when sending data to Scope          |
| `$SCOPE_REPOSITORY`   | Autodetected (2)        | Repository URL to use when sending data to Scope       |
| `$SCOPE_SOURCE_ROOT`  | Autodetected (2)        | Repository root path                                   |

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

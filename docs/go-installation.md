---
id: go-installation
title: Scope Go Agent instructions
sidebar_label: Installation
---


Installation of the Scope Agent is done via `go get`:

```bash
go get -u go.undefinedlabs.com/scopeagent
```

## Usage

In order to instrument your tests that use Go's native [`testing`](https://golang.org/pkg/testing/) package, you
have to follow these steps:
 
1. Write a `TestMain(*testing.M)` function that calls `scopeagent.GlobalAgent.Stop()` before exiting.
2. Call `scopeagent.StartTest(*testing.T)` at the beginning of each test, which will return a `scopeagent.Test` object, and `defer test.End()`.

For example:

```go
import (
    "go.undefinedlabs.com/scopeagent"
    "testing"
)

func TestMain(m *testing.M) {
    result := m.Run()
    scopeagent.GlobalAgent.Stop()  // This will ensure that we flush all pending results before exiting
    os.Exit(result)
}

func TestExample(t *testing.T) {
    test := scopeagent.StartTest(t)
    defer test.End()
    // ... test code here. `test.Context()` has information about the currently active span
}
```

Please check the [HTTP instrumentation](go-http-instrumentation.md) article for instructions on how to trace HTTP requests (both client and server).

You can also use [OpenTracing's Go API](https://github.com/opentracing/opentracing-go/blob/master/README.md) to add your
own custom spans and events. The Scope Agent's tracer will be registered as the global tracer automatically.


## Environment variables

The following environment variables need to be configured when instrumenting your tests or application:

| Environment variable  | Default value    | Description                                            |
|-----------------------|------------------|--------------------------------------------------------|
| `$SCOPE_APIKEY`       |                  | API key to use when sending data to Scope              |
| `$SCOPE_API_ENDPOINT` |                  | API endpoint of the Scope installation to send data to |
| `$SCOPE_COMMIT_SHA`   | Autodetected (*) | Commit hash to use when sending data to Scope          |
| `$SCOPE_REPOSITORY`   | Autodetected (*) | Repository URL to use when sending data to Scope       |
| `$SCOPE_SOURCE_ROOT`  | Autodetected (*) | Repository root path                                   |

The following optional parameters can also be configured:

| Environment variable | Default value    | Description                                      |
|----------------------|------------------|--------------------------------------------------|
| `$SCOPE_SERVICE`     | `default`        | Service name to use when sending data to Scope   |

(*) Autodetection of git information works if either tests run on a [supported CI provider](python-compatibility.md#ci-providers),
or if the `.git` folder is present locally, and there is an `origin` remote configured pointing to the right repository.

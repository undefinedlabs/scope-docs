---
id: go-installation
title: Go Agent instructions
sidebar_label: Installation
---


## Compatibility

The Scope Go agent is compatible with the following versions of Go:

| Language    | Version |
| ----------- | :-----: |
| Go          |  1.11+  |

The Scope Go agent is compatible with the following libraries:

| Name                                                         | Span/event creation | Extract | Inject |
| ------------------------------------------------------------ | :-----------------: | :-----: | :----: |
| [`testing`](https://golang.org/pkg/testing/)                 |          ✓          |         |        |
| [`net/http`](https://golang.org/pkg/net/http/)               |          ✓          |    ✓    |    ✓   |

> Do you use a language or library not listed here? Please [let us know](https://home.undefinedlabs.com/goto/support)!

## Installation

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


## CI provider configuration

The following environment variables need to be configured in your CI provider:

| Environment variable | Description |
|---|---|
| `$SCOPE_APIKEY` | API key to use when sending data to Scope |
| `$SCOPE_API_ENDPOINT` | API endpoint of the Scope installation to send data to |


The following optional parameters can also be configured:

| Environment variable  | Default | Description |
|---|---|---|
| `$SCOPE_SERVICE` | `default` | Service name to use when sending data to Scope |
| `$SCOPE_COMMIT_SHA` | Autodetected | Commit hash to use when sending data to Scope |
| `$SCOPE_REPOSITORY` | Autodetected | Repository URL to use when sending data to Scope |
| `$SCOPE_SOURCE_ROOT` | Autodetected | Repository root path |

Autodetection of git information works if either tests run on Jenkins, CircleCI, Travis or GitLab.

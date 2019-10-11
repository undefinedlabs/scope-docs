---
id: go-http-instrumentation
title: Scope Go Agent HTTP Instrumentation
sidebar_label: HTTP Instrumentation
---


## Instrumenting the HTTP client

First, make sure the agent has been [installed](go-installation.md) in your Go application.

The Scope Go agent provides a helper function to instrument the default HTTP client at `http.DefaultClient`:

```go
import (
    "go.undefinedlabs.com/scopeagent/instrumentation/nethttp"
)

func main() {
    nethttp.PatchHttpDefaultClient()

    // ...
}
```

If you create a custom `http.Client` instance, you must use the Scope Go agent transport:

```go
import (
    "go.undefinedlabs.com/scopeagent/instrumentation/nethttp"
    "net/http"
)

func main() {
    client := &http.Client{Transport: &nethttp.Transport{}}

    // ...
}
```

After this, in order for the Scope Go agent to trace an outgoing request, you must attach the current context to it. 
For example:

```go
import (
    "context"
    "net/http"
)

func main() {
    // ...
    req, err := http.NewRequest("GET", url, nil)
    if err != nil {
        return err
    }
    req = req.WithContext(ctx)
    resp, err := http.DefaultClient.Do(req)
    if err != nil {
        return err
    }

    // ...
}
```


## Instrumenting the HTTP server

First, make sure the agent has been [installed](go-installation.md) in your Go application.

In order to instrument an HTTP server using the Scope Go agent, wrap the `http.Handler` you are serving with `nethttp.Middleware(h http.Handler)`.

For example, if using the default handler (`http.DefaultServeMux`):

```go
import (
    "go.undefinedlabs.com/scopeagent/agent"
    "go.undefinedlabs.com/scopeagent/instrumentation/nethttp"
    "net/http"
    "io"
)

func main() {
    // Make sure the agent is installed first
    scopeAgent, err := agent.NewAgent()
    if err != nil {
        panic(err)
    }
    defer scopeAgent.Stop()

    http.HandleFunc("/hello", func(w http.ResponseWriter, req *http.Request) {
        io.WriteString(w, "Hello, world!\n")
    })
    
    err := http.ListenAndServe(":8080", nethttp.Middleware(nil))
    if err != nil {
        panic(err)
    }
}
```


If you are using a custom handler, pass it to `nethttp.Middleware(h http.Handler)`:

```go
import (
    "go.undefinedlabs.com/scopeagent/agent"
    "go.undefinedlabs.com/scopeagent/instrumentation/nethttp"
    "net/http"
    "io"
)

func main() {
    // Make sure the agent is installed first
    scopeAgent, err := agent.NewAgent()
    if err != nil {
        panic(err)
    }
    defer scopeAgent.Stop()

    handler := http.NewServeMux()
    handler.HandleFunc("/hello", func(w http.ResponseWriter, req *http.Request) {
        io.WriteString(w, "Hello, world!\n")
    })
    
    err := http.ListenAndServe(":8080", nethttp.Middleware(handler))
    if err != nil {
        panic(err)
    }
}
```

---
id: go-http-instrumentation
title: Scope Go Agent HTTP Instrumentation
sidebar_label: HTTP Instrumentation
---


## Instrumenting the HTTP client

The Scope Go agent automatically instruments the default HTTP client at `http.DefaultClient`. If you create a custom
`http.Client` instance, you must use the Scope Go agent transport:

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

func makeRequest(url string, ctx context.Context) err {
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

In order to instrument an HTTP server using the Scope Go agent, wrap the `http.Handler` you are serving with `nethttp.Middleware(h http.Handler)`.

For example, if using the default handler (`http.DefaultServeMux`):

```go
import (
    _ "go.undefinedlabs.com/scopeagent"
    "go.undefinedlabs.com/scopeagent/instrumentation/nethttp"
    "net/http"
    "io"
)

func main() {
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
    _ "go.undefinedlabs.com/scopeagent"
    "go.undefinedlabs.com/scopeagent/instrumentation/nethttp"
    "net/http"
    "io"
)

func main() {
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

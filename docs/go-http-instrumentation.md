---
id: go-http-instrumentation
title: HTTP Instrumentation
sidebar_label: HTTP Instrumentation
---


## Instrumenting the HTTP client

The Scope Go agent automatically instruments the default HTTP client at `http.DefaultClient`. If you create a custom
`http.Client` instance, you must use the Scope Go agent transport:

```go
import (
	"github.com/undefinedlabs/go-agent/instrumentation/nethttp"
	"net/http"
)

func main() {
	client := &http.Client{Transport: &nethttp.Transport{}}
	// ...
}
```


## Injecting the trace information to an outgoing request

In order for the Scope Go agent to trace an outgoing request, you must attach the context to the it. For example:

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

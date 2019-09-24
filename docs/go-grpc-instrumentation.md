---
id: go-grpc-instrumentation
title: Scope Go Agent gRPC Instrumentation
sidebar_label: gRPC Instrumentation
---


## Instrumenting the gRPC client

The easiest way would be to use the Scope Go agent's `grpc.Dial`, which returns an instrumented client automatically.
For example:

```go
import (
    scopegrpc "go.undefinedlabs.com/scopeagent/instrumentation/grpc"

    "google.golang.org/grpc"
)

func myFunc() {
    // ...
    conn, err := scopegrpc.Dial(address)
    // ...
}
```

Alternatively, you can manually add Scope's client interceptors when calling `grpc.Dial`. For example:

```go
import (
    scopegrpc "go.undefinedlabs.com/scopeagent/instrumentation/grpc"

    "google.golang.org/grpc"
)

func getInstrumentedGrpcClient(address string, opts ...grpc.DialOption) (*grpc.ClientConn, error) {
    opts = append(opts, scopegrpc.GetClientInterceptors()...)
    return grpc.Dial(address, opts...)
}
```


After this, in order for the Scope Go agent to trace an outgoing request, you must attach the current context to it.
Remember that if you are inside an [instrumented test](go-installation.md), you can access the context via `test.Context()`.
For example:

```go
import (
    "go.undefinedlabs.com/scopeagent"
    scopegrpc "go.undefinedlabs.com/scopeagent/instrumentation/grpc"

    "google.golang.org/grpc"
    pb "google.golang.org/grpc/examples/helloworld/helloworld"
)

func makeRequest(conn *grpc.ClientConn, ctx context.Context) err {
    client := pb.NewGreeterClient(conn)
    r, err := client.SayHello(ctx, &pb.HelloRequest{Name: "world"})
    if err != nil {
        panic(err)
    }
    // ...
}
```


## Instrumenting the gRPC server

The easiest way would be to use the Scope Go agent's `grpc.NewServer`, which returns an instrumented server automatically.
For example:

```go
import (
    scopegrpc "go.undefinedlabs.com/scopeagent/instrumentation/grpc"

    "google.golang.org/grpc"
)

func myFunc() {
    // ...
    server := scopegrpc.NewServer()
    // ...
}
```


Alternatively, you can add Scope's server interceptors when calling `grpc.NewServer()`.
For example:

```go
import (
    "go.undefinedlabs.com/scopeagent"
    scopegrpc "go.undefinedlabs.com/scopeagent/instrumentation/grpc"

    "google.golang.org/grpc"
)

func getInstrumentedGrpcServer(opts ...grpc.ServerOption) *grpc.Server {
    opts = append(opts, scopegrpc.GetServerInterceptors()...)
    return grpc.NewServer(opts...)
}
```

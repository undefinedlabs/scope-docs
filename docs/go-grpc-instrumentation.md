---
id: go-grpc-instrumentation
title: Scope Go Agent gRPC Instrumentation
sidebar_label: gRPC Instrumentation
---


## Instrumenting the gRPC client

First, make sure the agent has been [installed](go-installation.md) in your Go application.

Then, add Scope's client interceptors when calling `grpc.Dial`. For example:

```go
import (
    scopegrpc "go.undefinedlabs.com/scopeagent/instrumentation/grpc"

    "google.golang.org/grpc"
)

func main() {
    // ...
    conn, err := grpc.Dial(address, scopegrpc.GetClientInterceptors()...)

    // ...
}
```


After this, in order for the Scope Go agent to trace an outgoing request, you must attach the current context to it.
Remember that if you are inside an [instrumented test](go-installation.md), you can access the context via `test.Context()`.
For example:

```go
import (
    scopegrpc "go.undefinedlabs.com/scopeagent/instrumentation/grpc"

    "google.golang.org/grpc"
    pb "google.golang.org/grpc/examples/helloworld/helloworld"
)

func main() {
    // ...
    conn, err := grpc.Dial(address, scopegrpc.GetClientInterceptors()...)
    client := pb.NewGreeterClient(conn)
    r, err := client.SayHello(ctx, &pb.HelloRequest{Name: "world"})
    if err != nil {
        panic(err)
    }

    // ...
}
```


## Instrumenting the gRPC server

Add Scope's server interceptors when calling `grpc.NewServer()`. For example:

```go
import (
    "go.undefinedlabs.com/scopeagent/agent"
    scopegrpc "go.undefinedlabs.com/scopeagent/instrumentation/grpc"

    "google.golang.org/grpc"
)

func main() {
    // Make sure the agent is installed first
    scopeAgent, err := agent.NewAgent()
    if err != nil {
        panic(err)
    }
    defer scopeAgent.Stop()

    server := grpc.NewServer(scopegrpc.GetServerInterceptors()...)

    // ...
}
```

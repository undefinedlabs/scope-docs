---
id: go-process-instrumentation
title: Scope Go Agent Process Instrumentation
sidebar_label: Process Instrumentation
---


The Scope Go agent can also be used to instrument tests that launch processes via `os/exec`.


## Instrumenting the code that launches a new process

In order to do so, the code that launches the process via `exec.Command` needs to inject the current context in the
environment variables array of the process using `process.InjectToCmd`. For example:

```go
import (
    "context"
    "os/exec"

    "go.undefinedlabs.com/scopeagent/instrumentation/process"
)

func myFunc(ctx context.Context) {
    cmd := exec.Command("my-cli")
    process.InjectToCmd(ctx, cmd)

    // ...
}
```

If you want to easily create a span representing the execution of the command, you can use `process.InjectToCmdWithSpan` instead:

```go
import (
    "context"
    "os/exec"

    "go.undefinedlabs.com/scopeagent/instrumentation/process"
)

func myFunc(ctx context.Context) {
    cmd := exec.Command("my-cli")
    span, ctx := process.InjectToCmdWithSpan(ctx, cmd)
    defer span.Finish()

    // ...
}
```


## Instrumenting the process that is launched

In the process that is launched, a call to `process.StartSpan` will start a span following the trace found in the environment, if available.
For example:

```go
import (
    "context"
    "os"
    "path/filepath"

    "github.com/opentracing/opentracing-go"
    "go.undefinedlabs.com/scopeagent"
    "go.undefinedlabs.com/scopeagent/instrumentation/process"
)

func main() {
    // Make sure we stop the agent cleanly before exiting
    defer scopeagent.Stop()

    // Start a span representing this process execution, following the trace found in the environment (if available)
    span := process.StartSpan(filepath.Base(os.Args[0]))
    defer span.Finish()

    // Create a new context to be used in my application
    ctx := opentracing.ContextWithSpan(context.Background(), span)

    // ...
}
```

This will automatically read any context information stored in environment variables via `process.InjectToCmd` and
will create a child span automatically.

---
id: go-logging-instrumentation
title: Scope Go Agent Logging Instrumentation
sidebar_label: Logging Instrumentation
---

The Scope Go agent has support for capturing logs from the following sources:

- Standard library test logs (calls to `testing.T.Log` and related methods) are automatically instrumented. Includes support for capturing source file and number information, and also for the exact timestamp and level of the log event. It is compatible with parallel tests.
- Standard logger (calls to `log.Println` and related methods) is automatically instrumented. Includes support for capturing source file and number information, and also for the exact timestamp of the log event. It is not compatible with parallel tests - if logs are emitted through the standard logger while tests are running in parallel (using `t.Parallel()`), logs are attached to any running test at that time.
- Custom loggers (`log.Logger` instances) can be manually instrumented with the same capabilities as the standard logger autoinstrumentation.
- Standard output/error (`os.Stdout` and `os.Stderr`) can be manually instrumented. Includes support for the timestamp of the log event but not the source file or line number information. It is not compatible with parallel tests.

> Note that instrumentation for `log.Logger` and standard output/error is done globally in the application, and is not compatible with parallel tests. In order to differentiate the logs of a given test, only sequential tests are supported for these instrumentations. Only per-test logs (calls to `t.Log()` and other test methods) support parallel tests.

> The standard test library automatic logging instrumentation (calls to `testing.T.Log` and related methods), which is achieved using monkey patching, can be disabled by adding the environment variable `SCOPE_DISABLE_MONKEY_PATCHING=true`. In this case, in order to attach logs to tests, you can use the Scope `test` object logs as explain in the following section.

## Scope Test logs

In case the standard library test automatic logging instrumentation is disabled (by using the environment variable `SCOPE_DISABLE_MONKEY_PATCHING=true`), the Scope `test` struct implements the same logging interface as `logging.T` and it's instrumented. It also support all features, such as capturing the source file and line number, exact timestamp, and level of the log.

Usage:

```go
import (
    "go.undefinedlabs.com/scopeagent"
    "testing"
)

func TestMain(m *testing.M) {
    os.Exit(scopeagent.Run(m))
}

func TestExample(t *testing.T) {
    test := scopeagent.GetTest(t)   // Gets the Scope Go agent representation of test `t`
    
    // test.Error()
    // test.Errorf()
    // test.Fatal()
    // test.Fatalf()
    // test.Log()
    // test.Logf()
    // test.Skip()
    // test.Skipf()

    // ...	
}
```


## Standard logger

By default the Scope Go agent instruments the standard logger in the `log` package.

In order to have more precise log info, it's recommended to set the logger flags to:

```go
import (
    "log"
)

func main() {
    log.SetFlags(log.LstdFlags | log.Lmicroseconds | log.Llongfile)

    // ...
}
```


## Instrumenting a custom logger

The Scope Go agent provides a helper function to instrument a custom `log.Logger` instance:

```go
import (
    "go.undefinedlabs.com/scopeagent/instrumentation/logging"
    "log"
)

func main() {
    myLogger := log.New(os.Stderr, "", log.LstdFlags|log.Lmicroseconds|log.Llongfile)

    logging.PatchLogger(myLogger)

    // ...
}
```


## Instrumenting the standard output / error


To activate the standard output or the standard error instrumentation, use the following functions:


```go
import (
    "go.undefinedlabs.com/scopeagent/instrumentation/logging"
)

func main() {
    // Instruments Standard Output
    logging.PatchStdOut()

    // Instruments Standard Error
    logging.PatchStdErr()

    // ...
}
```

> Please note that using a `log.Logger` instance is the recommended way to emit logs, as they will contain timestamp and source file and line number metadata.

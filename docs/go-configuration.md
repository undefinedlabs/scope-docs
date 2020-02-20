---
id: go-configuration
title: Scope Go Agent configuration
sidebar_label: Configuration
---

The behaviour of Scope Agent can be modified either by code or using environment variables.

Configuration by code is supported for both `scopeagent.Run(m)` and `agent.NewAgent()` as agent options parameters.

> If these properties are manually configured, use `true` or `false` only for the boolean value.


## Changing service name

You can specify the name of the service when sending data to Scope. Scope uses `default` as fallback.

<!--DOCUSAURUS_CODE_TABS-->
<!--Environment Variable-->

```sh
SCOPE_SERVICE="service-name"
```

<!--Testing instrumentation-->

```go
import (
    "os"
    "testing"

    "go.undefinedlabs.com/scopeagent"
    "go.undefinedlabs.com/scopeagent/agent"
)

func TestMain(m *testing.M) {
    os.Exit(scopeagent.Run(m, agent.WithServiceName("service-name")))
}

func TestExample(t *testing.T) {
    // ...
}

func BenchmarkExample(b *testing.B) {
    // ...
}
```

<!--Runtime instrumentation-->

```go
import (
    "go.undefinedlabs.com/scopeagent/agent"
)

func main() {
    scopeAgent, err := agent.NewAgent(agent.WithServiceName("service-name"))
    if err != nil {
        panic(err)
    }
    defer scopeAgent.Stop()
    
    // ...
}
```


<!--END_DOCUSAURUS_CODE_TABS-->


## Setting Scope as Global Tracer

If you set Scope as OpenTracing Global Tracer, your own spans will be captured and shown as part of the Scope trace view for a certain test.

<!--DOCUSAURUS_CODE_TABS-->
<!--Environment Variable-->

```sh
SCOPE_TRACER_GLOBAL=true
```

<!--Testing instrumentation-->

```go
import (
    "os"
    "testing"

    "go.undefinedlabs.com/scopeagent"
    "go.undefinedlabs.com/scopeagent/agent"
)

func TestMain(m *testing.M) {
    os.Exit(scopeagent.Run(m, agent.WithSetGlobalTracer()))
}

func TestExample(t *testing.T) {
    // ...
}

func BenchmarkExample(b *testing.B) {
    // ...
}
```

<!--Runtime instrumentation-->

```go
import (
    "go.undefinedlabs.com/scopeagent/agent"
)

func main() {
    scopeAgent, err := agent.NewAgent(agent.WithSetGlobalTracer())
    if err != nil {
        panic(err)
    }
    defer scopeAgent.Stop()

    // ...
}
```

<!--END_DOCUSAURUS_CODE_TABS-->

## Changing testing mode

This variable indicates whether the agent is running tests or it is being used for runtime instrumentation. 

If `SCOPE_TESTING_MODE` is not specified, the agent sets to  `true` when running in CI or if the tests are started using `scopeagent.Run()` or if is instrumented using the `go.undefinedlabs.com/scopeagent/autoinstrument` import,  and `false` otherwise.

<!--DOCUSAURUS_CODE_TABS-->
<!--Environment Variable-->

```sh
SCOPE_TESTING_MODE=false
```

<!--Testing instrumentation-->

```go
import (
    "os"
    "testing"

    "go.undefinedlabs.com/scopeagent"
    "go.undefinedlabs.com/scopeagent/agent"
)

func TestMain(m *testing.M) {
    os.Exit(scopeagent.Run(m, agent.WithTestingModeEnabled()))
}

func TestExample(t *testing.T) {
    // ...
}

func BenchmarkExample(b *testing.B) {
    // ...
}
```

<!--END_DOCUSAURUS_CODE_TABS-->

## Enabling test retries on failure

The Scope agent has support for retrying failed tests. By default, no retries are performed.

<!--DOCUSAURUS_CODE_TABS-->
<!--Environment Variable-->

```sh
SCOPE_TESTING_FAIL_RETRIES=3
```

<!--Testing instrumentation-->

```go
import (
    "os"
    "testing"

    "go.undefinedlabs.com/scopeagent"
    "go.undefinedlabs.com/scopeagent/agent"
)

func TestMain(m *testing.M) {
    os.Exit(scopeagent.Run(m, agent.WithRetriesOnFail(3)))
}

func TestExample(t *testing.T) {
    // ...
}

func BenchmarkExample(b *testing.B) {
    // ...
}
```

<!--END_DOCUSAURUS_CODE_TABS-->

## Handling test panic as a failure

By default, the standard testing framework exits the test process on panic. This behavior can be changed to handle panics as test failures, allowing the complete execution of the test suite. 

Also, this option can be combined with test retries, to retry tests that panic.

<!--DOCUSAURUS_CODE_TABS-->
<!--Environment Variable-->

```sh
SCOPE_TESTING_PANIC_AS_FAIL=true
```

<!--Testing instrumentation-->

```go
import (
    "os"
    "testing"

    "go.undefinedlabs.com/scopeagent"
    "go.undefinedlabs.com/scopeagent/agent"
)

func TestMain(m *testing.M) {
    os.Exit(scopeagent.Run(m, agent.WithHandlePanicAsFail()))
}

func TestExample(t *testing.T) {
    // ...
}

func BenchmarkExample(b *testing.B) {
    // ...
}
```

<!--END_DOCUSAURUS_CODE_TABS-->

## Adding agent metadata

You can add custom agent metadata that will be appended to the default metadata that the agent collects (such as host information).

Additionally, it is possible to set an environment variable as metadata value for a certain key, whose final value will be evaluated at runtime.

<!--DOCUSAURUS_CODE_TABS-->
<!--Environment Variable-->

```sh
SCOPE_METADATA="CustomKey1=MyValue, CustomKey2=MyValue2, CustomPath=\$PATH"
```

This is equivalent to: 
```go
    map[string]interface{}{
		"CustomKey1": "MyValue",
		"CustomKey2": "MyValue2",
		"CustomPath": os.Getenv("PATH"),
	}
```

<!--Testing instrumentation-->

```go
import (
    "os"
    "testing"

    "go.undefinedlabs.com/scopeagent"
    "go.undefinedlabs.com/scopeagent/agent"
)

func TestMain(m *testing.M) {
    os.Exit(scopeagent.Run(m, agent.WithMetadata(map[string]interface{}{
        "CustomKey1": "MyValue",
        "CustomKey2": "MyValue2",
        "CustomPath": os.Getenv("PATH"),
    })))
}

func TestExample(t *testing.T) {
    // ...
}

func BenchmarkExample(b *testing.B) {
    // ...
}
```

<!--Runtime instrumentation-->

```go
import (
    "go.undefinedlabs.com/scopeagent/agent"
)

func main() {
    scopeAgent, err := agent.NewAgent(agent.WithMetadata(map[string]interface{}{
        "CustomKey1": "MyValue",
        "CustomKey2": "MyValue2",
        "CustomPath": os.Getenv("PATH"),
    }))
    if err != nil {
        panic(err)
    }
    defer scopeAgent.Stop()
    
    // ...
}
```

<!--END_DOCUSAURUS_CODE_TABS-->

## Select agent metadata as test configuration

Yon can select metadata keys to be considered as relevant in the configuration of the test.

By default, Scope Go agent adds the folowwing metadata keys to the test configuration:

- **platform.name**: the result of calling `runtime.GOOS`
- **platform.architecture**: depends of the current architecture, can be `X64`, `X86`, `Arm`, `Arm64`
- **go.version**: the result of calling `runtime.Version()`


<!--DOCUSAURUS_CODE_TABS-->
<!--Environment Variable-->

```sh
SCOPE_CONFIGURATION="CustomKey1, CustomKey2"
```

This is equivalent to: 
```go
    []string{"CustomKey1", "CustomKey2"}
```

<!--Testing instrumentation-->

```go
import (
    "os"
    "testing"

    "go.undefinedlabs.com/scopeagent"
    "go.undefinedlabs.com/scopeagent/agent"
)

func TestMain(m *testing.M) {
    os.Exit(scopeagent.Run(m, agent.WithConfigurationKeys([]string{"CustomKey1", "CustomKey2"})))
}

func TestExample(t *testing.T) {
    // ...
}

func BenchmarkExample(b *testing.B) {
    // ...
}
```

<!--Runtime instrumentation-->

```go
import (
    "go.undefinedlabs.com/scopeagent/agent"
)

func main() {
    scopeAgent, err := agent.NewAgent(agent.WithConfigurationKeys([]string{"CustomKey1", "CustomKey2"}))
    if err != nil {
        panic(err)
    }
    defer scopeAgent.Stop()
    
    // ...
}
```

<!--END_DOCUSAURUS_CODE_TABS-->


## Include DB statements values in DB span tags

You can include DB statement values in the related DB spans.

By default, Scope Go Agent will not send DB statement values as they are considered sensitive information.

<!--DOCUSAURUS_CODE_TABS-->
<!--Environment Variable-->

```sh
SCOPE_INSTRUMENTATION_DB_STATEMENT_VALUES=true
```

<!--Testing instrumentation-->

```go
import (
    "os"
    "testing"

    "github.com/lib/pq"
    "github.com/go-sql-driver/mysql"

    "go.undefinedlabs.com/scopeagent"
    scopesql "go.undefinedlabs.com/scopeagent/instrumentation/sql"
)

func TestMain(m *testing.M) {
    sql.Register("scope-postgres", scopesql.WrapDriver(&pq.Driver{}, scopesql.WithStatementValues()))
    sql.Register("scope-mysql", scopesql.WrapDriver(&mysql.MySQLDriver{}, scopesql.WithStatementValues()))

    os.Exit(scopeagent.Run(m))
}

func TestExample(t *testing.T) {
    // ...
}

func BenchmarkExample(b *testing.B) {
    // ...
}
```

<!--Runtime instrumentation-->

```go
import (
    "database/sql"
    
    "github.com/lib/pq"
    "github.com/go-sql-driver/mysql"

    scopesql "go.undefinedlabs.com/scopeagent/instrumentation/sql"
)

func main() {
    // ...

    sql.Register("scope-postgres", scopesql.WrapDriver(&pq.Driver{}, scopesql.WithStatementValues()))
    sql.Register("scope-mysql", scopesql.WrapDriver(&mysql.MySQLDriver{}, scopesql.WithStatementValues()))

    // ...
}

// ...
```

<!--END_DOCUSAURUS_CODE_TABS-->


## Include HTTP payloads in HTTP span tags

You can include HTTP payloads in the related HTTP spans, truncated to the first 512 bytes.

By default, Scope Go Agent will not send HTTP payloads as they are considered sensitive information.

<!--DOCUSAURUS_CODE_TABS-->
<!--Environment Variable-->

```sh
SCOPE_INSTRUMENTATION_HTTP_PAYLOADS=true
```

<!--Testing instrumentation-->

```go
import (
    "os"
    "testing"

    "go.undefinedlabs.com/scopeagent"
    "go.undefinedlabs.com/scopeagent/instrumentation/nethttp"
)

func TestMain(m *testing.M) {
    // Default Http Client
	nethttp.PatchHttpDefaultClient(nethttp.WithPayloadInstrumentation())

    os.Exit(scopeagent.Run(m))
}

func TestExample(t *testing.T) {
    // Custom http.Client instance
    client := &http.Client{Transport: &nethttp.Transport{ PayloadInstrumentation: true }}

    // ...
}

func BenchmarkExample(b *testing.B) {
    // ...
}
```

<!--Runtime instrumentation-->

```go
import (
    "go.undefinedlabs.com/scopeagent/instrumentation/nethttp"
)

func main() {
    // Default Http Client
    nethttp.PatchHttpDefaultClient(nethttp.WithPayloadInstrumentation())

    // Custom http.Client instance
    client := &http.Client{Transport: &nethttp.Transport{ PayloadInstrumentation: true }}

    // ...
}
```

<!--END_DOCUSAURUS_CODE_TABS-->


## Changing the log directory

By default, the log directory were the Scope agent stores its logs depends on the platform:

* Linux: `/var/log/scope`
* Windows: `${HOME}/AppData/Roaming/scope/logs`
* Mac OS: `${HOME}/Library/Logs/Scope`

> If the agent can't write to the default log folder, then it will create a temporary directory

You can also specify a custom log directory:

```sh
SCOPE_LOGGER_ROOT=/home/user/my-logs
```

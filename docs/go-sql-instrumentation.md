---
id: go-sql-instrumentation
title: Scope Go Agent SQL Instrumentation
sidebar_label: SQL Instrumentation
---


## Instrumenting the SQL driver

First, make sure the agent has been [installed](go-installation.md) in your Go application.

The Scope Go agent provides a wrapper function to instrument an existing `database/sql` driver. 

Currently, the instrumentation supports the following libraries:

- Postgres (https://github.com/lib/pq)
- MySQL (https://github.com/go-sql-driver/mysql)

To instrument the driver you need to register a new one using the wrapper:

```go
import (
    "database/sql"

    "github.com/lib/pq"
    "github.com/go-sql-driver/mysql"

    scopesql "go.undefinedlabs.com/scopeagent/instrumentation/sql"
)

func main() {
    // ...

    sql.Register("scope-postgres", scopesql.WrapDriver(&pq.Driver{}))
    sql.Register("scope-mysql", scopesql.WrapDriver(&mysql.MySQLDriver{}))

    // ...
}
```

After this, in order for the Scope Go agent to trace queries to the database, you have to open the instrumented driver and attach the current context in each query. 
For example:

<!--DOCUSAURUS_CODE_TABS-->
<!--Postgres-->

```go
import (
    "database/sql"

    _ "github.com/lib/pq"

    "go.undefinedlabs.com/scopeagent"
    scopesql "go.undefinedlabs.com/scopeagent/instrumentation/sql"
)

func main() {
    // ...

    psqlInfo := fmt.Sprintf("host=%s port=%d user=%s "+"password=%s dbname=%s sslmode=disable",
        host, port, user, password, dbname)

    db, err := sql.Open("scope-postgres", psqlInfo)
    if err != nil {
        panic(err)
    }
    defer db.Close()

    selectQuery := "SELECT * FROM my_table"
    rows, err := db.QueryContext(ctx, selectQuery)
    if err != nil {
        panic(err)
    }
    defer rows.Close()

    // ...
}
```

<!--MySQL-->

```go
import (
    "database/sql"

    _ "github.com/go-sql-driver/mysql"

    "go.undefinedlabs.com/scopeagent"
    scopesql "go.undefinedlabs.com/scopeagent/instrumentation/sql"
)

func main() {
    // ...

    db, err := sql.Open("scope-mysql", "user:password@/dbname")
    if err != nil {
        panic(err)
    }
    defer db.Close()

    selectQuery := "SELECT * FROM my_table"
    rows, err := db.QueryContext(ctx, selectQuery)
    if err != nil {
        panic(err)
    }
    defer rows.Close()

    // ...
}
```

<!--END_DOCUSAURUS_CODE_TABS-->

## Statement values

By using `scopesql.WithStatementValues()` the SQL statement values will be instrumented as well. 

For example:

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
```

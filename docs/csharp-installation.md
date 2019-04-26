---
id: csharp-installation
title: C# Agent instructions
sidebar_label: Installation
---


## Compatibility

The Scope C# agent is compatible with the following libraries:

Name | Span/event creation | Extract | Inject |
-----|:-------------:|:-------:|:------:
`ASP.NET Core (WebApi/MVC)` | ✓ | ✓ | | 
[`Entity Framework Core`](https://www.nuget.org/packages/Microsoft.EntityFrameworkCore/) | ✓ |  | |
`ASP.NET (WebApi/MVC)` | ✓ | ✓ | |
`.NET Core BCL HttpClient, WebClient and HttpWebRequest` | ✓ |  | ✓|
`.NET Framework BCL HttpClient, WebClient and HttpWebRequest` | ✓ |  | ✓|
`.NET BCL System.Diagnostics.Trace listener` | ✓ |  | |
[`System.Data.SqlClient`](https://www.nuget.org/packages/System.Data.SqlClient/) | ✓ |  | |
[`MySql.Data`](https://www.nuget.org/packages/MySql.Data/) | ✓ |  | |
[`MySqlConnector`](https://www.nuget.org/packages/MySqlConnector/) | ✓ |  | |
[`Npgsql`](https://www.nuget.org/packages/Npgsql/) | ✓ |  | |
[`Microsoft.Extensions.Logging`](https://www.nuget.org/packages/Microsoft.Extensions.Logging) based instrumentation | ✓ |  | |
[`NUnit`](https://www.nuget.org/packages/NUnit/) | ✓ |  | |
[`xUnit`](https://www.nuget.org/packages/xunit/) | ✓ |  | |
[`MSTest`](https://www.nuget.org/packages/MSTest.TestFramework/) | ✓ |  | |


## Prerequisites
- [`.NET Core 2.2`](https://dotnet.microsoft.com/download/dotnet-core/2.2)

## Installation
Installation of the Scope Agent is done via [NuGet](https://www.nuget.org/) as [`.NET Core CLI Global tool`](https://docs.microsoft.com/en-us/dotnet/core/tools/global-tools).

The first time you have to install the [`ScopeAgent.Runner`](https://www.nuget.org/packages/ScopeAgent.Runner/) package in your CI using:
```
dotnet tool install --global ScopeAgent.Runner
```

This will install the `scope-run` command in the machine with all packages needed to `Profile` and `Instrument` your tests.

## Usage
To run your test, prefix your startup command with `scope-run`:
```
scope-run dotnet test
```

### Parameters

| Flag | Required? | Default | Description | Environment variable |
|---|:---:|---|---|:---:|
| `-k`, `--apikey` | Y |  | API key tog use when sending data to Scope | `$SCOPE_APIKEY` |
| `-e`, `--api-endpoint` | Y |  | API endpoint of the Scope installation to send data to | `$SCOPE_API_ENDPOINT` |
| `-n`, `--name` | N | `default` | Service name to use when sending data to Scope | `$SCOPE_SERVICE` |
| `-c`, `--commit` | N | `$(git rev-parse HEAD)` | Commit hash to use when sending data to Scope | `$SCOPE_COMMIT_SHA` |
| `-r`, `--repository` | N | `$(git remote get-url origin)` | Repository URL to use when sending data to Scope | `$SCOPE_REPOSITORY` |
| `--root` | N | `$(git rev-parse --show-toplevel)` | Repository root path | `$SCOPE_SOURCE_ROOT` |

Commit, repository, and source root information will automatically be detected if running on CircleCI or Jenkins via environment variables.


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

Autodetection of git information works if either tests run on Jenkins, CircleCI, Travis or GitLab, or if the `.git` folder
is present locally, and there is a `origin` remote configured pointing to the right repository.

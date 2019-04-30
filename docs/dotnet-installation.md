---
id: dotnet-installation
title: .NET Agent instructions
sidebar_label: Installation
---


## Compatibility

The Scope .NET agent is compatible with the following platforms:

| Name        | Version | Windows | Linux | OS X |
|-------------|:-------:|:-------:|:-----:|:----:|
| `.NET Core` |   2.2+  |    ✓    |   ✓   |      |

The Scope .NET agent is compatible with the following classes and libraries:

| Name                                                                                          | Span/event creation | Extract | Inject |
|-----------------------------------------------------------------------------------------------|:-------------------:|:-------:|:------:|
| `ASP.NET Core`                                                                                |          ✓          |    ✓    |        |
| [`Entity Framework Core`](https://www.nuget.org/packages/Microsoft.EntityFrameworkCore/)      |          ✓          |         |        |
| ` HttpClient`<br/>`WebClient`<br/>`HttpWebRequest`                                            |          ✓          |         |    ✓   |
| `System.Diagnostics.Trace`                                                                    |          ✓          |         |        |
| [`System.Data.SqlClient`](https://www.nuget.org/packages/System.Data.SqlClient/)              |          ✓          |         |        |
| [`MySql.Data`](https://www.nuget.org/packages/MySql.Data/)                                    |          ✓          |         |        |
| [`MySqlConnector`](https://www.nuget.org/packages/MySqlConnector/)                            |          ✓          |         |        |
| [`Npgsql`](https://www.nuget.org/packages/Npgsql/)                                            |          ✓          |         |        |
| [`Microsoft.Extensions.Logging`](https://www.nuget.org/packages/Microsoft.Extensions.Logging) |          ✓          |         |        |
| [`NUnit`](https://www.nuget.org/packages/NUnit/)                                              |          ✓          |         |        |
| [`xUnit`](https://www.nuget.org/packages/xunit/)                                              |          ✓          |         |        |
| [`MSTest`](https://www.nuget.org/packages/MSTest.TestFramework/)                              |          ✓          |         |        |

> Do you use a platform or library not listed here? Please [let us know](https://home.codescope.com/goto/support)!

## Installation

Installation of the Scope Agent is done via [NuGet](https://www.nuget.org/) as a [`.NET Core CLI Global tool`](https://docs.microsoft.com/en-us/dotnet/core/tools/global-tools).

The first time you have to install the [`ScopeAgent.Runner`](https://www.nuget.org/packages/ScopeAgent.Runner/) package in your CI using:

```bash
dotnet tool install --global ScopeAgent.Runner
```

This will install the `scope-run` command in the machine with all packages needed to instrument your tests.

## Usage

To use the agent, prefix your test or startup command with `scope-run`. For example:

```bash
scope-run dotnet test
```

All tests will be instrumented automatically.


## CI provider configuration

The following environment variables need to be configured in your CI provider:

| Environment variable  | Description                                            |
|-----------------------|--------------------------------------------------------|
| `$SCOPE_APIKEY`       | API key to use when sending data to Scope              |
| `$SCOPE_API_ENDPOINT` | API endpoint of the Scope installation to send data to |


The following optional parameters can also be configured:

| Environment variable | Default      | Description                                      |
|----------------------|--------------|--------------------------------------------------|
| `$SCOPE_SERVICE`     | `default`    | Service name to use when sending data to Scope   |
| `$SCOPE_COMMIT_SHA`  | Autodetected | Commit hash to use when sending data to Scope    |
| `$SCOPE_REPOSITORY`  | Autodetected | Repository URL to use when sending data to Scope |
| `$SCOPE_SOURCE_ROOT` | Autodetected | Repository root path                             |

Autodetection of git information works if either tests run on [Jenkins](https://jenkins.io/), 
[CircleCI](https://circleci.com/), [Travis CI](https://travis-ci.com/) or [GitLab CI](https://about.gitlab.com/), 
or if the `.git` folder is present locally, and there is an `origin` remote configured pointing to the right repository.

These configuration settings can also be provided via CLI flags. Run `scope-run --help` for more information.

---
id: dotnet-installation
title: .NET Agent instructions
sidebar_label: Installation
---


## Compatibility

The Scope .NET agent is compatible with the following platforms:

| Name        | Version | Windows | Linux | OS X |
|-------------|:-------:|:-------:|:-----:|:----:|
| `.NET Core` |   2.1+  |    ✓    |   ✓   |      |

The Scope .NET agent is compatible with the following classes and libraries:

### Testing Frameworks
Name                                                             |   Version   | Span/event creation | Extract | Inject |
-----------------------------------------------------------------|:-----------:|:-------------------:|:-------:|:------:|
[`MSTest`](https://www.nuget.org/packages/MSTest.TestFramework/) | `>=1.3.0`   |          ✓          |         |        |
[`NUnit`](https://www.nuget.org/packages/NUnit/)                 | `>=3.11.0`  |          ✓          |         |        |
[`xUnit`](https://www.nuget.org/packages/xunit/)                 | `>=2.4.0`   |          ✓          |         |        |

### Loggers
Name                                                                                          |  Version  | Span/event creation | Extract | Inject |
----------------------------------------------------------------------------------------------|:---------:|:-------------------:|:-------:|:------:|
[`Microsoft.Extensions.Logging`](https://www.nuget.org/packages/Microsoft.Extensions.Logging) | `>=2.0.0` |           ✓         |         |        |
[`Serilog`](https://www.nuget.org/packages/Serilog/)                                          | `>=2.8.0` |           ✓         |         |        |
[`NLog`](https://www.nuget.org/packages/NLog/)                                                | `>=4.5.0` |           ✓         |         |        |
[`log4net`](https://www.nuget.org/packages/log4net/)                                          | `>=2.0.8` |           ✓         |         |        |

### Database Connectors
Name                                                                                     |   Version   | Span/event creation | Extract | Inject |
-----------------------------------------------------------------------------------------|:-----------:|:-------------------:|:-------:|:------:|
[`Entity Framework Core`](https://www.nuget.org/packages/Microsoft.EntityFrameworkCore/) | `>=2.0.0`   |           ✓         |         |        |
[`StackExchange.Redis`](https://www.nuget.org/packages/StackExchange.Redis/)             | `>=2.0.495` |           ✓         |         |        |
[`System.Data.SqlClient`](https://www.nuget.org/packages/System.Data.SqlClient/)         | `>=4.1.0`   |           ✓         |         |        |
[`MySql.Data`](https://www.nuget.org/packages/MySql.Data/)                               | `>=6.8.8`   |           ✓         |         |        |
[`MySqlConnector`](https://www.nuget.org/packages/MySqlConnector/)                       | `>=0.35.0`  |           ✓         |         |        |
[`Npgsql`](https://www.nuget.org/packages/Npgsql/)                                       | `>=4.0.0`   |           ✓         |         |        |

### Other libraries
Name                                               | Span/event creation | Extract | Inject |
---------------------------------------------------|:-------------------:|:-------:|:------:|
`.NET System.Diagnostics.Trace`                    |          ✓          |         |        |
`ASP.NET Core`                                     |          ✓          |    ✓    |        |
` HttpClient`<br/>`WebClient`<br/>`HttpWebRequest` |          ✓          |         |    ✓   |


> Do you use a platform or library not listed here? Please [let us know](https://home.codescope.com/goto/support)!

## Installation

Installation of the Scope Agent is done via [NuGet](https://www.nuget.org/) as a [.NET Core CLI Global tool](https://docs.microsoft.com/en-us/dotnet/core/tools/global-tools):

```bash
dotnet tool install --global ScopeAgent.Runner
```

This will install the `scope-run` command globally in the machine.

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

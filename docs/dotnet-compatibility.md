---
id: dotnet-compatibility
title: Scope .NET Agent compatibility matrix
sidebar_label: Compatibility
---


The Scope .NET agent is compatible with the following platforms:

| Name        | Version  | Windows | Linux | OS X |
|-------------|:--------:|:-------:|:-----:|:----:|
| `.NET Core` | 3.0, 2.x |    ✓    |   ✓   |   ✓  |

The Scope .NET agent is compatible with the following classes and libraries:

### Testing Frameworks

Name                                                             |        Version        | Span/event creation | Extract | Inject |
-----------------------------------------------------------------|:---------------------:|:-------------------:|:-------:|:------:|
[`MSTest`](https://www.nuget.org/packages/MSTest.TestFramework/) | `1.2.x, 1.3.x, 1.4.x` |          ✓          |         |        |
[`NUnit`](https://www.nuget.org/packages/NUnit/)                 |    `3.11.0, 3.12.x`   |          ✓          |         |        |
[`xUnit`](https://www.nuget.org/packages/xunit/)                 |         `2.4.x`       |          ✓          |         |        |

### Loggers

Name                                                                                          |        Version        | Span/event creation | Extract | Inject |
----------------------------------------------------------------------------------------------|:---------------------:|:-------------------:|:-------:|:------:|
[`Microsoft.Extensions.Logging`](https://www.nuget.org/packages/Microsoft.Extensions.Logging) | `2.x`                 |           ✓         |         |        |
[`Serilog`](https://www.nuget.org/packages/Serilog/)                                          | `2.x`                 |           ✓         |         |        |
[`NLog`](https://www.nuget.org/packages/NLog/)                                                | `4.5.x, 4.6.x`        |           ✓         |         |        |
[`log4net`](https://www.nuget.org/packages/log4net/)                                          | `2.0.6, 2.0.7, 2.0.8` |           ✓         |         |        |

### Database Connectors

Name                                                                                     |       Version       | Span/event creation | Extract | Inject |
-----------------------------------------------------------------------------------------|:-------------------:|:-------------------:|:-------:|:------:|
[`Entity Framework Core`](https://www.nuget.org/packages/Microsoft.EntityFrameworkCore/) | `2.x`               |           ✓         |         |        |
[`Dapper`](https://www.nuget.org/packages/Dapper/)                                       | `2.x`               |           ✓         |         |        |
[`StackExchange.Redis`](https://www.nuget.org/packages/StackExchange.Redis/)             | `2.0.x`             |           ✓         |         |        |
[`System.Data.SqlClient`](https://www.nuget.org/packages/System.Data.SqlClient/)         | `[4.3.1 - 4.6.x]`   |           ✓         |         |        |
[`Microsoft.Data.Sqlite`](https://www.nuget.org/packages/Microsoft.Data.SQLite/2.1.0/)   | `2.x`               |           ✓         |         |        |
[`MySql.Data`](https://www.nuget.org/packages/MySql.Data/)                               | `6.9.12, 6.10.x`    |           ✓         |         |        |
[`MySqlConnector`](https://www.nuget.org/packages/MySqlConnector/)                       | `[0.35.0 - 0.56.0]` |           ✓         |         |        |
[`Npgsql`](https://www.nuget.org/packages/Npgsql/)                                       | `3.2.x, 4.x`        |           ✓         |         |        |
[`MongoDB.Driver`](https://www.nuget.org/packages/MongoDB.Driver/2.8.0)                  | `[2.7.x - 2.9.x]`   |           ✓         |         |        |

### Other libraries

Name                                               | Span/event creation | Extract | Inject |
---------------------------------------------------|:-------------------:|:-------:|:------:|
`.NET System.Diagnostics.Trace`                    |          ✓          |         |        |
`ASP.NET Core`                                     |          ✓          |    ✓    |        |
` HttpClient`<br/>`WebClient`<br/>`HttpWebRequest` |          ✓          |         |    ✓   |


> Do you use a platform or library not listed here? Please [let us know](https://home.undefinedlabs.com/goto/support)!


### CI providers

The Scope .NET agent will work on any CI provider, but will autodetect build and git information 
(repository, commit, branch and source root directory) if running on the following CI providers:

* [Jenkins](https://jenkins.io/)
* [CircleCI](https://circleci.com/)
* [GitLab CI](https://docs.gitlab.com/ee/ci/)
* [Travis](https://travis-ci.org/)
* [AppVeyor](https://www.appveyor.com/)
* [Azure Pipelines](https://azure.microsoft.com/en-us/services/devops/pipelines/)
* [Bitbucket Pipelines](https://bitbucket.org/product/features/pipelines)
* [TeamCity](https://www.jetbrains.com/teamcity/)

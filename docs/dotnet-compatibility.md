---
id: dotnet-compatibility
title: Scope .NET Agent compatibility matrix
sidebar_label: Compatibility
---


The Scope .NET agent is compatible with the following platforms:

| Name        | Version | Windows | Linux | OS X |
|-------------|:-------:|:-------:|:-----:|:----:|
| `.NET Core` |   2.1+  |    ✓    |   ✓   |   ✓  |

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
[`Microsoft.Data.Sqlite`](https://www.nuget.org/packages/Microsoft.Data.SQLite/2.1.0/)   | `>=2.1.0`   |           ✓         |         |        |
[`MySql.Data`](https://www.nuget.org/packages/MySql.Data/)                               | `>=6.8.8`   |           ✓         |         |        |
[`MySqlConnector`](https://www.nuget.org/packages/MySqlConnector/)                       | `>=0.35.0`  |           ✓         |         |        |
[`Npgsql`](https://www.nuget.org/packages/Npgsql/)                                       | `>=4.0.0`   |           ✓         |         |        |
[`MongoDB.Driver`](https://www.nuget.org/packages/MongoDB.Driver/2.8.0)                  | `>=2.8.0`   |           ✓         |         |        |

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

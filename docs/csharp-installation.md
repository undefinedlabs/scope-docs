---
id: csharp-installation
title: C# Agent instructions
sidebar_label: Installation
---


## Compatibility

The Scope C# agent is compatible with the following libraries:

Name | Span/event creation | Extract | Inject
-----|:-------------:|:-------:|:------:
`ASP.NET Core (WebApi/MVC)` | ✓ | ✓ | |
[`Entity Framework Core`](https://www.nuget.org/packages/Microsoft.EntityFrameworkCore/) | ✓ |  | |
`.NET Core BCL HttpClient, WebClient and HttpWebRequest` | ✓ |  | ✓|
`.NET BCL System.Diagnostics.Trace listener` | ✓ |  | |
[`Microsoft.Extensions.Logging`](https://www.nuget.org/packages/Microsoft.Extensions.Logging) based instrumentation | ✓ |  | |
[`NUnit`](https://www.nuget.org/packages/NUnit/) | ✓ |  | |
[`xUnit`](https://www.nuget.org/packages/xunit/) | ✓ |  | |
[`MSTest`](https://www.nuget.org/packages/MSTest.TestFramework/) | ✓ |  | |


## Installation

Installation of the Scope Agent is done via [NuGet](https://www.nuget.org/)

You can install it either using the Visual Studio `Install-Package` in the Nuget Package Manager or from the dotnet CLI using `dotnet add package` by adding the following packages to your test project:

1. Depending of the testing framework you will need to install one of these packages:

| Framework | Package Name 						|
|-----------|:---------------------------------:|
| NUnit     | [`ScopeAgent.TestFrameworks.NUnit`](https://www.nuget.org/packages/ScopeAgent.TestFrameworks.NUnit/)   |
| xUnit     | [`ScopeAgent.TestFrameworks.xUnit`](https://www.nuget.org/packages/ScopeAgent.TestFrameworks.xUnit/)   |
| MSTest    | [`ScopeAgent.TestFrameworks.MSTest`](https://www.nuget.org/packages/ScopeAgent.TestFrameworks.MSTest/)  |

2. Then you need to install the .NET Core agent extensions included in the [`ScopeAgent.Extensions.NetCore`](https://www.nuget.org/packages/ScopeAgent.Extensions.NetCore/) package. This package is required to instrument `ASP.NET Core (WebApi/MVC)` and [`Microsoft.Extensions.Logging`](https://www.nuget.org/packages/Microsoft.Extensions.Logging)


## Usage
Depending of the testing framework you have to do some changes to your test project:

### NUnit
To instrument NUnit tests, add the following code to the top of any project `.cs` file: 
```
[assembly: ScopeAgent]
```
All tests on that project will be instrumented by the Scope Agent automatically.

### xUnit
To instrument xUnit tests, add the following code to the top of any project `.cs` file:
```
[assembly: TestFramework("ScopeAgentFramework", "ScopeAgent.TestFrameworks.xUnit")]
```
All tests on that project will be instrumented by the Scope Agent automatically.

### MSTest
To instrument MSTest tests, you need to change the `[TestClass]` decoration attribute to `[ScopeTestClass]` so all defined tests in that class would be instrumented.

For example:

```
namespace ScopeAgent.MSTest.Example
{
    [ScopeTestClass]		//We only have to change the [TestClass] to [ScopeTestClass]
    public class UnitTest1
    {
        [TestMethod]
        public void MyAwesomeTest()
        {
            var res = Math.Sqrt(9);
            Assert.AreEqual(3, res);
        }
        
        [TestMethod]
        public void CrashingTest()
        {
            var x = 0;
            var y = 1 / x;
        }
    }
}
```

>After this, you can run your test project as you normally do, for example using the `dotnet test` command.

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

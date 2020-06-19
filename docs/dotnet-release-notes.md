---
id: dotnet-release-notes
title: Scope .NET Agent release notes
sidebar_label: Release notes
---


## Scope .NET Agent v0.3.1

*June 19, 2020*

#### Added:
- Support for stacktraces in HTTP and DB Spans (#424)
- Ingest control entity. `ingest.error` and `process.end` support. (#429)
        
#### Changed:
- Sends the metadata only in the first payload (#425)
- Extend support for InContainer flag to more platforms (#427)
- Expand tilde in source root (#428)
- Instrumentation for MongoDb and Redis uses the ducktyping version.
        
#### Fixed:
- Travis build url (#426)


## Scope .NET Agent v0.3.0

*June 15, 2020*

#### Added:
- Intelligent test runner cached tests.
        
#### Changed:
- Performance improvements in Dispatcher and Transports.
- Removes dependencies to instrumented libraries.



## Scope .NET Agent v0.2.0

*May 14, 2020*

**Added:**
- Testing mode in metadata
- Buildkite support
- CreateDefaultBinder and ConfigureWebDefaults AspNetCore method wrapper
        
**Changed:**
- Trace IDs are now 128 bits.
        
**Fixes:**
- Git info attribute in the coverage processor.
- TestMapPropagationCodec fixes
- Coverage middleware key fix
- Test report shown on runtime mode
- Support for git HEAD hash and symbolic ref
- ASP.NET Core middleware status code
        
**NOTE:** all agents involved in a trace must be updated to support 128 bits.


## Scope .NET Agent v0.1.22-beta.1

*January 28, 2020*

**Fixes:**
- Git info attribute in the coverage processor.


## Scope .NET Agent v0.1.21

*January 14, 2020*

**Fixes:**
- Multi dotnet core version support and debug flag error.
- Symbols resolver now write to log in case of an exception.


## Scope .NET Agent v0.1.20

*December 11, 2019*

**Adds:**
- Support for integration test with the Microsoft.AspNetCore.Mvc.Testing package.


## Scope .NET Agent v0.1.19

*December 10, 2019*

**Adds:**
- Retry option for failing tests.
- Support for .NET Core 3.1


## Scope .NET Agent v0.1.18

*November 28, 2019*

**Fixes:**
- Azure DevOps Pipelines CI support


## Scope .NET Agent v0.1.17

*November 28, 2019*

**Changes:**

- Rename `SCOPE_CODEPATH` to `SCOPE_CODE_PATH`


## Scope .NET Agent v0.1.16

*November 27, 2019*

**Changes:**
- Remove the Error status from tests
- Env vars renaming

**Fixes:**
- Runner arguments parser.


## Scope .NET Agent v0.1.15

*November 19, 2019*

**Added:**
- DB params instrumentation flag. (disabled by default)
- Http payload and headers instrumentation.
- Dependencies version dictionary on metadata.
- BenchmarkDotNet exporter for scope.
- Scope DSN support.

**Changes:**
- Complete refactor of the agent. 
- Standalone version of the coverage algorithm.
- Error messages after finishing test suite.


## Scope .NET Agent v0.1.14

*November 06, 2019*

**Fixes:**
- .NET Core 3.0 runtime targeting an old .NET Core version
- Reduce package file size

**Changes:**
- Http and DB spans operation name now follows the agents semantic conventions


## Scope .NET Agent v0.1.13

*October 22, 2019*

**Added:**
- Support for .NET Core 3.0
- Scope api endpoint fallback to app.scope.dev if the environment variable is null.
- Support for `scope.yml` and `scope.yaml` configuration filename.
- Dapper ORM instrumentation
- Support for TeamCity CI
      
**Fixes:**
- Handling of multiple interceptors for databases.


## Scope .NET Agent v0.1.12

*September 09, 2019*

**Changed:**
- The code coverage format has been changed to version 0.2.0
- Scope configuration file changed to `Yaml` format

**Fixes:**
- Exceptions logged by a logger should have `event.type = "log"`
- Health check flush in production mode


## Scope .NET Agent v0.1.11

*August 28, 2019*

**Added:**
- The `SCOPE_LOGS_PATH` Environment variable and `logs_path` toml key to change the default log folder.
- Commit hash in the log filename.
- Test configurations aggregation based on both agent metadata and custom environment variables.
- Add support to add aggregations programmatically.

**Changed:**
- The coverage engine has been changed to improve the performance and to enable or disable it at runtime with lower performance impact.
- Parameterized test handling now are shown as a different test with a hash over the test arguments.
- Change the duration calculation for skipped tests.
- Better flush scheduling.

**Fixes:**
- Scheduled dispatcher task waits before process exit.
- Serializing Assembly type on json.
- Async continuations race condition.
- Span log implementation from the ISpan interface.


## Scope .NET Agent v0.1.10

*July 31, 2019*

**Added:**
- Desktop configuration file reader to load the current scope profile.
- `no-params` option in the scope runner for long running apps with child processes (ex: Visual Studio).
- Support for `test.arguments` and `test.traits`.
- xUnit `[Theory]` parent span support.
- Support for xUnit test logger ITestOutputHelper.
        
**Changed:**
- Agent logs are now stored in the home scope folder for windows, ~/Library/Logs/Scope (OSX) and /var/log/scope (linux).
- The dispatcher force flush is delayed to the end of all tests, so we don't block any thread until the end.
- Diff summary is enabled by default (not working in linux).

**Fixed:**
- Fix missing covered lines on instructions with `brfalse.s` OpCode
- Performance improvements.
- Fixes code coverage in tests with multiple threads.


## Scope .NET Agent v0.1.9

*July 10, 2019*

Added:
- Support for .toml agent configuration file.
- Error tag on failed tests spans.
- `db.prepare_statement` tag with the unresolved sql statement.
- Adds http dispatcher support for `HttpClientTransportSerializer` and `HttpClientTransportEncoding` settings. 
- Adds http server support for `EnableHttpServerInstrumentation` and `EnableHttpServerCodeCoverage` settings.
- Support for the Universal Code Coverage Format.
- Support for code coverage in http server requests.
- DbParam object standard format implementation.
- Support for the Universal Git Diff Summary Format.

Changed:
- Span tags according the semantic conventions.
- Refactoring of the Tags class also including the coverage and execution plan tags.  
- Environment variables now uses a fallback in order `PROCESS -> USER -> MACHINE`

Fixed:
- Span duration time precision.
- Coverage DataCollector SourceRoot


## Scope .NET Agent v0.1.8

*June 17, 2019*

**Added:**

- Profiler support for multiple assembly versions interceptors.
- Code coverage by test support.
- MongoDB instrumentation
- `SCOPE_AUTO_INSTRUMENT`, `SCOPE_SET_GLOBAL_TRACER` and `SCOPE_TESTING_MODE` Environment variables.
- MessagePack format as default serializer in the `HttpClientDispatcherTransport` 
- Database query execution plan support for `SqlServer`, `Postgress` and `MySql`

**Changed:**
- Sampling logic moved from instrumentation to the dispatcher.
- Exception log writer moved to the OpenTracing log extensions.

**Fixed:**
- Random generator collision, removing the default generator for a cryptographic one.
- Span error tags issues.


## Scope .NET Agent v0.1.7

*May 27, 2019*

**Added:**
- `Microsoft.Data.Sqlite` database client instrumentation. 
- Automatic `Microsoft.Extensions.Logging.LoggerFactory` instrumentation by profiler.
- `OSX-X64` Profiler version.
- `ScopeAgent.Runner` ApiEndpoint and ApiKey validation.

**Changed:**
- Static pending task collection on the `Profiler.AsyncHandling` to an `AsyncLocal` version.

**Fixed:**
- Await test result `Task` and the status report issue on `NUnit framework`.
- Duration problem with unit test returning Tasks with parallel execution on `xUnit framework`.
- Agent results url.


## Scope .NET Agent v0.1.6

*May 17, 2019*

**Added:**
- .NET Framework 4.7.2 compilation.
- `AppVeyor CI` support.
- `Azure Pipelines CI` support.
- `Bitbucket Pipelines CI` support.
- `AgentSettings` class with all agent supported settings and instrumentation switches.
- Opentracing extension to know if the span context is marked as sampled.
- Incoming HttpServer `SpanContext` modes support (`All Requests`, `TestTraceKind`, `Sampled`).
- `Web Proxy` support on the `HttpDispatcher`.
- Detect the .NET language and add it to the test span as `language`.
- Agent results url when the `scope-run` command has finished.

**Changed:**
- Global debug interface performance optimizations.
- Debug concat performance optimizations.
- Stacktrace frames cache optimization.
- `Microsoft.Extensions.DependencyModel` is no longer required on the target project.
- Compilation in `Release` mode.
- Remove all `Linq` dependencies to reduce allocations and closures.
- Reduce Dispatcher allocations using the object pool.
- Reducing allocations by removing `Task.Unwrap()` when is not needed.
- Adding the required arguments to the `InvokeWithRetry` method avoiding the allocation of a closure class.
- Adding the BadRequest status code to avoid the retry in that case.
- Reducing the retry count from 10 to 5.

**Fixed:**
- Exception handling on `Tracer.Dispose`.
- Exception when `SourceRoot` is null.
- Skipped tests were not being sent to the backend.
- Exception handling on `Dispatcher.Flush`.


## Scope .NET Agent v0.1.5

*May 08, 2019*

**Added:**
- `NLog` target logger support.
- `NLog` profiler auto instrumentation.
- `ScopeEventContext` class with `event_id` and without `baggage`.
- `log4net` logger appender.
- `log4net` profiler auto instrumentation.
- `ApplyNtpOffset` method to the `Clock` class.
- `StackExchange.Redis` profiler auto instrumentation.

**Changed:**
- Dispatcher changes to be compatible with the `ScopeEventContext`.
- ScopeTracer now stores the `Timestamp` when the exception is thrown, so we can log exactly the time of the exception when the `UnhandledException` event is fired.

**Fixed:**
- Events timestamp with the NTP offset.
- Scope agent debug interface filepaths.
- Profiler method wrappers Task return value finalization.
- Other smaller fixes.


## Scope .NET Agent v0.1.4

*April 30, 2019*

**Added:**
- `.NET Core 2.1` support
- Added support to overwrite event tag in a log item
- Serilog sink logger support
- Serilog profiler auto instrumentation
- Add `agent.type` metadata to: `dotnet`
- Add `VERBOSE` log level

**Changed:**
- MSTest, NUnit and xUnit `Assert` exception with `event tag` as `test_failure`
- Reduce `ScopeAgent.Core` package dependencies
- Remove the target project dependency on the `ScopeAgent.Runner`
- Optimized version to get randomId using `stackalloc`
- Fix typo in the runner help
- `HttpClientDispatcher` now recognize the healthcheck payload and cached it to reduce cpu and allocation cost
- `FileDispatcherTransport` ignores the healthcheck payload when writing the payload to disk
- `Span creation rule:` Server HTTP span is created only if the baggage of the context has `trace.kind = test`
- `Span creation rule:` Client HTTP span is created only if we have a previous active span
- `Span creation rule:` DB client span is created only if we have a previous active span
- Exception extensions refactoring and public interfaces

**Fixed:**
- Fix `Microsoft.Extensions.Logger` structured exception support
- Fix typo in the runner help
- Fix standard span tags and log fields according the semantic conventions


## Scope .NET Agent v0.1.3

*April 26, 2019*

 **Added:**
- New native profiler engine for win-x64 and linux-x64 that hooks at low level to the dotnet runtime to instrument the test automatically without source code modification.
- New `ScopeAgent.Runner` package. A dotnet core global tool called `scope-run`, to configure the profiler automatically before running the desired command.
- NTP Network time support
- `SqlCommand` parameters supports on span tags.
- Autodetect git info for TravisCI and GitlabCI

**Changed:**
- Clock uses the NTP time (`pool.ntp.org`) on creation with a fallback to the previous `DateTime.UTCNow`
- Single `Global.Diagnostics` debug interface to write all agent debugging info


## Scope .NET Agent v0.1.2

*April 12, 2019*

**Added:**
- New structured exception format, used to display interactive stacktraces in Scope's UI.



## Scope .NET Agent v0.1.1

*April 09, 2019*

**Added:**
- Span log extensions null check.
- Package icon url and authors metadata
- ObjectPool to recycle objects and reduce memory allocations.

**Changed:**
- **Breaking change:** LogLevels enum namespace change, from: `ScopeAgent.Utils.Tags.Log.LogLevels` to `ScopeAgent.LogLevels`.
- Increase the clock resolution with a high frequency timer, changing the `DateTime.UTCNow` approach to a `Stopwatch.GetTimestamp()`
- Ensures the stackframe source line for span logs is inside the source root.
- The metadata is now being cached to reduce allocations.
- The scope dispatcher is now being called every `ScopeDispatcherSettings.FlushFrequencyInMs` (default 1000ms) with or without data in the buffer.

**Fixed:**
- NullReferenceException when a stacktrace doesn't have any stackframe.
- Race condition over the Tracer get in the ScopeTestExecutor (used on all testing frameworks)


## Scope .NET Agent v0.1.0

*April 05, 2019*

Initial agent release




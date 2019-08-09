---
id: dotnet-release-notes
title: Scope .NET Agent release notes
sidebar_label: Release notes
---


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




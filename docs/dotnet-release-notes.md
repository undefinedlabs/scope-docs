---
id: dotnet-release-notes
title: Scope .NET Agent release notes
sidebar_label: Release notes
---


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




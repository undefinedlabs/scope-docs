---
id: csharp-release-notes
title: Scope C# Agent release notes
sidebar_label: Release notes
---


## Scope C# Agent v0.1.3

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


## Scope C# Agent v0.1.2

*April 12, 2019*

**Added:**
- New structured exception format, used to display interactive stacktraces in Scope's UI.



## Scope C# Agent v0.1.1

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


## Scope C# Agent v0.1.0

*April 05, 2019*

Initial agent release




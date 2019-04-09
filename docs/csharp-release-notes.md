---
id: csharp-release-notes
title: Release notes
sidebar_label: Release notes
---


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




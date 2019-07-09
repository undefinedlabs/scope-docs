---
id: java-release-notes
title: Scope Java Agent release notes
sidebar_label: Release notes
---


## Scope Java Agent v0.1.6

*June 28, 2019*

**Added**
- Added test classes to `test.coverage` info.

**Fixed**
- Fixed `test.coverage` information using `JDK 11`.
- Fixed avoid being mandatory to have `gRPC` in the classpath.


## Scope Java Agent v0.1.5

*June 27, 2019*

**Added**
- Added `gRPC` `v1.4.0 to latest` client instrumentation.
- Added `gRPC` `v1.4.0 to latest` server instrumentation. 
- Added `test.coverage` info per test execution using `JaCoCo`.
- Added `JMS` and `Spring-JMS` `v1.1 to latest` messaging instrumentation.  
- Added support to configure `Scope` via `scope.toml` configuration file.

**Changed**
- Changed `db.statement` to reflect native SQLs and `db.prepared_statement` to reflect SQL prepared statements.
- Changed `boolean` extraction logic for Environment Variables.
- Changed `test.coverage` format to implement `Scope Universal Code Coverage` format.

**Fixed**
- Fixed `Baggage` `trace.kind = test` is only set on testing frameworks instrumentation.
- Fixed avoid stopping `Scope Sender` by `JVM` before sending all `ScopeSpans`. 


## Scope Java Agent v0.1.4

*June 10, 2019*

**Added**
- Support ```MySQL``` ```v8.x``` instrumentation.
- Support ```H2 (DBMS)``` ```v1.4.x``` instrumentation.
- Added Scope Report URL to log when build finished.
- Added auto-detection of ```metadata.repository``` based on ```.git``` folder.
- Added auto-detection of ```metadata.commit``` based on ```.git``` folder.
- Added environment variables detection for ```Travis CI```.
- Added environment variables detection for ```GitLab```.
- Added environment variables detection for ```Azure Pipelines```.
- Added environment variables detection for ```BitBucket Pipelines```.
- Added environment variables detection for ```AppVeyor```.
- Support `SCOPE_AUTO_INSTRUMENT` flag to activate/deactivate instrumentation.
- Support `SCOPE_SET_GLOBAL_TRACER` flag to activate/deactivate ScopeTracer as GlobalTracer.
- Support `SCOPE_TEST_MODE` flag to set flush interval to one second/one minute.

**Fixed**
- Fixed ```NPE``` on logging instrumentation when there is no active ```Span```.
- Fixed ```OkHttpClient``` connection leaked error.
- Fixed empty information Spans on ```H2 (DBMS)```.
- Fixed duplicate Spans on ```commit```/```rollback``` operations.
- Fixed avoid symbolicating source frames with line number ```-1```.
- Fixed avoid creating `span.kind=client` Spans if there is no previous active `Span`.
- Fixed `ScopeAgent` to initialize only one time if it is used in several Maven plugins.
- Fixed `exception.error.object` field to support `Exception` with self-references.
- Fixed issue about closing `io.opentracing.Scope` when the `Span` finishes.


## Scope Java Agent v0.1.3

*May 30, 2019*

**Added**

- Support ```java.net (HttpURLConnection)``` instrumentation.
- Support ```Apache Tomcat``` instrumentation from ```v7.x``` to ```v9.x```.

**Changed**

- Removed `event.exception.file` and `event.exception.line` if there is no attached source code.
- Added `event.exception.java` information about `StackTraceElement` object. 
- Removed ```(``` ```)``` characters for JUnit5 Test Names.

**Fixed**
- Fixed `event` value to lower case in `JUnit5`.


## Scope Java Agent v0.1.2

*May 14, 2019*

**Added**
- Supported absolute source code info in Span.
- Supported absolute source code info in Exception events.
- Supported absolute source code info in Logging events.
- Added ```event.context.event_id``` to avoid duplicated Events.
- Added ```agent.type``` in Metadata.
- Added synchronization Span/Event timestamps using NTP offset.
- Support instrumentation ```JUnit5``` Test Framework.
- Support instrumentation ```TestNG``` Test Framework.

**Changed**
- Span ```span.test.code``` has been renamed to ```span.source```.
- Span ```span.test.framework``` now shows the test framework used to create tests.

**Fixed**
- Fixed instrumentation ```OkHttp3 Client v3.12.x``` in ```JDK1.7```.


## Scope Java Agent v0.1.1

*May 07, 2019*

**Added**

- Send structured exceptions when error or exception is thrown in JUnit4 tests.
- Support instrumentation SLF4J Logging
- Support instrumentation OkHttp3 Client


## Scope Java Agent v0.1.0

*April 24, 2019*

Initial agent release




---
id: java-release-notes
title: Scope Java Agent release notes
sidebar_label: Release notes
---


## Scope Java Agent v0.5.2

*March 12, 2020*

**Fixed**
- Fixed detection `testingMode` on `ScalaTests`.


## Scope Java Agent v0.5.1

*March 09, 2020*

**Fixed**
- Fixed request / response payloads instrumentation regression added in version `0.5.0`.


## Scope Java Agent v0.5.0

*March 06, 2020*

**Added**
- Added `stacktrace` to `HTTP` client spans (opt-in)
- Added `stacktrace` to `DB` client spans (opt-in)
- Added support for `OkHttp3` version `4.x.y`

**Changed**
- Changed `ByteBuddy` version to v`1.10.8`.

**Fixed**
- Fixed `http.request.payload` data in HTTP spans.


## Scope Java Agent v0.4.0

*March 04, 2020*

**Added**
- Added limit of spans and events per request.
- Added retries on HTTP 500 on sending to Scope Backend.

**Fixed**
- Fixed `Opentelemetry` `tracestate` header.
- Fixed NPE when Git diff is being calculated.
- Fixed Throwable serialization on Exception events.
- Fixed starting agent on Runtime due to spans buffers size.
- Fixed showing logs when agent runs on Runtime.


## Scope Java Agent v0.3.2

*February 28, 2020*

**Added**
* Added `GITHUB_RUN_ID` and `GITHUB_RUN_NUMBER` for GitHub actions build.


## Scope Java Agent v0.3.1

*February 21, 2020*

**Added**
- Added the capability to use tilde for home user dir in unix systems.


## Scope Java Agent v0.3.0

*February 20, 2020*

**Added**
- Added logic to support `OpenTelemetry` inject and extract `tracecontext`. 
- Added `agent.metadata.testing` flag based on if a testing framework is present on classpath.
- Added `tracestate` header with `tracer.baggage` content.
- Added support for `TeamCity` CI.
- Added support for `Buildkite` CI.
- Added improvement to Log traces when Span info cannot be captured.
- Added improvement to Log traces when Scope Agent could not be started.

**Changed**
- Changed `ByteBuddy` version to `1.10.7`.
- Changed log traces to avoid showing `SCOPE_APIKEY` and `SCOPE_API_ENDPOINT`.
- Changed configuration based on new `scope.yaml` spec.

**Fixed**
- Fixed `scope.medatada` yaml to use dictionaries.
- Fixed prevent to send `null` version in ingest `User-Agent`.
- Fixed coverage session propagation.
- Fixed start coverage session on `JUnit5` tests.
- Fixed start coverage session on `TestNG` tests.
- Fixed ignore active span on `Benchmark` tests.
- Fixed avoid sending coverage info if filepath is `null`.
- Fixed avoid error on SLF4J instrumentation on MockLoggers.
- Fixed class loading prevalence of same classes with different version.


## Scope Java Agent v0.2.4

*December 13, 2019*

**Changed**

- Changed `User-Agent` to `scope-agent-java/VERSION`.


## Scope Java Agent v0.2.3

*November 29, 2019*

**Changed**
- Changed code path config property to `SCOPE_CODE_PATH`.
- Changed `TEST_ERROR` status into `TEST_FAILED` status.


## Scope Java Agent v0.2.2

*November 18, 2019*

**Added**
- Added dependencies to `agent.metadata` based on `Maven`, `Gradle` and `Coursier` on platforms `Unix` and `Windows`.

**Fixed**
- Fixed Code Coverage reporting `null` filepath in some packages.
- Fixed `test.coverage` to return correct start/end boundary.


## Scope Java Agent v0.2.1

*November 04, 2019*

**Added**
- Added capability to hide sensible information on datastores spans.
- Added `http.response_payload` info on HTTP spans.
- Added `http.response_headers` and `http.request_headers` on `HTTP` spans.
- Added `language` tag to `scala` on `ScalaTest` and `Scala` frameworks.
- Added support to use `SCOPE_DSN` has configuration for `SCOPE_APIKEY` and `SCOPE_API_ENDPOINT`.
- Added `response.body` on `Sender` log message.
- Added print all `ScopeSettings` in `DEBUG` log level.
- Added `Statistics` on spans remote reporting.
- Added `configuration` in `agent.metadata`. 
- Added filename and line number in not symbolicated exceptions stacktrace object.
- Added `db.statement.unavailable=disabled` info when DB statements are disabled.
- Added `SCOPE_CONFIG_FILE` as environment variable to set the config file path manually.
- Added `fileName` attribute on stack frames.
- Added instrumentation for benchmark `JMH` for `v1.x`.

**Changed**
- Changed log information to show to user based on number of failed tests.
- Changed set real `http.status_code` when `Tomcat` or `Netty` throws an exception.
- Changed `scope.test_aggregations` by `scope.metadata`.
- Changed `http.payload` on requests and responses from `null` to empty string.

**Fixed**
- Fixed support `nested classes` on `JUnit5` tests.
- Fixed instrumentation for Runtime mode.
- Fixed `git` information on Runtime/Local environment.
- Fixed prevent `JVM` does not finish when `ScopeAgent` is run on Runtime.
- Fixed prevent sending `healthcheck` info every second if it is not `testing.mode=true`


## Scope Java Agent v0.2.0

*October 02, 2019*

**Added**
- Added fallback endpoint to `app.scope.dev` if `$SCOPE_API_ENDPOINT` EnvVar is not set.
- Added `Scala` support from `2.10` to `2.13`.
- Added `ScalaTest` support from `2.2.x` to `3.0.x`.
- Added `Netty` support for versions `4.1.x.`.
- Added `Akka Actors` support for versions `2.3.x` to `2.5.x`.
- Added `Akka HTTP` support for versions `10.0.x` to `10.1.x`

**Changed**
- Changed `ByteBuddy` to `v1.9.16`.
- Changed context propagation on `Thread`/`Executor` instrumentation to avoid using reflection.
- Changed `CI_PROVIDER` on `GitHub Actions` to `GitHub`.
- Changed use of `ScopeGlobalTracer` instead of `GlobalTracer` as default tracer facade.
- Changed default value for `SCOPE_SET_GLOBAL_TRACER` to false.

**Fixed**
- Fixed support for configuration files with extension `.yaml` and `.yml`.
- Fixed avoid applying coverage context propagation if coverage is not configured.
- Fixed `NPE` on Jenkins settings due to `SOURCE_ROOT` setting.
- Fixed set `error=true` when `HTTP 400` on `Akka HTTP`.


## Scope Java Agent v0.1.9

*September 10, 2019*

**Added**
- Added support for async/concurrent code coverage.
- Added support for code coverage in server mode.
- Added logic to use env var `SCOPE_LOG_ROOT_PATH` to set custom log file root path.
- Added support to send aggregations info in agent metadata.
- Added instrumentation for `Apache HttpClient` `4.3` to `4.5.9`.
- Added support for `GitHub Actions` as `CI` provider. 
- Added hashes based on `parameterized tests` on `JUnit4`, `JUnit5` and `TestNG`
- Added support to configure `Logger` level threshold.

**Changed**
- Changed propagation context to avoid using `gRPC Context`.
- Changed `test.coverage` by removing uncovered code lines information.
- Changed coverage format to use an array `[line, column, count]` on boundaries.
- Changed `Scope` configuration file from `TOML` to `YAML` syntax.
- Changed `test.name` to avoid hash iterations on `JUnit4` and `JUnit5`.

**Fixed**
- Fixed `JUnit4` iteration extraction from `test.name` on parameterized tests.
- Fixed avoid formatting log events with empty parameters array.
- Fixed send spans/events every second in `SERVER` mode if they exist.
- Fixed avoid parsing `null` payloads con coverage.
- Fixed set correct logger level on start/end coverage session.
- Fixed use `SOURCE_ROOT` as root path to gather source code files.
- Fixed support `ForkJoinPool` to propagate `Context` for active span.


## Scope Java Agent v0.1.8

*August 09, 2019*

**Added**
- Added `Scope` statistics based on log file.
- Added support to configure `Scope` credentials based on selected profile by native app.
- Added a credential checker of `SCOPE_APIKEY` and `SCOPE_API_ENDPOINT` before starting `ScopeTracer`.
- Added external configuration properties for `Scope` reporter and sender.
- Added support to add code coverage by configuration property.
- Added automatization testing for every version of each instrumented library.
- Added support for `test.code` and `source` to `Kotlin` projects.
- Added support for `Parameterized` test on `JUnit4`, `JUnit5` and `TestNG`.

**Changed**
- Changed `Scope` log file path based on operative system.
- Changed `log` filename to include `commit` hash.

**Fixed**
- Fixed show `test.code` when test is kept on super classes.
- Fixed losing test spans when same test is launched multiple times in parallel on `JUnit4`.
- Fixed encoding mismatching to create `Scope` log filenames.
- Fixed `SourceCode` resolver errors when class is not loaded in the current test module.
- Fixed avoid agent exception when `log` file path cannot be created/accessed.


## Scope Java Agent v0.1.7

*July 12, 2019*

**Added**
- Added `branch` name to the `agent.metadata`.
- Added support propagation active `Span` between threads and thread pools.
- Added `diff` information about working directory to `agent.metadata`.
- Added `peer.service` tag, `test.language` tag, and `component` tag to `span` metadata.
- Added `test.code` information to the test `Span`.
- Added additional logs when `ScopeAgent` sends info to backend.

**Changed**
- Changed `span.db.params` format to the `Scope DB Params` standard format.
- Changed `span.operationName` max 255 chars with Ellipsis.

**Fixed**
- Fixed avoid sending logging events when `NOP` Logger is configured.
- Fixed `NPE` on `test` instrumentation.
- Fixed `NPE` on `JUnit5 uniqueId`.
- Fixed parameter type extraction on `H2 JDBC` instrumentation.
- Fixed `NPE` on `SLF4J` instrumentation.
- Fixed link with start and end line representation.
- Fixed `MsgPack` serialization due to `Jackson` version.
- Fixed report all `Ignored` tests when `Ignored` annotation is set at class level in `JUnit4`.
- Fixed `test.code` link based on inner classes.
- Fixed avoid reporting `Span` with empty `test.suite` tag in JUnit5.
- Fixed avoid using `STOUT` to print logs.
- Fixed avoid show `logging` traces when log level is not enabled.


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




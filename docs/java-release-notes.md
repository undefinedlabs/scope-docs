---
id: java-release-notes
title: Scope Java Agent release notes
sidebar_label: Release notes
---


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




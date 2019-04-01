---
id: ios-release-notes
title: Release notes
sidebar_label: Release notes
---


## Scope iOS Agent v0.1.18

*April 01, 2019*

**Fixed**

* Fixed potential crash when handling end of asynchronous child Spans


## Scope iOS Agent v0.1.17

*March 25, 2019*

**Added**

* `ScopeAgent` now adds `opentracing` as a dependency when installed with CocoaPods. It allows the use of `opentracing` APIs natively from the application/framework when linking with ScopeAgent.

**Changed**

* **Breaking change**: `SALogger.log()` can now be used without the level parameter. This changes the order of the parameters.

**Fixed**

* No previous traces are lost when a test crashes.
* Fixed a potential thread race condition when adding logs from several threads.



## Scope iOS Agent v0.1.16

*March 15, 2019*

**Fixed**

* Fixed a bug when trying to call `SALogger.log()` from applications that link to `ScopeAgent`


## Scope iOS Agent v0.1.15

*March 15, 2019*

**Added**

* `ScopeAgent` now exposes `SALogger.log()` for applications to send custom log events to Scope


## Scope iOS Agent v0.1.13

*March 08, 2019*

**Added**

* Created a thin client library called `ScopeAgentClient` that can be linked with applications for logging to Scope without affecting bundle size




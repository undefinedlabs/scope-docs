---
id: ios-release-notes
title: Scope iOS Agent release notes
sidebar_label: Release notes
---


## Scope iOS Agent v0.2.2

*May 23, 2019*

**Added**
* Automatically integrate NSLog, os_log  and print directives to Scope Logs (they will appear with level notSet)
* Use ntp synchronisation to improve integration with other services
* Improved start time and crash time to show microseconds granularity
* Document that option `DWARF with dSYM` file is needed for symbolicating stack traces

**Fixed**
* Some logs could appear twice under some conditions
* Some spans could potentially get lost in some rare situations
* Use thread name or queue name in crash exception
* Error level messages now shows as log event instead of as error event
* Improved accuracy of asynchronous activity


## Scope iOS Agent v0.2.1

*April 30, 2019*

**Added**
* Added Carthage support and documentation 
* Added documentation and support for GitLab CI and Travis CI

**Fixed**
* Some spans were sent duplicated after a crash and were never shown in results
* Spans that crashed could appear with shorter duration than real, even with duration 0


## Scope iOS Agent v0.2.0

*April 17, 2019*

**Added**
* Support for Xcode 10.2 and Swift 5
* Support for fully symbolicated stack traces
* Added documentation and script for uploading project symbols
* Documentation about adding HTTP headers for integration with server tracing
* Print errors when sending spans to server fail
* Retry sending spans to server in some failures
* Added CI metadata to spans

**Changed**
* In `SALogger.log()` function, first parameter is now of type `String?`  instead of `Any?`
* Updated KSCrash library to newest version

**Fixed**
* Potential thread-race condition in KSCrash library 
* Full compatibility with opentracing  0.5.0


## Scope iOS Agent v0.1.19

*April 03, 2019*

**Added**

* Published a new `ScopeAgent.CSURLSessionObserver` class to help adding headers to URLRequests from the client code.
* Added ScopeAgent version to headers

**Fixed**

* Baggage was not correctly being added to Spans and could not be sent in the HTTP headers



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




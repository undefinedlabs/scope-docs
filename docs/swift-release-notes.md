---
id: swift-release-notes
title: Scope Swift Agent release notes
sidebar_label: Release notes
---


## Scope Swift Agent v0.6.0

*May 05, 2020*

**Added**
* Support for Intelligent test runner, only runs tests that check that code changed between commits (needs Xcode 11.4+)
* Support for runtime skipped tests in XCTest (needs Xcode 11.4+)
* Add support for runtime evaluated metadata values, it was documented but not implemented
* Support for unfinished spans, spans that were started during a test and not finished are now also reported to the backend.
* Support for more CI: Bitbucket Pipelines, AppVeyor and Azure Pipelines
* Add testing bundle to test spans in `test.traits`tag


**Changed**
* **Test Environment variables for XCode** (Check documentation for exact changes for your CI)
* Reduced size of data sent to Scope
* Added msgpack format for sending tests results
* Agent is now compiled with Xcode 11.4
* Improved error messages


## Scope Swift Agent v0.5.13

*April 21, 2020*

**Fixed**
* Code Path was not complete when using Xcode 11.4+


## Scope Swift Agent v0.5.12

*April 16, 2020*

**Fixed**
* Code Path was not working with Scope release v.1.10.3 (released in app.scope.dev on 16 April)


## Scope Swift Agent v0.5.10

*April 13, 2020*

**Fixed**
* Code Path was not working when using Xcode 11.4 to compile and run tests



## Scope Swift Agent v0.5.9

*March 16, 2020*

**Fixed**
* Fixed Code Path when paths generated from build files contained space character
* Some errors were still reporting Scope APIKEY instead of SCOPE_DSN 


## Scope Swift Agent v0.5.8

*March 09, 2020*

**Added**
* Save Code coverage on crashed tests
* Limit the number of logs to 10000 per span

**Fixed**
* Avoid long delays when sending data if there are too many spans or events.


## Scope Swift Agent v0.5.7

*March 02, 2020*

**Added**
* Support GitHub Actions Run ID and Run Number

**Fixed**
* CodePath was not being generated in some projects


## Scope Swift Agent v0.5.6

*February 27, 2020*

**Fixed**
* CodePath was not being generated correctly in some projects


## Scope Swift Agent v0.5.5

*February 17, 2020*

**Fixed**
* Manual testing was not being loaded properly


## Scope Swift Agent v0.5.4

*February 13, 2020*

**Added**
* Support for adding agent metadata
* Agent metadata can be selected as test configuration
* Additional HTTP Headers can be added to HTTP span tags
* Support for Buildkite CI

**Changed**
* Agent can now handle when environment variables include newline and/or space characters at the end
* Network instrumentation overhead reduced for non instrumented calls
* Improve error messages from scope_upload and process-coverage scripts

**Fixed**
* Symbols sometimes were not uploaded properly. 


## Scope Swift Agent v0.5.3

*January 29, 2020*

**Fixed**
* Swift SPM projects were not reporting tests properly


## Scope Swift Agent v0.5.2

*January 28, 2020*

**Changed**
* Rename agent to Swift, changing agent.type metadata 
* Lower deployment target for the agent to versions (10.0 for iOS and tvOS and 10.12 for macOS)
* Improve information when some error happens during testing.

**Fixed**
* Writing log file sometimes could produce a crash when the tests ended.
* User-Agent header was being modified when instrumenting network calls



## Scope Swift Agent v0.5.1

*January 22, 2020*

**Added**
* Support for macOS and tvOS projects

**Changed**
* **Important for Cocoapods configuration**: upload_symbols and scope-coverage paths have changed, check documentation for new paths and reconfigure project
* Path for Carthage distribution is now  `https://releases.undefinedlabs.com/scope/agents/carthage/ScopeAgent.json`

**Fixed**
* SCOPE_DSN now supports including newline and `/` characters at the end


## Scope Swift Agent v0.5.0

*January 22, 2020*

**Added**
* Support for macOS and tvOS projects

**Changed**
* **Important for Cocoapods configuration**: upload_symbols and scope-coverage paths have changed, check documentation for new paths and reconfigure project
* Path for Carthage distribution is now  `https://releases.undefinedlabs.com/scope/agents/carthage/ScopeAgent.json`


## Scope Swift Agent v0.4.4

*January 13, 2020*

**Added**
* Agent writes a log file with all the logs generated from agent. This file is saved in `Library/Logs` folder of the app running in the simulator/device
* Support for TeamCity CI

**Fixed**
* Duration of the first test run was higher than it should


## Scope Swift Agent v0.4.3

*December 23, 2019*

**Changed**
* Improve Code Path evaluation time with big binaries


## Scope Swift Agent v0.4.2

*December 18, 2019*

**Fixed**
* Code Path information failed to generate in with complex code


## Scope Swift Agent v0.4.1

*December 16, 2019*

**Added**
* **Code Path** functionality when project configured properly (see documentation)
* SCOPE_DSN global variable replaces both SCOPE_APIKEY and SCOPE_API_ENDPOINT
* SCOPE_XCODE_DSN global variables replaces both SCOPE_XCODE_APIKEY and SCOPE_XCODE_API_ENDPOINT
* Library dependencies for the test run

**Fixed**
* URLSession methods that used URL directly where not adding instrumentation headers
* Symbols upload was not working if endpoint was not set, now it reports to app.scope.dev by default

**Changed**
* **Previous ERROR and FAIL status for tests are now unified in FAIL status**
* Updated Scope Logo in manual testing
* Xcode 11.2.1 used for building the framework


## Scope Swift Agent v0.4.0

*November 28, 2019*

**Added**
* **Code Path** functionality when project configured properly (see documentation)
* SCOPE_DSN global variable replaces both SCOPE_APIKEY and SCOPE_API_ENDPOINT
* SCOPE_XCODE_DSN global variables replaces both SCOPE_XCODE_APIKEY and SCOPE_XCODE_API_ENDPOINT
* Library dependencies for the test run

**Fixed**
* URLSession methods that used URL directly where not adding instrumentation headers
* Symbols upload was not working if endpoint was not set, now it reports to app.scope.dev by default

**Changed**
* **Previous ERROR and FAIL status for tests are now unified in FAIL status**
* Updated Scope Logo in manual testing
* Xcode 11.2.1 used for building the framework


## Scope Swift Agent v0.3.3

*October 31, 2019*

**Added**
* Support for iOS 13 Applications that use UIWindowScene
* Report empty payloads when payload instrumentation is configured (Scope was not reporting the payload when empty)

**Fixed**
* Disabling network instrumentation was not working
* Automatic network instrumentation could make some requests fail
* Some instrumentation was being initialised before checking the environment variable


## Scope Swift Agent v0.3.2

*October 18, 2019*

**Fixed**
* Manual testing UI was not drawing correctly with some Xcode 11.1 projects


## Scope Swift Agent v0.3.1

*October 15, 2019*

**Changed**
* Use SCOPE_INSTRUMENTATION_HTTP_CLIENT env variable to disable network instrumentation

**Fixed**
* Crash in agent when logging some requests


## Scope Swift Agent v0.3.0

*October 10, 2019*

**Added**
* Auto-intrumentation for Http requests and responses
* Added support for manual testing 
* Network spans include now the headers of requests and responses (filtering security sensible ones)
* Scope can include the payloads of the request/responses when configured with `SCOPE_INSTRUMENTATION_HTTP_PAYLOADS` environment variable
* Integrate Spans into native signpost interval, so if Scope is linked to the application the different spans will be seen as Signposts when profiling with Instruments

**Changed**
* Code added to instrument network requests or add instrumentation headers should not be needed now.
* Don't set Scope as global OpenTracing tracer by default( standard Opentracing calls will not be automatically captured by Scope)
* Scope.framework doesn't include complete OpenTracing library, if you want to use OpenTracing you need to link separately

**Fixed**
* Network responses were not being shown as children of the network request


## Scope Swift Agent v0.2.6

*September 19, 2019*

**Added**
* Support for Http instrumentation using `ScopeAgentClient.framework` 
* Option to add Http instrumentation through `URLSessionConfiguration` class

**Changed**
* License covering the code
* There is no need to use parameters when using scope-coverage
* Use SaaS endpoint by default if none is specified

**Fixed**
* Improve OpenTracing specification in network Spans


## Scope Swift Agent v0.2.5

*September 03, 2019*

**Added**
* Support for local development
* Spans of Network request that return an error, or spans where exceptions happened are marked as error themselves
* Support for Github Actions
* Full support for Xcode 11
* Coverage info per test (not activated)

**Fix**
* Previously agent could upload more symbols than needed if several configurations were being built
* Agent reported a malformed repository if none existed
* Small leak in network instrumentation
* Sometimes a test could report incorrect/negative duration after a crash 


## Scope Swift Agent v0.2.4

*July 09, 2019*

**Fixed**
* Some timestamps could appear rounded incorrectly
* Some extra empty lines could appear in logs
* Restore agent id after a crash happens during a test session, so all test session will use the same agent id
* Fix an issue that could lose spans when test name was very long
* Fix a crash when handling url's with data scheme

**Added**
* Support for disabling instrumentation
* Added NOTICE file with all the licenses used in project


## Scope Swift Agent v0.2.3

*June 10, 2019*

**Fixed**
* Some test spans could appear as child of previous spans when previous span had asynchronous code running after the test ended.
* Fixed potential crash when writing logs concurrently
* Multiline stderr messages could appear as a single log in Scope

**Added**
* Print URL for Scope results in output



## Scope Swift Agent v0.2.2

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


## Scope Swift Agent v0.2.1

*April 30, 2019*

**Added**
* Added Carthage support and documentation 
* Added documentation and support for GitLab CI and Travis CI

**Fixed**
* Some spans were sent duplicated after a crash and were never shown in results
* Spans that crashed could appear with shorter duration than real, even with duration 0


## Scope Swift Agent v0.2.0

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


## Scope Swift Agent v0.1.19

*April 03, 2019*

**Added**

* Published a new `ScopeAgent.CSURLSessionObserver` class to help adding headers to URLRequests from the client code.
* Added ScopeAgent version to headers

**Fixed**

* Baggage was not correctly being added to Spans and could not be sent in the HTTP headers



## Scope Swift Agent v0.1.18

*April 01, 2019*

**Fixed**

* Fixed potential crash when handling end of asynchronous child Spans


## Scope Swift Agent v0.1.17

*March 25, 2019*

**Added**

* `ScopeAgent` now adds `opentracing` as a dependency when installed with CocoaPods. It allows the use of `opentracing` APIs natively from the application/framework when linking with ScopeAgent.

**Changed**

* **Breaking change**: `SALogger.log()` can now be used without the level parameter. This changes the order of the parameters.

**Fixed**

* No previous traces are lost when a test crashes.
* Fixed a potential thread race condition when adding logs from several threads.



## Scope Swift Agent v0.1.16

*March 15, 2019*

**Fixed**

* Fixed a bug when trying to call `SALogger.log()` from applications that link to `ScopeAgent`


## Scope Swift Agent v0.1.15

*March 15, 2019*

**Added**

* `ScopeAgent` now exposes `SALogger.log()` for applications to send custom log events to Scope


## Scope Swift Agent v0.1.13

*March 08, 2019*

**Added**

* Created a thin client library called `ScopeAgentClient` that can be linked with applications for logging to Scope without affecting bundle size




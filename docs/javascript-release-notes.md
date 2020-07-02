---
id: javascript-release-notes
title: Scope Javascript Agent release notes
sidebar_label: Release notes
---


## Scope Javascript Agent v0.7.3

*June 24, 2020*

#### Fixed
- Fix compatibility issues with development in Windows.
- Fix minor bugs. 
- Fallback to NTP offset when connectivity to NTP servers is not possible. 




## Scope Javascript Agent v0.7.2

*June 02, 2020*

#### Added
- Requests done via `cy.request` are now instrumented

#### Fixed
- Cypress support file no longer attempts to import files from the file system under some circumstances. 
- `cy.spy` and `cy.stub` can now be safely used for `window.fetch` and `console` functions. 


## Scope Javascript Agent v0.7.1

*May 27, 2020*

#### Fixed
- Fix a bug where test code would not appear in Cypress under some circumstances. 
- Fix a bug where failed snapshot tests were not retried with the intelligent test runner. 


## Scope Javascript Agent v0.7.0

*May 07, 2020*

#### Changed
- Trace IDs are now 128 bits. **Note:** all agents involved in a trace must be updated to support 128 bits.


## Scope Javascript Agent v0.6.1

*May 05, 2020*

#### Fixed
- Fix logic in skipping tests with intelligent test runner.
- Fix minor bugs.


## Scope Javascript Agent v0.6.0

*April 29, 2020*

#### Added
- Intelligent Test Runner support: automatically cache tests that are not affected by your commit changes.
- Automatically retry failed tests.

#### Changed
- HTTP connections are kept alive.
- Add option to set global tracer for opentracing.



## Scope Javascript Agent v0.5.2

*April 23, 2020*

#### Fixed
- `~` is properly expanded in source root.




## Scope Javascript Agent v0.5.1

*April 23, 2020*

#### Fixed
- `~` is properly expanded in source root.




## Scope Javascript Agent v0.5.0

*April 15, 2020*

#### Added
- **Code Path**: You may now run your tests with per test code coverage.

#### Changed
- Remove dependency on `jest-jasmine2` and `jest-runner`.
- Change `jest` configuration: now using `globalSetup` and not using `runner` anymore.



## Scope Javascript Agent v0.4.2

*April 02, 2020*

#### Fixed
- Fixed travis URL in builds.
- Fix bug in fetch instrumentation.
- Fix retry logic in ingest. 



## Scope Javascript Agent v0.4.1

*March 25, 2020*

#### Changed
- cypress instrumentation has been improved with more robust ingests.

#### Fixed
- Fixed bug where the agent would crash with older node versions. 



## Scope Javascript Agent v0.4.0

*March 23, 2020*

#### Added
- [`pg`](https://node-postgres.com/features/queries) test and runtime instrumentation support. 
- [`node-redis`](https://github.com/NodeRedis/node-redis) test and runtime instrumentation support.
- A message is logged when `SCOPE_DSN` is not set and tests run just like they would without Scope. 
- You may now add custom metadata to the agent through configuration.
- Support for `keydown` events in `jsdom`. 


#### Changed
- Improve connection with the ingest backend.
- Limit number of events per span. 

#### Fixed
- Traces are flushed when the process is shut down in runtime instrumentation. 
- Minor bugs and inconsistencies fixed.
- Fix http instrumentation bugs.


## Scope Javascript Agent v0.3.9

*February 26, 2020*

#### Fixed
- Fix release tag





## Scope Javascript Agent v0.3.8

*February 26, 2020*

#### Fixed
- Fix minor bugs





## Scope Javascript Agent v0.3.7

*February 17, 2020*

#### Fixed
- Fix 4xx and 5xx http responses not being shown as errors yet.





## Scope Javascript Agent v0.3.6

*February 07, 2020*

#### Added
- Add support for BuildKite.
- Richer agent metadata like node versions, cypress version and more.
- Now a link to the results is shown after jest tests are run.

#### Changed
- `fetch` instrumentation in jest is now richer.
- 4xx and 5xx http responses are shown as error spans.





## Scope Javascript Agent v0.3.5

*January 27, 2020*

#### Changed
- Testing mode can now be controlled via `SCOPE_TESTING_MODE` env variable, to distinguish between runtime and testing instrumentation.  


## Scope Javascript Agent v0.3.4

*December 19, 2019*

#### Changed
- Auto instrumentation is enabled by default.


## Scope Javascript Agent v0.3.3

*December 12, 2019*

#### Changed
- User agent is now sent as http header in ingest



## Scope Javascript Agent v0.3.2

*December 03, 2019*

#### Added
- Added support for CI: Travis, Jenkins, Gitlab, AppVeyor, Azure Pipelines, Bitbucket pipelines, GitHub and TeamCity. 
- Support for DSN.
- Send dependencies as agent metadata. 

#### Changed
- The agent is now resilient to missing configuration. 
- Update test suite and test name.
- Improve the distribution of the package. 

#### Fixed
- All jest test status are now supported.
- Missing spans in cypress due to race conditions should now appear.



## Scope Javascript Agent v0.3.1

*November 28, 2019*

#### Changed
- Improve Node.js automatic instrumentation.


## Scope Javascript Agent v0.3.0

*November 27, 2019*

#### Added
- Add support for global exceptions in jest.
- Add support for global click events.

#### Changed
- Better ingest management.
- Better automatic instrumentation.
- Remove `testing-library/react` and `node-fetch` specific instrumentations.

#### Fixed
- Errored spans are now sending `error=true` as span tag.


## Scope Javascript Agent v0.2.5

*November 26, 2019*

#### Added
- Add support for node js libraries: `express` and  `node-fetch`.
- Add support for `console`: console logs now appear as span events.
- Add support for `fetch` in ui tests: they now appear as new spans.

#### Fixed
- Timing is now correctly calculated for tests shorter than 1ms.
- Better calculation and higher resolution in time calculations for start times and durations.

#### Changed
- The automatic instrumentation is now done through a jest `runner` and `testRunner` instead of a `reporter`.



## Scope Javascript Agent v0.2.4

*November 20, 2019*

#### Added
- Support for `@testing-library/react`.
- Improve time resolution in test duration.


## Scope Javascript Agent v0.2.3

*October 31, 2019*

#### Added
- Add request type for http requests.
- Control http aborts.
- Send incomplete http spans as `incomplete` for easier debugging.


## Scope Javascript Agent v0.2.2

*October 16, 2019*

#### Fixed
- Redacted http headers are now case insensitive.
- No unnecessary json stringify on strings.
- `fetch` instrumentation in cypress is more robust.

#### Changed
- Better Formatting Of HTTP Payloads.


## Scope Javascript Agent v0.1.3

*September 16, 2019*

#### Added
- Add support for Jest.
- Add support for Cypress. 




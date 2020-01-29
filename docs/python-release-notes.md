---
id: python-release-notes
title: Scope Python Agent release notes
sidebar_label: Release notes
---


## Scope Python Agent v0.3.11

*January 28, 2020*

### Added
* A link to the test results is shown in the console after your tests are run.
* It is now possible to configure whether to show DB statements in the span metadata.
* It is now possible to add custom headers in your HTTP instrumentation. 

### Changed
* `psycopg2` instrumentation has been updated with more metadata. 



## Scope Python Agent v0.3.10

*January 20, 2020*

### Fixed
* Fix wrong repository url for GitHub Actions. 
* Fix wrong initialisation of agent for runtime instrumentation. 


## Scope Python Agent v0.3.9

*January 17, 2020*

### Added
* Add support for [pytest-benchmark](https://pypi.org/project/pytest-benchmark/)
* Instrumentation of HTTP headers and payloads.
* Add `testing` metadata to distinguish runtime and testing implementation.
* Add project dependencies to the agent metadata.
* Add support for adding arbitrary metadata to the agent.



## Scope Python Agent v0.3.8

*December 19, 2019*

### Fixed
* Autoinstrumentation is now active by default 


## Scope Python Agent v0.3.7

*December 18, 2019*

#### Added
* Instrumentation for [Uvicorn](https://www.uvicorn.org) (ASGI server).
* Add support for `DSN`.
* Remove error state (now only fail).
* Add support for more CIs: AppVeyor, Azure Pipelines, Bitbucket pipelines, GitHub and TeamCity.


## Scope Python Agent v0.3.6

*October 09, 2019*

#### Added
* The agent now reports the `agent.type` metadata field

#### Changed
* By default, the API endpoint is now set to `https://app.scope.dev`
* The instrumentation now reports directly to the Scope tracer, but it can be configured to report to any OpenTracing-compatible tracer programmatically.
* The Scope tracer will now not be automatically configured as OpenTracing's global tracer, but can still be set manually if desired.

#### Fixed
* Fixed a bug where some CLI flags were not being parsed properly
* Fixed support for process forking after the agent has been initialized


## Scope Python Agent v0.3.5

*September 10, 2019*

#### Added

* Allow installing the agent in code without passing any config (and use autodetection).
* Added support for Django and Flask.

#### Changed

* Dropped compatibility with Python 3.4.

#### Fixed

* Flush span/event buffer if not empty every second regardless of healthcheck period (testing mode).
* Ensure health checks are sent even if no spans are generated.
* Log messages with level "ERROR" are now correctly marked as events of type "log".
* Fixed dry run behaviour.
* Fixed a compatibility issue when using the agent in conjunction with the Sentry SDK.


## Scope Python Agent v0.3.4

*August 09, 2019*

#### Added

* Support for the local development feature of Scope.
* Autodetect git information when using installation of the agent via code.
* Add flags to activate/deactivate autodetection of git information, testing mode, global tracer setup and autoinstrumentation.
* Events now have information about the source code line where they were generated.

#### Changed

* HTTP client and server spans that have a status code of 4xx or 5xx are marked with `error = True`.
* Spans with uncaught exceptions are marked with `error = True`.
* Use MessagePack serialization when sending data to the backend.

#### Fixed

* Test code end line number is now properly calculated.


## Scope Python Agent v0.3.3

*May 07, 2019*

**Added**

- Autodetect git information for TravisCI and GitLab CI.
- Send structured stacktraces to Scope.
- Send `extra` logging attributes as event metadata fields.



## Scope Python Agent v0.3.2

*April 17, 2019*

**Added**

* Agent will now ensure that messages are sent continuously to the backend for it to detect running state.

**Fixed**

* Fixed `test.code` attribute for skipped tests
* Fixed passing `--api-endpoint` on the `scope-run` CLI


## Scope Python Agent v0.3.1

*April 02, 2019*

**Added**

* PostgreSQL (`psycopg2`) automatic instrumentation

**Fixed**

* Properly report platform version on the `platform.version` metadata tag.
* Force tag values to be of an opentracing-compatible type.
* Allow any type that is JSON-serializable for event field values.
* Fixed WSGI instrumentation when using a `ClosingIterator`.


## Scope Python Agent v0.3.0

*March 20, 2019*

**Added**

* Add required `--api-endpoint/$SCOPE_API_ENDPOINT` parameter
* Autodetect commit, repository and source root path information for CircleCI and Jenkins providers
* Added custom user agent header when sending data to Scope


## Scope Python Agent v0.2.0

*March 08, 2019*

Initial agent version




---
id: python-release-notes
title: Scope Python Agent release notes
sidebar_label: Release notes
---


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




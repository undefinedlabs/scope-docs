---
id: python-release-notes
title: Scope Python Agent release notes
sidebar_label: Release notes
---


## <a href="https://github.com/undefinedlabs/scope-python-agent/releases/tag/0.3.5" target="_blank">Scope Python Agent v0.3.5</a>

*September 10, 2019*

#### Added

* Allow installing the agent in code without passing any config (and use autodetection).
* Added support for Django and Flask.

#### Changed

* The agent is now open source with an Apache 2.0 license.
* Dropped compatibility with Python 3.4.

#### Fixed

* Flush span/event buffer if not empty every second regardless of healthcheck period (testing mode).
* Ensure health checks are sent even if no spans are generated.
* Log messages with level "ERROR" are now correctly marked as events of type "log".
* Fixed dry run behaviour.
* Fixed a compatibility issue when using the agent in conjunction with the Sentry SDK.


## <a href="https://github.com/undefinedlabs/scope-python-agent/releases/tag/0.3.4" target="_blank">Scope Python Agent v0.3.4</a>

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


## <a href="https://github.com/undefinedlabs/scope-python-agent/releases/tag/0.3.3" target="_blank">Scope Python Agent v0.3.3</a>

*May 07, 2019*

**Added**

- Autodetect git information for TravisCI and GitLab CI.
- Send structured stacktraces to Scope.
- Send `extra` logging attributes as event metadata fields.



## <a href="https://github.com/undefinedlabs/scope-python-agent/releases/tag/0.3.2" target="_blank">Scope Python Agent v0.3.2</a>

*April 17, 2019*

**Added**

* Agent will now ensure that messages are sent continuously to the backend for it to detect running state.

**Fixed**

* Fixed `test.code` attribute for skipped tests
* Fixed passing `--api-endpoint` on the `scope-run` CLI


## <a href="https://github.com/undefinedlabs/scope-python-agent/releases/tag/0.3.1" target="_blank">Scope Python Agent v0.3.1</a>

*April 02, 2019*

**Added**

* PostgreSQL (`psycopg2`) automatic instrumentation

**Fixed**

* Properly report platform version on the `platform.version` metadata tag.
* Force tag values to be of an opentracing-compatible type.
* Allow any type that is JSON-serializable for event field values.
* Fixed WSGI instrumentation when using a `ClosingIterator`.


## <a href="https://github.com/undefinedlabs/scope-python-agent/releases/tag/0.3.0" target="_blank">Scope Python Agent v0.3.0</a>

*March 20, 2019*

**Added**

* Add required `--api-endpoint/$SCOPE_API_ENDPOINT` parameter
* Autodetect commit, repository and source root path information for CircleCI and Jenkins providers
* Added custom user agent header when sending data to Scope


## <a href="https://github.com/undefinedlabs/scope-python-agent/releases/tag/0.2.0" target="_blank">Scope Python Agent v0.2.0</a>

*March 08, 2019*

Initial agent version




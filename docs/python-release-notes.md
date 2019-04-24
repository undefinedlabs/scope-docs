---
id: python-release-notes
title: Scope Python Agent release notes
sidebar_label: Release notes
---


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




---
id: scope-for-chrome-release-notes
title: Scope For Chrome release notes
sidebar_label: Release notes
---

## Scope For Chrome v0.3.3

_October 23, 2019_

#### Fixed

- Test status is reset when discarding or starting a new recording.
- Minor bugs fixed in instrumentation.
- If there is no native app connectivity, an error is shown.

## Scope For Chrome v0.3.2

_October 16, 2019_

#### Added

- Default test name now appears when opening the popup.
- Url change event with origin and destination url.

#### Fixed

- Parse xhr headers to send an object, not a string.
- Protect against empty tab.
- Only apply open tracing headers if no CORS is required.
- Fix onreadystate monkey patching in XHR.
- Fix page reloads.
- Remove hostname from agent metadata.
- Append scripts on head instead of body (more robust).
- Relative urls are managed.

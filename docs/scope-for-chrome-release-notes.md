---
id: scope-for-chrome-release-notes
title: Scope For Chrome release notes
sidebar_label: Release notes
---


## Scope For Chrome v0.3.6

*December 13, 2019*

### Changed 
- Bump dependencies 


## Scope For Chrome v0.3.5

*November 11, 2019*

### Changed
- Update scope logo


## Scope For Chrome v0.3.4

*November 05, 2019*

### Added
- You will now see http spans for navigation requests (when you visit a webpage or `main_frame` requests).


### Changed
- Add manifest.json permissions to allow monitoring of web requests.
- Polished styling.

### Fixed
- Now user events should never be logged more than once under any circumstances. 
- Scope instance is correctly updated when changing it in the native app.
- Objects are now correctly recorded as event message in `console.log`.


## Scope For Chrome v0.3.3

*October 23, 2019*

### Fixed
- Test status is reset when discarding or starting a new recording.
- Minor bugs fixed in instrumentation.
- If there is no native app connectivity, an error is shown.


## Scope For Chrome v0.3.2

*October 16, 2019*

### Added
- Default test name now appears when opening the popup.
- Url change event with origin and destination url.

### Fixed
- Parse xhr headers to send an object, not a string.
- Protect against empty tab.
- Only apply open tracing headers if no CORS is required.
- Fix onreadystate monkey patching in XHR.
- Fix page reloads.
- Remove hostname from agent metadata.
- Append scripts on head instead of body (more robust).
- Relative urls are managed.





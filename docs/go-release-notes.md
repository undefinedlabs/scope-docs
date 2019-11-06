---
id: go-release-notes
title: Scope Go Agent release notes
sidebar_label: Release notes
---


## <a href="https://github.com/undefinedlabs/scope-go-agent/releases/tag/0.1.4" target="_blank">Scope Go Agent v0.1.4</a>

*October 11, 2019*

#### Added
* Added new options for agent configuration: `WithSetGlobalTracer` and `WithGitInfo`.

#### Changed
* Now, the agent will not be autoinstalled on package import. An agent instance needs to be manually created for runtime instrumentation, or the `scopeagent.Run` helper needs to be used for testing instrumentation. Check the Scope documentation for more details.



## <a href="https://github.com/undefinedlabs/scope-go-agent/releases/tag/0.1.3" target="_blank">Scope Go Agent v0.1.3</a>

*October 02, 2019*

#### Changed

* Deprecate the "autoinstrumentation" setting. Now, the `http.DefaultClient` needs to be instrumented manually by calling `nethttp.PatchHttpDefaultClient()` as per the documentation.


## <a href="https://github.com/undefinedlabs/scope-go-agent/releases/tag/0.1.2" target="_blank">Scope Go Agent v0.1.2</a>

*October 02, 2019*

#### Changed
* The instrumentation now reports directly to the Scope tracer, but it can be configured to report to any OpenTracing-compatible tracer programmatically.
* The Scope tracer will now not be automatically configured as OpenTracing's global tracer, but can still be set manually if desired.


## <a href="https://github.com/undefinedlabs/scope-go-agent/releases/tag/0.1.1" target="_blank">Scope Go Agent v0.1.1</a>

*September 30, 2019*

#### Added
* Add ability to programmatically create an agent with custom settings
* New convenience public APIs in `scopeagent` package

#### Changed
* The autoinstallation of the agent on package import will now silently fail if an API key could not be autodetected (to support programmatic installation)

#### Fixed
* Fixed a bug with multiline log events using the standard library's `log` package



## <a href="https://github.com/undefinedlabs/scope-go-agent/releases/tag/0.1.0" target="_blank">Scope Go Agent v0.1.0</a>

*September 24, 2019*

Initial release




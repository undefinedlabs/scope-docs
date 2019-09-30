---
id: go-release-notes
title: Scope Go Agent release notes
sidebar_label: Release notes
---


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




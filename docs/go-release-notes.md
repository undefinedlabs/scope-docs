---
id: go-release-notes
title: Scope Go Agent release notes
sidebar_label: Release notes
---


## <a href="https://github.com/undefinedlabs/scope-go-agent/releases/tag/0.1.11" target="_blank">Scope Go Agent v0.1.11</a>

*February 11, 2020*

**Fixes:**
- Scope log root path fix (#151)
- Recorder retry support for multiple error cases (#148)

**Changes:**
- Bump google.golang.org/grpc from 1.27.0 to 1.27.1 (#152)


## <a href="https://github.com/undefinedlabs/scope-go-agent/releases/tag/0.1.10" target="_blank">Scope Go Agent v0.1.10</a>

*February 11, 2020*

**Fixes:**
- Scope log root path fix (#151)
- Recorder retry support for multiple error cases (#148)

**Changes:**
- Bump google.golang.org/grpc from 1.27.0 to 1.27.1 (#152)


## <a href="https://github.com/undefinedlabs/scope-go-agent/releases/tag/0.1.9" target="_blank">Scope Go Agent v0.1.9</a>

*February 07, 2020*

**Fixes:**
- Lock in r.span reader to avoid race condition (#144)
- Avoid panic and agent failure in case of not DSN or ApiKey (#147)



## <a href="https://github.com/undefinedlabs/scope-go-agent/releases/tag/0.1.8" target="_blank">Scope Go Agent v0.1.8</a>

*February 06, 2020*

**Added:**
- Support Buildkite CI provider (#133)
- Auto Instrument without TestMain (#137)
- Runner configuration by env vars (#138)

**Changes:**
- Reflection refactor (#130)
- Remove http client events on normal requests, write if an error occurs (#140)

**Fixes:**
- Fix nil in Current User (#134)
- Checks if GetBody() is nil before call (#139)


## <a href="https://github.com/undefinedlabs/scope-go-agent/releases/tag/0.1.7" target="_blank">Scope Go Agent v0.1.7</a>

*January 31, 2020*

**Added:**
- Test retry support on fail.
- Go 1.11 support


## <a href="https://github.com/undefinedlabs/scope-go-agent/releases/tag/0.1.6" target="_blank">Scope Go Agent v0.1.6</a>

*January 30, 2020*

**Added:**
- Configuration metadata and configuration keys support.

**Changed:**
- Improvements in the grpc instrumentation (#126)

**Fixed:**
- Test results Url fix (#120)
- Fix http 401 response handler (#125)


## <a href="https://github.com/undefinedlabs/scope-go-agent/releases/tag/0.1.5" target="_blank">Scope Go Agent v0.1.5</a>

*January 23, 2020*

**Added:**
- Windows path support (#83)
- Benchmarks support (#84)
- SCOPE_DSN support (#87)
- TeamCity CI support (#89)
- Logs folder selection per platform (#86)
- Http client and server payload instrumentation (#88) 
- Sql instrumentation (#90)
- Test status tag values (#92)
- Agent id in payload first level (#93)
- Custom user agent support (#98) 
- Custom agent type support (#104) 
- Expose testing mode flag in agent metadata (#108)
- Extract dependencies from go mod graph if is available (#95) 
- Testing auto instrumentation (#102) 
- Benchmark auto instrumentation (#117) 
- Monkey patching on testing.T.common logging methods (#118) 

**Changed:**
- Do not finish parent span on HTTP client requests (#75)
- Calculate NTP offset in the recorder lazily
- Cmd OperationName (#82) 
- Release span lock before ingest call (#101)
- Logging as a separated instrumentation (#111) 
- Remove double panic (#114)


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




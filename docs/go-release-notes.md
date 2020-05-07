---
id: go-release-notes
title: Scope Go Agent release notes
sidebar_label: Release notes
---


## <a href="https://github.com/undefinedlabs/scope-go-agent/releases/tag/0.3.0" target="_blank">Scope Go Agent v0.3.0</a>

*May 07, 2020*

**Added:**
- Logrus instrumentation hook (#224) 
- Cached tests support - Intelligent Test Runner (#178)

**Changed:**
- Update dependencies (#226, #227, #228, #230)
- Show initialization error messages only if `SCOPE_DEBUG` is set (#229)
- Send metadata until at least one payload is successfully delivered (#182)
- Cryptorand logs in case of error (#232)
- Rand algorithm changes (#233)
- Trace IDs are now 128 bits. (#234)

**Fixed:**
- Metadata serialization data race (#231)

**NOTE:** all agents involved in a trace must be updated to support 128 bits.


## <a href="https://github.com/undefinedlabs/scope-go-agent/releases/tag/0.2.1" target="_blank">Scope Go Agent v0.2.1</a>

*April 16, 2020*

**Changed**
- Use `crypto/rand` to generate random seed (#223)

**Fixed**
- Avoid setting test source code if span is `nil` (#221)


## <a href="https://github.com/undefinedlabs/scope-go-agent/releases/tag/0.2.0" target="_blank">Scope Go Agent v0.2.0</a>

*April 13, 2020*

**Added**
- Added capability to set the function where the test source code is kept manually (#214)

**Changed**
- Calculation of the test suite and test name for subtests (#214)

**Fixed**
- Fixed Travis Build URL (#212)
- Fixed test start time when a test is marked as `t.Parallel()` (#214)
- Fixed bug in `t.Log` monkey patching methods, due a problem in Golang `reflect.makefunc` (#214)
- Avoid accessing 'agent.recoder' if not initialized (#216)



## <a href="https://github.com/undefinedlabs/scope-go-agent/releases/tag/0.1.15" target="_blank">Scope Go Agent v0.1.15</a>

*March 26, 2020*

**Fixed**
- Set Global Panic handler as agent option only on test autoinstrumentation (#208)


## <a href="https://github.com/undefinedlabs/scope-go-agent/releases/tag/0.1.14" target="_blank">Scope Go Agent v0.1.14</a>

*March 24, 2020*

**Fixed**
- Fixed wrong `file:line` on `testing.Test` error messages in terminal. (#206)


## <a href="https://github.com/undefinedlabs/scope-go-agent/releases/tag/0.1.13" target="_blank">Scope Go Agent v0.1.13</a>

*March 18, 2020*

**Added:**
- Adds BuildId and Build Number for GH Actions (#186) 
- Parallel flag detector for CodePath (#180) 
- Goroutines global panic handler (#188)
- Enable optional stacktrace tag in http and sql instrumentation. (#184) 
- Standard logger with context support (#131) 
- .git folder parser alternative without external dependencies (#197) 
- Support for projects without go.mod (#153) 
-  Adds panic stacktraces inside the logs (#202) 

**Changed:**
- Coverage detection (#168) 
- Recorder buffer refactor (#177) 
- Remove test.code empty (#192) 
- Forbid empty sourceroot and go.mod path finder (#194) 
- Ci branch and improved container detector (#201) 

**Fixed:**
- Fix support for import autoinstrument and TestMain scopeagent.Run (#145)
- Ensure the correct folder permissions when creating log folders (#183) 
- Try to extract request body payload when the `GetBody` func is nil (#189)
- Clean filepath to fix windows path issue (#172)
- Improves panic reports to scope and fixes source field on events (#170)
- Remove invalid peer.service tag (#198) 


## <a href="https://github.com/undefinedlabs/scope-go-agent/releases/tag/0.1.12" target="_blank">Scope Go Agent v0.1.12</a>

*February 19, 2020*

**Added:**
- Codepath implementation (#103)
- Expand '~' in source root (#159)
- Support to split a big payload in multiples payloads (#158)
- Http server instrumentation, panic support (#156)

**Changed:**
- Environment variables handler and missing keys (#154)
- Statement values instrumentation option rename (#161)
- SetTestingMode refactor (#163)
- Removes the ScopeDisableMonkeyPatching env var (#164)

**Fixes:**
- Fix go vet ./... in the agent (#155)
- Fixes retries response status code 400 (#157)
- Fixes panic handling of the agent runner (#160) 



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




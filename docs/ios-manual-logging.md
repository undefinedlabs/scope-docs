---
id: ios-manual-logging
title: Scope iOS Agent manual logging
sidebar_label: Manual logging
---

Scope captures `NSLog`, `print` and `os_log` (stdout and stderr) output automatically, and associates them to the active span when they were generated if possible, or to the test span otherwise.

In order for the Scope agent to capture information about the line of source code that generated each log event and use different log levels for later filtering, we recommend adding manual logging instrumentation, as described in the following sections.


## Manual instrumentation

### Installation

Link your application or framework target with `ScopeAgent`

<!--DOCUSAURUS_CODE_TABS-->
<!--Cocoapods-->
By adding the pod to your `Podfile` and running `pod install`. For example:

```
target 'MyApp' do
 pod 'ScopeAgent'
end
```

or

```
target 'MyFramework' do
 pod 'ScopeAgent'
end
```

<!--Carthage-->
Add the `ScopeAgent` dependency to your `Cartfile` if not already done in previous steps, and run `cart update`

```
binary "https://releases.undefinedlabs.com/scope/agents/ios/ScopeAgent.json"
```

In your application or framework targets, add `ScopeAgent.framework` located in `Carthage/Build/iOS` to the
*Linked frameworks and Libraries* in General target settings or to the *Link Binaries With Libraries* build phase. 

<!--END_DOCUSAURUS_CODE_TABS-->


### Using the thin client library

If linking the full `ScopeAgent` library to your main application is not an option, we provide a thin client package 
called `ScopeAgentClient` that provides the logging API described above and communicates with the full `ScopeAgent` 
library if it is present. With this approach, you link your main application with `ScopeAgentClient` and the tests target
with `ScopeAgent`, and all logs will be collected during your tests, with minimal impact to your distributable application. 

Install this dependency to your test targets by adding:

<!--DOCUSAURUS_CODE_TABS-->
<!--Cocoapods-->
```
target 'MyTests' do
 pod 'ScopeAgentClient'
end
```

<!--Carthage-->
```
binary "https://releases.undefinedlabs.com/scope/agents/ios/ScopeAgentClient.json"
```

<!--END_DOCUSAURUS_CODE_TABS-->


### Usage

Use the `SALogger.log()` method to send your log messages to Scope. The interface of `SALogger.log()` is as follows:

```swift
class SALogger {
   public class func log(_ message: String? = "",
                         _ logLevel: SALogger.LogLevel? = .notset,
                         filename: String? = nil,
                         line: Int? = nil,
                         fields extraFields: [String: Any]? = nil,
                         timestamp: Date? = nil )
}
```

You just need to call `SALogger.log()` with the proper parameters:

- `message`: any message or instance whose description will be logged in Scope

- `logLevel`: one of the following levels (default: `.notSet`)

```swift
enum LogLevel : String {
    case debug
    case info
    case warning
    case error
    case notset
}
```

- `filename:`: the name of the file where the log method is being called (default: the file where `SALogger.log()` was called)

- `line`: the line number of the file where the log method is being called (default: the line where `SALogger.log()` was called)`

- `fields`: optional dictionary to append extra info to the logs, only entries of the dictionary with values convertible to JSON will be appended.

- `timestamp`: the date and time when the log was written (default: the time when `SALogger.log()` was called)

Example code:

```swift
SALogger.log("HELLO FROM APP USING SCOPEAGENT")
```

or:

```swift
let url = URL(string: "http://httpbin.org/ip")!
let task = URLSession.shared.dataTask(with: url) { data,response,error  in
if let data = data {
   let string = String(data: data, encoding: .utf8)
   SALogger.log(string, .debug)
 }
}
task.resume()
```

or:

```swift
SALogger.log(items,
            .warning, 
            filename:fileName, 
            line:line, 
            fields: ["function Name":functionName])

```

---
id: ios-agent
title: iOS Agent instructions
sidebar_label: iOS Agent
---


## Compatibility

The Scope iOS agent is compatible with the following libraries:

* [XCTestCase](https://developer.apple.com/documentation/xctest/xctestcase)
* [Alamofire](https://github.com/Alamofire/Alamofire)


## Installation

Installation of the Scope Agent is done via [CocoaPods](https://cocoapods.org).

Add the `ScopeAgent` pod to the test target in your `Podfile`. For example:

```
target 'MyAppTests' do
  pod 'ScopeAgent'
end
```


## CI provider configuration

### Jenkins

Add the following environment variables to your test target ([instructions](https://help.apple.com/xcode/mac/10.1/index.html?localePath=en.lproj#/dev3ec8a1cb4)):

| Key                      | Value                       |
|--------------------------|-----------------------------|
| `SCOPE_APIKEY`           | `$(SCOPE_APIKEY)`           |
| `SCOPE_API_ENDPOINT`     | `$(SCOPE_API_ENDPOINT)`     |
| `SCOPE_COMMIT_SHA`       | `$(GIT_COMMIT)`             |
| `SCOPE_REPOSITORY`       | `$(GIT_URL)`                |
| `SCOPE_SOURCE_ROOT`      | `$(WORKSPACE)`              |

After this, configure your Jenkins build to add the following environment variables:

| Key                      | Value                                       |
|--------------------------|---------------------------------------------|
| `SCOPE_APIKEY`           | The API key generated from the Scope UI     |
| `SCOPE_API_ENDPOINT`     | The API endpoint of your Scope installation |



### CircleCI

Add the following environment variables to your test target ([instructions](https://help.apple.com/xcode/mac/10.1/index.html?localePath=en.lproj#/dev3ec8a1cb4)):

| Key                      | Value                         |
|--------------------------|-------------------------------|
| `SCOPE_APIKEY`           | `$(SCOPE_APIKEY)`             |
| `SCOPE_API_ENDPOINT`     | `$(SCOPE_API_ENDPOINT)`       |
| `SCOPE_COMMIT_SHA`       | `$(CIRCLE_SHA1)`              |
| `SCOPE_REPOSITORY`       | `$(CIRCLE_REPOSITORY_URL)`    |
| `SCOPE_SOURCE_ROOT`      | `$(CIRCLE_WORKING_DIRECTORY)` |

After this, configure your CircleCI project to add the following environment variables ([instructions](https://circleci.com/docs/2.0/env-vars/#setting-an-environment-variable-in-a-project)):

| Key                      | Value                                       |
|--------------------------|---------------------------------------------|
| `SCOPE_APIKEY`           | The API key generated from the Scope UI     |
| `SCOPE_API_ENDPOINT`     | The API endpoint of your Scope installation |
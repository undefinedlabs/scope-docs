---
id: ios-manual-testing
title: Scope iOS Agent Manual testing
sidebar_label: Manual testing
---

The Scope iOS agent allows you to perform manual tests on your application that will be recorded for later troubleshooting in Scope. You can either run your application from Xcode in your simulator or device, or distribute a build to your testers with the functionality built-in.

The results will appear in your **Local Development scratchpad** in Scope

## Installation

Link your application target with `ScopeAgent`

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

If you want to run your application from Xcode in your simulator or device, the following environment variables must be set in your **Run target** ([instructions](https://help.apple.com/xcode/mac/10.1/index.html?localePath=en.lproj#/dev3ec8a1cb4)):

| Key                        | Value                         |
| -------------------------- | ----------------------------- |
| `SCOPE_XCODE_APIKEY`       | `$(SCOPE_XCODE_APIKEY)`       |
| `SCOPE_XCODE_API_ENDPOINT` | `$(SCOPE_XCODE_API_ENDPOINT)` |

Alternatively, if you want to distribute the instrumented application (e.g. to the QA team), then you must add the following entries in your application's `Info.plist`:

| Key                  | Type     | Value                         |
| -------------------- | -------- | ----------------------------- |
| `SCOPE_APIKEY`       | `String` | `<Your Scope API key>`        |
| `SCOPE_API_ENDPOINT` | `String` | `<Your Scope API endpoint>`   |


## Usage

After the application launches, a floating Scope logo will appear in the screen over your application elements. When you want to start a test, click on the logo and provide the test with a name.

While the test is being recorded, the Scope logo will be glowing in red. To finish the test and stop the recording, click on the logo, and choose whether the test passed or failed. 

Manual tests will appear in your **Local Development scratchpad** section.


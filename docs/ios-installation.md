---
id: ios-installation
title: Scope iOS Agent instructions
sidebar_label: Installation
---

Installation of the Scope Agent is done via [CocoaPods](https://cocoapods.org) or [Carthage](https://github.com/Carthage/Carthage).

### CocoaPods

Add the `ScopeAgent` pod to the test target(s) in your `Podfile`. For example:

```ruby
target 'MyAppTests' do
  pod 'ScopeAgent'
end
```

Then, run `pod install` to install the agent in your project.


### Carthage

Add the `ScopeAgent` dependency to your `Cartfile`:

```
binary "https://releases.undefinedlabs.com/scope/agents/ios/ScopeAgent.json"
```

Then, run `cart update` to install the agent in your project.

In your test target(s), add `ScopeAgent.framework` located in `Carthage/Build/iOS` to the `Link Binaries With Libraries` build phase.

> Currently, the official OpenTracing library for iOS only supports installation using Cocoapods. If you are interested in adding custom traces with OpenTracing to your app using Carthage, please use [https://github.com/undefinedlabs/opentracing-objc](https://github.com/undefinedlabs/opentracing-objc)


## Instrumenting your tests

After installation, you can run your tests as you normally do, for example using the `xcodebuild test` command. 
Tests, network requests and application logs will be instrumented automatically.


## CI provider configuration

Add the following environment variables to your test target ([instructions](https://help.apple.com/xcode/mac/10.1/index.html?localePath=en.lproj#/dev3ec8a1cb4)):

<!--DOCUSAURUS_CODE_TABS-->
<!--Jenkins-->
| Key                      | Value                       |
|--------------------------|-----------------------------|
| `SCOPE_APIKEY`           | `$(SCOPE_APIKEY)`           |
| `SCOPE_API_ENDPOINT`     | `$(SCOPE_API_ENDPOINT)`     |
| `SCOPE_COMMIT_SHA`       | `$(GIT_COMMIT)`             |
| `SCOPE_REPOSITORY`       | `$(GIT_URL)`                |
| `SCOPE_SOURCE_ROOT`      | `$(WORKSPACE)`              |
| `JENKINS_URL`            | `$(JENKINS_URL)`            |
| `BUILD_ID`               | `$(BUILD_ID)`               |
| `BUILD_NUMBER`           | `$(BUILD_NUMBER)`           |
| `BUILD_URL`              | `$(BUILD_URL)`              |

<!--CircleCI-->
| Key                      | Value                         |
|--------------------------|-------------------------------|
| `SCOPE_APIKEY`           | `$(SCOPE_APIKEY)`             |
| `SCOPE_API_ENDPOINT`     | `$(SCOPE_API_ENDPOINT)`       |
| `SCOPE_COMMIT_SHA`       | `$(CIRCLE_SHA1)`              |
| `SCOPE_REPOSITORY`       | `$(CIRCLE_REPOSITORY_URL)`    |
| `SCOPE_SOURCE_ROOT`      | `$(CIRCLE_WORKING_DIRECTORY)` |
| `CIRCLECI`               | `$(CIRCLECI)`                 |
| `CIRCLE_BUILD_NUM`       | `$(CIRCLE_BUILD_NUM)`         |
| `CIRCLE_BUILD_URL`       | `$(CIRCLE_BUILD_URL)`         |

<!--GitLab CI-->
| Key                  | Value                   |
| -------------------- | ----------------------- |
| `SCOPE_APIKEY`       | `$(SCOPE_APIKEY)`       |
| `SCOPE_API_ENDPOINT` | `$(SCOPE_API_ENDPOINT)` |
| `SCOPE_COMMIT_SHA`   | `$(CI_COMMIT_SHA)`      |
| `SCOPE_REPOSITORY`   | `$(CI_REPOSITORY_URL)`  |
| `SCOPE_SOURCE_ROOT`  | `$(CI_PROJECT_DIR)`     |
| `GITLAB_CI`          | `$(GITLAB_CI)`          |
| `CI_JOB_ID`          | `$(CI_JOB_ID)`          |
| `CI_JOB_URL`         | `$(CI_JOB_URL)`         |

<!--Travis-->
| Key                   | Value                      |
| --------------------- | -------------------------- |
| `SCOPE_APIKEY`        | `$(SCOPE_APIKEY)`          |
| `SCOPE_API_ENDPOINT`  | `$(SCOPE_API_ENDPOINT)`    |
| `SCOPE_COMMIT_SHA`    | `$(TRAVIS_COMMIT)`         |
| `SCOPE_SOURCE_ROOT`   | `$(TRAVIS_BUILD_DIR)`      |
| `TRAVIS`              | `$(TRAVIS)`                |
| `TRAVIS_REPO_SLUG`    | `$(TRAVIS_REPO_SLUG)`      |
| `TRAVIS_BUILD_ID`     | `$(TRAVIS_BUILD_ID)`       |
| `TRAVIS_BUILD_NUMBER` | `$(TRAVIS_BUILD_NUMBER)`   |

<!--GitHub Actions-->
| Key                  | Value                   |
| -------------------- | ----------------------- |
| `SCOPE_APIKEY`       | `$(SCOPE_APIKEY)`       |
| `SCOPE_API_ENDPOINT` | `$(SCOPE_API_ENDPOINT)` |
| `SCOPE_COMMIT_SHA`   | `$(GITHUB_SHA)`         |
| `SCOPE_SOURCE_ROOT`  | `$(GITHUB_WORKSPACE)`   |
| `GITHUB_REPOSITORY`  | `$(GITHUB_REPOSITORY)`  |

<!--END_DOCUSAURUS_CODE_TABS-->


After this, add the following environment variables to your CI provider:

| Environment variable  | Default value           | Description                                            |
|-----------------------|-------------------------|--------------------------------------------------------|
| `$SCOPE_APIKEY`       |                         | API key to use when sending data to Scope              |
| `$SCOPE_API_ENDPOINT` | `https://app.scope.dev` | API endpoint of the Scope installation to send data to |


## Local development integration

For running tests in your local Xcode installation, the following environment variables must set in your **Test target** ([instructions](https://help.apple.com/xcode/mac/10.1/index.html?localePath=en.lproj#/dev3ec8a1cb4)):

| Key                        | Value                         |
| -------------------------- | ----------------------------- |
| `SCOPE_XCODE_APIKEY`       | `$(SCOPE_XCODE_APIKEY)`       |
| `SCOPE_XCODE_API_ENDPOINT` | `$(SCOPE_XCODE_API_ENDPOINT)` |

These environment variables are set automatically by the native Scope for Mac application that you can download from the **Local development/Scratchpad** area of Scope.

The following command must also be run on the terminal:

```bash
defaults write com.apple.dt.Xcode UseSanitizedBuildSystemEnvironment -bool NO
```

After these steps, after running your tests locally in Xcode, you will get a test report in Scope with the results.


## Uploading symbol files

By default, crash stack traces will be partially symbolicated. In order to fully symbolicate them and show file and line information,
you must run the following script as part of your build phase for the test targets:

1. First, make sure your Xcode project is configured to generate the debug symbols file:

   1. Click on your project and select **Build Settings**.
   2. On **Debug Information Format** confirm **DWARF with dSYM File** is selected.

2. Select your test target from the **Projects and Targets** view.

3. Open the target's **Build Phases** tab.

4. Click **+ Add a new build phase**, then select **New Run Script Phase**.

5. Add the following line to the **Type a script** text box

**For Cocoapods:**

```bash
${PODS_ROOT}/ScopeAgent/ScopeAgent.framework/upload_symbols
```

**For Carthage:**

```bash
${SRCROOT}/Carthage/Build/iOS/ScopeAgent.framework/upload_symbols
```

or the path where the Carthage folder is located.

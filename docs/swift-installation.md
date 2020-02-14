---
id: swift-installation
title: Scope Swift Agent instructions
sidebar_label: Installation
---

## Using GitHub Actions

You can simply add a step to your GitHub Actions workflow YAML that uses the [scope-for-swift-action](https://github.com/marketplace/actions/scope-for-swift) action:

```yaml
steps:
  - name: Checkout
    uses: actions/checkout@v1
  - name: Scope for Swift
    uses: undefinedlabs/scope-for-swift-action@v1
    with:
      dsn: ${{ secrets.SCOPE_DSN }} #required
```

You can find further information of this action at the [GitHub Marketplace](https://github.com/marketplace/actions/scope-for-swift), for further configuration. No more steps are needed to run you tests in Scope.

Start using Scope with the [Getting Started iOS with GitHub Actions](https://github.com/scope-demo/scope-ios-actions-starter) right now!

## Manual installation

Manual installation of the Scope Agent is done via [CocoaPods](https://cocoapods.org) or [Carthage](https://github.com/Carthage/Carthage).

#### CocoaPods

Add the `ScopeAgent` pod to the test target(s) in your `Podfile`. For example:

```ruby
target 'MyAppTests' do
  pod 'ScopeAgent'
end
```

Then, run `pod install` to install the agent in your project.


#### Carthage

Add the `ScopeAgent` dependency to your `Cartfile`:

```ruby
binary "https://releases.undefinedlabs.com/scope/agents/carthage/ScopeAgent.json"
```

Then, run `cart update` to install the agent in your project.

In your test target(s), add `ScopeAgent.framework` located in `Carthage/Build/<platform>` to the `Link Binaries With Libraries` build phase.

> Currently, the official OpenTracing library only supports installation using Cocoapods. If you are interested in adding custom traces with OpenTracing to your app using Carthage, please use [https://github.com/undefinedlabs/opentracing-objc](https://github.com/undefinedlabs/opentracing-objc)


### Instrumenting your tests

After installation, you can run your tests as you normally do, for example using the `xcodebuild test` command. 
Tests, network requests and application logs will be instrumented automatically.


### CI provider configuration

Add the following environment variables to your test target ([instructions](https://help.apple.com/xcode/mac/10.1/index.html?localePath=en.lproj#/dev3ec8a1cb4)):

<!--DOCUSAURUS_CODE_TABS-->
<!--Jenkins-->
| Key                      | Value                       |
|--------------------------|-----------------------------|
| `SCOPE_DSN`              | `$(SCOPE_DSN)`              |
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
| `SCOPE_DSN`              | `$(SCOPE_DSN)`                |
| `SCOPE_COMMIT_SHA`       | `$(CIRCLE_SHA1)`              |
| `SCOPE_REPOSITORY`       | `$(CIRCLE_REPOSITORY_URL)`    |
| `SCOPE_SOURCE_ROOT`      | `$(CIRCLE_WORKING_DIRECTORY)` |
| `CIRCLECI`               | `$(CIRCLECI)`                 |
| `CIRCLE_BUILD_NUM`       | `$(CIRCLE_BUILD_NUM)`         |
| `CIRCLE_BUILD_URL`       | `$(CIRCLE_BUILD_URL)`         |

<!--GitLab CI-->

| Key                  | Value                   |
| -------------------- | ----------------------- |
| `SCOPE_DSN`          | `$(SCOPE_DSN)`          |
| `SCOPE_COMMIT_SHA`   | `$(CI_COMMIT_SHA)`      |
| `SCOPE_REPOSITORY`   | `$(CI_REPOSITORY_URL)`  |
| `SCOPE_SOURCE_ROOT`  | `$(CI_PROJECT_DIR)`     |
| `GITLAB_CI`          | `$(GITLAB_CI)`          |
| `CI_JOB_ID`          | `$(CI_JOB_ID)`          |
| `CI_JOB_URL`         | `$(CI_JOB_URL)`         |

<!--Travis-->
| Key                   | Value                      |
| --------------------- | -------------------------- |
| `SCOPE_DSN`           | `$(SCOPE_DSN)`             |
| `SCOPE_COMMIT_SHA`    | `$(TRAVIS_COMMIT)`         |
| `SCOPE_SOURCE_ROOT`   | `$(TRAVIS_BUILD_DIR)`      |
| `TRAVIS`              | `$(TRAVIS)`                |
| `TRAVIS_REPO_SLUG`    | `$(TRAVIS_REPO_SLUG)`      |
| `TRAVIS_BUILD_ID`     | `$(TRAVIS_BUILD_ID)`       |
| `TRAVIS_BUILD_NUMBER` | `$(TRAVIS_BUILD_NUMBER)`   |

<!--GitHub Actions-->

| Key                  | Value                   |
| -------------------- | ----------------------- |
| `SCOPE_DSN`          | `$(SCOPE_DSN)`          |
| `SCOPE_COMMIT_SHA`   | `$(GITHUB_SHA)`         |
| `SCOPE_SOURCE_ROOT`  | `$(GITHUB_WORKSPACE)`   |
| `GITHUB_REPOSITORY`  | `$(GITHUB_REPOSITORY)`  |

<!--TeamCity-->

| Key                 | Value                  |
| ------------------- | ---------------------- |
| `SCOPE_DSN`         | `$(SCOPE_DSN)`         |
| `SCOPE_COMMIT_SHA`  | `$(BUILD_VCS_NUMBER)`  |
| `SCOPE_REPOSITORY`  | `$(BUILD_VCS_URL)`     |
| `SCOPE_SOURCE_ROOT` | `$(BUILD_CHECKOUTDIR)` |
| `BUILD_ID`          | `$(BUILD_ID)`          |
| `BUILD_NUMBER`      | `$(BUILD_NUMBER)`      |
| `SERVER_URL`        | `$(SERVER_URL)`        |

For `TeamCity`, additional environment variables must be exposed from the Teamcity `Parameters` section:

| Name                    | Value                          |
| ----------------------- | ------------------------------ |
| `env.BUILD_CHECKOUTDIR` | `%teamcity.build.checkoutDir%` |
| `env.BUILD_ID`          | `%teamcity.build.id%`          |
| `env.BUILD_VCS_URL`     | `%vcsroot.url%`                |

<!--Buildkite-->

| Key                      | Value                              |
| ------------------------ | ---------------------------------- |
| `SCOPE_DSN`              | `$(SCOPE_DSN)`                     |
| `SCOPE_COMMIT_SHA`       | `$(BUILDKITE_COMMIT)`              |
| `SCOPE_REPOSITORY`       | `$(BUILDKITE_REPO)`                |
| `SCOPE_SOURCE_ROOT`      | `$(BUILDKITE_BUILD_CHECKOUT_PATH)` |
| `BUILDKITE_BUILD_ID`     | `$(BUILDKITE_BUILD_ID)`            |
| `BUILDKITE_BUILD_NUMBER` | `$(BUILDKITE_BUILD_NUMBER)`        |
| `BUILDKITE_BUILD_URL`    | `$(BUILDKITE_BUILD_URL)`           |

<!--END_DOCUSAURUS_CODE_TABS-->


After this, add the following environment variables to your CI provider:

| Environment variable | Description                                                  |
| -------------------- | ------------------------------------------------------------ |
| `$SCOPE_DSN`        | Data source name (DSN) of Scope to be used when reporting results |


### Local development integration

For running tests in your local Xcode installation, the following environment variables must set in your **Test target** ([instructions](https://help.apple.com/xcode/mac/10.1/index.html?localePath=en.lproj#/dev3ec8a1cb4)):

| Key                        | Value                         |
| -------------------------- | ----------------------------- |
| `SCOPE_XCODE_DSN`          | `$(SCOPE_XCODE_DSN)`          |

These environment variables are set automatically by the native Scope for Mac application that you can download from the **Local development/Scratchpad** area of Scope.

The following command must also be run on the terminal:

```bash
defaults write com.apple.dt.Xcode UseSanitizedBuildSystemEnvironment -bool NO
```

After these steps, after running your tests locally in Xcode, you will get a test report in Scope with the results.


### Uploading symbol files

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

<!--DOCUSAURUS_CODE_TABS-->
<!--iOS-->
```bash
${PODS_ROOT}/ScopeAgent/ios/ScopeAgent.framework/upload_symbols
```
<!--Mac-->
```bash
${PODS_ROOT}/ScopeAgent/mac/ScopeAgent.framework/Resources/upload_symbols
```
<!--tvOS-->
```bash
${PODS_ROOT}/ScopeAgent/tvos/ScopeAgent.framework/upload_symbols
```

<!--END_DOCUSAURUS_CODE_TABS-->

**For Carthage:**

<!--DOCUSAURUS_CODE_TABS-->
<!--iOS-->
```bash
${SRCROOT}/Carthage/Build/iOS/ScopeAgent.framework/upload_symbols
```
<!--Mac-->
```bash
${SRCROOT}/Carthage/Build/Mac/ScopeAgent.framework/Resources/upload_symbols
```
<!--tvOS-->
```bash
${SRCROOT}/Carthage/Build/tvOS/ScopeAgent.framework/upload_symbols  
```
<!--END_DOCUSAURUS_CODE_TABS-->

### Code Path Support

To enable code path support for your tests, follow these steps:

1. First, make sure your Xcode project is configured to generate the debug symbols file:

   1. Click on your project and select **Build Settings**.
   2. On **Debug Information Format** confirm **DWARF with dSYM File** is selected

2. Enable code coverage in the "Test" action of your scheme ([instructions](https://help.apple.com/xcode/mac/10.1/index.html?localePath=en.lproj#/dev9e0e09978))

3. In the "Test" action of your scheme, add the following script to the "Post-actions" section (You can add a `Run Script Action` post-action expanding the disclosure triangle ![img](https://help.apple.com/xcode/mac/10.1/en.lproj/Art/sce_schemeeditor_disclosuretriangleicon.png) next to the "Test" action "Post-actions")

   **For Cocoapods:**

<!--DOCUSAURUS_CODE_TABS-->
<!--iOS-->
   ```bash
   ${PODS_ROOT}/ScopeAgent/ios/ScopeAgent.framework/scope-coverage
   ```
<!--Mac-->

   ```bash
   ${PODS_ROOT}/ScopeAgent/mac/ScopeAgent.framework/Resources/scope-coverage
   ```
<!--tvOS-->

   ```bash
   ${PODS_ROOT}/ScopeAgent/tvos/ScopeAgent.framework/scope-coverage
   ```
<!--END_DOCUSAURUS_CODE_TABS-->

   **For Carthage:**

<!--DOCUSAURUS_CODE_TABS-->
<!--iOS-->
   ```bash
   ${SRCROOT}/Carthage/Build/iOS/ScopeAgent.framework/scope-coverage
   ```
<!--Mac-->

   ```bash
   ${SRCROOT}/Carthage/Build/Mac/ScopeAgent.framework/Resources/scope-coverage
   ```
<!--tvOS-->

   ```bash
   ${SRCROOT}/Carthage/Build/tvOS/ScopeAgent.framework/scope-coverage
   ```
<!--END_DOCUSAURUS_CODE_TABS-->

   In the "Provide Build Setting" combo select the **Target Application** that will run the tests

4. If your target also supports UI testing, for every **UITest target** you must duplicate the previous `Run Script Action` and select the **UITest target** in the "Provide Build Setting" combo.

   

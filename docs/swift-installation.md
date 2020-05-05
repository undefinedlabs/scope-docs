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

Then, run `carthage update` to install the agent in your project.

In your test target(s), add `ScopeAgent.framework` located in `Carthage/Build/<platform>` to the `Link Binaries With Libraries` build phase.

> Currently, the official OpenTracing library only supports installation using Cocoapods. If you are interested in adding custom traces with OpenTracing to your app using Carthage, please use [https://github.com/undefinedlabs/opentracing-objc](https://github.com/undefinedlabs/opentracing-objc)


### Instrumenting your tests

After installation, you can run your tests as you normally do, for example using the `xcodebuild test` command. 
Tests, network requests and application logs will be instrumented automatically.

### Environment variables


#### CI provider configuration

Add the following environment variables to your test target ([instructions](https://help.apple.com/xcode/mac/10.1/index.html?localePath=en.lproj#/dev3ec8a1cb4)):

<!--DOCUSAURUS_CODE_TABS-->
<!--Jenkins-->
| Key                      | Value                       |
|--------------------------|-----------------------------|
| `SCOPE_DSN`              | `$(SCOPE_DSN)`              |
| `GIT_COMMIT`             | `$(GIT_COMMIT)`             |
| `GIT_URL`                | `$(GIT_URL)`                |
| `WORKSPACE`              | `$(WORKSPACE)`              |
| `GIT_BRANCH`             | `$(GIT_BRANCH)`             |
| `JENKINS_URL`            | `$(JENKINS_URL)`            |
| `BUILD_ID`               | `$(BUILD_ID)`               |
| `BUILD_NUMBER`           | `$(BUILD_NUMBER)`           |
| `BUILD_URL`              | `$(BUILD_URL)`              |

<!--CircleCI-->
| Key                        | Value                         |
|--------------------------- |-------------------------------|
| `SCOPE_DSN`                | `$(SCOPE_DSN)`                |
| `CIRCLE_SHA1`              | `$(CIRCLE_SHA1)`              |
| `CIRCLE_REPOSITORY_URL`    | `$(CIRCLE_REPOSITORY_URL)`    |
| `CIRCLE_WORKING_DIRECTORY` | `$(CIRCLE_WORKING_DIRECTORY)` |
| `CIRCLE_BRANCH `           | `$(CIRCLE_BRANCH)`            |
| `CIRCLECI`                 | `$(CIRCLECI)`                 |
| `CIRCLE_BUILD_NUM`         | `$(CIRCLE_BUILD_NUM)`         |
| `CIRCLE_BUILD_URL`         | `$(CIRCLE_BUILD_URL)`         |


<!--GitLab CI-->

| Key                  | Value                   |
| -------------------  | ----------------------- |
| `SCOPE_DSN`          | `$(SCOPE_DSN)`          |
| `CI_COMMIT_SHA`      | `$(CI_COMMIT_SHA)`      |
| `CI_REPOSITORY_URL`  | `$(CI_REPOSITORY_URL)`  |
| `CI_PROJECT_DIR`     | `$(CI_PROJECT_DIR)`     |
| `CI_COMMIT_BRANCH`   | `$(CI_COMMIT_BRANCH)`   |
| `CI_COMMIT_REF_NAME` | `$(CI_COMMIT_REF_NAME)` |
| `GITLAB_CI`          | `$(GITLAB_CI)`          |
| `CI_JOB_ID`          | `$(CI_JOB_ID)`          |
| `CI_JOB_URL`         | `$(CI_JOB_URL)`         |

<!--Travis-->
| Key                          | Value                           |
| ---------------------------- | ------------------------------- |
| `SCOPE_DSN`                  | `$(SCOPE_DSN)`                  |
| `TRAVIS_COMMIT`              | `$(TRAVIS_COMMIT)`              |
| `TRAVIS_BUILD_DIR`           | `$(TRAVIS_BUILD_DIR)`           |
| `TRAVIS`                     | `$(TRAVIS)`                     |
| `TRAVIS_REPO_SLUG`           | `$(TRAVIS_REPO_SLUG)`           |
| `TRAVIS_BUILD_ID`            | `$(TRAVIS_BUILD_ID)`            |
| `TRAVIS_BUILD_NUMBER`        | `$(TRAVIS_BUILD_NUMBER)`        |
| `TRAVIS_PULL_REQUEST_BRANCH` | `$(TRAVIS_PULL_REQUEST_BRANCH)` |
| `TRAVIS_BRANCH`              | `$(TRAVIS_BRANCH)`              |
| `TRAVIS_BUILD_WEB_URL `      | `$(TRAVIS_BUILD_WEB_URL)`       |

<!--GitHub Actions-->

| Key                 | Value                  |
| ------------------- | ---------------------- |
| `SCOPE_DSN`         | `$(SCOPE_DSN)`         |
| `GITHUB_SHA`        | `$(GITHUB_SHA)`        |
| `GITHUB_WORKSPACE`  | `$(GITHUB_WORKSPACE)`  |
| `GITHUB_REF`        | `$(GITHUB_REF)`        |
| `GITHUB_REPOSITORY` | `$(GITHUB_REPOSITORY)` |
| `GITHUB_RUN_ID`     | `$(GITHUB_RUN_ID)`     |
| `GITHUB_RUN_NUMBER` | `$(GITHUB_RUN_NUMBER)` |

<!--TeamCity-->

| Key                 | Value                  |
| ------------------- | ---------------------- |
| `SCOPE_DSN`         | `$(SCOPE_DSN)`         |
| `BUILD_VCS_NUMBER`  | `$(BUILD_VCS_NUMBER)`  |
| `BUILD_VCS_URL`     | `$(BUILD_VCS_URL)`     |
| `BUILD_CHECKOUTDIR` | `$(BUILD_CHECKOUTDIR)` |
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

| Key                             | Value                              |
| ------------------------------- | ---------------------------------- |
| `SCOPE_DSN`                     | `$(SCOPE_DSN)`                     |
| `BUILDKITE_COMMIT`              | `$(BUILDKITE_COMMIT)`              |
| `BUILDKITE_REPO`                | `$(BUILDKITE_REPO)`                |
| `BUILDKITE_BUILD_CHECKOUT_PATH` | `$(BUILDKITE_BUILD_CHECKOUT_PATH)` |
| `BUILDKITE_BRANCH`              | `$(BUILDKITE_BRANCH)`              |
| `BUILDKITE_BUILD_ID`            | `$(BUILDKITE_BUILD_ID)`            |
| `BUILDKITE_BUILD_NUMBER`        | `$(BUILDKITE_BUILD_NUMBER)`        |
| `BUILDKITE_BUILD_URL`           | `$(BUILDKITE_BUILD_URL)`           |

<!--Bitbucket Pipelines-->

| Key                        | Value                              |
| -------------------------- | ---------------------------------- |
| `SCOPE_DSN`                | `$(SCOPE_DSN)`                     |
| `BITBUCKET_COMMIT`         | `$(BITBUCKET_COMMIT)`              |
| `BITBUCKET_GIT_SSH_ORIGIN` | `$(BITBUCKET_GIT_SSH_ORIGIN)`      |
| `BITBUCKET_CLONE_DIR`      | `$(BITBUCKET_CLONE_DIR)`           |
| `BITBUCKET_BRANCH`         | `$(BITBUCKET_BRANCH)`              |
| `BITBUCKET_BUILD_NUMBER`   | `$(BITBUCKET_BUILD_NUMBER)`        |

<!--AppVeyor-->

| Key                                      | Value                                       |
| ---------------------------------------- | ------------------------------------------- |
| `SCOPE_DSN`                              | `$(SCOPE_DSN)`                              |
| `APPVEYOR_REPO_COMMIT`                   | `$(APPVEYOR_REPO_COMMIT)`                   |
| `APPVEYOR_REPO_NAME`                     | `$(APPVEYOR_REPO_NAME)`                     |
| `APPVEYOR_BUILD_FOLDER`                  | `$(APPVEYOR_BUILD_FOLDER)`                  |
| `APPVEYOR_PULL_REQUEST_HEAD_REPO_BRANCH` | `$(APPVEYOR_PULL_REQUEST_HEAD_REPO_BRANCH)` |
| `APPVEYOR_REPO_BRANCH`                   | `$(APPVEYOR_REPO_BRANCH)`                   |
| `APPVEYOR_BUILD_ID`                      | `$(APPVEYOR_BUILD_ID)`                      |
| `APPVEYOR_BUILD_NUMBER`                  | `$(APPVEYOR_BUILD_NUMBER)`                  |
| `APPVEYOR_PROJECT_SLUG`                  | `$(APPVEYOR_PROJECT_SLUG)`                  |

<!--Azure Pipelines-->

| Key                                  | Value                                   |
| ------------------------------------ | --------------------------------------- |
| `SCOPE_DSN`                          | `$(SCOPE_DSN)`                          |
| `BUILD_SOURCEVERSION`                | `$(BUILD_SOURCEVERSION)`                |
| `BUILD_REPOSITORY_URI`               | `$(BUILD_REPOSITORY_URI)`               |
| `BUILD_SOURCESDIRECTORY`             | `$(BUILD_SOURCESDIRECTORY)`             |
| `BUILD_SOURCEBRANCHNAME`             | `$(BUILD_SOURCEBRANCHNAME)`             |
| `BUILD_SOURCEBRANCH`                 | `$(BUILD_SOURCEBRANCH)`                 |
| `BUILD_BUILDID`                      | `$(BUILD_BUILDID)`                      |
| `BUILD_BUILDNUMBER`                  | `$(BUILD_BUILDNUMBER)`                  |
| `SYSTEM_TEAMPROJECT`                 | `$(SYSTEM_TEAMPROJECT)`                 |
| `SYSTEM_TEAMFOUNDATIONCOLLECTIONURI` | `$(SYSTEM_TEAMFOUNDATIONCOLLECTIONURI)` |

<!--END_DOCUSAURUS_CODE_TABS-->


After this, add the following environment variables to your CI provider:

| Environment variable | Description                                                  |
| -------------------- | ------------------------------------------------------------ |
| `$SCOPE_DSN`        | Data source name (DSN) of Scope to be used when reporting results |

##### SCOPE_DSN

**This is required setting**. If not set, tests will run as usual and an error message will be printed before the process finishes pointing to the agent logs for troubleshooting.

`SCOPE_DSN` contains the Data Source Name with connection information about the Scope installation to report to. Specifically, it contains the hostname of the Scope instance to report to, and the API key to be used for authentication.

Scope DSNs are generated per namespace. You can generate them by clicking on the `API Key` link of the namespace where you want to report to in the Scope UI.

##### SCOPE_COMMIT_SHA

This is a required setting when running in CI.

`SCOPE_COMMIT_SHA` contains the commit hash to be used when reporting to Scope.

If not explicitly set, the agent will try to automatically detect it reading  the commit hash from the environment variable set by the CI provider.

Example: `974c3566eb8e221d130db86a7ce1f99703fe2e69`

##### SCOPE_REPOSITORY

This is a required setting when running in CI.

`SCOPE_REPOSITORY` contains the repository URL to be used when reporting to Scope.

If not explicitly set, the agent will try to automatically detect it reading the repository URL from the environment variable set by the CI provider.

Examples: `https://github.com/undefinedlabs/scope-docs.git`, `git@github.com:undefinedlabs/scope-docs.git`

##### SCOPE_SOURCE_ROOT

This is a required setting when running in CI.

`SCOPE_SOURCE_ROOT` contains the absolute path to where the root of the project is located inside the filesystem. This information is used to automatically show excerpts of source code in the Scope UI in stacktraces, in the "Code Path" tab,
etc.

If not explicitly set, the agent will try to automatically detect it reading the source root from the environment variable set by the CI provider.

Example: `/home/user/projects/scope-docs`

#### Local development integration

For running tests in your local Xcode installation, the following environment variables must set in your **Test target** ([instructions](https://help.apple.com/xcode/mac/10.1/index.html?localePath=en.lproj#/dev3ec8a1cb4)):

| Key               | Value                |
| ----------------- | -------------------- |
| `SCOPE_XCODE_DSN` | `$(SCOPE_XCODE_DSN)` |

These environment variables are set automatically by the native Scope for Mac application that you can download from the **Local development/Scratchpad** area of Scope.

The following command must also be run on the terminal:

```bash
defaults write com.apple.dt.Xcode UseSanitizedBuildSystemEnvironment -bool NO
```

After these steps, after running your tests locally in Xcode, you will get a test report in Scope with the results.

##### SCOPE_XCODE_DSN

This is a required setting when running tests locally.

`SCOPE_XCODE_DSN` is used if `SCOPE_DSN` is not found.  If running locally using _Scope for Mac_ the `SCOPE_XCODE_DSN` environment variable is autogenerated when configuring the native application, and set when _Scope for Mac_ runs.

> Please, make sure  _Scope for Mac_ is running and configured before opening the app that will run the tests

Example: `https://cbfeff1f5fbf444086c728a096020cad@app.scope.dev/`


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

To enable Code Path support for your tests, follow these steps:

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

   

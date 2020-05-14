---
id: nodejs-installation
title: Scope Node.js Agent installation
sidebar_label: Installation
---

## GitHub Actions

Add a step to your GitHub Actions workflow YAML that uses the [Scope-for-Javascript](https://github.com/marketplace/actions/scope-for-javascript) action:

```yaml
steps:
  - uses: actions/checkout@v1
  - uses: actions/setup-node@v1
    with:
      node-version: 12
      registry-url: https://registry.npmjs.org/
  - name: Install dependencies
    run: npm install
  - name: Scope for Javascript
    uses: undefinedlabs/scope-for-javascript-action@v1
    with:
      dsn: ${{secrets.SCOPE_DSN}} # required
      command: npm test # optional - default is 'npm test'
```

You can find further information of this action at the [GitHub Marketplace](https://github.com/marketplace/actions/scope-for-javascript).

## Manual

Installation of the Scope Agent is done via [npm](https://www.npmjs.com/package/@undefinedlabs/scope-agent).

<!--DOCUSAURUS_CODE_TABS-->
<!--npm-->

```bash
npm install --save-dev @undefinedlabs/scope-agent
```

<!--yarn-->

```bash
yarn add --dev @undefinedlabs/scope-agent
```

<!--END_DOCUSAURUS_CODE_TABS-->

## Instrumenting your tests

### Jest

If you want to instrument tests run by Jest, you need to configure the following parameters: [testRunner](https://jestjs.io/docs/en/configuration#testrunner-string), [globalSetup](https://jestjs.io/docs/en/configuration#globalsetup-string) and [setupFilesAfterEnv](https://jestjs.io/docs/en/configuration#setupfilesafterenv-array).

```javascript
// jest.config.js
module.exports = {
  // ...
  testRunner: "@undefinedlabs/scope-agent/jest/testRunner",
  globalSetup: "@undefinedlabs/scope-agent/jest/globalSetup",
  setupFilesAfterEnv: ["@undefinedlabs/scope-agent/jest/setupTests"],
  // ...
};
```

> If you have custom `globalSetup` or `setupFilesAfterEnv` go to [Custom configuration](javascript-installation#custom-configuration).

After that you should be able to run your tests as you normally do e.g.:

```
yarn test
```

If you want to skip `jest.config.js` you may also run your tests with inline configuration:

```
yarn test --testRunner=@undefinedlabs/scope-agent/jest/testRunner --globalSetup=@undefinedlabs/scope-agent/jest/globalSetup --setupFilesAfterEnv=@undefinedlabs/scope-agent/jest/setupTests
```

#### Older versions of Jest

If you are using a version older than `24.0.0` (`>=23.0.0`) you may use `setupTestFrameworkScriptFile` instead of `setupFilesAfterEnv`:

```javascript
// jest.config.js
module.exports = {
  // ...
  testRunner: "@undefinedlabs/scope-agent/jest/testRunner",
  globalSetup: "@undefinedlabs/scope-agent/jest/globalSetup",
  setupTestFrameworkScriptFile: "@undefinedlabs/scope-agent/jest/setupTests",
  // ...
};
```

#### Custom configuration

> If you are using Jest's default `testRunner`, `globalSetup` and `setupFilesAfterEnv`, you may ignore this section.

If you have a custom configuration in [`globalSetup`](https://jestjs.io/docs/en/configuration#globalsetup-string) or [`setupFilesAfterEnv`](https://jestjs.io/docs/en/configuration#setupfilesafterenv-array), this section describes how you can make them work with Scope Javascript Agent.

##### `globalSetup`

Create a file in your project's folder e.g. `src/customGlobalSetup.js`:

```javascript
// src/customGlobalSetup.js
const globalSetup = require("@undefinedlabs/scope-agent/jest/globalSetup");
const yourCustomGlobalSetup = require("path/to/your/globalSetup");

module.exports = async (globalConfig) => {
  yourCustomGlobalSetup(globalConfig);
  await globalSetup(globalConfig);
};
```

Now point your Jest configuration to that file:

```javascript
// jest.config.js
module.exports = {
  // ...
  globalSetup: "<rootDir>/src/customGlobalSetup.js",
  // ...
};
```

##### `setupFilesAfterEnv`

For `setupFilesAfterEnv` you can simply add `"@undefinedlabs/scope-agent/jest/setupTests"` to the array:

```javascript
// jest.config.js
module.exports = {
  // ...
  setupFilesAfterEnv: [
    "<rootDir>/src/yourOldSetupFilesAfterEnv.js",
    "@testing-library/jest-dom/extend-expect",
    "@undefinedlabs/scope-agent/jest/setupTests",
  ],
  // ...
};
```

If you are using the deprecated `setupTestFrameworkScriptFile` you can simply add

```javascript
// yourOldSetupTestFrameworkScriptFile.js
require("@undefinedlabs/scope-agent/jest/setupTests");
```

to the top of your configuration file.

##### `testRunner`

Usage of a custom `testRunner` is not supported yet.

### Code Path

Code Path in Scope Node.js Agent leverages `babel` coverage in Jest, so if you want code path in your test results you also need to include the `coverage` option in your configuration:

```javascript
// jest.config.js
module.exports = {
  // ...
  coverage: true,
  forceCoverageMatch: ["**/*.test.js"], // optional if you want to include your test files in the coverage report
  testRunner: "@undefinedlabs/scope-agent/jest/testRunner",
  globalSetup: "@undefinedlabs/scope-agent/jest/globalSetup",
  setupFilesAfterEnv: ["@undefinedlabs/scope-agent/jest/setupTests"],
  // ...
};
```

You also need to setup the [Code Path configuration](nodejs-configuration#code-path).

## Environment variables

The following environment variables need to be configured when instrumenting your application in testing or runtime mode:

| Environment variable | Testing mode | Runtime mode | Autodetected |
| -------------------- | ------------ | ------------ | :----------: |
| `SCOPE_DSN`          | Required     | Required     |      ✗       |
| `SCOPE_COMMIT_SHA`   | Required     | Optional     |      ✓       |
| `SCOPE_REPOSITORY`   | Required     | Optional     |      ✓       |
| `SCOPE_SOURCE_ROOT`  | Required     | Optional     |      ✓       |

### SCOPE_DSN

**This is a required setting**. If not set in testing mode, tests will run as usual and an error message pointing to the agent logs for troubleshooting will be printed before the process finishes. If not set in runtime mode, the instrumented process will be executed as usual, a warning message will be printed at the beginning of the execution and no spans will be reported.

`SCOPE_DSN` contains the Data Source Name with connection information about the Scope installation to report to. Specifically, it contains
the hostname of the Scope instance to report to, and the API key to be used for authentication. _`SCOPE_DSN` is considered a secret and should not be checked out in a repository._

Scope DSNs are generated per namespace. You can generate them by clicking on the `API Key` link of the namespace you want to report to in the Scope UI. If running locally using the native apps _Scope for Mac_ or _Scope for Windows_, the DSN will be automatically configured by reading it from `~/.scope/config.json`, which is autogenerated by the native app.

Example value: `https://cbfeff1f5fbf444086c728a096020cad@app.scope.dev/`

### SCOPE_COMMIT_SHA

This is a required setting in testing mode, and optional in runtime mode.

`SCOPE_COMMIT_SHA` contains the commit hash to be used when reporting to Scope.

If not explicitly set, the agent will try to automatically detect it using the following algorithm:

1. If the process is being executed inside a [supported CI provider](nodejs-compatibility.md#ci-providers), it will try to read the commit hash from the environment variable set by the CI provider.
2. Else, it will try to extract the current commit from the local git information (if `.git/` is present).

Example value: `974c3566eb8e221d130db86a7ce1f99703fe2e69`

### SCOPE_REPOSITORY

This is a required setting in testing mode, and optional in runtime mode.

`SCOPE_REPOSITORY` contains the repository URL to be used when reporting to Scope.

If not explicitly set, the agent will try to automatically detect it using the following algorithm:

1. If the process is being executed inside a [supported CI provider](nodejs-compatibility.md#ci-providers), it will try to read the repository URL from the environment variable set by the CI provider.
2. If not, it will try to extract the current `origin` remote URL from the local git information (if `.git/` is present).

Example values: `https://github.com/undefinedlabs/scope-docs.git`, `git@github.com:undefinedlabs/scope-docs.git`

> This parameter may also be configured in a [`scope.yml` file](nodejs-configuration.md) using the key `repository`.

### SCOPE_SOURCE_ROOT

This is a required setting in testing mode, and optional in runtime mode.

`SCOPE_SOURCE_ROOT` contains the absolute path to where the root of the project is located inside the filesystem. This
information is used to automatically show excerpts of source code in the Scope UI in stacktraces, in the "Code Path" tab and others.

If not explicitly set, the agent will try to automatically detect it using the following algorithm:

1. If the process is being executed inside a [supported CI provider](nodejs-compatibility.md#ci-providers), it will try
   to read the source root from the environment variable set by the CI provider.
2. If not, it will try to extract the absolute path to the git repository using the local git information (if `.git/` is present).
3. If not, it will be set to the working directory of the command used to launch the application or tests.

Example value: `/home/user/projects/scope-docs`

> This parameter may also be configured in a [`scope.yml` file](nodejs-configuration.md) using the key `source_root`.

## Running tests inside a container

If you are running your application or tests inside a container, forward the following environment variables to it so the agent can autodetect the build information. Note that the variables depend on your CI provider.

> Note that you might also need to set `SCOPE_SOURCE_ROOT` manually with the absolute path inside the container where the code is present if it cannot be autodetected by the agent.

<!--DOCUSAURUS_CODE_TABS-->
<!-- Jenkins -->

- `SCOPE_DSN`
- `JENKINS_URL`
- `GIT_URL`
- `GIT_COMMIT`
- `BUILD_ID`
- `BUILD_NUMBER`
- `BUILD_URL`

<!-- CircleCI -->

- `SCOPE_DSN`
- `CIRCLECI`
- `CIRCLE_REPOSITORY_URL`
- `CIRCLE_SHA1`
- `CIRCLE_BUILD_NUM`
- `CIRCLE_BUILD_URL`

<!-- GitLab CI -->

- `SCOPE_DSN`
- `GITLAB_CI`
- `CI_REPOSITORY_URL`
- `CI_COMMIT_SHA`
- `CI_JOB_ID`
- `CI_JOB_URL`

<!-- Travis -->

- `SCOPE_DSN`
- `TRAVIS`
- `TRAVIS_REPO_SLUG`
- `TRAVIS_COMMIT`
- `TRAVIS_BUILD_ID`
- `TRAVIS_BUILD_NUMBER`

<!-- AppVeyor -->

- `SCOPE_DSN`
- `APPVEYOR`
- `APPVEYOR_REPO_NAME`
- `APPVEYOR_REPO_COMMIT`
- `APPVEYOR_BUILD_ID`
- `APPVEYOR_BUILD_NUMBER`
- `APPVEYOR_PROJECT_SLUG`

<!-- Azure Pipelines -->

- `SCOPE_DSN`
- `TF_BUILD`
- `Build.Repository.Uri`
- `Build.SourceVersion`
- `Build.BuildId`
- `Build.BuildNumber`
- `System.TeamFoundationCollectionUri`
- `System.TeamProject`

<!-- Bitbucket Pipelines -->

- `SCOPE_DSN`
- `BITBUCKET_GIT_SSH_ORIGIN`
- `BITBUCKET_COMMIT`
- `BITBUCKET_BUILD_NUMBER`

<!-- GitHub Actions -->

- `SCOPE_DSN`
- `GITHUB_REPOSITORY`
- `GITHUB_SHA`

<!-- Buildkite -->

- `SCOPE_DSN`
- `BUILDKITE`
- `BUILDKITE_REPO`
- `BUILDKITE_COMMIT`
- `BUILDKITE_BUILD_ID`
- `BUILDKITE_BUILD_NUMBER`
- `BUILDKITE_BUILD_URL`

<!-- TeamCity -->

- `SCOPE_DSN`
- `TEAMCITY_VERSION`
- `BUILD_VCS_URL`
- `BUILD_VCS_NUMBER`
- `BUILD_CHECKOUTDIR`
- `BUILD_NUMBER`
- `BUILD_ID`
- `SERVER_URL`

For `TeamCity`, additional environment variables must be exposed from the Teamcity `Parameters` section:

| Name                    | Value                          |
| ----------------------- | ------------------------------ |
| `env.BUILD_CHECKOUTDIR` | `%teamcity.build.checkoutDir%` |
| `env.BUILD_ID`          | `%teamcity.build.id%`          |
| `env.BUILD_VCS_URL`     | `%vcsroot.url%`                |

<!--END_DOCUSAURUS_CODE_TABS-->

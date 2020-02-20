---
id: javascript-installation
title: Scope Javascript Agent installation
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
      jest-command: npm test # optional - default is 'npm test'
      cypress-command: npm run cypress:run # optional - command to run cypress tests if your repository includes them
      cypress-endpoint: http://localhost:3000 # optional - URL to run the cypress tests against
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

### Instrumenting your tests

#### Jest tests

If you want to instrument tests run by Jest, you need to configure a custom [runner](https://jestjs.io/docs/en/configuration#runner-string), [testRunner](https://jestjs.io/docs/en/configuration#testrunner-string) and [setupFilesAfterEnv](https://jestjs.io/docs/en/configuration#setupfilesafterenv-array).

```javascript
// jest.config.js
module.exports = {
  // ...
  testRunner: "@undefinedlabs/scope-agent/jest/testRunner",
  runner: "@undefinedlabs/scope-agent/jest/runner",
  setupFilesAfterEnv: ["@undefinedlabs/scope-agent/jest/setupTests"]
  // ...
};
```

You may also run your jest tests with inline configuration:

```
yarn test --testRunner=@undefinedlabs/scope-agent/jest/testRunner --runner=@undefinedlabs/scope-agent/jest/runner --setupFilesAfterEnv=@undefinedlabs/scope-agent/jest/setupTests
```

##### Create React App

CRA does not allow `testRunner` or `runner` configuration for jest yet (more info in https://github.com/facebook/create-react-app/issues/2474) so you may not use the `jest` field in your `package.json`. The `setupFilesAfterEnv` configuration is already included in CRA via [setupTests.js](https://create-react-app.dev/docs/running-tests/#srcsetuptestsjs).

You can define the configuration inline in your `package.json`:

```json
...
"scripts": {
  "test": "react-scripts test --testRunner=@undefinedlabs/scope-agent/jest/testRunner --runner=@undefinedlabs/scope-agent/jest/runner"
}
...
```

And in your CRA's `src/setupTests.js` add the following line:

```javascript
import "@undefinedlabs/scope-agent/jest/setupTests";
```

After that you should be able to run your tests as you normally do e.g.:

```
yarn test
```

#### Cypress tests

If you want to instrument tests run by Cypress you need to add the scope-agent plugin.

Add the following to [cypress.json](https://docs.cypress.io/guides/references/configuration.html#Folders-Files):

```json
{
  "supportFile": "cypress/support/index.js",
  "pluginsFile": "cypress/plugins/index.js"
}
```

```javascript
// cypress/support/index.js
import "@undefinedlabs/scope-agent/cypress/support";

// ... any other configuration here
```

```javascript
// cypress/plugins/index.js
const {
  initCypressPlugin
} = require("@undefinedlabs/scope-agent/cypress/plugin");

module.exports = async (on, config) => {
  // ... any other plugin goes here
  const newConfig = await initCypressPlugin(on, config);
  return newConfig;
};
```

## Environment variables

The following environment variables need to be configured when instrumenting your application:

| Environment variable | Testing  | Autodetected |
| -------------------- | -------- | :----------: |
| `SCOPE_DSN`          | Required |      ✗       |
| `SCOPE_COMMIT_SHA`   | Required |      ✓       |
| `SCOPE_REPOSITORY`   | Required |      ✓       |
| `SCOPE_SOURCE_ROOT`  | Required |      ✓       |

### SCOPE_DSN

**This is a required setting**. If not set, tests will run as usual and an error message will be printed before the process finishes.

`SCOPE_DSN` contains the Data Source Name with connection information about the Scope installation to report to. Specifically, it contains the hostname of the Scope instance to report to, and the API key to be used for authentication. _`SCOPE_DSN` is considered a secret and should not be checked out in a repository._

Scope DSNs are generated per namespace. You can generate them by clicking on the `API Key` link of the namespace you want to report to in the Scope UI. If running locally using the native apps _Scope for Mac_ or _Scope for Windows_, the DSN will be automatically configured by reading it from `~/.scope/config.json`, which is autogenerated by the native app.

Example value: `https://cbfeff1f5fbf444086c728a096020cad@app.scope.dev/`

### SCOPE_COMMIT_SHA

`SCOPE_COMMIT_SHA` contains the commit hash to be used when reporting to Scope.

This is a required setting. If not explicitly set, the agent will try to automatically detect it using the following algorithm:

1. If the process is being executed inside a [supported CI provider](javascript-compatibility.md#ci-providers), it will try to read the commit hash from the environment variable set by the CI provider.
2. Else, it will try to extract the current commit from the local git information (if `.git/` is present).

Example value: `974c3566eb8e221d130db86a7ce1f99703fe2e69`

### SCOPE_REPOSITORY

`SCOPE_REPOSITORY` contains the repository URL to be used when reporting to Scope.

This is a required setting. If not explicitly set, the agent will try to automatically detect it using the following algorithm:

1. If the process is being executed inside a [supported CI provider](javascript-compatibility.md#ci-providers), it will try to read the repository URL from the environment variables set by the CI provider.
2. If not, it will try to extract the current `origin` remote URL from the local git information (if `.git/` is present).

Examples values: `https://github.com/undefinedlabs/scope-docs.git`, `git@github.com:undefinedlabs/scope-docs.git`

### SCOPE_SOURCE_ROOT

`SCOPE_SOURCE_ROOT` contains the absolute path to where the root of the project is located inside the filesystem. This
information is used to automatically show excerpts of source code in the Scope UI in stacktraces, in the "Code Path" tab and others.

This is a required setting. If not explicitly set, the agent will try to automatically detect it using the following algorithm:

1. If the process is being executed inside a [supported CI provider](javascript-compatibility.md#ci-providers), it will try to read the source root from the environment variable set by the CI provider.
2. If not, it will try to extract the absolute path to the git repository using the local git information (if `.git/` is present).
3. If not, it will be set to the working directory of the command used to launch the application or tests.

Example value: `/home/user/projects/scope-docs`

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

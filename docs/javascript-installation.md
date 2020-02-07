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
      command: npm test # optional - default is 'npm test'
      command-cypress: npm run cypress:run # optional - command to run cypress tests if your repository includes them
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

The following environment variables need to be configured when instrumenting your tests:

| Environment variable | Default value | Description                                                       |
| -------------------- | ------------- | ----------------------------------------------------------------- |
| `$SCOPE_DSN`         |               | Data source name (DSN) of Scope to be used when reporting results |

For `TeamCity`, additional environment variables must be exposed from the Teamcity `Parameters` section:

| Name                    | Value                          |
| ----------------------- | ------------------------------ |
| `env.BUILD_CHECKOUTDIR` | `%teamcity.build.checkoutDir%` |
| `env.BUILD_ID`          | `%teamcity.build.id%`          |
| `env.BUILD_VCS_URL`     | `%vcsroot.url%`                |

### Cypress

To configure environment variables in cypress you can have a look at [cypress documentation](https://docs.cypress.io/guides/guides/environment-variables.html#Setting) on this.
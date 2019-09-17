---
id: javascript-installation
title: Scope Javascript Agent installation
sidebar_label: Installation
---

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

### Jest tests

If you want to instrument tests run by Jest, you need to create a `reporter`.

In `src/reporter.js`

```javascript
const Reporter = require("@undefinedlabs/scope-agent").JestReporter;

module.exports = Reporter;
```

Then you have to configure [jest reporter](https://jestjs.io/docs/en/configuration#reporters-array-modulename-modulename-options)
to point to this file.

For example:

In your `jest.config.js`:

```javascript
module.exports = {
  // ...
  reporters: ["<rootDir>/src/reporter.js"]
  // ...
};
```

#### Create React App

In your `package.json`:

```json
...
"scripts": {
  "test:scope": "react-scripts test --reporters=default --reporters=./src/reporter.js"
}
...
```

CRA does not allow `reporter` configuration for jest yet (more info in https://github.com/facebook/create-react-app/issues/2474) so you may not use the `jest` field in your `package.json`.

### Cypress tests

If you want to instrument tests run by Cypress you need to add the scope-agent plugin.

Add the following to [cypress.json](https://docs.cypress.io/guides/references/configuration.html#Folders-Files):

```json
{
  "supportFile": "cypress/support/index.js",
  "pluginsFile": "cypress/plugins/index.js"
}
```

Where `cypress/support/index.js`:

```javascript
import { initializeCypress } from "@undefinedlabs/scope-agent";

initializeCypress();

// ... any other configuration here
```

And `cypress/plugins/index.js`:

```javascript
const { initCypressPlugin } = require("@undefinedlabs/scope-agent");

module.exports = async (on, config) => {
  // ... any other plugin goes here
  const newConfig = await initCypressPlugin(on, config);
  return newConfig;
};
```

## Environment variables

The following environment variables need to be configured when instrumenting your tests:

| Environment variable  | Default value | Description                                            |
| --------------------- | ------------- | ------------------------------------------------------ |
| `$SCOPE_APIKEY`       |               | API key to use when sending data to Scope              |
| `$SCOPE_API_ENDPOINT` |               | API endpoint of the Scope installation to send data to |

### Cypress

To configure environment variables in cypress you can have a look at [cypress documentation](https://docs.cypress.io/guides/guides/environment-variables.html#Setting) on this.

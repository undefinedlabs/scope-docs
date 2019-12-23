---
id: nodejs-installation
title: Scope Node.js Agent installation
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

After that you should be able to run your tests as you normally do e.g.:

```
yarn test
```

You may also run your jest tests with inline configuration:

```
yarn test --testRunner=@undefinedlabs/scope-agent/jest/testRunner --runner=@undefinedlabs/scope-agent/jest/runner --setupFilesAfterEnv=@undefinedlabs/scope-agent/jest/setupTests
```

### HTTP servers

You may also instrument your http server by simply including `require('@undefinedlabs/scope-agent/node')` at the top of your server main function. For example, in [express](https://expressjs.com/):

```javascript
// It needs to be before you import express
require("@undefinedlabs/scope-agent/node");
const express = require("express");

const app = express();

// Server configuration continues here
```

## Environment variables

The following environment variables need to be configured when instrumenting your tests:

| Environment variable | Default value | Description                                                    |
| -------------------- | ------------- | -------------------------------------------------------------- |
| `$SCOPE_DSN`         |               | Data source name (DSN) of Scope to be used when reporting results |

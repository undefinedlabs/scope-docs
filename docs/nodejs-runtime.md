---
id: nodejs-runtime
title: Scope Node.js Agent runtime instrumentation
sidebar_label: Runtime instrumentation
---

In order to see trace information from your Node.js service on integration and end-to-end tests, you need to use the Scope agent to instrument your running service.

This service might run, for example, in a container on CI, or in a QA/staging environment.

> If you're running the Scope Python Agent in runtime mode, you need to set [`SCOPE_TESTING_MODE`](python-configuration.md#change-testing-mode) to `false`.

### HTTP servers

You may instrument your http server by simply including `require('@undefinedlabs/scope-agent/node')` at the top of your server main function. For example, in [express](https://expressjs.com/):

```javascript
// It needs to be before you import express
require("@undefinedlabs/scope-agent/node");
const express = require("express");

const app = express();

// Server configuration continues here
```

Notice that setting the `SCOPE_DSN` environment variable is required.

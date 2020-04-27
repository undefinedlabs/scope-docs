---
id: nodejs-troubleshooting
title: Scope Node.js Agent troubleshooting
sidebar_label: Troubleshooting
---

## I don't see my tests in Scope after installing the Scope Node.js Agent

If you don't see any results in Scope after following the [Scope Node.js Agent installation](nodejs-installation.md), check the following:

**Have you configured a valid `SCOPE_DSN`?**

The Scope Node.js Agent needs a valid `SCOPE_DSN` configured as environment variable.

Keep in mind that `SCOPE_DSN` is different per **namespace** so if you configure a `SCOPE_DSN` from other namespace, you will not see results in Scope for that repository.

You can find further information in [Scope Node.js Agent - Environment variables](nodejs-installation.md#environment-variables) section.

**Have you forwarded the required environment variables?**

If you are executing your tests in a container, you need to forward some environment variables depending on your CI provider, so the agent can autodetect the build information.

You can find further information in [Scope Node.js Agent - Running tests inside a container](nodejs-installation.md#running-tests-inside-a-container) section.

**Have you checked the compatibility of Scope Node.js Agent with your project?**

If you are using certain libraries or version libraries that are not officially supported by the Scope Node.js agent, you might have not see data in Scope after executing the test phase.

You can find further information in [Scope Node.js Agent - Compatibility](nodejs-compatibility.md) section.

---
id: java-troubleshooting
title: Scope Java Agent troubleshooting
sidebar_label: Troubleshooting
---

## I don't see my tests in Scope after installing the Scope Java agent

If you don't see any results in Scope after following the [Scope Java agent installation](java-installation.md), check the following:

**Have you configured a valid `SCOPE_DSN`?**

The Scope Java agent needs a valid `SCOPE_DSN` configured as environment variable.

Keep in mind that `SCOPE_DSN` is different per **namespace** so if you configure a `SCOPE_DSN` from other namespace, you will not see results in Scope for that repository.

You can find further information in [Scope Java agent - Environment variables](java-installation.md#environment-variables) section.

**Have you forwarded the required environment variables?**

If you are executing your tests in a container, you need to forward several environment variables depending on your CI provider, so the agent can autodetect the build information.

You can find further information in [Scope Java agent - Running tests inside a container](java-installation.md#running-tests-inside-a-container) section.

**Have you checked the compatibility of Scope Java agent with your project?**

If you are using certain libraries or version libraries that are not officially supported by the Scope Java agent, you might have not see data in Scope after executing the test phase.

You can find further information in [Scope Java agent - Compatibility](java-compatibility.md) section.

## I'm getting `SSLException: Received close_notify during handshake` error

This error may occur if you are using an outdated JDK 1.7 patch version because some required cipher suites are not supported in that version.

To solve this issue, update your JDK 1.7 to `1.7.0_u131+` which comes with the required SSL cipher suites.

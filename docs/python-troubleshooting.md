---
id: python-troubleshooting
title: Scope Python Agent troubleshooting
sidebar_label: Troubleshooting
---

## I don't see my tests in Scope after installing the Scope Python Agent

If you don't see any results in Scope after following the [Scope Python Agent installation](python-installation.md), check the following:

**Have you configured a valid `SCOPE_DSN`?**

The Scope Python Agent needs a valid `SCOPE_DSN` configured as environment variable.

Keep in mind that `SCOPE_DSN` is different per **namespace** so if you configure a `SCOPE_DSN` from other namespace, you will not see results in Scope for that repository.

You can find further information in [Scope Python Agent - Environment variables](python-installation.md#environment-variables) section.

**Have you forwarded the required environment variables?**

If you are executing your tests in a container, you need to forward some environment variables depending on your CI provider, so the agent can autodetect the build information.

You can find further information in [Scope Python Agent - Running tests inside a container](python-installation.md#running-tests-inside-a-container) section.

**Have you checked the compatibility of Scope Python Agent with your project?**

If you are using certain libraries or version libraries that are not officially supported by the Scope Python agent, you might have not see data in Scope after executing the test phase.

You can find further information in [Scope Python Agent - Compatibility](python-compatibility.md) section.

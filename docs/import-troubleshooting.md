---
id: import-troubleshooting
title: Scope Import troubleshooting
sidebar_label: Troubleshooting
---

## I don't see my tests in Scope after installing the Scope Import tool

If you don't see any results in Scope after following the [Scope Import tool](import-installation.md), check the following:

**Have you configured a valid `SCOPE_DSN`?**

The Scope Java agent needs a valid `SCOPE_DSN` configured as environment variable.

Keep in mind that `SCOPE_DSN` is different per **namespace** so if you configure a `SCOPE_DSN` from other namespace, you will not see results in Scope for that repository.

You can find further information in [Scope Import - Environment variables](import-installation.md#environment-variables) section.

**Have you forwarded the required environment variables?**

If you are importing your test reports in a container, you need to forward several environment variables depending on your CI provider, so the tool can autodetect the build information.

You can find further information in [Scope Import - Import test reports inside a container](import-installation.md#import-test-reports-inside-a-container) section.

**Have you checked the compatibility of Scope Import tool with your project?**

If you are using certain test framework or tool that are not officially supported by the Scope Import tool, you might have not see data in Scope after processing your XML reports.

You can find further information in [Scope Import - Compatibility](import-compatibility.md) section.

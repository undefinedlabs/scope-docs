---
id: javascript-troubleshooting
title: Scope Javascript Agent troubleshooting
sidebar_label: Troubleshooting
---

## I don't see my tests in Scope after installing the Scope Javascript Agent

If you don't see any results in Scope after following the [Scope Javascript Agent installation](javascript-installation.md), check the following:

**Have you configured a valid `SCOPE_DSN`?**

The Scope Javascript Agent needs a valid `SCOPE_DSN` configured as environment variable.

Keep in mind that `SCOPE_DSN` is different per **namespace** so if you configure a `SCOPE_DSN` from other namespace, you will not see results in Scope for that repository.

You can find further information in [Scope Javascript Agent - Environment variables](javascript-installation.md#environment-variables) section.

**Have you forwarded the required environment variables?**

If you are executing your tests in a container, you need to forward some environment variables depending on your CI provider, so the agent can autodetect the build information.

You can find further information in [Scope Javascript Agent - Running tests inside a container](javascript-installation.md#running-tests-inside-a-container) section.

**Have you checked the compatibility of Scope Javascript Agent with your project?**

If you are using certain libraries or version libraries that are not officially supported by the Scope Javascript agent, you might have not see data in Scope after executing the test phase.

You can find further information in [Scope Javascript Agent - Compatibility](javascript-compatibility.md) section.

## I can't see the Test Code in the Test Code Tab

This is most likely caused by a problem with [`SCOPE_SOURCE_ROOT`](javascript-installation.md#environment-variables). While we try to autodetect the root of your repository, it is not always possible. For example, if your folder structure looks like this:

```bash
|-- source
    |-- root
        |-- src
            |-- admin-ui
            |   |-- cypress.json
            |   |-- cypress
            |       |-- smoke
            |           |-- smoke.spec.js
            |-- ui
                |-- cypress.json
                |-- cypress
                    |-- integration
                        |-- integration.spec.js
```

where there are multiple `cypress` roots that are run independently, the Scope Javascript Agent will currently autodetect two different source roots:

```bash
/source/root/src/ui
```

and

```bash
/source/root/src/admin-ui
```

This is _incorrect_ and will lead to the Test Code not working properly.

### How to fix it

Manually set `SCOPE_SOURCE_ROOT` env var to the root of your repository when you run your cypress commands, e.g.:

```bash
SCOPE_SOURCE_ROOT=/source/root yarn cypress:run-ui
```

```bash
SCOPE_SOURCE_ROOT=/source/root yarn cypress:run-admin
```

---
id: index
title: Scope documentation
sidebar_label: Introduction
---

**Welcome to the [Scope](https://scope.dev) documentation site!**

Here you will find instructions and reference information about how to install, configure and use Scope.

# Getting started

## Create an account

Go to [https://app.scope.dev](https://app.scope.dev) and log in using your GitHub account.

> Using GitHub Enterprise? Scope is also available for deployment on-premises. Get in touch at <support@scope.dev> for details.

## Install the GitHub app

First, you need to install the [Scope GitHub app](https://github.com/apps/scope-app) in the namespace(s) you plan to use with Scope.

Head over to the [Scope GitHub app installation page](https://github.com/apps/scope-app/installations/new)
and select the namespace where you want to install Scope. You can then select the repositories that you want to add, and click
**Install** to finish installation.

You will be redirected to Scope, and in a few seconds, your namespace and the repositories you selected will appear.

## Instrument your automated tests

After that, you need to instrument your tests using the **Scope agent** for your platform:

- [.NET agent instructions](dotnet-installation.md)
- [Java agent instructions](java-installation.md)
- [Swift agent instructions](swift-installation.md)
- [Python agent instructions](python-installation.md)
- [Go agent instructions](go-installation.md)
- [Javascript agent instructions](javascript-installation.md)
- [Node.js agent instructions](nodejs-installation.md)

If the platform you use is not listed here, we also provide the [Scope Import](import-installation.md) tool that can be
used to import jUnit XML files with your test results.

Commit the changes to your repository and let your existing CI provider execute your tests. You will start seeing results
in real time in Scope.

## Local development

You can also use Scope to debug tests that you run locally. The results will only be available to you.
In order to do so, download the **Scope Desktop** app for your OS:

- [Download Scope for Mac](https://home.undefinedlabs.com/goto/download-scope-for-mac)
- [Download Scope for Windows](https://home.undefinedlabs.com/goto/download-scope-for-windows)

After installation, head over to the **Local development/Scratchpad** section in Scope and click on **Configure App** to
automatically set the appropriate credentials.

Once the application has been configured, running your instrumented tests will automatically create a test report in your **Scratchpad** section.
You can also open the desktop app menu and go directly to any of the last five test reports.


## Manual testing

Scope also allows you to record manual browser tests using the [Scope for Chrome](scope-for-chrome-installation.md) extension.

First, setup the **Scope Desktop** app for your OS as described in the previous section. Then, head over to the
[Chrome Web Store](https://home.undefinedlabs.com/goto/scope-for-chrome-download) and install the Scope for Chrome extension.

Once install, you can start a recording by clicking on the Scope logo that appears in your browser. Click it again to 
finish the recording. All manual test recordings will be available in the **Local development/Manual Testing** section
in Scope.


## Questions?

If you have any questions or issues while using Scope, send us an email to <support@scope.dev>

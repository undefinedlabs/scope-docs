---
id: index
title: Scope documentation
sidebar_label: Introduction
---

**Welcome to the [Scope](https://scope.dev) documentation site!**

Here you will find instructions and reference information about how to install, configure and use Scope.


# Getting started

## Install the GitHub app

First, you need to install the [Scope GitHub app](https://github.com/apps/scope-app) in the namespace(s) you plan to use with Scope.

Head over to the [Scope GitHub app installation page](https://github.com/apps/scope-app/installations/new) 
and select the namespace where you want to install Scope. You can then select the repositories that you want to add, and click
**Install** to finish installation.

You will be redirected to Scope, and in a few seconds, your namespace and the repositories you selected will appear.


## Instrument your tests

After that, you need to instrument your tests using the **Scope agent** for your platform:

* [.NET agent instructions](dotnet-installation.md)
* [Java agent instructions](java-installation.md)
* [Scala agent instructions](java-installation.md)
* [iOS agent instructions](ios-installation.md)
* [Python agent instructions](python-installation.md)
* [Go agent instructions](go-installation.md)
* [Javascript agent instructions](javascript-installation.md)

Commit the changes to your repository and let your existing CI provider execute your tests. You will start seeing results
in real time in Scope.


## Local development

You can also use Scope to debug tests that you run locally. In order to do so, download the **Scope Desktop** app for your OS:

* [Download Scope for Mac](https://home.codescope.com/goto/download-scope-for-mac)
* [Download Scope for Windows](https://home.codescope.com/goto/download-scope-for-windows)

After installation, head over to the **Local development/Scratchpad** section in Scope and click on **Configure App** to
automatically set the appropriate credentials.

Once the application has been configured, running your instrumented tests will automatically create a test report in your **Scratchpad** section.
You can also open the desktop app menu and go directly to any of the last five test reports.


## Questions?

If you have any questions or issues while using Scope, send us an email to <support@scope.dev>

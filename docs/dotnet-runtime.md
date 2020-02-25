---
id: dotnet-runtime
title: Scope .NET Agent runtime instrumentation
sidebar_label: Runtime instrumentation
---

In order to see trace information from your .NET service on integration and end-to-end tests,
you need to use the Scope agent to instrument your running service.

This service might run, for example, in a container on CI, or in a QA/staging environment.

To instrument in runtime, prefix your service startup command with `scope-run`. For example:
                          
```bash
scope-run dotnet run
```

This will autoinstrument your application at runtime and will produce tracing information if it receives
a request from an instrumented test or application.

## Adding Code Path information for runtime binaries

Enabling the Code Path information of runtime applications requires to patch the assemblies 
with the coverage algorithm (apart of enabling it in the [configuration](dotnet-configuration.md)). 

To patch them you have to run the following command inside the folder where the binaries are:

```bash
scope-run --apply-coverage
```

With the binaries patched run your service using the `scope-run` command for the instrumentation.

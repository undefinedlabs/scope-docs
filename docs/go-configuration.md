---
id: go-configuration
title: Scope Go Agent configuration
sidebar_label: Configuration
---

The behaviour of Scope Agent can be modified using  environment variables.

> If these properties are manually configured, use `true` or `false` only for the boolean value.


## Setting Scope as Global Tracer

If you set Scope as OpenTracing Global Tracer, your own spans will be captured and shown as part of the Scope trace view for a certain test.

```sh
SCOPE_SET_GLOBAL_TRACER=true
```



## Change testing mode

This variable indicates whether the agent is running tests or it is being used for runtime instrumentation. 

If `SCOPE_TESTING_MODE` is not specified, the agent sets to  `true` when running in CI or if the tests are started using `scopeagent.Run()`,  and `false` otherwise.

```sh
SCOPE_TESTING_MODE=false
```

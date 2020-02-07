---
id: swift-configuration
title: Scope Swift Agent configuration
sidebar_label: Configuration
---

> If these properties are manually configured, use `true` or `false` only for the boolean value.

The behaviour of Scope Agent can be modified by adding  the following environment variables to your test target ([instructions](https://help.apple.com/xcode/mac/10.1/index.html?localePath=en.lproj#/dev3ec8a1cb4)), or to to your `Scope for Swift` GitHub Action:

## Disabling Scope instrumentation

Scope auto instruments your code and tests by default. You can disable this behaviour.

```sh
SCOPE_AUTO_INSTRUMENT=false
```



## Changing service name

You can specify the name of the service when sending data to Scope. Scope uses `default` as fallback.

```sh
SCOPE_SERVICE="service-name"
```



## Setting Scope as Global Tracer

If you set Scope as OpenTracing Global Tracer, your own spans will be captured and shown as part of the Scope trace view for a certain test.

```sh
SCOPE_SET_GLOBAL_TRACER=true
```



## Change testing mode

This variable indicates whether the agent is running tests or it is being used for runtime instrumentation. By default it will run in testing mode

```sh
SCOPE_TESTING_MODE=false
```



## Include HTTP payloads in HTTP span tags

You can include HTTP payloads in the related HTTP spans, truncated to the first 512 bytes.

By default, Scope Swift Agent will not send HTTP payloads as they are considered sensitive information.

```sh
SCOPE_INSTRUMENTATION_HTTP_PAYLOADS=true
```



## Disabling HTTP auto instrumentation

You can disable Scope HTTP auto instrumentation. By default Scope will autoinstrument all `Alamofire`, `URLSession` and `URLConnection`.

```sh
SCOPE_INSTRUMENTATION_HTTP_CLIENT=false
```


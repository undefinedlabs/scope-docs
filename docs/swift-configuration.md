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



## Change testing mode

This variable indicates whether the agent is running tests or it is being used for runtime instrumentation. By default it will run in testing mode

```sh
SCOPE_TESTING_MODE=false
```



## Adding agent metadata

You can send arbitrary metadata for every test associated with certain commit which will be shown by Scope.

Additionally, it is possible to set an environment variable as metadata value for a certain key, whose final value will be evaluated at runtime.

```sh
SCOPE_METADATA="sample.key1=$SAMPLE_VAR1,sample.key2=$SAMPLE_VAR2,sample.key3=sampleValue3"
```



## Select agent metadata as test configuration

Yon can select metadata keys to be considered as relevant in the configuration of the test.

```sh
SCOPE_CONFIGURATION="sample.key1,sample.key2"
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



## Include additional HTTP Headers in HTTP span tags

You can include additional HTTP Headers in HTTP span tags.

By default, Scope Swift agent will send common HTTP headers, filtering the content of those which can contain sensitive information, such as:

- `Authorization`
- `Cookie`
- `Set-Cookie`

Note that the content of every header configured explicitly to be shown in the HTTP span tags will not be filtered.

```sh
SCOPE_INSTRUMENTATION_HTTP_HEADERS="Authorization,My-Header-One,My-Header-Two"
```


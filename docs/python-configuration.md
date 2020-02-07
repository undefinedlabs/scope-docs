---
id: python-configuration
title: Scope Python Agent configuration
sidebar_label: Configuration
---

> If these properties are manually configured, use `true` or `false` only for the boolean value.

The behaviour of the Scope Agent can be modified using environment variables or a configuration file `scope.yml` in the source root of the project.


These configuration settings can also be provided via CLI flags. Check out the
[CLI reference](https://scope-python-agent.readthedocs.io/en/latest/cli.html) documentation for details.

## Disabling Scope instrumentation

Scope auto instruments your code and tests by default. You can disable this behaviour.

### Using Environment Variables

```sh
SCOPE_AUTO_INSTRUMENT=false
```

### Using YAML Configuration file

```yaml
scope:
  instrumentation:
    enabled: false
```



## Changing service name

You can specify the name of the service when sending data to Scope. Scope uses `default` as fallback.

### Using Environment Variables

```sh
SCOPE_SERVICE="service-name"
```

### Using YAML Configuration file

```yaml
scope:
  service: 'service-name'
```



## Setting Scope as Global Tracer

If you set Scope as OpenTracing Global Tracer, your own spans will be captured and shown as part of the Scope trace view for a certain test.

### Using Environment Variables

```sh
SCOPE_SET_GLOBAL_TRACER=true
```


## Change testing mode

This variable indicates whether the agent is running tests (`true`) or it is being used for runtime instrumentation (`false`).

### Using Environment Variables

```sh
SCOPE_TESTING_MODE=false
```

### Using YAML Configuration file

```yaml
scope:
  mode:
    testing: false
  
```

If `SCOPE_TESTING_MODE` is not specified, the agent sets to  `true`.



## Adding agent metadata

You can send arbitrary metadata for every test associated with certain commit which will be shown by Scope.

Additionally, it is possible to set an environment variable as metadata value for a certain key, whose final value will be evaluated at runtime.

### Using Environment Variables

```sh
SCOPE_METADATA="sample.key1=$SAMPLE_VAR1,sample.key2=$SAMPLE_VAR2,sample.key3=sampleValue3"
```



### Using YAML Configuration file

```yaml
scope:
  metadata:
    sample.key1: $SAMPLE_VAR1
    sample.key2: $SAMPLE_VAR2
    sample.key3: sampleValue3
```

## Include DB statements values in DB span tags

You can include DB statement values in the related DB spans.

By default, Scope Python Agent will not send DB statement values as they are considered sensitive information.

### Using Environment Variables

```sh
SCOPE_INSTRUMENTATION_DB_STATEMENT_VALUES=true
```



### Using YAML Configuration file

```yaml
scope:
  instrumentation:
    db:
      statement_values: true
```

## Include HTTP payloads in HTTP span tags

You can include HTTP payloads in the related HTTP spans, truncated to the first 512 bytes.

By default, Scope Python Agent will not send HTTP payloads as they are considered sensitive information.

### Using Environment Variables

```sh
SCOPE_INSTRUMENTATION_HTTP_PAYLOADS=true
```



### Using YAML Configuration file

```yaml
scope:
  instrumentation:
    http:
      payloads: true
```

## Include additional HTTP Headers in HTTP span tags

You can include additional HTTP Headers in HTTP span tags.

By default, Scope Python agent will send common HTTP headers, filtering the content of those which can contain sensitive information, such as:

- `Authorization`
- `Cookie`
- `Set-Cookie`


### Using Environment Variables

```sh
SCOPE_INSTRUMENTATION_HTTP_HEADERS="Authorization,My-Header-One,My-Header-Two"
```



### Using YAML Configuration file

```yaml
scope:
  instrumentation:
    http:
      headers:
        - My-Header-One
        - My-Header-Two
```

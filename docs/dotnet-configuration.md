---
id: dotnet-configuration
title: Scope .NET Agent configuration
sidebar_label: Configuration
---

The behaviour of the Scope Agent can be modified using environment variables or a configuration file `scope.yml` in the source root of the project.

> These configuration settings can also be provided via CLI flags. Run `scope-run --help` for more information.
> If these properties are manually configured, use `true` or `false` only for the boolean value.


## Disabling Scope instrumentation

Scope auto instruments your code and tests by default. You can disable this behaviour.

### Using Environment Variables

```sh
SCOPE_INSTRUMENTATION_ENABLED=false
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
  service: service-name
```



## Setting Scope as Global Tracer

Scope handles Open Tracing spans and traces using its own tracer. You can set Scope as the global tracer so that it captures all the spans generated by any Open Tracing library. 

### Using Environment Variables

```sh
SCOPE_TRACER_GLOBAL=True
```

### Using YAML Configuration file

```yaml
scope:
  tracer:
      global: true
```



## Change testing mode

This variable indicates whether the agent is running tests (`true`) or being used for runtime instrumentation (`false`).

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

If `SCOPE_TESTING_MODE` is not specified, the agent sets to  `true` when running in CI and `false` otherwise.

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
    'sample.key1': $SAMPLE_VAR1
    'sample.key2': $SAMPLE_VAR2
    'sample.key3': sampleValue3
```



## Select agent metadata as test configuration

Yon can select metadata keys to be considered as relevant in the configuration of the test.

By default, Scope .NET agent adds both `platform.name` and `dotnet.runtime` metadata key to the test configuration.

### Using Environment Variables

```sh
SCOPE_CONFIGURATION="sample.key1,sample.key2"
```

### Using YAML Configuration file

```yaml
scope:
  configuration:
    - 'sample.key1'
    - 'sample.key2'
```



## Adding Code Path information

You can add Code Path information to show the executed lines of a certain test in a certain commit.

By default, Scope .NET Agent will not send Code Path information.

### Using Environment Variables

```sh
SCOPE_CODE_PATH=True
```

### Using YAML Configuration file

```yaml
scope:
  code_path: true
```



## Include DB statements values in DB span tags

You can include DB statement values in the related DB spans.

By default, Scope .NET Agent will not send DB statement values as they are considered sensitive information.

### Using Environment Variables

```sh
SCOPE_INSTRUMENTATION_DB_STATEMENT_VALUES=True
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

By default, Scope .NET Agent will not send HTTP payloads as they are considered sensitive information.


### Using Environment Variables

```sh
SCOPE_INSTRUMENTATION_HTTP_PAYLOAD=True
```

### Using YAML Configuration file

```yaml
scope:
  instrumentation:
    http:
      payload: true
```



## Include additional HTTP Headers in HTTP span tags

You can include additional HTTP Headers in HTTP span tags.

By default, Scope .NET agent will send common HTTP headers, filtering the content of those which can contain sensitive information, such as:

- `Authorization`
- `Cookie`
- `Set-Cookie`

Note that the content of every header configured explicitly to be shown in the HTTP span tags will not be filtered. 

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
        - Authorization
        - My-Header-One
        - My-Header-Two
```

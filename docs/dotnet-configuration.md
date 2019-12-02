---
id: dotnet-configuration
title: Scope .NET Agent configuration
sidebar_label: Configuration
---

## Adding agent metadata

You can send arbitrary metadata for every test associated with certain commit which will be shown by Scope.

Additionally, it is possible to set an environment variable as metadata value for a certain key, whose final value will be evaluated at runtime.

### Using Environment Variables

```sh
export SCOPE_METADATA="sample.key1=$SAMPLE_VAR1,sample.key2=$SAMPLE_VAR2,sample.key3=sampleValue3"
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
export SCOPE_CONFIGURATION="sample.key1,sample.key2"
```

### Using YAML Configuration file

```yaml
scope:
  configuration:
    - 'sample.key1'
    - 'sample.key2'
```

## Adding code path information

You can add code path information to show the executed lines of a certain test in a certain commit.

By default, Scope .NET agent will not send code path information.

### Using Environment Variables

```sh
export SCOPE_CODE_PATH=True
```

### Using YAML Configuration file

```yaml
scope:
  code_path: true
```

## Include DB statements values in DB span tags

You can include DB statement values in the related DB spans.

By default, Scope .NET agent will not send DB statement values as they are considered sensitive information.

### Using Environment Variables

```sh
export SCOPE_INSTRUMENTATION_DB_STATEMENT_VALUES=True
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

By default, Scope .NET agent will not send HTTP payloads as they are considered sensitive information.


### Using Environment Variables

```sh
export SCOPE_INSTRUMENTATION_HTTP_PAYLOAD=True
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
export SCOPE_INSTRUMENTATION_HTTP_HEADERS="Authorization,My-Header-One,My-Header-Two"
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

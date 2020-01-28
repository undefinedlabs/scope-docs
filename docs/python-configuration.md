---
id: python-configuration
title: Scope Python Agent configuration
sidebar_label: Configuration
---

## Adding agent metadata

You can send arbitrary metadata for every test associated with certain commit which will be shown by Scope.

Additionally, it is possible to set an environment variable as metadata value for a certain key, whose final value will be evaluated at runtime.

### Using Environment Variables

`SCOPE_METADATA="sample.key1=$SAMPLE_VAR1,sample.key2=$SAMPLE_VAR2,sample.key3=sampleValue3"`

### Using YAML Configuration file

```yaml
scope:
  metadata:
    sample.key1: $SAMPLE_VAR1
    sample.key2: $SAMPLE_VAR2
    sample.key3: sampleValue3
```

## Include HTTP payloads in HTTP span tags

You can include HTTP payloads in the related HTTP spans, truncated to the first 512 bytes.

By default, Scope Python Agent will not send HTTP payloads as they are considered sensitive information.

### Using Environment Variables

`SCOPE_INSTRUMENTATION_HTTP_PAYLOADS=true`

### Using YAML Configuration file

```yaml
scope:
  instrumentation:
    http:
      payloads: true
```

## Include DB statements values in DB span tags

You can include DB statement values in the related DB spans.

By default, the Scope Python agent will not send DB statement values as they are considered sensitive information.

### Using Environment Variables

`SCOPE_INSTRUMENTATION_DB_STATEMENT_VALUES=true`

### Using YAML Configuration file

```yaml
scope:
  instrumentation:
    db:
      statement_values: true
```

## Include additional HTTP Headers in HTTP span tags

You can include additional HTTP Headers in HTTP span tags.

By default, the Scope Python agent will send common HTTP headers, filtering the content of those which can contain sensitive information, such as:

- `Authorization`
- `Cookie`
- `Set-Cookie`

### Using Environment Variables

`SCOPE_INSTRUMENTATION_HTTP_HEADERS="My-Header-One,My-Header-Two"`

### Using YAML Configuration file

```yaml
scope:
  instrumentation:
    http:
      headers:
        - My-Header-One
        - My-Header-Two
```

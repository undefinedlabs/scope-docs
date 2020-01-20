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

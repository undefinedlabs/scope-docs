---
id: java-configuration
title: Scope Java Agent configuration
sidebar_label: Configuration
---

## Adding agent metadata

You can send arbitrary metadata for every test associated with certain commit which will be shown by Scope.

Additionally, it is possible to set na environment variable as metadata value for a certain key, whose final value will be evaluated at runtime.

### Using Environment Variables

`SCOPE_METADATA="sample.key1=$SAMPLE_VAR1,sample.key2=$SAMPLE_VAR2,sample.key3=sampleValue3"`

### Using YAML Configuration file

```yaml
scope:
  metadata:
    - sample.key1: $SAMPLE_VAR1
    - sample.key2: $SAMPLE_VAR2
    - sample.key3: sampleValue3
```

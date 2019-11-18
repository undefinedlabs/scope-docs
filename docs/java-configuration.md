---
id: java-configuration
title: Scope Java Agent configuration
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
    - sample.key1: $SAMPLE_VAR1
    - sample.key2: $SAMPLE_VAR2
    - sample.key3: sampleValue3
```

## Select agent metadata as test configuration

Yon can select metadata keys to be considered as relevant in the configuration of the test.

By default, Scope Java agent adds the `java.version` metadata key to the test configuration.

### Using Environment Variables

`SCOPE_CONFIGURATION="sample.key1,sample.key2"`

### Using YAML Configuration file

```yaml
scope:
  configuration:
    - sample.key1
    - sample.key2
```

## Adding code path information

You can add code path information to certain spans to show the executed lines given a certain test in a certain commit.

Apart from the activation/deactivation of the code path flag, it is needed to configure which packages will be needed to be tracked by the Scope Java Agent.

You just need to indicate the base package, and every sub-package, starting from that point, will be included as observable package.

### Using Environment Variables

```sh
SCOPE_CODE_COVERAGE=true
SCOPE_CODE_COVERAGE_BASE_PACKAGES="foo.bar.xyz, bar.foo"
```

### Using YAML Configuration file

```yaml
scope:
  instrumentation:
    testsframeworks:
      code_coverage: true
      code_coverage_base_packages: "foo.bar.xyz, bar.foo"
```

## Include DB statements values in DB span tags

You can include DB statement values in the related DB spans.

By default, Scope Java agent will not send DB statement values due to be considered sensitive information.

### Using Environment Variables

`SCOPE_INSTRUMENTATION_DB_STATEMENT_VALUES=true`

### Using YAML Configuration file

```yaml
scope:
  instrumentation:
    db:
      statement_values: true
```

## Include HTTP payloads in HTTP span tags

You can include HTTP payloads in the related HTTP spans, truncated to the first 512 bytes.

By default, Scope Java agent will not send HTTP payloads due to be considered sensitive information.


### Using Environment Variables

`SCOPE_INSTRUMENTATION_HTTP_PAYLOADS=true`

### Using YAML Configuration file

```yaml
scope:
  instrumentation:
    http:
      payloads: true
```

## Include additional HTTP Headers in HTTP span tags

You can include additional HTTP Headers in HTTP span tags.

By default, Scope Java agent will send common HTTP headers, filtering the content of those which can contain sensitive information, such as:

- `Authorization`
- `Cookie`
- `Set-Cookie`

Note that the content of every header configured explicitly to be shown in the HTTP span tags will not be filtered. 

### Using Environment Variables

`SCOPE_INSTRUMENTATION_HTTP_HEADERS="Authorization,My-Header-One,My-Header-Two"`

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
---
id: python-configuration
title: Scope Python Agent configuration
sidebar_label: Configuration
---

> If these properties are manually configured, use only `true` or `false` for boolean values.

The behaviour of the Scope Agent can be modified using environment variables or a configuration file `scope.yml` in the source root of the project.

These configuration settings can also be provided via CLI flags. Check out the
[CLI reference](https://scope-python-agent.readthedocs.io/en/latest/cli.html) documentation for details.

## Disabling Scope instrumentation

Scope auto instruments your code and tests by default. You can disable this behaviour.

<!--DOCUSAURUS_CODE_TABS-->
<!--Environment Variable-->

```sh
SCOPE_AUTO_INSTRUMENT=false
```

<!--YAML Configuration File-->

```yaml
scope:
  instrumentation:
    enabled: false
```

<!--END_DOCUSAURUS_CODE_TABS-->

## Changing service name

You can specify the name of the service when sending data to Scope. Scope uses `default` as fallback.

<!--DOCUSAURUS_CODE_TABS-->
<!--Environment Variable-->

```sh
SCOPE_SERVICE="service-name"
```

<!--YAML Configuration File-->

```yaml
scope:
  service: "service-name"
```

<!--END_DOCUSAURUS_CODE_TABS-->

## Setting Scope as Global Tracer

If you set Scope as OpenTracing Global Tracer, your own spans will be captured and shown as part of the Scope trace view for a certain test.

<!--DOCUSAURUS_CODE_TABS-->
<!--Environment Variable-->

```sh
SCOPE_SET_GLOBAL_TRACER=true
```

<!--YAML Configuration File-->

```yaml
scope:
  tracer:
    global: true
```

<!--END_DOCUSAURUS_CODE_TABS-->

## Change testing mode

This variable indicates whether the agent is running tests (`true`) or it is being used for runtime instrumentation (`false`).

<!--DOCUSAURUS_CODE_TABS-->
<!--Environment Variable-->

```sh
SCOPE_TESTING_MODE=false
```

<!--YAML Configuration File-->

```yaml
scope:
  mode:
    testing: false
```

<!--END_DOCUSAURUS_CODE_TABS-->

If `SCOPE_TESTING_MODE` is not specified, the agent sets to `true`.

## Adding agent metadata

You can send arbitrary metadata for every test associated with certain commit which will be shown in Scope.

Additionally, it is possible to set an environment variable as metadata value for a certain key, whose final value will be evaluated at runtime.

<!--DOCUSAURUS_CODE_TABS-->
<!--Environment Variable-->

```sh
SCOPE_METADATA="sample.key1=$SAMPLE_VAR1,sample.key2=$SAMPLE_VAR2,sample.key3=sampleValue3"
```

<!--YAML Configuration File-->

```yaml
scope:
  metadata:
    sample.key1: $SAMPLE_VAR1
    sample.key2: $SAMPLE_VAR2
    sample.key3: sampleValue3
```

<!--END_DOCUSAURUS_CODE_TABS-->

## Include DB statements values in DB span tags

You can include DB statement values in the related DB spans.

By default, Scope Python Agent will not send DB statement values as they are considered sensitive information.

<!--DOCUSAURUS_CODE_TABS-->
<!--Environment Variable-->

```sh
SCOPE_INSTRUMENTATION_DB_STATEMENT_VALUES=true
```

<!--YAML Configuration File-->

```yaml
scope:
  instrumentation:
    db:
      statement_values: true
```

<!--END_DOCUSAURUS_CODE_TABS-->

## Include HTTP payloads in HTTP span tags

You can include HTTP payloads in the related HTTP spans, truncated to the first 512 bytes.

By default, Scope Python Agent will not send HTTP payloads as they are considered sensitive information.

<!--DOCUSAURUS_CODE_TABS-->
<!--Environment Variable-->

```sh
SCOPE_INSTRUMENTATION_HTTP_PAYLOADS=true
```

<!--YAML Configuration File-->

```yaml
scope:
  instrumentation:
    http:
      payloads: true
```

<!--END_DOCUSAURUS_CODE_TABS-->

## Include additional HTTP Headers in HTTP span tags

You can include additional HTTP Headers in HTTP span tags.

By default, Scope Python agent will send common HTTP headers, filtering the content of those which can contain sensitive information:

- `Authorization`
- `Cookie`
- `Set-Cookie`

Note that the content of every header configured explicitly to be shown in the HTTP span tags will not be redacted.

<!--DOCUSAURUS_CODE_TABS-->
<!--Environment Variable-->

```sh
SCOPE_INSTRUMENTATION_HTTP_HEADERS="Authorization,My-Header-One,My-Header-Two"
```

<!--YAML Configuration File-->

```yaml
scope:
  instrumentation:
    http:
      headers:
        - Authorization
        - My-Header-One
        - My-Header-Two
```

<!--END_DOCUSAURUS_CODE_TABS-->

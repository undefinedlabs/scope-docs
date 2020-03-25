---
id: nodejs-configuration
title: Scope Node.js configuration
sidebar_label: Configuration
---

> If these properties are manually configured, use only `true` or `false` for boolean values.

The behaviour of the Scope Agent can be modified using environment variables or a configuration file `scope.yml` in the source root of the project.

## Disabling Scope instrumentation

Scope auto instruments your code and tests by default. You can disable this behaviour.

<!--DOCUSAURUS_CODE_TABS-->
<!--Environment Variable-->

```sh
SCOPE_INSTRUMENTATION_ENABLED=false
```

<!--YAML Configuration File-->

```yaml
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
service: "service-name"
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
mode:
  testing: false
```

<!--END_DOCUSAURUS_CODE_TABS-->

If `SCOPE_TESTING_MODE` is not specified, the agent sets it to `true`.

## Adding agent metadata

You can send arbitrary metadata for every test associated with a certain commit.

<!--DOCUSAURUS_CODE_TABS-->
<!--Environment Variable-->

```sh
SCOPE_METADATA="sample.key1=sampleValue1,sample.key2=sampleValue2,sample.key3=sampleValue3"
```

<!--YAML Configuration File-->

```yaml
metadata:
  sample.key1: sampleValue1
  sample.key2: sampleValue2
  sample.key3: sampleValue3
```

<!--END_DOCUSAURUS_CODE_TABS-->

## Include HTTP payloads in HTTP span tags

You can include HTTP payloads in the related HTTP spans, truncated to the first 512 bytes.

By default, Scope Node.js Agent will not send HTTP payloads as they are considered sensitive information.

<!--DOCUSAURUS_CODE_TABS-->
<!--Environment Variable-->

```sh
SCOPE_INSTRUMENTATION_HTTP_PAYLOADS=true
```

<!--YAML Configuration File-->

```yaml
instrumentation:
  http:
    payloads: true
```

<!--END_DOCUSAURUS_CODE_TABS-->

## Include DB statements values in DB span tags

You can include DB statement values in the related DB spans.

By default, Scope Node.js Agent will not send DB statement values as they are considered sensitive information.

<!--DOCUSAURUS_CODE_TABS-->
<!--Environment Variable-->

```sh
SCOPE_INSTRUMENTATION_DB_STATEMENT_VALUES=true
```

<!--YAML Configuration File-->

```yaml
instrumentation:
  db:
    statement_values: true
```

<!--END_DOCUSAURUS_CODE_TABS-->

## Include additional HTTP Headers in HTTP span tags

You can include additional HTTP Headers in HTTP span tags.

By default, Scope Node.js Agent will send common HTTP headers, filtering the content of those which can contain sensitive information, such as:

- `Authorization`
- `Cookie`
- `Set-Cookie`

> Note that the content of every header configured explicitly to be shown in the HTTP span tags will **not** be filtered.

<!--DOCUSAURUS_CODE_TABS-->
<!--Environment Variable-->

```sh
SCOPE_INSTRUMENTATION_HTTP_HEADERS="Authorization,My-Header-One,My-Header-Two"
```

<!--YAML Configuration File-->

```yaml
instrumentation:
  http:
    headers:
      - Authorization
      - My-Header-One
      - My-Header-Two
```

<!--END_DOCUSAURUS_CODE_TABS-->

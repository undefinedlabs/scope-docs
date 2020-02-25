---
id: java-configuration
title: Scope Java Agent configuration
sidebar_label: Configuration
---

The behaviour of the Scope Agent can be modified using environment variables or a configuration file `scope.yml` in the source root of the project.

> If these properties are manually configured, use `true` or `false` only for the boolean value.

## Changing Scope Logger level

You can change the Scope Logger level using the values `error`, `warn`, `info`, `debug` and `trace` levels. By default, Scope Logger level is `info`.

<!--DOCUSAURUS_CODE_TABS-->
<!--Environment Variable-->

```sh
SCOPE_LOGGER_LEVEL=debug
```

<!--YAML Configuration File-->

```yaml
logger:
  level: "debug"
```

<!--END_DOCUSAURUS_CODE_TABS-->

## Changing Scope Logger root path

By default, Scope Java agent will create a log file in the following folder path based on your platform:

<!--DOCUSAURUS_CODE_TABS-->
<!-- Windows -->

`%APPDATA%/scope/logs/`

<!-- Linux -->

`/var/log/scope/`

<!-- macOS -->

`~/Library/Logs/Scope/`

<!--END_DOCUSAURUS_CODE_TABS-->

You can set the Scope Logger root path manually.

<!--DOCUSAURUS_CODE_TABS-->
<!--Environment Variable-->

```sh
SCOPE_LOGGER_ROOT=/home/user/projects/scope/log/
```

<!--YAML Configuration File-->

```yaml
logger:
  root: "/home/user/projects/scope/log/"
```

<!--END_DOCUSAURUS_CODE_TABS-->

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

## Setting Scope as Global Tracer

If you set Scope as OpenTracing Global Tracer, your own spans will be captured and shown as part of the Scope trace view for a certain test.

<!--DOCUSAURUS_CODE_TABS-->
<!--Environment Variable-->

```sh
SCOPE_TRACER_GLOBAL=true
```

<!--YAML Configuration File-->

```yaml
tracer:
  global: true
```

<!--END_DOCUSAURUS_CODE_TABS-->

## Change testing mode

This variable indicates whether the agent is running tests (`true`) or it is being used for runtime instrumentation (`false`). If `SCOPE_TESTING_MODE` is not set, the agent sets to `true` when testing frameworks are present in classpath. Otherwise, the agent sets to `false`.

<!--DOCUSAURUS_CODE_TABS-->
<!--Environment Variable-->

```sh
SCOPE_TESTING_MODE=false
```

<!--YAML Configuration File-->

```yaml
testing_mode: true
```

<!--END_DOCUSAURUS_CODE_TABS-->

## Adding agent metadata

You can send arbitrary metadata for every test associated with certain commit which will be shown by Scope.

Additionally, it is possible to set an environment variable as metadata value for a certain key, whose final value will be evaluated at runtime.

<!--DOCUSAURUS_CODE_TABS-->
<!--Environment Variable-->

```sh
SCOPE_METADATA="sample.key1=$SAMPLE_VAR1,sample.key2=$SAMPLE_VAR2,sample.key3=sampleValue3"
```

<!--YAML Configuration File-->

```yaml
metadata:
  sample.key1: $SAMPLE_VAR1
  sample.key2: $SAMPLE_VAR2
  sample.key3: sampleValue3
```

<!--END_DOCUSAURUS_CODE_TABS-->

## Select agent metadata as test configuration

Yon can select metadata keys to be considered as relevant in the configuration of the test.

By default, Scope Java agent adds the `java.version` metadata key to the test configuration.

<!--DOCUSAURUS_CODE_TABS-->
<!--Environment Variable-->

```sh
SCOPE_CONFIGURATION="sample.key1,sample.key2"
```

<!--YAML Configuration File-->

```yaml
configuration:
  - sample.key1
  - sample.key2
```

<!--END_DOCUSAURUS_CODE_TABS-->

## Adding Code Path information

You can add Code Path information to certain spans to show the executed lines given a certain test in a certain commit.

Apart from the activation/deactivation of the Code Path flag, it is needed to configure which packages will be needed to be tracked by the Scope Java Agent.

You just need to indicate the base package, and every sub-package, starting from that point, will be included as observable package.

<!--DOCUSAURUS_CODE_TABS-->
<!--Environment Variable-->

```sh
SCOPE_CODE_PATH_ENABLED=true
SCOPE_CODE_PATH_BASE_PACKAGES="foo.bar.xyz, bar.foo"
```

<!--YAML Configuration File-->

```yaml
code_path:
  enabled: true
  base_packages: "foo.bar.xyz, bar.foo"
```

<!--END_DOCUSAURUS_CODE_TABS-->

## Include DB statements values in DB span tags

You can include DB statement values in the related DB spans.

By default, Scope Java Agent will not send DB statement values as they are considered sensitive information.

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

## Include HTTP payloads in HTTP span tags

You can include HTTP payloads in the related HTTP spans, truncated to the first 512 bytes.

By default, Scope Java Agent will not send HTTP payloads as they are considered sensitive information.

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

## Include additional HTTP Headers in HTTP span tags

You can include additional HTTP Headers in HTTP span tags.

By default, Scope Java agent will send common HTTP headers, filtering the content of those which can contain sensitive information, such as:

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

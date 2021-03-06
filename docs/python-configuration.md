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
SCOPE_SET_GLOBAL_TRACER=true
```

<!--YAML Configuration File-->

```yaml
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
testing_mode: false
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
instrumentation:
  http:
    headers:
      - Authorization
      - My-Header-One
      - My-Header-Two
```

<!--END_DOCUSAURUS_CODE_TABS-->

## Code Path

You can add Code Path information that will show the executed lines in a certain test at a certain commit.

<!--DOCUSAURUS_CODE_TABS-->
<!--Environment Variable-->

```sh
SCOPE_CODE_PATH_ENABLED=true
```

<!--YAML Configuration File-->

```yaml
code_path:
  enabled: true
```

<!--END_DOCUSAURUS_CODE_TABS-->

## Scope Intelligent Test Runner

Scope's Intelligent Test Runner will selectively run only the subset of tests affected by code changes. For more information go to [Scope Intelligent Test Runner](intelligent-test-runner).

### Enable or disable

Through this configuration parameter you can enable or disable Scope Intelligent Test Runner. The rest of `runner` configuration parameters will have no effect if `enabled` is false.

<!--DOCUSAURUS_CODE_TABS-->
<!--Environment Variable-->

```sh
SCOPE_RUNNER_ENABLED=true
```

<!--YAML Configuration File-->

```yaml
runner:
  enabled: true
```

<!--END_DOCUSAURUS_CODE_TABS-->

### Fail retries

This parameter determines the number of times a test will be retried if it fails.

<!--DOCUSAURUS_CODE_TABS-->
<!--Environment Variable-->

```sh
SCOPE_RUNNER_FAIL_RETRIES=4
```

<!--YAML Configuration File-->

```yaml
runner:
  fail_retries: 4
```

<!--END_DOCUSAURUS_CODE_TABS-->

### Included and excluded branches

There are two parameters to control the branches in which you want to run the Scope Intelligent Test Runner: `runner.include_branches` and `runner.exclude_branches`. The way they work is the following:

- If `runner.include_branches` is configured, only configured branches are included.
- If `runner.exclude_branches` is configured, all branches except configured branches are included.
- If both `runner.include_branches` and `runner.exclude_branches` are configured, the runner will only take into account `runner.include_branches`. If the same branch is configured, a warning message will be shown.

<!--DOCUSAURUS_CODE_TABS-->
<!--Environment Variable-->

```sh
SCOPE_RUNNER_INCLUDE_BRANCHES=feature-branch-1,feature-branch-2
```

<!--YAML Configuration File-->

```yaml
runner:
  include_branches:
    - feature-branch-1
    - feature-branch-2
```

<!--END_DOCUSAURUS_CODE_TABS-->

<!--DOCUSAURUS_CODE_TABS-->
<!--Environment Variable-->

```sh
SCOPE_RUNNER_EXCLUDE_BRANCHES=master
```

<!--YAML Configuration File-->

```yaml
runner:
  exclude_branches:
    - master
```

<!--END_DOCUSAURUS_CODE_TABS-->

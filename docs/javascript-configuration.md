---
id: javascript-configuration
title: Scope Javascript Agent configuration
sidebar_label: Configuration
---

> If these properties are manually configured, use only `true` or `false` for boolean values.

The behaviour of the Scope Agent can be modified using environment variables or a configuration file `scope.yml` in the source root of the project.

An example `scope.yml`:

```yaml
service: "service-name"
repository: "https://github.com/undefinedlabs/scope-docs.git"
source_root: "/home/user/projects/scope-docs"
code_path:
  enabled: true
metadata:
  sample.key1: sampleValue1
testing_mode: true
instrumentation:
  enabled: true
  db:
    statement_values: true
  http:
    payloads: true
    headers:
      - Authorization
      - My-Header-One
      - My-Header-Two
tracer:
  global: true
runner:
  enabled: true
  fail_retries: 5
  include_branches:
    - feature-branch-1
    - feature-branch-2
  exclude_branches:
    - master
```

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

By default, Scope Javascript Agent will not send HTTP payloads as they are considered sensitive information.

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

By default, Scope Javascript Agent will send common HTTP headers, filtering the content of those which can contain sensitive information, such as:

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

> This is only available for tests run by Jest for the moment and it needs extra configuration. Have a look at the [code path configuration](javascript-installation#code-path).

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

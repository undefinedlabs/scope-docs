---
id: nodejs-configuration
title: Scope Node.js configuration
sidebar_label: Configuration
---

> If these properties are manually configured, use `true` or `false` only for the boolean value.

The behaviour of the Scope Agent can be modified using environment variables or a configuration file `scope.yml` in the source root of the project.

## Disabling Scope instrumentation

Scope auto instruments your code and tests by default. You can disable this behaviour.

### Using Environment Variables

```sh
SCOPE_AUTO_INSTRUMENT=false
```

### Using YAML Configuration file

```yaml
scope:
  instrumentation:
    enabled: false
```


## Changing service name

You can specify the name of the service when sending data to Scope. Scope uses `default` as fallback.

### Using Environment Variables

```sh
SCOPE_SERVICE="service-name"
```

### Using YAML Configuration file

```yaml
scope:
  service: 'service-name'
```

## Change testing mode

This variable indicates whether the agent is running tests (`true`) or it is being used for runtime instrumentation (`false`). By default it will run in testing mode

### Using Environment Variables

```sh
SCOPE_TESTING_MODE=false
```

## Include HTTP payloads in HTTP span tags

You can include HTTP payloads in the related HTTP spans, truncated to the first 512 bytes.

By default, Scope Node.js Agent will not send HTTP payloads as they are considered sensitive information.

### Using Environment Variables

```sh
SCOPE_INSTRUMENTATION_HTTP_PAYLOADS=true
```



### Using YAML Configuration file

```yaml
scope:
  instrumentation:
    http:
      payloads: true
```

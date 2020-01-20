---
id: nodejs-configuration
title: Scope Node.js configuration
sidebar_label: Configuration
---

## Include HTTP payloads in HTTP span tags

You can include HTTP payloads in the related HTTP spans, truncated to the first 512 bytes.

By default, Scope Node.js Agent will not send HTTP payloads as they are considered sensitive information.

### Using Environment Variables

`SCOPE_INSTRUMENTATION_HTTP_PAYLOADS=true`

### Using YAML Configuration file

```yaml
scope:
  instrumentation:
    http:
      payloads: true
```

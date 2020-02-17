---
id: import-configuration
title: Scope Import configuration
sidebar_label: Configuration
---

The behaviour of the Scope Import can be modified by using environment variables.

> If these properties are manually configured, use `true` or `false` only for the boolean value.

## Changing service name

You can specify the name of the service when sending data to Scope. Scope uses `default` as fallback.

<!--DOCUSAURUS_CODE_TABS-->
<!--Environment Variable-->

```sh
SCOPE_SERVICE="service-name"
```

<!--END_DOCUSAURUS_CODE_TABS-->

---
id: nodejs-compatibility
title: Scope Node.js Agent compatibility
sidebar_label: Compatibility
---

### Testing libraries

The instrumentation is automatic.

| Name                       | Span/event creation | Inject | Extract |
| -------------------------- | :-----------------: | :----: | :-----: |
| [Jest](https://jestjs.io/) |          ✓          |   ✓    |    ✓    |

### Libraries

| Name                                       | Span/event creation | Inject | Extract |
| ------------------------------------------ | :-----------------: | :----: | :-----: |
| [`http`](https://nodejs.org/api/http.html) |          ✓          |   ✓    |    ✓    |

### CI providers

The Scope Javascript agent will work on any CI provider, but will autodetect build information if running on the following CI providers:

- [CircleCI](https://circleci.com/)

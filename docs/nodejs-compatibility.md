---
id: nodejs-compatibility
title: Scope Node.js Agent compatibility
sidebar_label: Compatibility
---

### Testing libraries

The instrumentation is automatic.

| Name                       | Span/event creation | Inject | Extract | HTTP |
| -------------------------- | :-----------------: | :----: | :-----: | :--: |
| [Jest](https://jestjs.io/) |          ✓          |   ✓    |    ✓    |  ✓   |

### CI providers

The Scope Javascript agent will work on any CI provider, but will autodetect build information if running on the following CI providers:

- [CircleCI](https://circleci.com/)

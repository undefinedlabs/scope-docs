---
id: nodejs-compatibility
title: Scope Node.js Agent compatibility
sidebar_label: Compatibility
---

### Testing libraries

The instrumentation is automatic.

| Name                       | Span/event creation | Inject | Extract |                   HTTP Server                   |                        HTTP Client                         |
| -------------------------- | :-----------------: | :----: | :-----: | :---------------------------------------------: | :--------------------------------------------------------: |
| [Jest](https://jestjs.io/) |          ✓          |   ✓    |    ✓    | [express](https://github.com/expressjs/express) | All clients using [http](https://nodejs.org/api/http.html) |

### CI providers

The Scope Javascript agent will work on any CI provider, but will autodetect build information if running on the following CI providers:

- [CircleCI](https://circleci.com/)

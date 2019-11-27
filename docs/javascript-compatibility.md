---
id: javascript-compatibility
title: Scope Javascript Agent compatibility
sidebar_label: Compatibility
---

### Testing libraries

The instrumentation is automatic.

| Name                               | Span/event creation | Inject |    HTTP client    |  User events   | Console logs | Route changes | Exceptions |
| ---------------------------------- | :-----------------: | :----: | :---------------: | :------------: | :----------: | :-----------: | :--------: |
| [Jest](https://jestjs.io/)         |          ✓          |   ✓    |      `fetch`      |     click      |      ✓       |               |     ✓      |
| [Cypress](https://www.cypress.io/) |          ✓          |   ✓    | `fetch` and `xhr` | click and type |      ✓       |       ✓       |     ✓      |

### CI providers

The Scope Javascript agent will work on any CI provider, but will autodetect build information if running on the following CI providers:

- [CircleCI](https://circleci.com/)

---
id: javascript-compatibility
title: Scope Javascript Agent compatibility
sidebar_label: Compatibility
---

### Testing libraries

The instrumentation is automatic.

| Name                               | Span/event creation | Inject | HTTP (XHR and fetch) | User events | Console logs | Route changes | Exceptions |
| ---------------------------------- | :-----------------: | :----: | :------------------: | :---------: | :----------: | :-----------: | :--------: |
| [Jest](https://jestjs.io/)         |          ✓          |        |                      |             |              |               |            |
| [Cypress](https://www.cypress.io/) |          ✓          |   ✓    |          ✓           |      ✓      |      ✓       |       ✓       |     ✓      |

### CI providers

The Scope Javascript agent will work on any CI provider, but will autodetect build information if running on the following CI providers:

- [CircleCI](https://circleci.com/)

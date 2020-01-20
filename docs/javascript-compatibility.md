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

- [Jenkins](https://jenkins.io/)
- [CircleCI](https://circleci.com/)
- [GitLab CI](https://docs.gitlab.com/ee/ci/)
- [Travis](https://travis-ci.org/)
- [AppVeyor](https://ci.appveyor.com/)
- [Azure Pipelines](https://azure.microsoft.com/en-us/services/devops/pipelines/)
- [Bitbucket Pipelines](https://bitbucket.org/product/features/pipelines)
- [GitHub Actions](https://github.com/features/actions)
- [TeamCity](https://www.jetbrains.com/teamcity/)

---
id: javascript-compatibility
title: Scope Javascript Agent compatibility
sidebar_label: Compatibility
---

### Node.js versions

The Scope Javascript Agent is compatible with the following versions of Node.js:

| Language |        Versions        |
| -------- | :--------------------: |
| Node.js  | `10.x`, `12.x`, `13.x` |

### Testing libraries

The instrumentation is automatic.

| Name                               |         Versions         | Span/event creation | Inject and extract |    HTTP client    |      User events      | Console logs | Route changes | Exceptions |
| ---------------------------------- | :----------------------: | :-----------------: | :----------------: | :---------------: | :-------------------: | :----------: | :-----------: | :--------: |
| [Jest](https://jestjs.io/)         | `24.0.0`(\*) to `25.3.0` |          ✓          |         ✓          | `fetch` and `xhr` | `click` and `keydown` |      ✓       |               |     ✓      |
| [Cypress](https://www.cypress.io/) |    `3.5.0` to `4.3.0`    |          ✓          |         ✓          | `fetch` and `xhr` |  `click` and `type`   |      ✓       |       ✓       |     ✓      |

(\*) Compatibility with `>=23.0.0` can be achieved. Have a look at [installation instructions](javascript-installation#older-versions-of-jest).

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
- [Buildkite](https://buildkite.com/)

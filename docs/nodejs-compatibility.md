---
id: nodejs-compatibility
title: Scope Node.js Agent compatibility
sidebar_label: Compatibility
---

### Node.js versions

The Scope Node.js Agent is compatible with the following versions of Node.js:

| Language |     Versions     |
| -------- | :--------------: |
| Node.js  | 10.x, 12.x, 13.x |

### Testing libraries

The instrumentation is automatic.

| Name                       | Span/event creation | Inject and extract |    HTTP client    |      User events      | Console logs | Exceptions |
| -------------------------- | :-----------------: | :----------------: | :---------------: | :-------------------: | :----------: | :--------: |
| [Jest](https://jestjs.io/) |          ✓          |         ✓          | `fetch` and `xhr` | `click` and `keydown` |      ✓       |     ✓      |

### Libraries

| Name                                       | Span/event creation | Inject | Extract |
| ------------------------------------------ | :-----------------: | :----: | :-----: |
| [`http`](https://nodejs.org/api/http.html) |          ✓          |   ✓    |    ✓    |
| [`pg`](https://node-postgres.com/)         |          ✓          |        |    ✓    |
| [`redis`](https://redis.js.org/)           |          ✓          |        |    ✓    |

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

---
id: go-compatibility
title: Scope Go Agent compatibility
sidebar_label: Compatibility
---

The Scope Go agent is compatible with the following versions of Go:

| Language    | Version |
| ----------- | :-----: |
| Go          |  1.11+  |

### Libraries

The Scope Go agent is compatible with the following libraries:

| Name                                                         | Span/event creation | Extract | Inject |
| ------------------------------------------------------------ | :-----------------: | :-----: | :----: |
| [`testing`](https://golang.org/pkg/testing/)                 |          ✓          |         |        |
| [`net/http`](https://golang.org/pkg/net/http/)               |          ✓          |    ✓    |    ✓   |
| [`google.golang.org/grpc`](https://github.com/grpc/grpc-go)  |          ✓          |    ✓    |    ✓   |

> Do you use a language or library not listed here? Please [let us know](https://home.undefinedlabs.com/goto/support)!

### CI providers

The Scope Go agent will work on any CI provider, but will autodetect build and git information 
(repository, commit, branch and source root directory) if running on the following CI providers:

* [Jenkins](https://jenkins.io/)
* [CircleCI](https://circleci.com/)
* [GitLab CI](https://docs.gitlab.com/ee/ci/)
* [Travis](https://travis-ci.org/)
* [AppVeyor](https://www.appveyor.com/)
* [Azure Pipelines](https://azure.microsoft.com/en-us/services/devops/pipelines/)
* [Bitbucket Pipelines](https://bitbucket.org/product/features/pipelines)
* [GitHub Actions](https://github.com/features/actions)

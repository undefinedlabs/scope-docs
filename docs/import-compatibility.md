---
id: import-compatibility
title: Scope Import compatibility
sidebar_label: Compatibility
---

### Test reports

The Scope Import tool is compatible with the following test reports:

- [JUnit XML Reports](https://github.com/junit-team/junit5/blob/master/platform-tests/src/test/resources/jenkins-junit.xsd)

### CI providers

The Scope Import tool will work on any CI provider, but will autodetect build and git information
(repository, commit, branch and source root directory) if running on the following CI providers:

- [Jenkins](https://jenkins.io/)
- [CircleCI](https://circleci.com/)
- [GitLab CI](https://docs.gitlab.com/ee/ci/)
- [Travis](https://travis-ci.org/)
- [AppVeyor](https://www.appveyor.com/)
- [Azure Pipelines](https://azure.microsoft.com/en-us/services/devops/pipelines/)
- [Bitbucket Pipelines](https://bitbucket.org/product/features/pipelines)
- [GitHub Actions](https://github.com/features/actions)

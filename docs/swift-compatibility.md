---
id: swift-compatibility
title: Scope Swift Agent compatibility
sidebar_label: Compatibility
---

The Scope Swift agent is compatible with the following platforms:

| Platform    | Version |
| ----------- | :-----: |
| iOS         |  10.0+  |
| macOS       |  10.12+ |
| tvOS        |  10.0+  |

and the following languages:

| Language    | Version |
| ----------- | :-----: |
| Swift       |  4.0+   |
| Objective-C |  2.0+   |


### Libraries

The Scope Swift agent is compatible with the following libraries:

| Name                                                                      | Span/event creation | Extract | Inject |
|---------------------------------------------------------------------------|:-------------------:|:-------:|:------:|
| [XCTest](https://developer.apple.com/documentation/xctest)                |          ✓          |         |        |
| [Alamofire](https://github.com/Alamofire/Alamofire)                       |          ✓          |         |    ✓   |
| [URLSession](https://developer.apple.com/documentation/foundation/nsurlsession)                       |          ✓          |         |    ✓   |
| [URLConnection](https://developer.apple.com/documentation/foundation/nsurlconnection)                       |          ✓          |         |    ✓   |


> Do you use a language or library not listed here? Please [let us know](https://home.undefinedlabs.com/goto/support)!

* ### CI providers

  The Scope Swift agent will work on the following CI providers:

  - [Jenkins](https://jenkins.io/)
  - [CircleCI](https://circleci.com/)
  - [GitLab CI](https://docs.gitlab.com/ee/ci/)
  - [Travis](https://travis-ci.org/)
  - [GitHub Actions](https://github.com/features/actions)
  - [TeamCity](https://www.jetbrains.com/teamcity/)
---
id: java-compatibility
title: Scope Java Agent compatibility
sidebar_label: Compatibility
---

### JDK versions

The Scope Java agent is compatible with the following JDKs:

| JDK                                                                                        |   Versions    | Windows | Linux | OS X |
| ------------------------------------------------------------------------------------------ | :-----------: | :-----: | :---: | :--: |
| [`OpenJDK JVM`](https://openjdk.java.net/)                                                 | `1.7` to `12` |    ✓    |   ✓   |  ✓   |
| [`Oracle Hotspot JVM`](https://www.oracle.com/technetwork/java/javase/overview/index.html) | `1.7` to `12` |    ✓    |   ✓   |  ✓   |

### Scala versions

The Scope Java agent is compatible with the following Scala versions:

| Scala                                  |     Versions     | Windows | Linux | OS X |
| -------------------------------------- | :--------------: | :-----: | :---: | :--: |
| [`Scala`](https://www.scala-lang.org/) | `2.10` to `2.13` |    ✓    |   ✓   |  ✓   |

### Libraries

The Scope Java agent is compatible with the following libraries:

#### Testing frameworks

| Name                                     |      Versions      | Span/event creation | Extract | Inject |
| ---------------------------------------- | :----------------: | :-----------------: | :-----: | :----: |
| [`Junit 4`](https://junit.org/junit4/)   |       `4.x`        |          ✓          |         |        |
| [`Junit 5`](https://junit.org/junit5/)   |       `5.x`        |          ✓          |         |        |
| [`TestNG`](https://testng.org/)          |  `6.4` to `7.1.x`  |          ✓          |         |        |
| [`ScalaTest`](http://www.scalatest.org/) | `2.2.x` to `3.0.x` |          ✓          |         |        |

#### Frameworks and libraries

| Name                              |      Versions      | Span/event creation | Extract | Inject |
| --------------------------------- | :----------------: | :-----------------: | :-----: | :----: |
| [`SLF4J`](https://www.slf4j.org/) |      `1.7.x`       |          ✓          |         |        |
| [`Akka`](https://akka.io/)        | `2.3.x` to `2.5.x` |          ✓          |         |        |

#### Benchmark

| Name                                                       | Versions | Span/event creation | Extract | Inject |
| ---------------------------------------------------------- | :------: | :-----------------: | :-----: | :----: |
| [`JMH`](https://openjdk.java.net/projects/code-tools/jmh/) |  `1.x`   |          ✓          |         |        |

#### App/Web servers

| Name                                         |    Versions    | Span/event creation | Extract | Inject |
| -------------------------------------------- | :------------: | :-----------------: | :-----: | :----: |
| [`Apache Tomcat`](http://tomcat.apache.org/) | `7.x` to `9.x` |          ✓          |    ✓    |        |
| [`Netty`](https://netty.io/)                 |    `4.1.x`     |          ✓          |    ✓    |        |

#### HTTP and messaging

| Name                                                                                                        |       Versions       | Span/event creation | Extract | Inject |
| ----------------------------------------------------------------------------------------------------------- | :------------------: | :-----------------: | :-----: | :----: |
| [`OkHttp3`](https://square.github.io/okhttp/)                                                               |  `3.8.1` to `4.0.x`  |          ✓          |         |   ✓    |
| [`Apache HttpClient`](https://hc.apache.org/httpcomponents-client-4.5.x/index.html/)                        |   `4.3` to `4.5.x`   |          ✓          |         |   ✓    |
| [`java.net (HttpURLConnection)`](https://docs.oracle.com/javase/8/docs/api/java/net/HttpURLConnection.html) |    `1.7` to `12`     |          ✓          |         |   ✓    |
| [`gRPC`](https://grpc.io/)                                                                                  | `1.4.0` to `1.26.x`  |          ✓          |    ✓    |   ✓    |
| [`JMS`](https://docs.oracle.com/javaee/6/tutorial/doc/bncdq.html)                                           |     `1.1`, `2.x`     |          ✓          |    ✓    |   ✓    |
| [`Spring-JMS`](https://spring.io/guides/gs/messaging-jms/)                                                  |     `1.1`, `2.x`     |          ✓          |    ✓    |   ✓    |
| [`Akka HTTP`](https://doc.akka.io/docs/akka-http/current/index.html)                                        | `10.0.x` to `10.1.x` |          ✓          |    ✓    |        |

#### Datastores

| Name                                                   |        Versions         | Span/event creation | Extract | Inject |
| ------------------------------------------------------ | :---------------------: | :-----------------: | :-----: | :----: |
| [`H2 DBMS`](https://www.h2database.com/html/main.html) |  `1.3.146` to `1.4.x`   |          ✓          |         |   ✓    |
| [`MySQL`](https://www.h2database.com/html/main.html)   | `5.6.x`, `5.7.x`, `8.x` |          ✓          |         |   ✓    |

> Do you use a platform or library not listed here? Please [let us know](https://home.undefinedlabs.com/goto/support)!

### CI providers

The Scope Java agent will work on any CI provider, but will autodetect build and git information
(repository, commit, branch and source root directory) if running on the following CI providers:

- [Jenkins](https://jenkins.io/)
- [CircleCI](https://circleci.com/)
- [GitLab CI](https://docs.gitlab.com/ee/ci/)
- [Travis](https://travis-ci.org/)
- [AppVeyor](https://www.appveyor.com/)
- [Azure Pipelines](https://azure.microsoft.com/en-us/services/devops/pipelines/)
- [Bitbucket Pipelines](https://bitbucket.org/product/features/pipelines)
- [GitHub Actions](https://github.com/features/actions)

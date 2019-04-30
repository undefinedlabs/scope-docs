---
id: java-installation
title: Java Agent instructions
sidebar_label: Installation
---


## Compatibility

The Scope Java agent is compatible with the following JVMs:

| JVM                                                                                        | Versions | Windows | Linux | OS X |
|--------------------------------------------------------------------------------------------|----------|:-------:|:-----:|:----:|
| [`OpenJDK JVM`](https://openjdk.java.net/)                                                 | 1.7, 1.8 |    ✓    |   ✓   |   ✓  |
| [`Oracle Hotspot JVM`](https://www.oracle.com/technetwork/java/javase/overview/index.html) | 1.7, 1.8 |    ✓    |   ✓   |   ✓  |

The Scope Java agent is compatible with the following libraries:

| Name                                   | Span/event creation | Extract | Inject |
|----------------------------------------|:-------------------:|---------|--------|
| [`Junit 4`](https://junit.org/junit4/) |          ✓          |         |        |

> Do you use a platform or library not listed here? Please [let us know](https://home.codescope.com/goto/support)!

## Installation

Installation is done via [Maven](https://maven.apache.org/). Add the Scope agent dependency and version property to your `pom.xml` file,
replacing `0.1.0` with the latest version of the agent:

```xml
<properties>
  <scope.agent.version>0.1.0</scope.agent.version>
</properties>
```
```xml
<dependency>
  <groupId>com.undefinedlabs.scope</groupId>
  <artifactId>scope-agent</artifactId>
  <version>${scope.agent.version}</version>
  <scope>provided</scope>
</dependency>
```


## Usage

To use the agent, configure the [Maven Surefire Plugin](https://maven.apache.org/surefire/maven-surefire-plugin/) to use Scope agent as a Java agent:

```xml
<plugin>
  <groupId>org.apache.maven.plugins</groupId>
  <artifactId>maven-surefire-plugin</artifactId>
  <configuration>
    <argLine>-javaagent:${settings.localRepository}/com/undefinedlabs/scope/scope-agent/${scope.agent.version}/scope-agent-${scope.agent.version}.jar</argLine>
  </configuration>
</plugin>
```

After this, you can run your tests as you normally do, for example using the `mvn test` command.


## CI provider configuration

The following environment variables need to be configured in your CI provider:

| Environment variable  | Description                                            |
|-----------------------|--------------------------------------------------------|
| `$SCOPE_APIKEY`       | API key to use when sending data to Scope              |
| `$SCOPE_API_ENDPOINT` | API endpoint of the Scope installation to send data to |


The following optional parameters can also be configured:

| Environment variable | Default      | Description                                      |
|----------------------|--------------|--------------------------------------------------|
| `$SCOPE_SERVICE`     | `default`    | Service name to use when sending data to Scope   |
| `$SCOPE_COMMIT_SHA`  | Autodetected | Commit hash to use when sending data to Scope    |
| `$SCOPE_REPOSITORY`  | Autodetected | Repository URL to use when sending data to Scope |
| `$SCOPE_SOURCE_ROOT` | Autodetected | Repository root path                             |

Autodetection of git information works if either tests run on [Jenkins](https://jenkins.io/), 
[CircleCI](https://circleci.com/), [Travis CI](https://travis-ci.com/) or [GitLab CI](https://about.gitlab.com/).

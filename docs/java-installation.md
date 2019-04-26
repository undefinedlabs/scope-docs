---
id: java-installation
title: Java Agent instructions
sidebar_label: Installation
---


## Compatibility

The Scope Java agent is compatible with the following JVMs:

| JVM                | Versions   | Windows | Linux | OS X |
|--------------------|------------|:-------:|:-----:|:----:|
| [`OpenJDK JVM`](https://openjdk.java.net/) | 1.7, 1.8 | ✓ | ✓ | ✓ |
| [`Oracle Hotspot JVM`](https://www.oracle.com/technetwork/java/javase/overview/index.html) | 1.7, 1.8 | ✓ | ✓ | ✓ |

The Scope Java agent is compatible with the following libraries:

| Name    | Span/event creation | Extract | Inject |
|---------|:-------------------:|---------|--------|
| [`Junit 4`](https://junit.org/junit4/) | ✓ | | |

Do you use a library not listed here? Please [let us know](https://home.codescope.com/goto/support)!

## Installation

Download via `<dependency/>` and install adding `-javaagent:` in the Maven Surefire Plugin.

In your `pom.xml`:

1. Add Scope Agent dependency:

```xml
<dependency>
  <groupId>com.undefinedlabs.scope</groupId>
  <artifactId>scope-agent</artifactId>
  <version>0.1.0</version>
  <scope>provided</scope>
</dependency>
```

2. Configure Maven Surefire Plugin to use Scope Agent:

```xml
<plugin>
  <groupId>org.apache.maven.plugins</groupId>
  <artifactId>maven-surefire-plugin</artifactId>
  <configuration>
    <argLine>-javaagent:${settings.localRepository}/com/undefinedlabs/scope/scope-agent/0.1.0/scope-agent-0.1.0.jar</argLine>
  </configuration>
</plugin>
```

> After this, you can run your tests as you normally do, for example using the `mvn test` command.


## CI provider configuration

The following environment variables need to be configured in your CI provider:

| Environment variable | Description |
|---|---|
| `$SCOPE_APIKEY` | API key to use when sending data to Scope |
| `$SCOPE_API_ENDPOINT` | API endpoint of the Scope installation to send data to |


The following optional parameters can also be configured:

| Environment variable  | Default | Description |
|---|---|---|
| `$SCOPE_SERVICE` | `default` | Service name to use when sending data to Scope |
| `$SCOPE_COMMIT_SHA` | Autodetected | Commit hash to use when sending data to Scope |
| `$SCOPE_REPOSITORY` | Autodetected | Repository URL to use when sending data to Scope |
| `$SCOPE_SOURCE_ROOT` | Autodetected | Repository root path |

Autodetection of git information works if tests run on Jenkins, CircleCI, Travis or GitLab.

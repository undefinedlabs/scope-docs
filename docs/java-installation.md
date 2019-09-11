---
id: java-installation
title: Java Agent instructions
sidebar_label: Installation
---


## Compatibility

The Scope Java agent is compatible with the following JVMs:

| JVM                | Versions   | Windows | Linux | OS X |
|--------------------|:----------:|:-------:|:-----:|:----:|
| [`OpenJDK JVM`](https://openjdk.java.net/)        | `1.7` to `12` |    ✓    |   ✓   |   ✓  |
| [`Oracle Hotspot JVM`](https://www.oracle.com/technetwork/java/javase/overview/index.html) | `1.7` to `12` |    ✓    |   ✓   |   ✓  |

The Scope Java agent is compatible with the following libraries:

| Name    | Versions | Span/event creation | Extract | Inject |
|---------|:--------:|:-------------------:|:-------:|:------:|
| [`Junit 4`](https://junit.org/junit4/) | `4.x` |          ✓          |         |        |
| [`Junit 5`](https://junit.org/junit5/) | `5.x` |          ✓          |         |        |
| [`TestNG`](https://testng.org/) | `6.4` to `6.14.x` |          ✓          |         |        |
| [`SLF4J`](https://www.slf4j.org/) | `1.7.x` |          ✓          |         |        |
| [`OkHttp3`](https://square.github.io/okhttp/) | `3.8.1` to `4.0.x` |          ✓          |         |          ✓          |
| [`java.net (HttpURLConnection)`](https://docs.oracle.com/javase/8/docs/api/java/net/HttpURLConnection.html) | `1.7` to `12` |          ✓          |         |          ✓          |
| [`Apache Tomcat`](http://tomcat.apache.org/) | `7.x` to `9.x` |          ✓          |     ✓    |                    |
| [`H2 DBMS`](https://www.h2database.com/html/main.html) | `1.3.146` to `1.4.x` |          ✓          |         |          ✓          |
| [`MySQL`](https://www.h2database.com/html/main.html) | `5.6.x`, `5.7.x`, `8.x` |          ✓          |         |          ✓          |
| [`gRPC`](https://grpc.io/) | `1.4.0` to `1.22.x` |          ✓          |    ✓     |          ✓          |
| [`JMS`](https://docs.oracle.com/javaee/6/tutorial/doc/bncdq.html) | `1.1`, `2.x` |          ✓          |    ✓     |          ✓          |
| [`Spring-JMS`](https://spring.io/guides/gs/messaging-jms/) | `1.1`, `2.x` |          ✓          |     ✓    |          ✓          |

> Do you use a platform or library not listed here? Please [let us know](https://home.undefinedlabs.com/goto/support)!

## Installation

Installation is done via [Maven](https://maven.apache.org/). Add the Scope agent dependency and version property to your `pom.xml` file,
replacing `0.1.8` with the latest version of the agent:

```xml
<properties>
  <scope.agent.version>0.1.8</scope.agent.version>
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

### Testing

To use the agent, configure the [`Maven Surefire Plugin`](https://maven.apache.org/surefire/maven-surefire-plugin/) 
and/or the [`Maven Failsafe Plugin`](https://maven.apache.org/surefire/maven-failsafe-plugin/) to use Scope agent as a Java agent:

```xml
<plugin>
<groupId>org.apache.maven.plugins</groupId>
<artifactId>maven-surefire-plugin</artifactId>
<configuration>
  <argLine>-javaagent:${settings.localRepository}/com/undefinedlabs/scope/scope-agent/${scope.agent.version}/scope-agent-${scope.agent.version}.jar</argLine>
</configuration>
</plugin>
```

```xml
<plugin>
<groupId>org.apache.maven.plugins</groupId>
<artifactId>maven-failsafe-plugin</artifactId>
<configuration>
   <argLine>-javaagent:${settings.localRepository}/com/undefinedlabs/scope/scope-agent/${scope.agent.version}/scope-agent-${scope.agent.version}.jar</argLine>
</configuration>
<executions>
    <execution>
      <goals>
         <goal>integration-test</goal>
         <goal>verify</goal>
      </goals>
    </execution>
</executions>
</plugin>
```

After this, you can run your tests as you normally do, for example using the `mvn clean verify` command.


### Server

Modify your Java app startup script to add the `javaagent` parameter targeting to the downloaded Scope Agent JAR.

```bash
java -javaagent:/path/to/scope/agent/scope-agent.jar -jar /path/to/app/my-app.jar
``` 

Notice that it is needed that `$SCOPE_APIKEY`, `$SCOPE_API_ENDPOINT`, `$SCOPE_REPOSITORY`, and `$SCOPE_COMMIT_SHA` 
had been set as environment variables in the executing environment.


## Scope environment configuration

The following environment variables may modify the Scope Agent behavior.

| Environment variable  | Default | Description |
|---|---|---|
| `$SCOPE_AUTO_INSTRUMENT` | `true` | Boolean flag to apply Scope auto instrumentation |
| `$SCOPE_SET_GLOBAL_TRACER` | `true` | Boolean flag to register `ScopeTracer` as `GlobalTracer` |
| `$SCOPE_TESTING_MODE` | Autodetected | Boolean flag to indicate to `ScopeAgent` if a "heartbeat" must be sent every second (`true`) or every minute (`false`) |

Autodetection of `$SCOPE_TESTING_MODE` property depends on whether the build has been triggered by a CI server (`true`), or not (`false`). Supported CI providers are listed below.

If these properties are manually configured, they will be `true` only on encountering the string `true` configured on the environment variable. Any other value will be considered as `false`.


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

Autodetection of git information is available to the following CI providers: 

* [`AppVeyorCI`](https://www.appveyor.com/)
* [`BitBucket Pipelines`](https://bitbucket.org/product/features/pipelines)
* [`CircleCI`](https://circleci.com/)
* [`GitLab CI/CD`](https://docs.gitlab.com/ee/ci/)
* [`Jenkins`](https://jenkins.io/)
* [`Azure DevOps Server`](https://visualstudio.microsoft.com/tfs/)
* [`Travis CI`](https://travis-ci.org/)


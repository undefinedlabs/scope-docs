---
id: java-installation
title: Scope Java Agent instructions
sidebar_label: Installation
---

Installation is done via [Maven](https://maven.apache.org/). Add the Scope agent dependency and version property to your `pom.xml` file,
replacing `0.1.9` with the latest version of the agent:

```xml
<properties>
  <scope.agent.version>0.1.9</scope.agent.version>
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


## Instrumenting your tests

To use instrument your tests, configure the [`Maven Surefire Plugin`](https://maven.apache.org/surefire/maven-surefire-plugin/) 
and/or the [`Maven Failsafe Plugin`](https://maven.apache.org/surefire/maven-failsafe-plugin/) to use the Scope Agent as a Java agent:

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


### Runtime instrumentation

In order to see trace information from your Java service on integration and end-to-end tests,
you need to use the Scope agent to instrument your running service.

This service might run, for example, in a container on CI, or in a QA/staging environment.

Modify your Java app startup script to add the `javaagent` parameter pointing to the downloaded Scope Agent JAR.

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


## Environment variables

The following environment variables need to be configured when instrumenting your tests or application:

| Environment variable  | Default value    | Description                                            |
|-----------------------|------------------|--------------------------------------------------------|
| `$SCOPE_APIKEY`       |                  | API key to use when sending data to Scope              |
| `$SCOPE_API_ENDPOINT` |                  | API endpoint of the Scope installation to send data to |
| `$SCOPE_COMMIT_SHA`   | Autodetected (*) | Commit hash to use when sending data to Scope          |
| `$SCOPE_REPOSITORY`   | Autodetected (*) | Repository URL to use when sending data to Scope       |
| `$SCOPE_SOURCE_ROOT`  | Autodetected (*) | Repository root path                                   |

The following optional parameters can also be configured:

| Environment variable | Default value    | Description                                      |
|----------------------|------------------|--------------------------------------------------|
| `$SCOPE_SERVICE`     | `default`        | Service name to use when sending data to Scope   |

(*) Autodetection of git information works if either tests run on a [supported CI provider](java-compatibility.md#ci-providers).

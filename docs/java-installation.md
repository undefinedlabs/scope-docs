---
id: java-installation
title: Scope Java Agent instructions
sidebar_label: Installation
---

## Using Maven

Add the Scope agent dependency and version property to your `pom.xml` file, replacing `0.1.9` with the latest version of the agent:

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

## Using Gradle
Add the `testAgent` entry to the `configurations` task block and add the Scope agent dependency, replacing 0.1.9 with the latest version of the agent.

```groovy
configurations {
    testAgent
}

dependencies {
    testAgent "com.undefinedlabs.scope:scope-agent:0.1.9"
}
```

## Instrumenting your tests
### Using Maven
Configure the [`Maven Surefire Plugin`](https://maven.apache.org/surefire/maven-surefire-plugin/) and/or the [`Maven Failsafe Plugin`](https://maven.apache.org/surefire/maven-failsafe-plugin/) to use Scope agent as a Java agent:
```xml
<plugin>
  <groupId>org.apache.maven.plugins</groupId>
  <artifactId>maven-surefire-plugin</artifactId>
  <configuration>
    <argLine>-javaagent:${settings.localRepository}/com/undefinedlabs/scope/scope-agent/${scope.agent.version}/scope-agent-${scope.agent.version}.jar</argLine>
  </configuration>
</plugin>

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

### Using Gradle
Configure the `test` Gradle task by adding to the `jvmArgs` attribute the `-javaagent` argument targeting the Scope agent based on the `configurations.testAgent` property.

```groovy
test {
    jvmArgs = ["-javaagent:${configurations.testAgent.singleFile}"]
}
```

After this, you can run your tests as you normally do, for example using the `gradle cleanTest test --rerun-tasks` command.

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

| Environment variable  | Default value           | Description                                            |
|-----------------------|-------------------------|--------------------------------------------------------|
| `$SCOPE_APIKEY`       |                         | API key to use when sending data to Scope              |
| `$SCOPE_API_ENDPOINT` | `https://app.scope.dev` | API endpoint of the Scope installation to send data to |
| `$SCOPE_COMMIT_SHA`   | Autodetected (*)        | Commit hash to use when sending data to Scope          |
| `$SCOPE_REPOSITORY`   | Autodetected (*)        | Repository URL to use when sending data to Scope       |
| `$SCOPE_SOURCE_ROOT`  | Autodetected (*)        | Repository root path                                   |

The following optional parameters can also be configured:

| Environment variable | Default value    | Description                                      |
|----------------------|------------------|--------------------------------------------------|
| `$SCOPE_SERVICE`     | `default`        | Service name to use when sending data to Scope   |

(*) Autodetection of git information works if either tests run on a [supported CI provider](java-compatibility.md#ci-providers).

The following environment variables are also available to modify the Scope Agent behavior.

| Environment variable  | Default | Description |
|---|---|---|
| `$SCOPE_AUTO_INSTRUMENT` | `true` | Boolean flag to apply Scope auto instrumentation |
| `$SCOPE_SET_GLOBAL_TRACER` | `true` | Boolean flag to register `ScopeTracer` as OpenTracing's global tracer |
| `$SCOPE_TESTING_MODE` | Autodetected (*) | Boolean flag to indicate to `ScopeAgent` if it's running tests (`true`), or if it's being used for runtime instrumentation (`false`) |

(*) Autodetection of `$SCOPE_TESTING_MODE` property depends on whether the build has been triggered by a CI server (`true`), or not (`false`).

If these properties are manually configured, they will be `true` only on encountering the string `true` configured on the environment variable. Any other value will be considered as `false`.

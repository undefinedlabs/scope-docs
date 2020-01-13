---
id: java-installation
title: Scope Java Agent instructions
sidebar_label: Installation
---

## GitHub Actions

<!--DOCUSAURUS_CODE_TABS-->
<!--Maven-->

Add a step to your GitHub Actions workflow YAML that uses the [scope-for-maven](https://github.com/marketplace/actions/scope-for-maven) action:

```yaml
steps:
  - uses: actions/checkout@master
  - name: Set up JDK 1.8
    uses: actions/setup-java@v1
    with:
      java-version: 1.8
  - name: Scope for Maven Action
    uses: undefinedlabs/scope-for-maven-action@v1
    with:
      dsn: ${{secrets.SCOPE_DSN}}
```

You can find further information of this action at the [GitHub Marketplace](https://github.com/marketplace/actions/scope-for-maven).

Start using Scope with the [Getting Started Java Project with Maven + GitHub Actions](https://github.com/scope-demo/scope-java-maven-starter) right now!

<!--Gradle-->

Add a step to your GitHub Actions workflow YAML that uses the [scope-for-gradle](https://github.com/marketplace/actions/scope-for-gradle) action:

```yaml
steps:
  - uses: actions/checkout@master
  - name: Set up JDK 1.8
    uses: actions/setup-java@v1
    with:
      java-version: 1.8
  - name: Scope for Maven Action
    uses: undefinedlabs/scope-for-gradle-action@v1
    with:
      dsn: ${{secrets.SCOPE_DSN}}
```

You can find further information of this action at the [GitHub Marketplace](https://github.com/marketplace/actions/scope-for-gradle).

Start using Scope with the [Getting Started Java Project with Gradle + GitHub Actions](https://github.com/scope-demo/scope-java-gradle-starter) right now!

<!--END_DOCUSAURUS_CODE_TABS-->

## Manual

<!--DOCUSAURUS_CODE_TABS-->
<!--Maven-->

Add the Scope agent dependency and version property to your `pom.xml` file, replacing `0.2.4` with the latest version of the agent:

```xml
<properties>
  <scope.agent.version>0.2.4</scope.agent.version>
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

### Instrumenting your tests

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

<!--Gradle-->

Add the `testAgent` entry to the `configurations` task block and add the Scope agent dependency, replacing `0.2.4` with the latest version of the agent.

```groovy
configurations {
    testAgent
}

dependencies {
    testAgent "com.undefinedlabs.scope:scope-agent:0.2.4"
}
```

### Instrumenting your tests

Configure the `test` Gradle task by adding to the `jvmArgs` attribute the `-javaagent` argument targeting the Scope agent based on the `configurations.testAgent` property.

```groovy
test {
    jvmArgs = ["-javaagent:${configurations.testAgent.singleFile}"]
}
```

After this, you can run your tests as you normally do, for example using the `gradle cleanTest test --rerun-tasks` command.

<!--sbt-->

Add the `sbt-javaagent` entry to the `project/plugins.sbt` file.

```scala
addSbtPlugin("com.lightbend.sbt" % "sbt-javaagent" % "0.1.5")
```

Enable the `JavaAgent` plugin in your `build.sbt` configuring the Scope agent dependency, replacing `0.2.4` with the latest version of the agent.

```scala
lazy val root = project
  .in(file("."))
  .enablePlugins(JavaAgent)
  .settings(
    javaAgents += "com.undefinedlabs.scope" % "scope-agent" % "0.2.4" % "test"
  )
```

### Instrumenting your tests

After this, you can run your tests as you normally do, for example using the `sbt clean test` command.

<!--END_DOCUSAURUS_CODE_TABS-->

## Environment variables

The following environment variables need to be configured when instrumenting your tests or application:

| Environment variable | Default value     | Description                                                       |
| -------------------- | ----------------- | ----------------------------------------------------------------- |
| `$SCOPE_DSN`         |                   | Data source name (DSN) of Scope to be used when reporting results |
| `$SCOPE_COMMIT_SHA`  | Autodetected (\*) | Commit hash to use when sending data to Scope                     |
| `$SCOPE_REPOSITORY`  | Autodetected (\*) | Repository URL to use when sending data to Scope                  |
| `$SCOPE_SOURCE_ROOT` | Autodetected (\*) | Repository root path                                              |

(\*) Autodetection of git information works if either tests run on a [supported CI provider](java-compatibility.md#ci-providers).

The following optional parameters can also be configured:

| Environment variable | Default value | Description                                    |
| -------------------- | ------------- | ---------------------------------------------- |
| `$SCOPE_SERVICE`     | `default`     | Service name to use when sending data to Scope |

The following environment variables are also available to modify the Scope Agent behavior.

| Environment variable       | Default           | Description                                                                                                                          |
| -------------------------- | ----------------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| `$SCOPE_AUTO_INSTRUMENT`   | `true`            | Boolean flag to apply Scope auto instrumentation                                                                                     |
| `$SCOPE_SET_GLOBAL_TRACER` | `false`           | Boolean flag to register `ScopeTracer` as OpenTracing's global tracer                                                                |
| `$SCOPE_TESTING_MODE`      | Autodetected (\*) | Boolean flag to indicate to `ScopeAgent` if it's running tests (`true`), or if it's being used for runtime instrumentation (`false`) |

(\*) Autodetection of `$SCOPE_TESTING_MODE` property depends on whether the build has been triggered by a CI server (`true`), or not (`false`).

If these properties are manually configured, they will be `true` only on encountering the string `true` configured on the environment variable. Any other value will be considered as `false`.

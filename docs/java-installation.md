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

Add the Scope agent dependency and version property to your `pom.xml` file, replacing `0.3.2` with the latest version of the agent:

```xml
<properties>
  <scope.agent.version>0.6.1</scope.agent.version>
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

Add the `testAgent` entry to the `configurations` task block and add the Scope agent dependency, replacing `0.3.2` with the latest version of the agent.

```groovy
configurations {
    testAgent
}

dependencies {
    testAgent "com.undefinedlabs.scope:scope-agent:0.6.1"
}
```

### Instrumenting your tests

Configure the `test` Gradle task by adding to the `jvmArgs` attribute the `-javaagent` argument targeting the Scope agent based on the `configurations.testAgent` property.

```
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

Enable the `JavaAgent` plugin in your `build.sbt` configuring the Scope agent dependency, replacing `0.3.2` with the latest version of the agent.

```scala
lazy val root = project
  .in(file("."))
  .enablePlugins(JavaAgent)
  .settings(
    javaAgents += "com.undefinedlabs.scope" % "scope-agent" % "0.6.1" % "test"
  )
```

### Instrumenting your tests

After this, you can run your tests as you normally do, for example using the `sbt clean test` command.

<!--END_DOCUSAURUS_CODE_TABS-->

## Environment variables

The following environment variables need to be configured when instrumenting your application in testing or runtime modes:

| Environment variable | Testing mode | Runtime mode | Autodetected |
| -------------------- | ------------ | ------------ | :----------: |
| `SCOPE_DSN`          | Required     | Required     |      ✗       |
| `SCOPE_COMMIT_SHA`   | Required     | Optional     |      ✓       |
| `SCOPE_REPOSITORY`   | Required     | Optional     |      ✓       |
| `SCOPE_SOURCE_ROOT`  | Required     | Optional     |      ✓       |

### SCOPE_DSN

**This is a required setting**. If not set in testing mode, tests will run as usual and an error message pointing to the agent logs for troubleshooting will be printed before the process finishes. If not set in runtime mode, the instrumented process will be executed as usual, a warning message will be printed at the beginning of the execution and no spans will be reported.

`SCOPE_DSN` contains the Data Source Name with connection information about the Scope installation to report to. Specifically, it contains
the hostname of the Scope instance to report to, and the API key to be used for authentication. _`SCOPE_DSN` is considered a secret and should not be checked out in a repository._

Scope DSNs are generated per namespace. You can generate them by clicking on the `API Key` link of the namespace you want to report to in the Scope UI. If running locally using the native apps _Scope for Mac_ or _Scope for Windows_, the DSN will be automatically configured by reading it from `~/.scope/config.json`, which is autogenerated by the native app.

Example value: `https://cbfeff1f5fbf444086c728a096020cad@app.scope.dev/`

### SCOPE_COMMIT_SHA

This is a required setting in testing mode, and optional in runtime mode.

`SCOPE_COMMIT_SHA` contains the commit hash to be used when reporting to Scope.

If not explicitly set, the agent will try to automatically detect it using the following algorithm:

1. If the process is being executed inside a [supported CI provider](java-compatibility.md#ci-providers), it will try
   to read the commit hash from the environment variable set by the CI provider.
2. If not, it will try to extract the current commit from the local git information (if `.git/` is present).

Example value: `974c3566eb8e221d130db86a7ce1f99703fe2e69`

### SCOPE_REPOSITORY

This is a required setting in testing mode, and optional in runtime mode.

`SCOPE_REPOSITORY` contains the repository URL to be used when reporting to Scope.

If not explicitly set, the agent will try to automatically detect it using the following algorithm:

1. If the process is being executed inside a [supported CI provider](java-compatibility.md#ci-providers), it will try to read the repository URL from the environment variables set by the CI provider.
2. If not, it will try to extract the current `origin` remote URL from the local git information (if `.git/` is present).

Examples values: `https://github.com/undefinedlabs/scope-docs.git`, `git@github.com:undefinedlabs/scope-docs.git`

### SCOPE_SOURCE_ROOT

This is a required setting in testing mode, and optional in runtime mode.

`SCOPE_SOURCE_ROOT` contains the absolute path to where the root of the project is located inside the filesystem. This
information is used to automatically show excerpts of source code in the Scope UI in stacktraces, the "Code Path" tab and others.

If not explicitly set, the agent will try to automatically detect it using the following algorithm:

1. If the process is being executed inside a [supported CI provider](java-compatibility.md#ci-providers), it will try
   to read the source root from the environment variable set by the CI provider.
2. If not, it will try to extract the absolute path to the git repository using the local git information (if `.git/` is present).
3. If not, it will be set to the working directory of the command used to launch the application or tests.

Example value: `/home/user/projects/scope-docs`

## Running tests inside a container

If you are running your application or tests inside a container, forward the following environment variables to it so the agent can autodetect the build information. Note that the variables depend on your CI provider.

> Note that you might also need to set `SCOPE_SOURCE_ROOT` manually with the absolute path inside the container where the code is present if it cannot be autodetected by the agent.

<!--DOCUSAURUS_CODE_TABS-->
<!-- Jenkins -->

- `SCOPE_DSN`
- `JENKINS_URL`
- `GIT_URL`
- `GIT_COMMIT`
- `BUILD_ID`
- `BUILD_NUMBER`
- `BUILD_URL`
- `GIT_BRANCH`

<!-- CircleCI -->

- `SCOPE_DSN`
- `CIRCLECI`
- `CIRCLE_REPOSITORY_URL`
- `CIRCLE_SHA1`
- `CIRCLE_BUILD_NUM`
- `CIRCLE_BUILD_URL`
- `CIRCLE_BRANCH`

<!-- GitLab CI -->

- `SCOPE_DSN`
- `GITLAB_CI`
- `CI_REPOSITORY_URL`
- `CI_COMMIT_SHA`
- `CI_JOB_ID`
- `CI_JOB_URL`
- `CI_COMMIT_BRANCH`
- `CI_COMMIT_REF_NAME`

<!-- Travis -->

- `SCOPE_DSN`
- `TRAVIS`
- `TRAVIS_REPO_SLUG`
- `TRAVIS_COMMIT`
- `TRAVIS_BUILD_ID`
- `TRAVIS_BUILD_NUMBER`

<!-- AppVeyor -->

- `SCOPE_DSN`
- `APPVEYOR`
- `APPVEYOR_REPO_NAME`
- `APPVEYOR_REPO_COMMIT`
- `APPVEYOR_BUILD_ID`
- `APPVEYOR_BUILD_NUMBER`
- `APPVEYOR_PROJECT_SLUG`
- `APPVEYOR_PULL_REQUEST_HEAD_REPO_BRANCH`
- `APPVEYOR_REPO_BRANCH`

<!-- Azure Pipelines -->

- `SCOPE_DSN`
- `TF_BUILD`
- `Build.Repository.Uri`
- `Build.SourceVersion`
- `Build.BuildId`
- `Build.BuildNumber`
- `System.TeamFoundationCollectionUri`
- `System.TeamProject`
- `Build.SourceBranchName`
- `Build.SourceBranch`

<!-- Bitbucket Pipelines -->

- `SCOPE_DSN`
- `BITBUCKET_GIT_SSH_ORIGIN`
- `BITBUCKET_COMMIT`
- `BITBUCKET_CLONE_DIR`
- `BITBUCKET_BUILD_NUMBER`
- `BITBUCKET_BRANCH`

<!-- GitHub Actions -->

- `SCOPE_DSN`
- `GITHUB_REPOSITORY`
- `GITHUB_SHA`
- `GITHUB_WORKSPACE`
- `GITHUB_RUN_ID`
- `GITHUB_RUN_NUMBER`
- `GITHUB_REF`

<!-- TeamCity -->

- `SCOPE_DSN`
- `TEAMCITY_VERSION`
- `BUILD_VCS_URL`
- `BUILD_CHECKOUTDIR`
- `BUILD_ID`
- `BUILD_NUMBER`
- `SERVER_URL`

<!-- Buildkite -->

- `SCOPE_DSN`
- `BUILDKITE`
- `BUILDKITE_REPO`
- `BUILDKITE_COMMIT`
- `BUILDKITE_BUILD_ID`
- `BUILDKITE_BUILD_NUMBER`
- `BUILDKITE_BUILD_URL`
- `BUILDKITE_BRANCH`

<!--END_DOCUSAURUS_CODE_TABS-->

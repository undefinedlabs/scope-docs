---
id: java-runtime
title: Scope Java Agent runtime instrumentation
sidebar_label: Runtime instrumentation
---

In order to see trace information from your Java service on integration and end-to-end tests,
you need to use the Scope agent to instrument your running service.

This service might run, for example, in a container on CI, or in a QA/staging environment.

## Using `javaagent` VM param

Download the Scope Java Agent, replacing `0.2.4` with the latest version.

```bash
cd /path/to/scope/agent
curl -s -o scope-agent.jar "https://repo1.maven.org/maven2/com/undefinedlabs/scope/scope-agent/0.2.4/scope-agent-0.2.3.jar"
```

Modify your Java app startup script to add the `javaagent` parameter pointing to the downloaded Scope Agent JAR.

```bash
java -javaagent:/path/to/scope/agent/scope-agent.jar -jar /path/to/app/my-app.jar
```

Notice that setting the `$SCOPE_DSN` environment variable is required.

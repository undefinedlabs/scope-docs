---
id: intelligent-test-runner
title: Scope Intelligent Test Runner
sidebar_label: Intelligent Test Runner
---

The **Intelligent Test Runner** is a Scope agent feature that allows them to skip tests
that have not been affected by source code changes since the last time they were run.
This can lead to significant time and cost savings.

This is done by comparing each test code path information (the affected code) with git file change information.
If the source code files a passing test covered have not been changed in a later commit, that test is skipped 
when that commit is tested.

> Note that the Intelligent Test Runner feature is in beta and not yet supported on all platforms

## Configuration

The Intelligent Test Runner is enabled in specific branches of your repository. For example, to enable it
for all branches other than `master`, set the following environment variables:

```sh
SCOPE_CODE_PATH_ENABLED="true"
SCOPE_RUNNER_ENABLED="true"
SCOPE_RUNNER_EXCLUDE_BRANCHES="master"
```

Note that Code Path has to be also enabled in order for the Intelligent Test Runner to work.
Check out the agent configuration documentation for more information.

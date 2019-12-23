---
id: dotnet-installation
title: Scope .NET Agent instructions
sidebar_label: Installation
---

## Using GitHub Actions

Add a step to your GitHub Actions workflow YAML that uses the [scope-for-dotnet-action](https://github.com/marketplace/actions/scope-for-net) action:

```yaml
steps:
  - uses: actions/checkout@v1
  - name: Setup .NET Core
    uses: actions/setup-dotnet@v1
    with:
      dotnet-version: 3.0.100
  - name: Build with dotnet
    run: dotnet build
  - name: Scope for .NET
    uses: undefinedlabs/scope-for-dotnet-action@v1
    with:
      dsn: ${{secrets.SCOPE_DSN}} # required
      use-solutions: true  # optional - default is 'true'
      command: dotnet test # optional - default is 'dotnet test'
```

You can find further information of this action at the [GitHub Marketplace](https://github.com/marketplace/actions/scope-for-net).

Start using Scope with the [Getting Started ASP.NET Core Project with React + GitHub Actions](https://github.com/scope-demo/scope-dotnet-aspnetcore-react-starter) right now!

## Manual

Installation of the Scope Agent is done via [NuGet](https://www.nuget.org/) as a [.NET Core CLI Global tool](https://docs.microsoft.com/en-us/dotnet/core/tools/global-tools):

```bash
dotnet tool install --global ScopeAgent.Runner
```

This will install the `scope-run` command globally in the machine.

In case your have a previous version of the Scope Agent, you can update using:

```bash
dotnet tool update --global ScopeAgent.Runner
```

## Instrumenting your tests

To use the agent, prefix your test command with `scope-run`. For example:

```bash
scope-run dotnet test
```

All tests will be instrumented automatically.

## Environment variables

The following environment variables need to be configured when instrumenting your tests or application:

| Environment variable  | Default value    | Description                                                |
|-----------------------|------------------|------------------------------------------------------------|
| `$SCOPE_DSN`          |                  | Data source name (DSN) of Scope to be used when reporting results |
| `$SCOPE_COMMIT_SHA`   | Autodetected (*) | Commit hash to use when sending data to Scope              |
| `$SCOPE_REPOSITORY`   | Autodetected (*) | Repository URL to use when sending data to Scope           |
| `$SCOPE_SOURCE_ROOT`  | Autodetected (*) | Repository root path                                       |

(*) Autodetection of git information works if either tests run on a [supported CI provider](dotnet-compatibility.md#ci-providers),
or if the `.git` folder is present locally, and there is an `origin` remote configured pointing to the right repository.

The following optional parameters can also be configured:

| Environment variable | Default value    | Description                                      |
|----------------------|------------------|--------------------------------------------------|
| `$SCOPE_SERVICE`     | `default`        | Service name to use when sending data to Scope   |

These configuration settings can also be provided via CLI flags. Run `scope-run --help` for more information.

For `TeamCity`, additional environment variables must be exposed from the Teamcity `Parameters` section:

|          Name           |            Value               |
|-------------------------|--------------------------------|
| `env.BUILD_CHECKOUTDIR` | `%teamcity.build.checkoutDir%` |
| `env.BUILD_ID`          | `%teamcity.build.id%`          |
| `env.BUILD_VCS_URL`     | `%vcsroot.url%`                |

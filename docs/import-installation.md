---
id: import-installation
title: Scope Import instructions
sidebar_label: Installation
---

## GitHub Actions

Add a step to your GitHub Actions workflow YAML that uses the [scope-import](https://github.com/marketplace/actions/scope-import) action:

```yaml
- name: Scope Import
    uses: undefinedlabs/scope-import-action@v1
    with:
      dsn: ${{ secrets.SCOPE_DSN }}
      path: path/to/test-reports
```

You can find further information of this action at the [GitHub Marketplace](https://github.com/marketplace/actions/scope-import).

## Manual

If you haven’t done it yet, install the Scope Import CLI running the following command in your local shell:

<!--DOCUSAURUS_CODE_TABS-->

<!--Linux/MacOS-->

```
curl https://home.undefinedlabs.com/download/scope-import/`uname -s`/`uname -m` -o /usr/local/bin/scope-import && chmod +x /usr/local/bin/scope-import
```

<!--Windows-->

```
wget https://home.undefinedlabs.com/download/scope-import/windows/x86_64 -OutFile c:\windows\system32\scope-import.exe
```

If you use a Windows 32bit machine, change the architecture in the URL to `i386`.

<!--END_DOCUSAURUS_CODE_TABS-->

### Usage

```
scope-import --path path/to/test-reports
```

## Environment variables

The following environment variables need to be configured when instrumenting your tests or application:

| Environment variable | Default value     | Description                                                       |
| -------------------- | ----------------- | ----------------------------------------------------------------- |
| `$SCOPE_DSN`         |                   | Data source name (DSN) of Scope to be used when reporting results |
| `$SCOPE_COMMIT_SHA`  | Autodetected (\*) | Commit hash to use when sending data to Scope                     |
| `$SCOPE_REPOSITORY`  | Autodetected (\*) | Repository URL to use when sending data to Scope                  |
| `$SCOPE_SOURCE_ROOT` | Autodetected (\*) | Repository root path                                              |

(\*) Autodetection of git information works if tool is run to import test reports on a [supported CI provider](import-compatibility.md#ci-providers).

The following optional parameters can also be configured:

| Environment variable | Default value | Description                                    |
| -------------------- | ------------- | ---------------------------------------------- |
| `$SCOPE_SERVICE`     | `default`     | Service name to use when sending data to Scope |

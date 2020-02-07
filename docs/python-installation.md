---
id: python-installation
title: Scope Python Agent installation
sidebar_label: Installation
---

## GitHub Actions

Add a step to your GitHub Actions workflow YAML that uses the [Scope-for-Python](https://github.com/marketplace/actions/scope-for-python) action:

```yaml
steps:
  - uses: actions/checkout@v1
  - uses: actions/setup-python@v1
    with:
      python-version: "3.x"
  - name: Install dependencies
    run: pip install -r requirements.txt
  - name: Scope for Python
    uses: undefinedlabs/scope-for-python-action@v1
    with:
      dsn: ${{secrets.SCOPE_DSN}} # required
      command: pytest # optional - default is 'pytest'
```

You can find further information of this action at the [GitHub Marketplace](https://github.com/marketplace/actions/scope-for-python).

## Manual

Installation of the Scope Agent is done via [pip](https://pypi.org/project/scopeagent/).

```bash
pip install scopeagent
```

### Instrumenting your tests

There are two ways to instrument your tests: using the `scope-run` CLI as a wrapper (easiest method), or by installing the agent
in your Python code (giving you more control).

#### Using the `scope-run` CLI wrapper

To use the agent without modifying your source code, prefix your test command with `scope-run`:

<!--DOCUSAURUS_CODE_TABS-->
<!--unittest-->

```bash
scope-run python -m unittest discover
```

<!--pytest-->

```bash
scope-run pytest
```

<!--Django tests-->

```bash
scope-run python manage.py test
```

<!--END_DOCUSAURUS_CODE_TABS-->

#### Usage with `tox`

In order to use the `scope-run` CLI with [`tox`](https://tox.readthedocs.io/en/latest/), make sure you prefix your
testing command inside your `tox.ini` file, instead of the `tox` command itself.

For example:

```ini
# tox.ini
[testenv]
commands = scope-run pytest
passenv =
    SCOPE_DSN
```

And then, run `tox` as usual.

Check out the [CLI reference](https://scope-python-agent.readthedocs.io/en/latest/cli.html) documentation for details.

#### Installing the agent in your code

You can also install the agent in your application's code, as early in the execution as possible:

```python
import scopeagent

agent = scopeagent.Agent()
agent.install()
```

> If using `gevent`, make sure monkey patching happens _before_ installing the Scope agent

After this, you can run your tests as you normally do (for example using `pytest` or `python -m unittest` commands).

Check out the [API reference](https://scope-python-agent.readthedocs.io/en/latest/api.html) documentation for details.

## Environment variables

The following environment variables need to be configured when instrumenting your tests or application:

| Environment variable | Default value     | Description                                                       |
| -------------------- | ----------------- | ----------------------------------------------------------------- |
| `$SCOPE_DSN`         |                   | Data source name (DSN) of Scope to be used when reporting results |
| `$SCOPE_COMMIT_SHA`  | Autodetected (\*) | Commit hash to use when sending data to Scope                     |
| `$SCOPE_REPOSITORY`  | Autodetected (\*) | Repository URL to use when sending data to Scope                  |
| `$SCOPE_SOURCE_ROOT` | Autodetected (\*) | Repository root path                                              |

(\*) Autodetection of git information works if either tests run on a [supported CI provider](python-compatibility.md#ci-providers),
or if the `.git` folder is present locally, and there is an `origin` remote configured pointing to the right repository.

For `TeamCity`, additional environment variables must be exposed from the Teamcity `Parameters` section:

| Name                    | Value                          |
| ----------------------- | ------------------------------ |
| `env.BUILD_CHECKOUTDIR` | `%teamcity.build.checkoutDir%` |
| `env.BUILD_ID`          | `%teamcity.build.id%`          |
| `env.BUILD_VCS_URL`     | `%vcsroot.url%`                |


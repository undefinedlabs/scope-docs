---
id: python-installation
title: Scope Python Agent installation
sidebar_label: Installation
---

Installation of the Scope Agent is done via [pip](https://pypi.org/project/scopeagent/).

```bash
pip install scopeagent
```

## Instrumenting your tests

There are two ways to instrument your tests: using the `scope-run` CLI as a wrapper (easiest method), or by installing the agent
in your Python code (giving you more control).


### Using the `scope-run` CLI wrapper

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
    SCOPE_APIKEY
    SCOPE_API_ENDPOINT
```

And then, run `tox` as usual.

Check out the [CLI reference](https://scope-python-agent.readthedocs.io/en/latest/cli.html) documentation for details.


### Installing the agent in your code

You can also install the agent in your application's code, as early in the execution as possible:

```python
import scopeagent

agent = scopeagent.Agent()
agent.install()
```

> If using `gevent`, make sure monkey patching happens *before* installing the Scope agent

After this, you can run your tests as you normally do (for example using `pytest` or `python -m unittest` commands).

Check out the [API reference](https://scope-python-agent.readthedocs.io/en/latest/api.html) documentation for details.


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

(*) Autodetection of git information works if either tests run on a [supported CI provider](python-compatibility.md#ci-providers),
or if the `.git` folder is present locally, and there is an `origin` remote configured pointing to the right repository.

These configuration settings can also be provided via CLI flags. Check out the 
[CLI reference](https://scope-python-agent.readthedocs.io/en/latest/cli.html) documentation for details.

The following environment variables are also available to modify the Scope Agent behavior.

| Environment variable  | Default | Description |
|---|---|---|
| `$SCOPE_AUTO_INSTRUMENT` | `true` | Boolean flag to apply Scope auto instrumentation |
| `$SCOPE_SET_GLOBAL_TRACER` | `true` | Boolean flag to register `ScopeTracer` as OpenTracing's global tracer |
| `$SCOPE_TESTING_MODE` | Autodetected (*) | Boolean flag to indicate to `ScopeAgent` if it's running tests (`true`), or if it's being used for runtime instrumentation (`false`) |

(*) Autodetection of `$SCOPE_TESTING_MODE` property depends on whether the build has been triggered by a CI server (`true`), or not (`false`).

If these properties are manually configured, they will be `true` only on encountering the string `true` configured on the environment variable. Any other value will be considered as `false`.

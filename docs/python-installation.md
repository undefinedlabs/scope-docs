---
id: python-installation
title: Python Agent installation
sidebar_label: Installation
---

The [Scope Python agent](https://github.com/undefinedlabs/scope-python-agent) is an open source project that helps 
instrument your tests and runtime Python projects for use with [Scope](https://scope.dev).


## Compatibility

The Scope Python agent is compatible with the following versions of Python:

| Language | Versions   |
|----------|:----------:|
| Python   | 2.7+, 3.5+ |

The Scope Python agent is compatible with the following libraries:

| Name                                                          | Span/event creation | Extract | Inject |
|---------------------------------------------------------------|:-------------------:|:-------:|:------:|
| [`celery`](http://www.celeryproject.org)                      |          ✓          |         |        |
| [`gunicorn`](https://pypi.org/project/gunicorn/)              |          ✓          |    ✓    |        |
| [`requests`](https://pypi.org/project/requests/)              |          ✓          |         |    ✓   |
| [`unittest`](https://docs.python.org/3/library/unittest.html) |          ✓          |         |        |
| [`pytest`](https://pytest.org)                                |          ✓          |         |        |
| [`kombu`](https://github.com/celery/kombu)                    |          ✓          |    ✓    |    ✓   |
| [`logging`](https://docs.python.org/3/library/logging.html)   |          ✓          |         |        |

> Do you use a Python version or library not listed here? Please [let us know](https://home.codescope.com/goto/support)!

## Installation

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


### Installing the agent in your code

You can also install the agent in your application's code, as early in the execution as possible:

```python
import scopeagent

agent = scopeagent.Agent(api_key="xxxxxxxx", api_endpoint="https://scope.mycompany.corp")
agent.install()
```

> If using `gevent`, make sure monkey patching happens *before* installing the Scope agent

After this, you can run your tests as you normally do (for example using `pytest` or `python -m unittest` commands).


## CI provider configuration

The following environment variables need to be configured in your CI provider:

| Environment variable  | Description                                            |
|-----------------------|--------------------------------------------------------|
| `$SCOPE_APIKEY`       | API key to use when sending data to Scope              |
| `$SCOPE_API_ENDPOINT` | API endpoint of the Scope installation to send data to |


The following optional parameters can also be configured:

| Environment variable | Default      | Description                                      |
|----------------------|--------------|--------------------------------------------------|
| `$SCOPE_SERVICE`     | `default`    | Service name to use when sending data to Scope   |
| `$SCOPE_COMMIT_SHA`  | Autodetected | Commit hash to use when sending data to Scope    |
| `$SCOPE_REPOSITORY`  | Autodetected | Repository URL to use when sending data to Scope |
| `$SCOPE_SOURCE_ROOT` | Autodetected | Repository root path                             |

Autodetection of git information works if either tests run on [Jenkins](https://jenkins.io/), 
[CircleCI](https://circleci.com/), [Travis CI](https://travis-ci.com/) or [GitLab CI](https://about.gitlab.com/), 
or if the `.git` folder is present locally, and there is an `origin` remote configured pointing to the right repository.

These configuration settings can also be provided via CLI flags. Run `scope-run --help` for more information.

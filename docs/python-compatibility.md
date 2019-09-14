---
id: python-compatibility
title: Scope Python Agent compatibility
sidebar_label: Compatibility
---

### Python versions

The Scope Python agent is compatible with the following versions of Python:

| Language | Versions   |
|----------|:----------:|
| Python   | 2.7+, 3.5+ |


### Libraries

The Scope Python agent is compatible with the following libraries:

| Name                                                          | Span/event creation | Extract | Inject |
|---------------------------------------------------------------|:-------------------:|:-------:|:------:|
| [`celery`](http://www.celeryproject.org)                      |          ✓          |         |        |
| [`Django`](https://pypi.org/project/gunicorn/)                |          ✓          |    ✓    |        |
| [`Flask`](https://pypi.org/project/gunicorn/)                 |          ✓          |    ✓    |        |
| [`requests`](https://pypi.org/project/requests/)              |          ✓          |         |    ✓   |
| [`unittest`](https://docs.python.org/3/library/unittest.html) |          ✓          |         |        |
| [`pytest`](https://pytest.org)                                |          ✓          |         |        |
| [`kombu`](https://github.com/celery/kombu)                    |          ✓          |    ✓    |    ✓   |
| [`logging`](https://docs.python.org/3/library/logging.html)   |          ✓          |         |        |

> Do you use a Python version or library not listed here? Please [let us know](https://home.undefinedlabs.com/goto/support)!


### CI providers

The Scope Python agent will work on any CI provider, but will autodetect build and git information 
(repository, commit, branch and source root directory) if running on the following CI providers:

* [Jenkins](https://jenkins.io/)
* [CircleCI](https://circleci.com/)
* [GitLab CI](https://docs.gitlab.com/ee/ci/)
* [Travis](https://travis-ci.org/)

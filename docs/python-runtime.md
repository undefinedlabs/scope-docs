---
id: python-runtime
title: Scope Python Agent runtime instrumentation
sidebar_label: Runtime instrumentation
---

In order to see trace information from your Python service on integration and end-to-end tests,
you need to use the Scope agent to instrument your running service.

This service might run, for example, in a container on CI, or in a QA/staging environment.


## Using the `scope-run` CLI wrapper

To use the agent without modifying your source code, prefix the startup command of your WSGI-compliant server with `scope-run`. For example:

<!--DOCUSAURUS_CODE_TABS-->
<!--gunicorn-->
```bash
scope-run gunicorn -w 4 myapp:app
```

<!--uWSGI-->
```bash
scope-run uwsgi --http :9090 --wsgi-file foobar.py
```

<!--Other WSGI-compliant servers-->
```bash
scope-run python manage.py runserver
```

<!--END_DOCUSAURUS_CODE_TABS-->


## Installing the agent in your code

You can also install the agent in your application's code, as early in the execution as possible:

```python
import scopeagent

agent = scopeagent.Agent()
agent.install()
```

> If using `gevent`, make sure gevent's monkey patching happens *before* installing the Scope agent

After this, you can run the startup command of your WSGI-compliant server as before.

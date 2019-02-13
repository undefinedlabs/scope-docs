---
id: installation
title: Installing CodeScope
sidebar_label: Installation
---

## Prerequisites

CodeScope requires a **Kubernetes 1.11+ cluster** for deployment.

You need to have **cluster admin** privileges to the cluster being used.


## Quick installation

To install the latest stable version of CodeScope with the default configuration, run the following command:

```bash
kubectl apply -f https://home.codescope.com/installer.yml
```

This will install CodeScope in a namespace called `codescope`, with built-in PostgreSQL and Redis instances.

> If you want to customize this, read the below section on "Customizing your installation"

To get the CodeScope UI URL and set it up, run:

```bash
kubectl -n codescope get service/codescope-default-core --template="https://{{or (index .status.loadBalancer.ingress 0).hostname (index .status.loadBalancer.ingress 0).ip}}"
```

Open the printed URL in a browser, ignore the certificate warning (as it ships with a self-signed certificate that you
can change later on) and continue with the *Setup wizard* shown.

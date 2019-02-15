---
id: installation
title: Installing Scope
sidebar_label: Installation
---

## Prerequisites

Scope requires a **Kubernetes 1.11+ cluster** for deployment.

You need to have **cluster admin** privileges to the cluster being used.


## Quick installation

To install the latest stable version of Scope with the default configuration, run the following command:

```bash
kubectl apply -f https://home.codescope.com/installer.yml
```

This will install Scope in a namespace called `codescope`, with built-in PostgreSQL and Redis instances.

> If you want to use an existing PostgreSQL or Redis instance, or customize any other parameter, read the section below on ["Customizing your installation"](#customizing-your-installation)

To get the Scope UI URL and set it up, wait a few minutes until the load balancer resource has been assigned a hostname or IP, and run:

```bash
kubectl -n codescope get service/codescope-default-core --template="https://{{or (index .status.loadBalancer.ingress 0).hostname (index .status.loadBalancer.ingress 0).ip}}"
```

Open the printed URL in a browser, ignore the certificate warning (as it ships with a self-signed certificate that you
can change later on) and continue with the *Setup wizard* shown.


## Customizing your installation

In order to customize the installation, download the installer YAML file at `https://home.codescope.com/installer.yml`:

```bash
curl https://home.codescope.com/installer.yml -o installer.yml
```
 
Open it and modify the settings present in the `codescope-default-installer-config` config map:

| Setting | Default | Description |
| ------- | ------- | ----------- |
| `CODESCOPE_NAME` | `default` | The name of the Scope instance, to be used when naming resources. Use this setting if you have more than one Scope instance in the same namespace |
| `CODESCOPE_DB_DSN` | (empty) | A DSN to use an existing PostgreSQL instance and avoid deploying a built-in one (e.g. `postgresql://user:pass@host:port/db`) |
| `CODESCOPE_REDIS_DSN` | (empty) | A DSN to use an existing Redis instance and avoid deploying a built-in one (e.g. `redis://host:port`) |
| `CODESCOPE_CORE_REPLICAS` | `2` | Number of initial replicas for Scope's API/UI component deployment |
| `CODESCOPE_WORKER_REPLICAS` | `2` | Number of initial replicas for Scope's worker component deployment |


You can also customize the name of the namespace to be used by modifying the name of the `Namespace` resource
and updating all references to the namespace in the other resources.

Once customized, apply it to your Kubernetes cluster and follow the regular instructions to set it up:

```bash
kubectl apply -f installer.yml
```

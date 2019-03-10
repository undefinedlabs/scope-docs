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

If you are installing Scope locally on Docker for Mac, Docker for Windows or minikube, run the following command instead:

```bash
kubectl apply -f "https://home.codescope.com/installer.yml?http_port=8080&https_port=8443"
```

> Please note that in this case, GitHub won't be able to contact your local Scope installation unless you set up a local tunnel such as [ngrok](https://ngrok.com)

This will install Scope in a namespace called `scope`, with built-in PostgreSQL and Redis instances.
If you want to use an existing PostgreSQL or Redis instance, or customize any other parameter, read the section below on ["Customizing your installation"](#customizing-your-installation)

To get the Scope UI URL and set it up, wait a few minutes until the load balancer resource has been assigned a hostname or IP, and run:

```bash
kubectl -n scope get service/scope-default-router --template="https://{{or (index .status.loadBalancer.ingress 0).hostname (index .status.loadBalancer.ingress 0).ip}}:{{(index .spec.ports 0).port}}"
```

Open the printed URL in a browser, ignore the certificate warning (as it ships with a self-signed certificate that you
can change later on) and continue with the *Setup wizard* shown.


## Customizing your installation

In order to customize the installation, download the installer YAML file at `https://home.codescope.com/installer.yml`:

```bash
curl https://home.codescope.com/installer.yml -o installer.yml
```
 
Open it and modify the settings present in the `scope-default-installer-config` config map:

| Setting | Default | Description |
| ------- | ------- | ----------- |
| `SCOPE_NAME` | `default` | The name of the Scope instance, to be used when naming resources. Use this setting if you have more than one Scope instance in the same namespace |
| `SCOPE_DB_DSN` | (empty) | A DSN to use an existing PostgreSQL instance and avoid deploying a built-in one (e.g. `postgresql://user:pass@host:port/db`) |
| `SCOPE_REDIS_DSN` | (empty) | A DSN to use an existing Redis instance and avoid deploying a built-in one (e.g. `redis://host:port`) |
| `SCOPE_HTTP_PORT` | `80` | HTTP port to be exposed in the publicly reachable service |
| `SCOPE_HTTPS_PORT` | `443` | HTTPS port to be exposed in the publicly reachable service |
| `SCOPE_SERVICE_TYPE` | `LoadBalancer` | The service type to use for the publicly reachable service |


You can also customize the name of the namespace to be used by modifying the name of the `Namespace` resource
and updating all references to the namespace in the other resources.

Once customized, apply it to your Kubernetes cluster and follow the regular instructions to set it up:

```bash
kubectl apply -f installer.yml
```

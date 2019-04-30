---
id: installation
title: Installing Scope
sidebar_label: Installation
---

## Compatibility

Scope requires a **Kubernetes 1.11+ cluster** for deployment. You need to have *cluster admin* privileges to the cluster being used.

The following source code management providers are currently supported:

Name | Version |
-----|:------:
[GitHub.com](https://github.com) |  |
[GitHub Enterprise](https://github.com/enterprise) | 2.16.1+ |

> Do you use a source code management provider not listed here? Please [let us know](https://home.codescope.com/goto/support)!

Each agent has its own list of compatible platforms and libraries - please check out their documentation.


## Installation

To install Scope, run the following command:

```bash
bash <(curl -sL https://home.codescope.com/installer.sh)
```

and follow the instructions.

Scope will be accessible via the service named `scope-default-router` in the target namespace. If you chose a `LoadBalancer`
service type (the default), Scope will be accessible via HTTP and HTTPS through that service. The publicly accessible
URLs will be shown after the installation finishes.

> Please note that the installation process will generate a self-signed certificate for the HTTPS port 
that can be replaced during the setup wizard, or at any time in the admin panel

If you chose a `ClusterIP` service type, Scope will only be accessible internally in your cluster. For this service type, 
we recommend you configure your edge routing layer to forward traffic to port 80 of service `scope-default-router`.


## Configuring your installation

After the installation script has finished, open the URL of Scope in a browser. You will be shown a setup wizard - follow
the instructions to perform the initial configuration.

After the setup wizard is complete, you can manage your installation by navigating to `/admin` and entering your
admin password as entered during the setup wizard.

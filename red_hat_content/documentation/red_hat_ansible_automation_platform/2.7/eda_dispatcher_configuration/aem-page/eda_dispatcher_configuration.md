+++
title = "Dispatcherd configuration - Red Hat Ansible Automation Platform 2.7"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/eda_dispatcher_configuration"
template = "docs/aem-title.html"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"]]
category = ""
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/eda_dispatcher_configuration/aem-page/eda_dispatcher_configuration.html"
last_crumb = "Dispatcherd configuration"
modified = "2026-06-05T07:48:10.594Z"
multi_page_path = ""
name = "Dispatcherd configuration"
oversized = "false"
page_slug = "eda_dispatcher_configuration"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/eda_dispatcher_configuration"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/eda_dispatcher_configuration/toc/toc.json"
type = "aem-page"
+++

# Dispatcherd configuration

`Dispatcherd` uses PostgreSQL's pg_notify as its message transport to coordinate background task processing for Event-Driven Ansible controller. The following environment variables control how `dispatcherd` connects to PostgreSQL, identifies worker queues, and manages health checks.

For single-node deployments, the default values are sufficient and no additional configuration is required. `Dispatcherd` automatically connects to the same PostgreSQL instance used by Event-Driven Ansible controller.

For multi-node deployments, you must configure queue names to ensure that each node runs its own activation workers and that workloads are distributed across nodes. See the **Multi-node deployments** for details.

*Table 1. Dispatcherd environment variables*

| Variable                                    | Description                                                                                                                                                               | Default                         |
| ------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------- |
| `EDA_PG_NOTIFY_DSN_SERVER`                  | The PostgreSQL connection string for the pg\_notify broker. Must point to the same PostgreSQL instance used by the Event-Driven Ansible controller.                       | Application database connection |
| `EDA_RULEBOOK_QUEUE_NAME`                   | The base queue name for the activation worker on the current node.                                                                                                        | `activation`                    |
| `EDA_RULEBOOK_WORKER_QUEUES`                | A comma-separated list of all activation worker queue names across the deployment. Required for multi-node deployments (for example, activation-node1, activation-node2). | Empty (single-node)             |
| `EDA_DISPATCHERD_QUEUE_HEALTHCHECK_TIMEOUT` | The amount of time, in seconds, to wait when checking worker health.                                                                                                      | `3`                             |

## Worker services

Each Event-Driven Ansible controller deployment requires at least one default worker and one activation worker. Use the following commands to initialize these services:

```
aap-eda-manage dispatcherd --worker-class DefaultWorker
aap-eda-manage dispatcherd --worker-class ActivationWorker
```

## Multi-node deployments

In multi-node deployments, each node runs its own activation workers with a unique queue name. You must set `EDA_RULEBOOK_QUEUE_NAME` to a node-specific value on each node and set `EDA_RULEBOOK_WORKER_QUEUES` to the full list of all node queue names across the deployment. This ensures the Event-Driven Ansible controller can distribute activation workloads and route operations to the correct node.

## Deprecated Redis variables

The following Redis-related variables are no longer used by the Event-Driven Ansible controller in Ansible Automation Platform 2.7. You can safely remove these from your inventory files:

- `EDA_MQ_HOST`
- `EDA_MQ_PORT`
- `EDA_MQ_USER`
- `EDA_MQ_USER_PASSWORD`
- `EDA_MQ_CLIENT_CERT_PATH`
- `EDA_MQ_CLIENT_KEY_PATH`
- `EDA_MQ_CLIENT_CACERT_PATH`

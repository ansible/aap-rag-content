+++
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-ref_metrics_service_configuration_variables"
title = "Metrics service configuration variables - Red Hat Ansible Automation Platform 2.7"
template = "docs/aem-title.html"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-con_understand_metrics_service_architecture/", "Understand metrics service architecture"]]
category = "Install"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/install-ref_metrics_service_configuration_variables/aem-page/install-ref_metrics_service_configuration_variables.html"
last_crumb = "Metrics service configuration variables"
latest = "true"
modified = "2026-10-06T15:21:13.207Z"
multi_page_path = ""
name = "Metrics service configuration variables"
oversized = "false"
page_slug = "install-ref_metrics_service_configuration_variables"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/install-ref_metrics_service_configuration_variables"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/install-ref_metrics_service_configuration_variables/toc/toc.json"
type = "aem-page"
+++

# Metrics service configuration variables

Review configuration variables to customize metrics service deployment, database connections, security settings, and operational parameters.

## Inventory variables reference

**Required variables for automationmetrics group**

The following variables must be defined when deploying metrics service with the containerized installer:

| Variable                                        | Default | Required/Optional | Description                                                                                                            |
| ----------------------------------------------- | ------- | ----------------- | ---------------------------------------------------------------------------------------------------------------------- |
| `automationmetrics_pg_host`                     | (none)  | **Required**      | PostgreSQL host for the metrics database                                                                               |
| `automationmetrics_pg_password`                 | (none)  | **Required**\*    | Password for the metrics database user. \*Not required when`automationmetrics_pg_cert_auth: true` is set.              |
| `automationmetrics_controller_read_pg_host`     | (none)  | **Required**\*    | PostgreSQL host for the controller database                                                                            |
| `automationmetrics_controller_read_pg_password` | (none)  | **Required**\*    | Password for the read-only controller database user. \*Not required when`automationmetrics_pg_cert_auth: true` is set. |

**Optional variables with defaults**

| Variable                             | Default           | Description                                         |
| ------------------------------------ | ----------------- | --------------------------------------------------- |
| `automationmetrics_pg_port`          | `5432`            | PostgreSQL port                                     |
| `automationmetrics_pg_database`      | `metrics_service` | Database name                                       |
| `automationmetrics_pg_username`      | `metrics_service` | Database user                                       |
| `automationmetrics_api_port`         | `8006`            | Port the metrics service API listens on (Gunicorn)  |
| `automationmetrics_nginx_http_port`  | `8087`            | nginx HTTP port (redirects to HTTPS)                |
| `automationmetrics_nginx_https_port` | `8450`            | nginx HTTPS port                                    |
| `automationmetrics_pg_cert_auth`     | `false`           | Use certificate authentication instead of passwords |

Note:

**Note on certificate authentication:** When `automationmetrics_pg_cert_auth: true`, password variables (`automationmetrics_pg_password` and `automationmetrics_controller_read_pg_password`) are not required. The service uses PostgreSQL certificate-based authentication instead.

**Flag:** `FEATURE_INDIRECT_NODE_COLLECTION_ENABLED`

**Default:** `false`

**Level:** Gateway AAPFlag (platform-level)

**Restart required:** No

**Purpose:** Enable daily collection of indirect node audit data from the controller database

When enabled (`FEATURE_INDIRECT_NODE_COLLECTION_ENABLED: true`):

- Collects daily snapshots of API-managed indirect nodes (for example, network devices managed through Ansible collections)
- Includes indirect node counts grouped by Ansible collection and module in the anonymized payload sent to Red Hat
- Host names and organization names are stripped from the payload before transmission

This flag is set at the Gateway level, not through `automationmetrics_*` inventory variables. No additional inventory configuration is required.

Feature flags resolve through the following priority chain (highest to lowest):

1. DB Setting (`dynamic_settings` table)
2. Dynaconf / environment variable
3. Direct settings attribute
4. DAB AAPFlag (Gateway-level)
5. Default value

## Events collector settings

The events collector (main_jobevent_service) processes job event data to extract collection, module, and role usage statistics. These variables are configurable as Django settings or environment variables without a code change. Use them to control collection volume on large deployments.

| Variable             | Default | Description                                                                                                      |
| -------------------- | ------- | ---------------------------------------------------------------------------------------------------------------- |
| `JOBEVENT_ROW_LIMIT` | 200,000 | Maximum number of job event rows to process per hourly collection cycle. Set to 0 for unlimited processing.      |
| `JOBEVENT_JOB_LIMIT` | 1,000   | Maximum number of jobs to process for event data per hourly collection cycle. Set to 0 for unlimited processing. |

Warning:

Setting `JOBEVENT_ROW_LIMIT` or `JOBEVENT_JOB_LIMIT` to 0 removes the limit entirely, causing the collector to process all available events. On large deployments with high job volumes, this can significantly increase collection time and database load. To effectively disable event collection for performance reasons, set both values to 1.

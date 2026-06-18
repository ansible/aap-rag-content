+++
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.6/ref_metrics_service_configuration_variables"
template = "docs/aem-title.html"
title = "Metrics service configuration variables - Red Hat Ansible Automation Platform 2.6"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6", "2.6"]]
category = ""
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/ref_metrics_service_configuration_variables/aem-page/ref_metrics_service_configuration_variables.html"
last_crumb = "Metrics service configuration variables"
modified = "2026-05-21T14:12:12.122Z"
multi_page_path = ""
name = "Metrics service configuration variables"
oversized = "false"
page_slug = "ref_metrics_service_configuration_variables"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.6"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/ref_metrics_service_configuration_variables"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/ref_metrics_service_configuration_variables/toc/toc.json"
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

**Dashboard and feature flags**

| Variable                               | Default | Required/Optional | Description                                                                                                                                                                                                                                                                                          |
| -------------------------------------- | ------- | ----------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `FEATURE_DASHBOARD_COLLECTION_ENABLED` | `false` | Optional          | Enable automation dashboard data collection. When`true`, metrics service collects dashboard-specific metrics (cost data, ROI calculations, and pricing information) in addition to standard anonymized metrics. Maps to environment variable`METRICS_SERVICE_FEATURE_ENABLED__DASHBOARD_COLLECTION`. |

## Dashboard feature flag

**Inventory Variable:** `FEATURE_DASHBOARD_COLLECTION_ENABLED`

**Default:** `false`

**Purpose:** Enable automation dashboard data collection

When enabled (`FEATURE_DASHBOARD_COLLECTION_ENABLED: true`):

- Collects dashboard-specific data (cost, ROI, pricing information)
- Runs on 6-hourly schedule to minimize database impact

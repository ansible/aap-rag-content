+++
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.6/optimize-inventory_file_variables_for_automation_dashboard"
title = "Inventory file variables for automation dashboard - Red Hat Ansible Automation Platform 2.6"
template = "docs/aem-title.html"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6", "2.6"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6/optimize-con_user_data_tracking/", "Get insights on automation across your environment with Automation Analytics"]]
category = "Optimize"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/optimize-inventory_file_variables_for_automation_dashboard/aem-page/optimize-inventory_file_variables_for_automation_dashboard.html"
last_crumb = "Inventory file variables for automation dashboard"
modified = "2026-05-21T14:12:12.122Z"
multi_page_path = ""
name = "Inventory file variables for automation dashboard"
oversized = "false"
page_slug = "optimize-inventory_file_variables_for_automation_dashboard"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.6"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/optimize-inventory_file_variables_for_automation_dashboard"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/optimize-inventory_file_variables_for_automation_dashboard/toc/toc.json"
type = "aem-page"
+++

# Inventory file variables for automation dashboard

The inventory variables required by the automation dashboard installation program are described in the following table:

| Inventory variable                             | Description                                                                                                                                                                                                                                               |
| ---------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `aap_auth_provider_name`                       | Natural language name shown on the login page. Default: Ansible Automation Platform                                                                                                                                                                       |
| `aap_auth_provider_protocol`                   | Enter http or https                                                                                                                                                                                                                                       |
| `aap_auth_provider_aap_version`                | You must preconfigure and assign labels to Ansible Automation Platform for display in the automation dashboard. Valid values are 2.4, 2.5, 2.6, or 2.7                                                                                                    |
| `aap_auth_provider_host`                       | Ansible Automation Platform IP or DNS name, with optional port                                                                                                                                                                                            |
| `aap_auth_provider_check_ssl`                  | Enforce TLS check or not                                                                                                                                                                                                                                  |
| `aap_auth_provider_client_id`                  | Ansible Automation Platform OAuth2 application`client_id`. Required for SSO authentication.                                                                                                                                                               |
| `aap_auth_provider_client_secret`              | Ansible Automation Platform OAuth2 application`client_secret`                                                                                                                                                                                             |
| `initial_sync_days`                            | Requests x number of days of old data, counting from "today"                                                                                                                                                                                              |
| `initial_sync_since`                           | Requests data from the specified date until "today"                                                                                                                                                                                                       |
| `dashboard_update_secret`                      | Forces regeneration of autogenerated Podman secrets. Store the password for database access by using a Podman secret. Set`dashboard_update_secret` to true if you changed the`dashboard_pg_password` in inventory.                                        |
| `nginx_disable_https`                          | Enables use of http instead of https for automation dashboard                                                                                                                                                                                             |
| `nginx_http_port`                              | Configures the HTTP port for automation dashboard                                                                                                                                                                                                         |
| `nginx_https_port`                             | Configures the HTTPS port for automation dashboard                                                                                                                                                                                                        |
| `dashboard_tls_cert`                           | The public TLS certificate for the automation dashboard. This file must include the server certificate, intermediate CA certificates, and the root CA certificate. The server certificate must appear at the beginning of the file.                       |
| `dashboard_tls_key`                            | The private TLS key for the automation dashboard. If not specified, the installation program generates a self-signed key.                                                                                                                                 |
| `postgresql_admin_username`                    | Admin username to access PostgreSQL database                                                                                                                                                                                                              |
| `postgresql_admin_password`                    | Admin password to access PostgreSQL database                                                                                                                                                                                                              |
| `registry_username`                            | Username used to pull container images from`registry.redhat.io`. This variable is required when using an online installation program.                                                                                                                     |
| `registry_password`                            | Password used to pull container images from`registry.redhat.io`. This variable is required when using an online installation program.                                                                                                                     |
| `dashboard_pg_containerized`                   | Configures the installation program to install and configure the database as a container on the same host as automation dashboard.`True` is also the only supported value.                                                                                |
| `dashboard_admin_password`                     | The password for the automation dashboard administrator user. The username is always`admin`.                                                                                                                                                              |
| `dashboard_pg_host`                            | The hostname or IP address of the PostgreSQL database. This host must be accessible from the installation program node on port 5432. If a public IP address blocks this port, you must use the internal IP address.                                       |
| `dashboard_pg_username`                        | The database user for automation dashboard.                                                                                                                                                                                                               |
| `dashboard_pg_password`                        | The password for the`dashboard_pg_username`.                                                                                                                                                                                                              |
| `dashboard_pg_database`                        | The database schema name for automation dashboard.                                                                                                                                                                                                        |
| `bundle_install`                               | Indicates the required container images are already included in the installation bundle (tar file).                                                                                                                                                       |
| `bundle_dir`                                   | The directory where the installation bundle unpacks`+ /bundle` (for example:/home/<username>/ansible-automation-dashboard-containerized-setup/bundle). The default value is relative to the current directory (PWD) and should work without modification. |
| `redis_mode`                                   | Configures the Redis deployment mode. The required value is`standalone`.                                                                                                                                                                                  |
| `registry_url_aap_automation_dashboard`        | Configures a custom container registry URL specifically for the automation dashboard images. Use this if you must pull dashboard images from a different registry than your database or Redis images.                                                     |
| `registry_ns_aap_automation_dashboard`         | Configures a custom namespace specifically for the automation dashboard images.                                                                                                                                                                           |
| `registry_username_aap_automation_dashboard`   | The username for the custom registry defined in`registry_url_aap_automation_dashboard`. Required if the dashboard registry differs from the primary registry.                                                                                             |
| `registry_password_aap_automation_dashboard`   | The password for the custom registry defined in`registry_url_aap_automation_dashboard`. Required if the dashboard registry differs from the primary registry.                                                                                             |
| `registry_tls_verify_aap_automation_dashboard` | Enforces or disables TLS certificate verification when pulling automation dashboard images from a custom registry. Default:`True`.                                                                                                                        |

## Cost and savings analysis metrics

The costs and savings analysis generates metrics that quantify the return on investment (ROI) derived from automation execution.

The costs and savings analysis generates the following metrics to quantify the return on investment (ROI) derived from automation execution.

| Metric                                              | Description                                                                                                                                                                                              |
| --------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Cost of manual automation                           | Total cost if all jobs were run manually. Calculated as: (Manual time in minutes × Host executions) × Average labor cost per minute.                                                                     |
| Cost of automated execution                         | Total cost of running jobs on Ansible Automation Platform. Calculated as: (Running time in minutes × Prorated subscription cost per minute).                                                             |
| Total savings/cost avoided                          | The difference between manual and automated costs.                                                                                                                                                       |
| Total hours saved/avoided                           | Time saved by automation compared to manual execution.                                                                                                                                                   |
| Time taken to manually execute (min)                | Estimated manual execution time in minutes.                                                                                                                                                              |
| Time taken to create automation (min)               | Estimated time spent creating or authoring the automation (for example, writing playbooks or setting up jobs). Included in cost calculations when enabled in settings.                                   |
| Hourly rate for manually running the job ($)        | The hourly labor cost used to estimate the expense of running jobs manually. Used to calculate manual cost and savings.                                                                                  |
| Monthly cost of running Ansible Automation Platform | Monthly cost of running the Ansible Automation Platform. This value includes license, labor and infrastructure costs to run Ansible Automation Platform. It is used to calculate the automation savings. |

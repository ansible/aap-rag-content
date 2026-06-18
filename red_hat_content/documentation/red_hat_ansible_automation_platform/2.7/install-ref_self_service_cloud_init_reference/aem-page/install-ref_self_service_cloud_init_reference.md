+++
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-ref_self_service_cloud_init_reference"
template = "docs/aem-title.html"
title = "Cloud-init reference - Red Hat Ansible Automation Platform 2.7"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-con_self_service_rhel_appliances/", "Deploy Ansible automation portal RHEL appliance"]]
category = "Install"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/install-ref_self_service_cloud_init_reference/aem-page/install-ref_self_service_cloud_init_reference.html"
last_crumb = "Cloud-init reference"
modified = "2026-06-05T07:48:10.594Z"
multi_page_path = ""
name = "Cloud-init reference"
oversized = "false"
page_slug = "install-ref_self_service_cloud_init_reference"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/install-ref_self_service_cloud_init_reference"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/install-ref_self_service_cloud_init_reference/toc/toc.json"
type = "aem-page"
+++

# Cloud-init reference

The following tables describe all cloud-init fields supported by the Ansible automation portal RHEL appliance.

## SSH access (standard cloud-init)

*Table 1. SSH access fields*

| Field                           | Required | Default | Description                                    |
| ------------------------------- | -------- | ------- | ---------------------------------------------- |
| `users[].name`                  | Yes      | --      | Linux username for SSH access.                 |
| `users[].sudo`                  | Yes      | --      | Sudo privileges. Use `ALL=(ALL) NOPASSWD:ALL`. |
| `users[].ssh_authorized_keys[]` | Yes      | --      | One or more SSH public keys.                   |

## Ansible Automation Platform connection

*Table 2. Ansible Automation Platform connection fields*

| Field                     | Required | Default | Description                                                               |
| ------------------------- | -------- | ------- | ------------------------------------------------------------------------- |
| `aap.host_url`            | Yes      | --      | Ansible Automation Platform URL (for example, `https://aap.example.com`). |
| `aap.token`               | Yes      | --      | Ansible Automation Platform API token with administrator privileges.      |
| `aap.check_ssl`           | No       | `true`  | Set `false` for self-signed Ansible Automation Platform certificates.     |
| `aap.oauth.client_id`     | Yes      | --      | OAuth 2.0 application client ID.                                          |
| `aap.oauth.client_secret` | Yes      | --      | OAuth 2.0 application client secret.                                      |

## Database

*Table 3. Database fields*

| Field                             | Required          | Default       | Description                                                                                                                                                                                       |
| --------------------------------- | ----------------- | ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `database.type`                   | No                | `builtin`     | `builtin` or `external`. When set to `builtin`, the `database.external.*` fields are ignored. When set to `external`, you must provide `database.external.host` and `database.external.password`. |
| `database.builtin.password`       | No                | `auto`        | PostgreSQL user password. `auto` generates a random value.                                                                                                                                        |
| `database.builtin.admin_password` | No                | `auto`        | PostgreSQL admin password. `auto` generates a random value.                                                                                                                                       |
| `database.builtin.name`           | No                | `portal_db`   | Database name.                                                                                                                                                                                    |
| `database.builtin.user`           | No                | `portal_user` | Database user.                                                                                                                                                                                    |
| `database.external.host`          | Yes (if external) | --            | External PostgreSQL hostname.                                                                                                                                                                     |
| `database.external.port`          | No                | `5432`        | External PostgreSQL port.                                                                                                                                                                         |
| `database.external.name`          | No                | `portal_db`   | External database name.                                                                                                                                                                           |
| `database.external.user`          | No                | `portal_user` | External database user. Requires the `CREATEDB` privilege.                                                                                                                                        |
| `database.external.password`      | Yes (if external) | --            | External database password.                                                                                                                                                                       |
| `database.external.ssl`           | No                | `true`        | Enable SSL for external database connection.                                                                                                                                                      |

## Security

*Table 4. Security fields*

| Field                     | Required | Default | Description                                                     |
| ------------------------- | -------- | ------- | --------------------------------------------------------------- |
| `security.backend_secret` | No       | `auto`  | Backend authentication secret. `auto` generates a random value. |

## Network

*Table 5. Network fields*

| Field              | Required | Default       | Description                                                                                                                                                                                                |
| ------------------ | -------- | ------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `network.port`     | No       | `443`         | Ansible automation portal HTTPS listen port. If you are using the standard port 443, you do not need to specify this field.                                                                                |
| `network.base_url` | No       | Auto-detected | User-accessible URL that users enter in their browser. Set this when users access Ansible automation portal through a hostname, route, or load balancer. If omitted, auto-detected from the VM IP address. |

## Source control integrations

*Table 6. Source control integration fields*

| Field                       | Required | Default      | Description                                               |
| --------------------------- | -------- | ------------ | --------------------------------------------------------- |
| `integrations.github.url`   | No       | `github.com` | GitHub hostname. For GitHub Enterprise, omit `https://`.  |
| `integrations.github.token` | No       | --           | GitHub personal access token.                             |
| `integrations.gitlab.url`   | No       | `gitlab.com` | GitLab hostname. For self-hosted GitLab, omit `https://`. |
| `integrations.gitlab.token` | No       | --           | GitLab personal access token.                             |

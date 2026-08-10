# Cloud-init reference

The following tables describe all cloud-init fields supported by the Ansible automation portal RHEL appliance.

## SSH access (standard cloud-init)

*Table 1. SSH access fields*

| Field                           | Required | Default | Description                                   |
| ------------------------------- | -------- | ------- | --------------------------------------------- |
| `users[].name`                  | Yes      | --      | Linux username for SSH access.                |
| `users[].sudo`                  | Yes      | --      | Sudo privileges. Use`ALL=(ALL) NOPASSWD:ALL`. |
| `users[].ssh_authorized_keys[]` | Yes      | --      | One or more SSH public keys.                  |

## Ansible Automation Platform connection

*Table 2. Ansible Automation Platform connection fields*

| Field                     | Required | Default | Description                                                              |
| ------------------------- | -------- | ------- | ------------------------------------------------------------------------ |
| `aap.host_url`            | Yes      | --      | Ansible Automation Platform URL (for example,`https://aap.example.com`). |
| `aap.token`               | Yes      | --      | Ansible Automation Platform API token with administrator privileges.     |
| `aap.check_ssl`           | No       | `true`  | Set`false` for self-signed Ansible Automation Platform certificates.     |
| `aap.oauth.client_id`     | Yes      | --      | OAuth 2.0 application client ID.                                         |
| `aap.oauth.client_secret` | Yes      | --      | OAuth 2.0 application client secret.                                     |

## Database

*Table 3. Database fields*

| Field                             | Required          | Default       | Description                                                                                                                                                                                 |
| --------------------------------- | ----------------- | ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `database.type`                   | No                | `builtin`     | `builtin` or`external`. When set to`builtin`, the`database.external.*` fields are ignored. When set to`external`, you must provide`database.external.host` and`database.external.password`. |
| `database.builtin.password`       | No                | `auto`        | PostgreSQL user password.`auto` generates a random value.                                                                                                                                   |
| `database.builtin.admin_password` | No                | `auto`        | PostgreSQL admin password.`auto` generates a random value.                                                                                                                                  |
| `database.builtin.name`           | No                | `portal_db`   | Database name.                                                                                                                                                                              |
| `database.builtin.user`           | No                | `portal_user` | Database user.                                                                                                                                                                              |
| `database.external.host`          | Yes (if external) | --            | External PostgreSQL hostname.                                                                                                                                                               |
| `database.external.port`          | No                | `5432`        | External PostgreSQL port.                                                                                                                                                                   |
| `database.external.name`          | No                | `portal_db`   | External database name.                                                                                                                                                                     |
| `database.external.user`          | No                | `portal_user` | External database user. Requires the`CREATEDB` privilege.                                                                                                                                   |
| `database.external.password`      | Yes (if external) | --            | External database password.                                                                                                                                                                 |
| `database.external.ssl`           | No                | `true`        | Enable SSL for external database connection.                                                                                                                                                |

## Security

*Table 4. Security fields*

| Field                     | Required | Default | Description                                                    |
| ------------------------- | -------- | ------- | -------------------------------------------------------------- |
| `security.backend_secret` | No       | `auto`  | Backend authentication secret.`auto` generates a random value. |

## Network

*Table 5. Network fields*

| Field                         | Required | Default       | Description                                                                                                                                                                                              |
| ----------------------------- | -------- | ------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `network.port`                | No       | `443`         | Ansible automation portal HTTPS listen port. If you are using the standard port 443, you do not need to specify this field.                                                                              |
| `network.base_url`            | No       | Auto-detected | User-accessible URL that users enter in their browser. Set this when users access Ansible automation portal through a hostname, route, or load balancer. If omitted, auto-detected from the VM IP address. |
| `network.node_extra_ca_certs` | No       | --            | Absolute path to a PEM file containing additional CA certificates that Node.js trusts. Use this when connecting to an external PostgreSQL database or other services that use certificates signed by a custom CA. |

## Source control integrations

Configure source control integration for content discovery. For GitHub, use either a personal access token or a GitHub App. A GitHub App is the recommended option. You do not need both, but having both configured does not break the install.

Note:

Cloud-init supports a single GitHub and a single GitLab host. For multiple hosts (for example, `github.com` and a GitHub Enterprise instance) or advanced configurations, define the `integrations:` section in `app-config.production.yaml` instead. When `integrations:` is present in `app-config.production.yaml`, the auto-generated integration from cloud-init tokens is skipped.

*Table 6. GitHub integration fields*

| Field                                     | Required | Default      | Description                                                                                                   |
| ----------------------------------------- | -------- | ------------ | ------------------------------------------------------------------------------------------------------------- |
| `integrations.github.url`                 | No       | `github.com` | GitHub hostname. For GitHub Enterprise, omit`https://`.                                                       |
| `integrations.github.token`               | No       | --           | GitHub personal access token for content discovery. Alternative to GitHub App.                                |
| `integrations.github.app.id`              | No       | --           | GitHub App ID. Required when using GitHub App authentication.                                                 |
| `integrations.github.app.client_id`       | No       | --           | GitHub App client ID.                                                                                         |
| `integrations.github.app.client_secret`   | No       | --           | GitHub App client secret.                                                                                     |
| `integrations.github.app.private_key`     | No       | --           | GitHub App private key in PEM format. Multi-line PEM keys are base64-encoded automatically during processing. |
| `integrations.github.oauth.client_id`     | No       | --           | GitHub OAuth client ID for saving execution environment definitions to repositories.                          |
| `integrations.github.oauth.client_secret` | No       | --           | GitHub OAuth client secret.                                                                                   |

*Table 7. GitLab integration fields*

| Field                                     | Required | Default      | Description                                                                          |
| ----------------------------------------- | -------- | ------------ | ------------------------------------------------------------------------------------ |
| `integrations.gitlab.url`                 | No       | `gitlab.com` | GitLab hostname. For self-hosted GitLab, omit`https://`.                             |
| `integrations.gitlab.token`               | No       | --           | GitLab personal access token for content discovery.                                  |
| `integrations.gitlab.oauth.client_id`     | No       | --           | GitLab OAuth client ID for saving execution environment definitions to repositories. |
| `integrations.gitlab.oauth.client_secret` | No       | --           | GitLab OAuth client secret.                                                          |

Note:

Source control integration fields are optional. If not provided via cloud-init, you can configure source control integrations post-deployment by creating Podman secrets manually and adding Quadlet drop-in files. Cloud-init delivery eliminates the need for manual `podman secret create` and Quadlet drop-in setup.

## Backup

*Table 8. Backup fields*

| Field                   | Required | Default | Description                       |
| ----------------------- | -------- | ------- | --------------------------------- |
| `backup.enabled`        | No       | --      | Enable automated backups.         |
| `backup.schedule`       | No       | --      | Backup schedule.                  |
| `backup.retention_days` | No       | --      | Number of days to retain backups. |

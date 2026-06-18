+++
title = "Portal CLI commands reference - Red Hat Ansible Automation Platform 2.7"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-ref_self_service_portal_cli_commands"
template = "docs/aem-title.html"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-con_self_service_rhel_appliances/", "Deploy Ansible automation portal RHEL appliance"]]
category = "Install"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/install-ref_self_service_portal_cli_commands/aem-page/install-ref_self_service_portal_cli_commands.html"
last_crumb = "Portal CLI commands reference"
modified = "2026-06-05T07:48:10.594Z"
multi_page_path = ""
name = "Portal CLI commands reference"
oversized = "false"
page_slug = "install-ref_self_service_portal_cli_commands"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/install-ref_self_service_portal_cli_commands"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/install-ref_self_service_portal_cli_commands/toc/toc.json"
type = "aem-page"
+++

# Portal CLI commands reference

The Ansible automation portal appliance provides the `ansible-portal` management CLI for administration and troubleshooting.

## Accessing the appliance

You can access the appliance using SSH with the key you provided during initial configuration:

```terminal
ssh -i /path/to/ssh-key/id_ed25519 -p *port_number* admin@*VM_IP*
```
Replace the following placeholders:

- `/path/to/ssh-key/id_ed25519` with the path to your SSH private key.
- `*port_number*` with the SSH port number (default is 22).
- `*VM_IP*` with the IP address or hostname of your appliance.

## The ansible-portal CLI

The `ansible-portal` command is the primary management interface for the appliance, following Red Hat Ansible tooling conventions (`ansible-navigator`, `ansible-builder`, `ansible-lint`).

```terminal
ansible-portal <command> [options]
```

*Table 1. Available commands*

| Command          | Description                                                  |
| ---------------- | ------------------------------------------------------------ |
| `status`         | Show portal service status and diagnostics.                  |
| `backup`         | Create portal backup. Use `--list` to list backups.          |
| `restore *file*` | Restore from backup archive. Use `--latest` for most recent. |
| `registry-login` | Log in to container registry for image upgrades.             |


Run `ansible-portal *command* --help` for command-specific options.

## ansible-portal status

Displays the current status of all Ansible automation portal services.

**Usage:**

```terminal
sudo ansible-portal status            # One-shot status display
sudo ansible-portal status --watch    # Refresh status every 5 seconds
```
**Description:**

Displays the current status of all Ansible automation portal services, including:

- Setup completion status
- PostgreSQL database state and connectivity
- Devtools service state
- Portal service state and plug-in installation status
- Scheduled backup status
- Disk and memory resource usage


Use this command to verify that all services are running correctly after installation or troubleshooting. Use `--watch` to continuously monitor service status.

## ansible-portal backup

Creates a backup of the portal configuration and data.

**Usage:**

```terminal
sudo ansible-portal backup                          # Interactive backup (select content)
sudo ansible-portal backup --full                   # Full backup (all items)
sudo ansible-portal backup --minimal                # Required items only
sudo ansible-portal backup --list                   # List existing backups
sudo ansible-portal backup --export /path/to/dir/   # Copy latest backup to a directory
```
**Description:**

Creates a backup archive containing the portal configuration, Podman secrets, and data. Use this command before making significant configuration changes or for disaster recovery planning.

- `backup` without options starts an interactive backup where you select the content to include.
- `--full` creates a complete backup of all configuration and data.
- `--minimal` backs up only the required configuration items.
- `--list` lists existing backups.
- `--export` copies the latest backup to the specified directory. If no backup exists, one is created first.


Important:

Backup archives contain credentials in plain text. Restrict file permissions on backup archives. Encrypt archives before transferring to remote storage:

```terminal
gpg --symmetric --cipher-algo AES256 /var/lib/portal/backups/*backup-file*.tar.gz
```

**Example output:**

```terminal
Backup contents selection
═══════════════════════════════════════════════════════════

Current selection (Y=included, N=excluded):

━━━ Required (always included) ━━━
  [Y] marker: Setup Marker
      Setup complete marker file
  [Y] config: Portal Configuration
      Core configuration (app-config.production.yaml)

━━━ Recommended ━━━
  [Y] database: PostgreSQL Database
      Full database dump
  [Y] backup_config: Backup Settings
      Backup schedule and retention
  [Y] plugins: Plugin Configuration
      Dynamic plug-ins config
  [Y] ssl: SSL Certificates
      HTTPS certificates (cert.pem, key.pem)

━━━ Optional (sensitive) ━━━
  [N] registry_auth: Registry Credentials
      Container registry auth (auth.json)
  [N] config_history: Config History
      Previous configuration snapshots

Options:
  1. Proceed with current selection
  2. Include all items (full backup)
  3. Toggle optional items
  4. Cancel

Choice [1]: 1

[INFO] Creating backup: portal-backup-2026-05-07T143022
[INFO] Backing up configuration...
[INFO] Backing up SSL certificates...
[INFO] Backing up database...
[OK] Database backed up
[INFO] Backing up plugins configuration...
[INFO] Creating backup archive...
[OK] Backup created: /var/lib/portal/backups/portal-backup-2026-05-07T143022.tar.gz

Backup file: /var/lib/portal/backups/portal-backup-2026-05-07T143022.tar.gz
Size: 2.1M

Contents included:
  Portal Configuration
  Setup Marker
  PostgreSQL Database
  Backup Settings
  Plugin Configuration
  SSL Certificates
```

## ansible-portal restore

Restores the portal from a backup.

**Usage:**

```terminal
sudo ansible-portal restore --list                  # List available backups
sudo ansible-portal restore --latest                # Restore the newest backup
sudo ansible-portal restore --latest --dry-run      # Preview restore without changes
sudo ansible-portal restore /path/to/backup.tar.gz  # Restore a specific backup file
```
**Description:**

Restores the portal configuration, Podman secrets, Quadlet drop-in files, and data from a backup created by `ansible-portal backup`.

- `--list` lists all available backups.
- `--latest` restores from the most recent backup.
- `--dry-run` previews what would be restored without making changes.
- Specify a file path to restore from a specific backup archive.


Note:

Restoring a backup overwrites the current portal configuration. Use `--dry-run` to preview the restore before executing. Create a backup of the current state before restoring if you want to preserve it.

**Example output:**

```terminal
[INFO] Using latest backup: portal-backup-2026-05-07T143022.tar.gz
[INFO] Restoring from: /var/lib/portal/backups/portal-backup-2026-05-07T143022.tar.gz
[INFO] Extracting backup...
[INFO] Backup created: 2026-05-07T14:30:22+00:00
[INFO] Stopping services...
[INFO] Current config backed up
[INFO] Restoring configuration...
[INFO] Restoring Podman secrets...
[OK] Podman secrets restored
[INFO] Generated secrets drop-in: /etc/containers/systemd/portal.container.d/secrets.conf
[INFO] Generated secrets drop-in: /etc/containers/systemd/postgres.container.d/secrets.conf
[INFO] Generated postgres config drop-in: /etc/containers/systemd/postgres.container.d/config.conf (user=portal_user, db=portal_db)
[OK] Configuration restored
[INFO] Restoring plug-ins configuration...
[OK] Plug-ins configuration restored
[INFO] Starting PostgreSQL...
[INFO] Restoring database...
[OK] Database restored
[INFO] Starting Portal...
[OK] Restore complete.

Services have been restarted.
Check status with: portal-status
```
Services stop during restore and restart automatically.

## ansible-portal registry-login

Manages container registry credentials for pulling portal images.

**Usage:**

```terminal
sudo ansible-portal registry-login                 # Log in to registry.redhat.io (default)
sudo ansible-portal registry-login *registry_host* # Log in to a specific registry
sudo ansible-portal registry-login --test          # Test stored credentials
sudo ansible-portal registry-login --logout        # Remove stored credentials
```
**Description:**

Manages authentication to container registries used for pulling Ansible automation portal images and updates.

- `registry-login` without arguments prompts for credentials for `registry.redhat.io`.
- Specify a registry hostname to authenticate to a different registry, such as a private mirror.
- `--test` verifies that stored credentials are valid by inspecting the registry without downloading images.
- `--logout` clears stored credentials for the registry.


Use this command to configure registry authentication for `bootc upgrade` operations. In disconnected environments, use this command to authenticate to your private registry mirror.

In disconnected environments where no registry is available, you can bypass the registry authentication gate by creating an override marker:

```terminal
sudo touch /etc/portal/.registry-auth-override
```

## Configuration management

The appliance uses two YAML configuration files at `/etc/portal/configs/app-config/`:

`app-config.yaml`
Infrastructure configuration (base URL, database connection, TLS, system defaults). This file is set during initial deployment and is not typically modified.

`app-config.production.yaml`
Application configuration (Ansible Automation Platform connection, OAuth settings, SCM integrations, catalog sync). Edit this file for day-to-day configuration changes.

Sensitive values such as tokens and passwords are stored as Podman secrets and injected into the portal container through environment variable interpolation (`${VAR}` syntax in the YAML files).

**Updating configuration**

To update the portal configuration:

1. Edit the application configuration file:

```terminal
sudo vi /etc/portal/configs/app-config/app-config.production.yaml
```

2. Restart the portal service to apply the changes:

```terminal
sudo systemctl restart portal
```

## Managing secrets

The portal stores sensitive values as Podman secrets, separate from the configuration files.

*Table 2. Portal secrets reference*

| Secret name                         | Environment variable         | Type                                     |
| ----------------------------------- | ---------------------------- | ---------------------------------------- |
| `portal_backend_secret`             | `BACKEND_SECRET`             | Auto-generated                           |
| `portal_postgresql_password`        | `POSTGRESQL_PASSWORD`        | Auto-generated or user-provided          |
| `portal_postgresql_admin_password`  | `POSTGRESQL_ADMIN_PASSWORD`  | Auto-generated                           |
| `portal_aap_token`                  | `AAP_TOKEN`                  | User-provided                            |
| `portal_aap_oauth_client_secret`    | `AAP_OAUTH_CLIENT_SECRET`    | User-provided                            |
| `portal_github_token`               | `GITHUB_TOKEN`               | Optional                                 |
| `portal_gitlab_token`               | `GITLAB_TOKEN`               | Optional                                 |
| `portal_github_app_id`              | `GITHUB_APP_ID`              | User-provided (EE Builder, GitHub App)   |
| `portal_github_app_client_id`       | `GITHUB_APP_CLIENT_ID`       | User-provided (EE Builder, GitHub App)   |
| `portal_github_app_client_secret`   | `GITHUB_APP_CLIENT_SECRET`   | User-provided (EE Builder, GitHub App)   |
| `portal_github_app_private_key`     | `GITHUB_APP_PRIVATE_KEY`     | User-provided (EE Builder, GitHub App)   |
| `portal_github_oauth_client_id`     | `GITHUB_OAUTH_CLIENT_ID`     | User-provided (EE Builder, GitHub OAuth) |
| `portal_github_oauth_client_secret` | `GITHUB_OAUTH_CLIENT_SECRET` | User-provided (EE Builder, GitHub OAuth) |
| `portal_gitlab_oauth_client_id`     | `GITLAB_OAUTH_CLIENT_ID`     | User-provided (EE Builder, GitLab OAuth) |
| `portal_gitlab_oauth_client_secret` | `GITLAB_OAUTH_CLIENT_SECRET` | User-provided (EE Builder, GitLab OAuth) |


Note:

EE Builder secrets (prefixed with `portal_github_app_`, `portal_github_oauth_`, or `portal_gitlab_oauth_`) require a Quadlet drop-in file (`ee-builder-secrets.conf`) to map Podman secrets to container environment variables. See the Configuring execution environment builder guide for instructions.

Important:

The `portal-backup` utility does not capture EE Builder secrets or custom Quadlet drop-in files. Store secret values and the contents of `ee-builder-secrets.conf` in a secure external location.

**Listing secrets**

```terminal
sudo podman secret ls
```
**Updating a secret**

To update a secret value, write the new value to a temporary file on tmpfs to avoid exposing it in the process list, then replace the secret:

```terminal
temp_file=$(mktemp -p /dev/shm) && chmod 600 "$temp_file"
printf '%s' "*new_token_value*" > "$temp_file"
sudo podman secret create --replace portal_aap_token "$temp_file"
rm -f "$temp_file"
sudo systemctl restart portal
```

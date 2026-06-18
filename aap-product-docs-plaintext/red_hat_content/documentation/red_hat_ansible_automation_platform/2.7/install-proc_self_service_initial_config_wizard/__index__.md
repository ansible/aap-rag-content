# Configure the appliance at first boot

Provide initial configuration for the Ansible automation portal appliance so that portal services can start and connect to Ansible Automation Platform.

You must supply SSH keys and portal settings through one of the supported configuration methods during or before deployment.

## Prerequisites

- The Ansible Automation Platform OAuth application Client ID and Client Secret.
- The Ansible Automation Platform admin token.
- An SSH public key for administrative access.
- The URL of your Ansible Automation Platform instance.

## Using cloud-init user-data

Use this method for Red Hat OpenShift Virtualization, cloud, and KVM/QEMU deployments.

1. Create a cloud-init user-data file:

```yaml
#cloud-config
users:
- name: admin
groups: sudo
ssh_authorized_keys:
- <your_ssh_public_key>

aap:
host_url: https://<aap_host>
token: <aap_admin_token>
oauth:
client_id: <oauth_client_id>
client_secret: <oauth_client_secret>
check_ssl: true

database:
type: builtin
```
Replace the placeholder values with your Ansible Automation Platform credentials and SSH public key.

The appliance parses the custom `aap` and `database` fields directly from the cloud-init user-data at first boot.

The following additional fields are available for cloud-init configuration:

- `network.base_url` -- Set the user-accessible URL (auto-detected from the VM IP address if not specified). Set this when users access Ansible automation portal through a hostname, route, or load balancer.
- `network.port` -- Set the HTTPS port (default: 443).
- `security.backend_secret` -- Set the backend authentication secret (`auto` generates a random value).
- `database.builtin.password` and `database.builtin.admin_password` -- Set built-in database passwords (`auto` generates random values).
- `database.external.*` -- Configure an external PostgreSQL database (`host`, `port`, `name`, `user`, `password`, `ssl`). The database user requires the `CREATEDB` privilege.
- `integrations.github.url`, `integrations.github.token` -- Configure GitHub integration (URL defaults to `github.com`).
- `integrations.gitlab.url`, `integrations.gitlab.token` -- Configure GitLab integration (URL defaults to `gitlab.com`).
- `backup.enabled`, `backup.schedule`, `backup.retention_days` -- Configure automated backups.

2. Provide the user-data file during deployment:
- For Red Hat OpenShift Virtualization, add a `cloudInitNoCloud` volume to the `VirtualMachine` manifest.
- For cloud providers (AWS, GCP, Azure), pass the user-data through the instance launch configuration.
- For local KVM/QEMU, create a cloud-init ISO or use the `-smbios` option to pass user-data.

## Using VMware guestinfo properties

Use this method for VMware vSphere deployments.

1. Set the following `guestinfo` properties on the virtual machine in vSphere:

```terminal
guestinfo.portal.ssh_public_key = "<your_ssh_public_key>"
guestinfo.portal.config = "<base64_encoded_config_yaml>"
```
Where `<base64_encoded_config_yaml>` is the Base64-encoded content of your portal configuration YAML.

2. Power on the virtual machine. The appliance detects and applies the `guestinfo` properties on first boot.

## Using a pre-seeded configuration file

Use this method for automated deployments with Ansible or Terraform.

1. Place a YAML configuration file at `/etc/portal/config.yaml` on the appliance disk image before first boot:

```yaml
aap:
host_url: https://<aap_host>
token: <aap_admin_token>
oauth:
client_id: <oauth_client_id>
client_secret: <oauth_client_secret>
database:
type: builtin
```

2. Boot the appliance. The first-boot service detects and applies the configuration automatically.

## Configure after deployment

If you deployed the appliance without providing configuration, portal services do not start. You can configure the appliance after deployment by editing the configuration files directly.

1. SSH into the appliance using the key you provided through cloud-init or another method.
2. Edit the application configuration file:

```terminal
$ sudo vi /etc/portal/configs/app-config/app-config.production.yaml
```

3. Restart the portal service:

```terminal
$ sudo systemctl restart portal
```

## Verification

- Verify that portal services are running:

```terminal
$ sudo ansible-portal status
```

- Access the portal URL from your browser.
- Log in using your Ansible Automation Platform credentials.

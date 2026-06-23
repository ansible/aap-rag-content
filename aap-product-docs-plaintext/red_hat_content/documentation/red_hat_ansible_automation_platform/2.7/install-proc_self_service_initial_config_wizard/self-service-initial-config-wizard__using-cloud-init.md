# Configure the appliance at first boot
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


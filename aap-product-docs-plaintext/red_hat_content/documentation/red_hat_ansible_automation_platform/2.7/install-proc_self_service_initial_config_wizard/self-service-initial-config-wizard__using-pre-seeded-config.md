# Configure the appliance at first boot
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


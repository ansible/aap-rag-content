---
title: "Authentication Guide — mycompany.infrastructure"
url: "https://github.com/ansible/aap-rag-content/blob/main/byok/ansible-collection-docs/guides/authentication.md"
---
# Authentication Guide — mycompany.infrastructure

**Collection:** mycompany.infrastructure

---

## Overview

All modules and plugins in the `mycompany.infrastructure` collection authenticate to cloud provider APIs through the **MyCompany API Gateway**, which acts as a centralised authentication proxy. Only a single gateway token is required — you do not need to configure provider-specific credentials on every control node.

For environments where direct provider SDK access is preferred (local development, CI pipelines with provider credentials already configured), the collection also supports native SDK authentication as a fallback.

---

## Authentication Methods

### MyCompany API Gateway Token (Recommended)

A short-lived token issued by the MyCompany identity platform. Pass it via the `auth_token` parameter or the `MYCOMPANY_AUTH_TOKEN` environment variable.

**Obtain a token:**

```bash
mycompany-cli auth login --environment production
```

The CLI writes the token to `~/.mycompany/credentials`, where it is picked up automatically. Tokens expire after 8 hours.

**Configuration priority (lowest to highest):**

1. `~/.mycompany/credentials` file
2. `MYCOMPANY_AUTH_TOKEN` environment variable
3. `auth_token` task parameter

---

### AWS IAM / Instance Profiles

When running on AWS without a gateway token, the collection falls back to the standard boto3 credential chain:

1. Environment variables (`AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`)
2. AWS profile (`~/.aws/credentials`)
3. EC2 Instance Profile / ECS Task Role

No additional configuration is needed when running on EC2 with an appropriate IAM role attached.

---

### Azure Managed Identity

On Azure VMs or Azure DevOps agents, the collection uses the Azure managed identity (system-assigned or user-assigned) automatically via the `azure-mgmt-*` SDK credential chain.

Set `AZURE_USE_MSI=true` to force managed identity use when multiple credential sources are available.

---

### GCP Workload Identity / Service Account

On GCP Compute Engine instances, Application Default Credentials (ADC) are used automatically.

**Configure ADC on the control node:**

```bash
gcloud auth application-default login
```

For CI/CD pipelines, set `GOOGLE_APPLICATION_CREDENTIALS` to the path of a service account JSON key file.

---

### VMware vSphere

For VMware targets, provide credentials directly via environment variables:

| Variable | Description |
|---|---|
| `VMWARE_HOST` | vCenter hostname |
| `VMWARE_USER` | vCenter username |
| `VMWARE_PASSWORD` | vCenter password (**use Vault — see below**) |

---

## Vault Integration

All authentication secrets (tokens, service account keys, passwords) should be stored in HashiCorp Vault and retrieved at runtime using the [vault_secret lookup](../lookup/vault_secret.md).

```yaml
vars:
  mycompany_auth_token: >-
    {{ lookup('mycompany.infrastructure.vault_secret',
              'secret/ansible/gateway_token',
              field='value') }}
```

---

## Configuring the Collection via ansible.cfg

Global defaults can be set in `ansible.cfg` under the `[mycompany_infrastructure]` section:

```ini
[mycompany_infrastructure]
vault_url = https://vault.mycompany.example
vault_auth_method = approle
config_service_url = https://config.mycompany.example/api/v1
default_region = us-east-1
default_environment = production
```

These values are overridden by environment variables, which are in turn overridden by task-level parameters.

---

## Troubleshooting

| Error | Cause | Resolution |
|---|---|---|
| `Authentication token expired` | The gateway token has exceeded its 8-hour TTL. | Run `mycompany-cli auth login` to refresh. |
| `No credentials found for provider 'aws'` | No IAM role, profile, or env vars are configured. | Attach an IAM role, configure `~/.aws/credentials`, or set `AWS_ACCESS_KEY_ID`/`AWS_SECRET_ACCESS_KEY`. |
| `Unable to reach MyCompany API gateway` | The control node cannot reach the gateway endpoint. | Verify firewall rules and proxy settings from the control node. |

---

## See Also

- [vault_secret lookup](../lookup/vault_secret.md) — Retrieve secrets from Vault for use as authentication credentials.
- [config_value lookup](../lookup/config_value.md) — Look up gateway URLs and other non-secret configuration values.
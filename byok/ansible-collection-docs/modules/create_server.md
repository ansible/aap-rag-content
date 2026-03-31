---
title: "Module: mycompany.infrastructure.create_server"
url: "https://github.com/ansible/aap-rag-content/blob/main/byok/ansible-collection-docs/modules/create_server.md"
---
# Module: mycompany.infrastructure.create_server

**Short description:** Create or update a virtual server instance
**Collection:** mycompany.infrastructure
**Version added:** 1.0.0

---

## Synopsis

- Creates a new virtual server instance on the specified cloud provider or VMware environment.
- If a server with the given `name` already exists in the target `region` and `project`, it will be updated to match the desired state unless `state=absent`.
- Supports AWS EC2, Azure Virtual Machines, GCP Compute Engine, and VMware vSphere.
- Returns server metadata including instance ID, private IP, public IP, and status.

---

## Requirements

The following must be installed on the host executing this module:

- python >= 3.9
- boto3 >= 1.26 *(for `provider=aws`)*
- azure-mgmt-compute >= 29.0 *(for `provider=azure`)*
- google-cloud-compute >= 1.14 *(for `provider=gcp`)*
- pyvmomi >= 7.0 *(for `provider=vmware`)*
- requests >= 2.28

---

## Parameters

| Parameter | Type | Required | Default | Choices | Description |
|---|---|---|---|---|---|
| `name` | string | yes | | | Name of the server instance. Must be unique within the project and region. Must match `^[a-z][a-z0-9\-]{1,62}$`. |
| `provider` | string | yes | | `aws`, `azure`, `gcp`, `vmware` | Cloud or virtualization provider to use. |
| `state` | string | no | `present` | `present`, `absent`, `stopped`, `running` | Desired state of the server instance. |
| `instance_type` | string | no | `t3.medium` (AWS) | | Instance type or VM size. AWS: e.g. `t3.medium`. Azure: e.g. `Standard_D2s_v3`. GCP: e.g. `n2-standard-2`. Ignored for VMware (use `cpu_count` and `memory_mb`). |
| `image` | string | no | `rhel-9-latest` | | OS image or AMI ID. AWS: AMI ID or alias (e.g. `rhel-9-latest`). Azure and GCP: image alias or full reference. |
| `region` | string | no | | | Cloud region. Falls back to `MYCOMPANY_REGION` env var, then `~/.mycompany/config`. |
| `project` | string | no | | | Project or account under which to create the server. Falls back to `MYCOMPANY_PROJECT` env var. |
| `tags` | dictionary | no | `{}` | | Key/value tags to apply to the instance. Tags are merged with existing tags. *(Added in 1.1.0)* |
| `purge_tags` | boolean | no | `false` | `true`, `false` | When `true`, tags not listed in `tags` are removed from the instance. *(Added in 1.1.0)* |
| `wait` | boolean | no | `true` | `true`, `false` | Whether to wait for the server to reach the desired state before returning. |
| `wait_timeout` | integer | no | `300` | | Maximum seconds to wait for the instance to reach the desired state. |
| `auth_token` | string | no | | | Authentication token for the MyCompany API gateway. Falls back to SDK credentials (IAM roles, managed identities). **no_log.** Env var: `MYCOMPANY_AUTH_TOKEN`. |

---

## Attributes

| Attribute | Support | Description |
|---|---|---|
| check_mode | full | Runs without making any changes; reports what would change. |
| diff_mode | full | Returns before/after comparison when changes are made. |
| platform | all | No target OS restrictions. |

---

## Notes

- The module uses the MyCompany API gateway for all provider operations. Ensure the gateway URL is reachable from the Ansible control node.
- When using `state=absent`, any attached disks **not** marked as `delete_on_termination` will be retained.
- For VMware environments, `pyvmomi` must be installed and the vCenter hostname must be resolvable from the control node.
- Idempotency is guaranteed for all operations except `state=running` and `state=stopped` when the instance is already in that state.

---

## See Also

- [configure_network](configure_network.md) — Configure the VPC and subnet before creating servers.
- [deploy_application](deploy_application.md) — Deploy applications on servers created with this module.
- [dynamic_cloud inventory](../inventory/dynamic_cloud.md) — Dynamically discover server instances for use in playbooks.

---

## Examples

```yaml
# Create a minimal RHEL 9 instance on AWS
- name: Create web server on AWS
  mycompany.infrastructure.create_server:
    name: web-prod-01
    provider: aws
    region: us-east-1
    project: myapp-production
    instance_type: t3.medium
    image: rhel-9-latest
    state: present
  register: server_result

# Create a server with custom tags, wait up to 10 minutes
- name: Create tagged application server
  mycompany.infrastructure.create_server:
    name: app-staging-02
    provider: gcp
    region: us-central1
    project: myapp-staging
    instance_type: n2-standard-4
    image: rhel-9-latest
    tags:
      environment: staging
      team: platform
      cost-center: "1234"
    purge_tags: true
    wait: true
    wait_timeout: 600
    state: present

# Stop a running instance
- name: Stop server during maintenance window
  mycompany.infrastructure.create_server:
    name: app-staging-02
    provider: gcp
    region: us-central1
    project: myapp-staging
    state: stopped

# Delete a server
- name: Decommission old server
  mycompany.infrastructure.create_server:
    name: legacy-server-01
    provider: aws
    region: us-east-1
    project: myapp-production
    state: absent

# Create Azure VM using auth token from Vault
- name: Create Azure VM with explicit token
  mycompany.infrastructure.create_server:
    name: api-prod-az-01
    provider: azure
    region: eastus
    project: myapp-prod-rg
    instance_type: Standard_D4s_v4
    image: rhel-9-latest
    auth_token: "{{ lookup('mycompany.infrastructure.vault_secret', 'secret/azure/token') }}"
    state: present
```

---

## Return Values

| Key | Description | Returned | Type |
|---|---|---|---|
| `server` | Dictionary describing the server instance. | when `state != absent` | dict |
| `server.instance_id` | Provider-assigned ID of the instance. | always | string — e.g. `"i-0a1b2c3d4e5f67890"` |
| `server.name` | Name of the instance. | always | string — e.g. `"web-prod-01"` |
| `server.state` | Current state of the instance. | always | string — e.g. `"running"` |
| `server.private_ip` | Private IPv4 address assigned to the instance. | always | string — e.g. `"10.0.1.42"` |
| `server.public_ip` | Public IPv4 address, if assigned. | when a public IP is configured | string — e.g. `"54.201.10.5"` |
| `server.region` | Region where the instance was created. | always | string — e.g. `"us-east-1"` |
| `server.provider` | Provider managing this instance. | always | string — e.g. `"aws"` |
| `server.tags` | Tags currently applied to the instance. | always | dict — e.g. `{"environment": "staging"}` |
| `changed` | Whether the module made any changes. | always | bool |

---

## Authors

- Alice Nguyen (@alice-n) — alice.nguyen@mycompany.example
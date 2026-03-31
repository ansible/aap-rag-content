---
title: "Inventory Plugin: mycompany.infrastructure.dynamic_cloud"
url: "https://github.com/ansible/aap-rag-content/blob/main/byok/ansible-collection-docs/inventory/dynamic_cloud.md"
---
# Inventory Plugin: mycompany.infrastructure.dynamic_cloud

**Short description:** Build a dynamic inventory from multi-cloud provider APIs
**Collection:** mycompany.infrastructure
**Version added:** 1.0.0

---

## Synopsis

- Generates a dynamic Ansible inventory by querying AWS EC2, Azure Virtual Machines, GCP Compute Engine, and/or VMware vSphere for running instances.
- Groups hosts automatically by provider, region, environment tag, and team tag.
- Supports filtering instances by tag key-value pairs, instance state, and region.
- Cache-friendly: results are cached locally for a configurable TTL to reduce API calls during repeated inventory runs.

---

## Requirements

The following must be installed on the host executing this inventory plugin:

- python >= 3.9
- boto3 >= 1.26 *(for `providers` including `aws`)*
- azure-mgmt-compute >= 29.0 *(for `providers` including `azure`)*
- google-cloud-compute >= 1.14 *(for `providers` including `gcp`)*
- pyvmomi >= 7.0 *(for `providers` including `vmware`)*
- requests >= 2.28

---

## Parameters

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| `plugin` | string | yes | | Must be `mycompany.infrastructure.dynamic_cloud`. Identifies this file as a source for this plugin. |
| `providers` | list of strings | no | `["aws", "azure", "gcp"]` | Cloud providers to query. Choices: `aws`, `azure`, `gcp`, `vmware`. |
| `regions` | list of strings | no | `[]` (all regions) | Restrict inventory to the specified regions. |
| `filters` | dictionary | no | `{}` | Tag-based filters. Only instances matching **all** specified tag key-value pairs are included. |
| `instance_states` | list of strings | no | `["running"]` | Only include instances in the specified states. |
| `hostnames` | list of strings | no | `["private_dns", "private_ip"]` | Priority list of attributes to use as the Ansible hostname. First non-empty attribute wins. Choices per element: `private_ip`, `public_ip`, `private_dns`, `public_dns`, `name`. |
| `compose` | dictionary | no | `{}` | Create additional host variables using Jinja2 expressions evaluated against each instance's attributes. |
| `groups` | dictionary | no | `{}` | Add hosts to additional groups based on Jinja2 expressions that evaluate to truthy. Keys are group names; values are expressions. |
| `cache` | boolean | no | `true` | Enable caching of inventory results. Config: INI `[inventory] cache`, env `ANSIBLE_INVENTORY_CACHE`. |
| `cache_timeout` | integer | no | `300` | Cache TTL in seconds. Config: INI `[inventory] cache_timeout`, env `ANSIBLE_INVENTORY_CACHE_TIMEOUT`. |
| `cache_plugin` | string | no | `ansible.builtin.jsonfile` | Cache backend plugin. Config: INI `[inventory] cache_plugin`, env `ANSIBLE_INVENTORY_CACHE_PLUGIN`. |

---

## Automatic Groups

The plugin creates the following groups automatically for every discovered instance:

| Group name | Members |
|---|---|
| `all` | All discovered instances |
| `provider_<name>` | Instances per provider — e.g. `provider_aws`, `provider_gcp` |
| `region_<name>` | Instances per region — e.g. `region_us_east_1` |
| `env_<value>` | Instances grouped by the `environment` tag value |
| `team_<value>` | Instances grouped by the `team` tag value |

---

## Notes

- Provider credentials are picked up from the standard SDK credential chain (AWS profiles/IAM roles, Azure managed identity/env vars, GCP workload identity/ADC). No explicit credential parameters are needed when running on cloud infrastructure with appropriate roles attached.
- The `compose` and `groups` keys use the same Jinja2 expression evaluation as `ansible.builtin.constructed`.
- To exclude instances without filtering them entirely, use `groups` to add them to a known group, then limit runs with `--limit`.

---

## Configuration File

The plugin is activated by creating a YAML inventory source file whose name matches the pattern `*.mycompany_cloud.yml` or `*.mycompany_cloud.yaml`.

---

## See Also

- [create_server module](../modules/create_server.md) — Create the server instances this plugin discovers.
- [extract_tags filter](../filter/infrastructure_filters.md#extract_tags) — Post-process tag data from inventory host variables.

---

## Examples

```yaml
# production.mycompany_cloud.yml
plugin: mycompany.infrastructure.dynamic_cloud

providers:
  - aws
  - gcp

regions:
  - us-east-1
  - us-central1

filters:
  environment: production

instance_states:
  - running

hostnames:
  - private_dns
  - private_ip

compose:
  ansible_host: private_ip
  ansible_user: "'ec2-user' if provider == 'aws' else 'gcp-user'"

groups:
  web_servers: "'web' in name"
  db_servers: "'db' in name or tags.get('role') == 'database'"

cache: true
cache_timeout: 600
```

```yaml
# staging_all_clouds.mycompany_cloud.yml
plugin: mycompany.infrastructure.dynamic_cloud

providers:
  - aws
  - azure
  - gcp
  - vmware

filters:
  environment: staging
  team: platform

hostnames:
  - private_ip

compose:
  ansible_host: private_ip
  cloud_provider: provider
  cloud_region: region
```

---

## Authors

- Bob Ramirez (@bob-r) — bob.ramirez@mycompany.example
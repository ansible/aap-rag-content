---
title: "Filter Plugins: mycompany.infrastructure"
url: "https://github.com/ansible/aap-rag-content/blob/main/byok/ansible-collection-docs/filter/infrastructure_filters.md"
---
# Filter Plugins: mycompany.infrastructure

**Collection:** mycompany.infrastructure
**Version added:** 1.1.0

This document covers all filter plugins provided by the `mycompany.infrastructure` collection. Filters are available automatically once the collection is installed and require no additional imports.

---

## Filter: to_cidr

**Short description:** Convert an IP address and prefix length to CIDR notation
**Version added:** 1.1.0

### Description

Converts a combination of an IP address and a prefix length (or subnet mask) into standard CIDR notation. Useful when building network configuration from data sources that store the address and mask as separate fields.

### Input

| Argument | Type | Required | Description |
|---|---|---|---|
| `ip` | string | yes | IPv4 or IPv6 address (pipe input). |
| `prefix` | integer or string | yes | Prefix length (e.g. `24`) or dotted-decimal subnet mask (e.g. `"255.255.255.0"`). |

### Returns

- **string** — CIDR notation, e.g. `"10.0.1.0/24"`.

### Raises

- `AnsibleFilterError` if the IP is invalid, the prefix is out of range, or the IP and mask combination is not a valid network address.

### Examples

```yaml
# Basic usage with prefix length
- name: Build CIDR from separate fields
  ansible.builtin.set_fact:
    subnet_cidr: "{{ '10.0.1.0' | mycompany.infrastructure.to_cidr(24) }}"
# Result: "10.0.1.0/24"

# Using a dotted-decimal subnet mask
- name: Convert subnet mask to CIDR
  ansible.builtin.set_fact:
    cidr: "{{ network_address | mycompany.infrastructure.to_cidr(subnet_mask) }}"
# Where network_address="192.168.10.0", subnet_mask="255.255.255.128"
# Result: "192.168.10.0/25"

# Build subnet CIDRs from a list of raw data
- name: Build subnet CIDRs from inventory data
  ansible.builtin.set_fact:
    subnet_cidrs: "{{ subnet_cidrs | default([]) + [item.ip | mycompany.infrastructure.to_cidr(item.prefix)] }}"
  loop: "{{ raw_subnets }}"
```

---

## Filter: parse_json_string

**Short description:** Parse a JSON string and return a Python object
**Version added:** 1.1.0

### Description

Deserialises a JSON-encoded string into the corresponding Python object (dict, list, string, integer, boolean, or null). Useful when an API or config service returns structured data as a JSON string rather than a native object.

### Input

| Argument | Type | Required | Description |
|---|---|---|---|
| `value` | string | yes | A valid JSON-encoded string (pipe input). |
| `default` | any | no | Value to return if parsing fails or the input is empty. If not specified, a parse error raises an `AnsibleFilterError`. |

### Returns

- **any** — The deserialised Python object.

### Examples

```yaml
# Parse a JSON object string
- name: Parse API response
  ansible.builtin.set_fact:
    config_obj: "{{ raw_json_string | mycompany.infrastructure.parse_json_string }}"
# Where raw_json_string='{"max_retries": 3, "timeout": 30}'
# Result: {"max_retries": 3, "timeout": 30}

# Parse a JSON array string
- name: Parse allowed IPs list
  ansible.builtin.set_fact:
    allowed_ips: "{{ ip_list_json | mycompany.infrastructure.parse_json_string }}"
# Where ip_list_json='["10.0.0.1","10.0.0.2"]'
# Result: ["10.0.0.1", "10.0.0.2"]

# Use default value on empty input
- name: Parse with fallback default
  ansible.builtin.set_fact:
    feature_config: "{{ maybe_empty | mycompany.infrastructure.parse_json_string(default={}) }}"

# Combine with config_value lookup
- name: Parse JSON config from config service
  ansible.builtin.set_fact:
    rate_limits: >-
      {{ lookup('mycompany.infrastructure.config_value', 'myapp.rate_limits')
         | mycompany.infrastructure.parse_json_string }}
```

---

## Filter: extract_tags

**Short description:** Extract key-value tag pairs from a resource object
**Version added:** 1.2.0

### Description

Extracts the `tags` dictionary from a resource object returned by a cloud provider module, and optionally filters or renames keys. Normalises tag structures across providers, which return tags in different formats — AWS returns a list of `{Key, Value}` dicts; GCP and Azure return a plain dict.

### Input

| Argument | Type | Required | Description |
|---|---|---|---|
| `resource` | dict | yes | A resource object as returned by a module (e.g. the `server` dict from `create_server`). Pipe input. |
| `keys` | list of strings | no | Return only the tags whose keys are in this list. All tags are returned when omitted. |
| `prefix` | string | no | Return only tags whose keys start with this prefix. The prefix is stripped from the returned keys. |
| `normalize` | boolean | no (default `true`) | Normalise tag key casing to lowercase and replace spaces/hyphens with underscores. |

### Returns

- **dict** — A plain `{key: value}` dictionary of the extracted (and optionally filtered) tags.

### Notes

- AWS resources return tags as a list of `{"Key": ..., "Value": ...}` dicts. The `extract_tags` filter handles this format automatically, converting to a plain dict before applying filters.
- Keys that collide after normalisation (e.g. `"My-Tag"` and `"my_tag"`) are merged, with the last value winning. Use `normalize=false` if key uniqueness cannot be guaranteed.

### Examples

```yaml
# Extract all tags from a server resource
- name: Get server tags
  ansible.builtin.set_fact:
    server_tags: "{{ server_result.server | mycompany.infrastructure.extract_tags }}"
# Result: {"environment": "production", "team": "platform", "cost_center": "1234"}

# Extract only specific tag keys
- name: Get environment and team tags only
  ansible.builtin.set_fact:
    meta_tags: "{{ server_result.server | mycompany.infrastructure.extract_tags(keys=['environment', 'team']) }}"
# Result: {"environment": "production", "team": "platform"}

# Extract tags with a common prefix, stripping the prefix from returned keys
- name: Extract billing tags
  ansible.builtin.set_fact:
    billing_tags: "{{ db_result.database | mycompany.infrastructure.extract_tags(prefix='billing/') }}"
# Where tags include "billing/cost-center": "1234" and "billing/project": "myapp"
# Result: {"cost_center": "1234", "project": "myapp"}

# Preserve original key casing
- name: Extract tags without normalisation
  ansible.builtin.set_fact:
    raw_tags: "{{ server_result.server | mycompany.infrastructure.extract_tags(normalize=false) }}"
```

---

## See Also

- [create_server module](../modules/create_server.md) — Source of `server` resource objects processed by `extract_tags`.
- [configure_network module](../modules/configure_network.md) — Provides `network` resource objects that also contain tag structures.
- [config_value lookup](../lookup/config_value.md) — Combine with `parse_json_string` to decode JSON config values.

---

## Authors

- Alice Nguyen (@alice-n) — alice.nguyen@mycompany.example
- Bob Ramirez (@bob-r) — bob.ramirez@mycompany.example
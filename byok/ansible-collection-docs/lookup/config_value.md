---
title: "Lookup Plugin: mycompany.infrastructure.config_value"
url: "https://github.com/ansible/aap-rag-content/blob/main/byok/ansible-collection-docs/lookup/config_value.md"
---
# Lookup Plugin: mycompany.infrastructure.config_value

**Short description:** Look up configuration values from the internal config service
**Collection:** mycompany.infrastructure
**Version added:** 1.1.0

---

## Synopsis

- Retrieves non-secret configuration values (feature flags, service endpoints, capacity settings, environment-specific parameters) from the MyCompany central configuration service.
- Supports hierarchical key lookup with environment and region overrides.
- Values returned are strings by default; use `convert_type` to automatically coerce values to integers, booleans, or JSON-parsed objects.
- Results are cached per play to avoid redundant API calls.

---

## Requirements

The following must be installed on the host executing this lookup:

- python >= 3.9
- requests >= 2.28

---

## Parameters

| Parameter | Type | Required | Default | Choices | Description |
|---|---|---|---|---|---|
| `_terms` | list of strings | yes | | | One or more dot-separated configuration key paths (e.g. `myapp.api.max_connections`). |
| `environment` | string | no | `production` | `development`, `staging`, `production` | Environment context. Environment-specific values override global defaults. Env `MYCOMPANY_ENVIRONMENT`, var `mycompany_environment`. |
| `region` | string | no | | | Region context. Region-specific values override environment-level values. Env `MYCOMPANY_REGION`, var `mycompany_region`. |
| `convert_type` | string | no | `string` | `string`, `int`, `bool`, `json` | Automatically convert the returned string value to the specified type. `json` parses the value as JSON and returns the resulting object. |
| `default` | any | no | | | Fallback value when the key does not exist. If not specified and the key is missing, the lookup raises an error. |
| `url` | string | no | `$MYCOMPANY_CONFIG_URL` | | URL of the MyCompany config service API. Config: INI `[mycompany_infrastructure] config_service_url`, env `MYCOMPANY_CONFIG_URL`, var `mycompany_config_url`. |
| `auth_token` | string | no | | | Bearer token for authenticating to the config service API. Falls back to Ansible controller credentials. **no_log.** Env `MYCOMPANY_AUTH_TOKEN`, var `mycompany_auth_token`. |

---

## Notes

- Results are cached for the duration of the play. To force a fresh fetch, set `MYCOMPANY_CONFIG_CACHE=0` in the environment.
- The lookup respects the configuration hierarchy: **global → environment → region**. The most specific value wins.
- Boolean conversion treats `"true"`, `"yes"`, `"1"` (case-insensitive) as `True`; all other values are `False`.

> **Configuration priority (lowest to highest):** global default → environment → region → task parameter.

---

## See Also

- [vault_secret lookup](vault_secret.md) — Retrieve sensitive secrets rather than plain configuration values.

---

## Examples

```yaml
# Retrieve a string value with environment context
- name: Get API endpoint
  ansible.builtin.set_fact:
    api_url: "{{ lookup('mycompany.infrastructure.config_value',
                        'myapp.api.endpoint',
                        environment='production') }}"

# Retrieve an integer value with a fallback default
- name: Get max DB connections
  ansible.builtin.set_fact:
    max_conn: "{{ lookup('mycompany.infrastructure.config_value',
                         'myapp.database.max_connections',
                         convert_type='int',
                         default=50) }}"

# Retrieve a feature flag as a boolean
- name: Check feature flag
  ansible.builtin.set_fact:
    new_ui_enabled: "{{ lookup('mycompany.infrastructure.config_value',
                              'myapp.features.new_ui',
                              convert_type='bool',
                              environment='staging') }}"

# Retrieve a JSON-parsed configuration object
- name: Get rate limiting config
  ansible.builtin.set_fact:
    rate_limits: "{{ lookup('mycompany.infrastructure.config_value',
                            'myapp.rate_limits',
                            convert_type='json',
                            environment='production',
                            region='us-east-1') }}"

# Use directly in a task variable
- name: Configure worker count from config service
  ansible.builtin.template:
    src: worker.conf.j2
    dest: /etc/myapp/worker.conf
  vars:
    worker_count: "{{ lookup('mycompany.infrastructure.config_value',
                             'myapp.worker.count',
                             convert_type='int') }}"
```

---

## Return Values

| Key | Description | Returned | Type |
|---|---|---|---|
| `_raw` | The configuration value(s). Type depends on `convert_type`: string (default), int, bool, or JSON-parsed object. A list when multiple keys are passed. | success | any — e.g. `"https://api.mycompany.example/v2"` |

---

## Authors

- Bob Ramirez (@bob-r) — bob.ramirez@mycompany.example
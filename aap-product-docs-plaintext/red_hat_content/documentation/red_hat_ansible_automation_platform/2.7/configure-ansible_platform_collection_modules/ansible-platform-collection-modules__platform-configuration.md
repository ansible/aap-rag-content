# Modules in the ansible.platform collection
## Platform configuration

| Module         | Description                                                                                                                                                                                                                                                                                       | Supported states                  |
| -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------- |
| `settings`     | Modify platform-wide settings including token authentication, JWT configuration, password policies, and session settings. This module has no`state` parameter and always applies changes. To get a full list of available setting keys for your environment, query the platform gateway REST API. | N/A (always applies)              |
| `feature_flag` | Query and manage feature flags. Only run-time flags can be modified; install-time flags are read-only. This module defaults to`exists` instead of`present`, so you must explicitly set`state: present` to modify a flag.                                                                          | present, absent, exists, enforced |


The `settings` module requires a dictionary of setting keys and values, but the full list of available keys depends on your Ansible Automation Platform deployment. To discover all available setting keys and their current values, query the following REST API endpoint on your platform gateway:

`https://*aap-host*/api/gateway/v1/settings/all/`


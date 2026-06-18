# Manage feature flags

Feature flags help you to manage your users’ experiences at a granular level by controlling access to Technology Preview and Developer Preview features in Ansible Automation Platform.

Use feature flags to enable or disable specific platform features without requiring a reinstallation or restart of Ansible Automation Platform.

The Feature Flags page in the Ansible Automation Platform user interface (UI) displays all public feature flags that are currently enabled. Runtime feature flags can be managed from the UI, while install-time feature flags are read-only from the UI.

Note:

The `RUNTIME_FEATURE_FLAGS` parameter is set to `True` by default.

Configure feature flags in your inventory file during installation. To make feature flag information visible in the UI, the parameter`RUNTIME_FEATURE_FLAGS` must be set to `True`.

If you do not want feature flag information to be visible in the UI to users, set the `RUNTIME_FEATURE_FLAGS` parameter to `False`.

In a containerized installation, the parameter in your inventory file looks like this:

```
## Enables runtime feature flags (Default: True)
gateway_extra_settings=[{"setting": "RUNTIME_FEATURE_FLAGS", "value": 'True'}]
```

In an OpenShift Container Platform deployment, your Ansible Automation Platform Operator configuration looks like this:

```
extra_settings: ## Enables runtime feature flags (Default: True) - setting: RUNTIME_FEATURE_FLAGS value: 'True'
```

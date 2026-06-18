+++
title = "Manage feature flags - Red Hat Ansible Automation Platform 2.7"
template = "docs/aem-title.html"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/configure-manage_feature_flags"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/configure-assembly_gw_settings/", "Configure Ansible Automation Platform"]]
category = "Configure"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/configure-manage_feature_flags/aem-page/configure-manage_feature_flags.html"
last_crumb = "Manage feature flags"
modified = "2026-06-05T07:48:10.594Z"
multi_page_path = ""
name = "Manage feature flags"
oversized = "false"
page_slug = "configure-manage_feature_flags"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/configure-manage_feature_flags"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/configure-manage_feature_flags/toc/toc.json"
type = "aem-page"
+++

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

+++
template = "docs/aem-title.html"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-configure_feature_flags_for_a_containerized_installation"
title = "Configure feature flags for a containerized installation - Red Hat Ansible Automation Platform 2.7"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-con_aap_containerized_installation_intro/", "Install containerized Ansible Automation Platform"]]
category = "Install"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/install-configure_feature_flags_for_a_containerized_installation/aem-page/install-configure_feature_flags_for_a_containerized_installation.html"
last_crumb = "Configure feature flags for a containerized installation"
modified = "2026-06-05T07:48:10.594Z"
multi_page_path = ""
name = "Configure feature flags for a containerized installation"
oversized = "false"
page_slug = "install-configure_feature_flags_for_a_containerized_installation"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/install-configure_feature_flags_for_a_containerized_installation"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/install-configure_feature_flags_for_a_containerized_installation/toc/toc.json"
type = "aem-page"
+++

# Configure feature flags for a containerized installation

Turn on the feature flags capability for your containerized installation.

## Procedure

 To enable the feature flags UI page, add the `RUNTIME_FEATURE_FLAGS` setting to `gateway_extra_settings` in your inventory file:

```
gateway_extra_settings=[{"setting": "RUNTIME_FEATURE_FLAGS", "value": "@bool True"}]
```

To lock specific feature flags at install time, add a `feature_flags` block, as in the following example, to your inventory file. Flags set at install time are read-only and cannot be changed at runtime.

```
feature_flags:
   FEATURE_EDA_ANALYTICS_ENABLED: True
   FEATURE_POLICY_AS_CODE_ENABLED: True
```

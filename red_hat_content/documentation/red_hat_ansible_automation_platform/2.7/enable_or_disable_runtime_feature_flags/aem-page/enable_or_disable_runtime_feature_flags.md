+++
title = "Enable or disable runtime feature flags - Red Hat Ansible Automation Platform 2.7"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/enable_or_disable_runtime_feature_flags"
template = "docs/aem-title.html"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"]]
category = ""
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/enable_or_disable_runtime_feature_flags/aem-page/enable_or_disable_runtime_feature_flags.html"
last_crumb = "Enable or disable runtime feature flags"
modified = "2026-06-05T07:48:10.594Z"
multi_page_path = ""
name = "Enable or disable runtime feature flags"
oversized = "false"
page_slug = "enable_or_disable_runtime_feature_flags"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/enable_or_disable_runtime_feature_flags"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/enable_or_disable_runtime_feature_flags/toc/toc.json"
type = "aem-page"
+++

# Enable or disable runtime feature flags

Runtime feature flags can be enabled or disabled from the UI.

## Before you begin

You must be a superuser to enable or disable a feature flag.

## Procedure

1.  Navigate to Settings> (and then)Feature Flags.
2.  Locate the feature flag you want to modify.
3.  Click the toggle switch next to the flag name.

## Results

When you toggle the switch, a confirmation dialog appears with a warning explaining the support level of the feature, along with a link to Red Hat support documentation. Click Confirm to enable/disable the flag, or click Cancel to abort.

If successful, the toggle switch updates immediately to reflect the new state, and the change takes effect without requiring a system restart.

If you cancel the confirmation dialog, the toggle switch reverts to its original state and no changes are made.

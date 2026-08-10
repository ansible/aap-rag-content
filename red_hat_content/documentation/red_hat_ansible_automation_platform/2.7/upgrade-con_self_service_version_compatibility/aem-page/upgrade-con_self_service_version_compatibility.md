+++
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/upgrade-con_self_service_version_compatibility"
title = "Ansible automation portal version compatibility - Red Hat Ansible Automation Platform 2.7"
template = "docs/aem-title.html"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/upgrade-assembly_self_service_upgrading/", "Upgrade Ansible automation portal"]]
category = "Upgrade"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/upgrade-con_self_service_version_compatibility/aem-page/upgrade-con_self_service_version_compatibility.html"
last_crumb = "Ansible automation portal version compatibility"
modified = "2026-07-30T17:12:56.473Z"
multi_page_path = ""
name = "Ansible automation portal version compatibility"
oversized = "false"
page_slug = "upgrade-con_self_service_version_compatibility"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/upgrade-con_self_service_version_compatibility"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/upgrade-con_self_service_version_compatibility/toc/toc.json"
type = "aem-page"
+++

# Ansible automation portal version compatibility

Use the Helm chart version and `imageTagInfo` settings from the lifecycle page for your target release.

When you upgrade Ansible automation portal, use the `redhat-rhaap-portal` Helm chart version and `imageTagInfo` settings documented for your target release on the Ansible automation portal lifecycle page.

- **OCI delivery (recommended):** Set `pluginMode: oci`. Set `imageTagInfo` to the plug-in tag listed for your chart version on the lifecycle page. The chart pulls `registry.redhat.io/ansible-automation-platform/automation-portal:<plugin-version>`.
- **HTTP plug-in registry (deprecated):** Set `pluginMode: tarball`. Refresh the plug-in bundle so its major.minor matches the chart; the bundle patch must be equal to or greater than the chart patch. Prefer migrating from tarball to OCI during upgrade.

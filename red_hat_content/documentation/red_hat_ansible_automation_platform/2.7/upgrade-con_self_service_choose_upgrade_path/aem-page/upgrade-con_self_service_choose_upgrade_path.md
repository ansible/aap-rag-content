+++
title = "Choose an upgrade path - Red Hat Ansible Automation Platform 2.7"
template = "docs/aem-title.html"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/upgrade-con_self_service_choose_upgrade_path"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/upgrade-assembly_self_service_upgrading/", "Upgrade Ansible automation portal"]]
category = "Upgrade"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/upgrade-con_self_service_choose_upgrade_path/aem-page/upgrade-con_self_service_choose_upgrade_path.html"
last_crumb = "Choose an upgrade path"
modified = "2026-07-30T17:12:56.473Z"
multi_page_path = ""
name = "Choose an upgrade path"
oversized = "false"
page_slug = "upgrade-con_self_service_choose_upgrade_path"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/upgrade-con_self_service_choose_upgrade_path"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/upgrade-con_self_service_choose_upgrade_path/toc/toc.json"
type = "aem-page"
+++

# Choose an upgrade path

Select the upgrade procedure that matches how your Ansible automation portal deployment currently delivers Ansible plug-ins.

The following upgrade paths are available:

- **Upgrade with OCI container delivery (recommended):** Your release already uses `pluginMode: oci`, or you will set it during this upgrade.
- **Migrate from tarball to OCI during upgrade:** You currently use the deprecated HTTP plug-in registry and want to move to OCI container delivery in one maintenance window.
- **Upgrade with HTTP plug-in registry (deprecated):** You must stay on tarball delivery temporarily. Refresh tarball files, update the plug-in registry, then upgrade the Helm release.

Note:

If you upgrade in a disconnected or air-gapped OpenShift Container Platform environment, mirror `registry.redhat.io/ansible-automation-platform/automation-portal:<plugin-version>` where `<plugin-version>` is the `imageTagInfo` value from the lifecycle page. Configure `imageRegistry` or `ociPluginImage` before you upgrade.

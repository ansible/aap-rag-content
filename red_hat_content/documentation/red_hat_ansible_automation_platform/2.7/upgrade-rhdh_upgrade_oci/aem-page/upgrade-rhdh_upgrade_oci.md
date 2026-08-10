+++
template = "docs/aem-title.html"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/upgrade-rhdh_upgrade_oci"
title = "Upgrade the Ansible plug-ins using OCI delivery - Red Hat Ansible Automation Platform 2.7"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/upgrade-upgrade_plug_ins_for_rhdh/", "Upgrade Ansible plug-ins for Red Hat Developer Hub"]]
category = "Upgrade"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/upgrade-rhdh_upgrade_oci/aem-page/upgrade-rhdh_upgrade_oci.html"
last_crumb = "Upgrade the Ansible plug-ins using OCI delivery"
modified = "2026-07-30T17:12:56.473Z"
multi_page_path = ""
name = "Upgrade the Ansible plug-ins using OCI delivery"
oversized = "false"
page_slug = "upgrade-rhdh_upgrade_oci"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/upgrade-rhdh_upgrade_oci"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/upgrade-rhdh_upgrade_oci/toc/toc.json"
type = "aem-page"
+++

# Upgrade the Ansible plug-ins using OCI delivery

To upgrade the Ansible plug-ins for Red Hat Developer Hub, update the OCI image tag in your dynamic plug-ins configuration to the new version.

## Before you begin

- You have installed the Ansible plug-ins using OCI container delivery.
- You have the new Ansible plug-ins image tag for your release.

## Procedure

1.  Edit your dynamic plug-ins configuration:

  - For Operator deployments, edit the dynamic plug-ins ConfigMap (for example, `dynamic-plugins-rhdh`).
  - For Helm deployments, in the OpenShift Container Platform Developer UI, navigate to **Helm** > **developer-hub** > **Actions** > **Upgrade** > **Yaml view**.

2.  Update the `<tag>` value in each `oci://registry.redhat.io/ansible-automation-platform/automation-portal:<tag>` reference to the new version.
3.  Apply the changes:

  - For Operator deployments, click **Save**. The Red Hat Developer Hub pod restarts automatically with the updated plug-ins.
  - For Helm deployments, click **Upgrade**.

## Results

Verify the upgrade:

1. Check the `install-dynamic-plugin` container logs for the new version.
2. Verify that the Ansible plug-in is present in the navigation pane.

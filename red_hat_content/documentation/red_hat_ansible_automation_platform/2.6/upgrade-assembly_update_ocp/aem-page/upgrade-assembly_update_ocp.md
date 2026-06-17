+++
title = "Patch update for Operator-based Ansible Automation Platform - Red Hat Ansible Automation Platform 2.6"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.6/upgrade-assembly_update_ocp"
template = "docs/aem-title.html"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6", "2.6"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6/upgrade-assembly_operator_upgrade/", "Upgrade your Operator-based deployment of Ansible Automation Platform"]]
category = "Upgrade"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/upgrade-assembly_update_ocp/aem-page/upgrade-assembly_update_ocp.html"
last_crumb = "Patch update for Operator-based Ansible Automation Platform"
modified = "2026-05-21T14:12:12.122Z"
multi_page_path = ""
name = "Patch update for Operator-based Ansible Automation Platform"
oversized = "false"
page_slug = "upgrade-assembly_update_ocp"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.6"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/upgrade-assembly_update_ocp"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/upgrade-assembly_update_ocp/toc/toc.json"
type = "aem-page"
+++

# Patch update for Operator-based Ansible Automation Platform

You can use an upgrade patch to update your operator-based Ansible Automation Platform.

## Patch updating Ansible Automation Platform on OpenShift Container Platform

When you perform a patch update for an installation of Ansible Automation Platform on OpenShift Container Platform, most updates happen within a channel:

1. A new update becomes available in the marketplace (through the redhat-operator CatalogSource).
2. A new InstallPlan is automatically created for your Ansible Automation Platform subscription. If the subscription is set to Manual, the InstallPlan must be manually approved in the OpenShift UI. If the subscription is set to Automatic, it upgrades as soon as the new version is available. Note:
      Set a manual install strategy on your Ansible Automation Platform Operator subscription. With a manual strategy, you are prompted to approve an upgrade when it becomes available in your selected update channel. Stable channels are available for each X.Y release (for example, stable-*X.Y*).

3. A new Subscription, CSV, and Operator containers will be created alongside the old Subscription, CSV, and containers. Then the old resources will be cleaned up if the new install was successful.

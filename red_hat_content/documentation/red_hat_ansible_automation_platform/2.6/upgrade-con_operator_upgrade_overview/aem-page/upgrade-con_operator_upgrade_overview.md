+++
template = "docs/aem-title.html"
title = "Overview - Red Hat Ansible Automation Platform 2.6"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.6/upgrade-con_operator_upgrade_overview"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6", "2.6"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6/upgrade-assembly_operator_upgrade/", "Upgrade your Operator-based deployment of Ansible Automation Platform"]]
category = "Upgrade"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/upgrade-con_operator_upgrade_overview/aem-page/upgrade-con_operator_upgrade_overview.html"
last_crumb = "Overview"
modified = "2026-05-21T14:12:12.122Z"
multi_page_path = ""
name = "Overview"
oversized = "false"
page_slug = "upgrade-con_operator_upgrade_overview"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.6"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/upgrade-con_operator_upgrade_overview"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/upgrade-con_operator_upgrade_overview/toc/toc.json"
type = "aem-page"
+++

# Overview

Upgrade Ansible Automation Platform on Red Hat OpenShift Container Platform. You can perform full upgrades from supported previous versions or apply patch updates within your current version.

The Ansible Automation Platform Operator manages deployments, upgrades, backups, and restores of automation controller and automation hub. It also handles deployments of AnsibleJob and JobTemplate resources from the Ansible Automation Platform Resource Operator.

Each operator version has default automation controller and automation hub versions. When the operator is upgraded, it also upgrades the automation controller and automation hub deployments it manages, unless overridden in the spec.

OpenShift deployments of Ansible Automation Platform use the built-in Operator Lifecycle Management (OLM) functionality. For more information, see **Operator Lifecycle Manager concepts and resources**. OpenShift does this by using Subscription, CSV, InstallPlan, and OperatorGroup objects. Most users will not have to interact directly with these resources. They are created when the Ansible Automation Platform Operator is installed from **OperatorHub** and managed through the **Subscriptions** tab in the OpenShift console UI. For more information, refer to **Accessing the web console**.

 ![Subscription tab in the OpenShift console](/webassets/aem/red_hat_ansible_automation_platform/2.6/images/aap-2-6-view.png)

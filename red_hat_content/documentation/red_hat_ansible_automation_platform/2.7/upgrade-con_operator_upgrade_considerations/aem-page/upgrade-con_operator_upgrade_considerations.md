+++
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/upgrade-con_operator_upgrade_considerations"
title = "Upgrade considerations - Red Hat Ansible Automation Platform 2.7"
template = "docs/aem-title.html"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/upgrade-assembly_operator_upgrade/", "Upgrade your Operator-based deployment of Ansible Automation Platform"]]
category = "Upgrade"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/upgrade-con_operator_upgrade_considerations/aem-page/upgrade-con_operator_upgrade_considerations.html"
last_crumb = "Upgrade considerations"
latest = "true"
modified = "2026-10-06T15:21:13.207Z"
multi_page_path = ""
name = "Upgrade considerations"
oversized = "false"
page_slug = "upgrade-con_operator_upgrade_considerations"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/upgrade-con_operator_upgrade_considerations"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/upgrade-con_operator_upgrade_considerations/toc/toc.json"
type = "aem-page"
+++

# Upgrade considerations

Before you upgrade Red Hat Ansible Automation Platform, verify that your OpenShift Container Platform cluster version is supported by the target Red Hat Ansible Automation Platform version.

If your OpenShift Container Platform version is not supported by the Red Hat Ansible Automation Platform version you are upgrading to, you must upgrade your OpenShift Container Platform cluster to a supported version first.

Refer to the **Red Hat Ansible Automation Platform Life Cycle** to determine the OpenShift Container Platform version needed.

For information about upgrading your cluster, refer to **Updating clusters**.

## Event streams database user for external databases

If you use an external PostgreSQL database for Event-Driven Ansible and are upgrading your Ansible Automation Platform, verify that a dedicated `eda_event_stream` database user exists on your external database before upgrading. This user is required for event stream operations in Ansible Automation Platform 2.7 and later. See the following related links for more information.

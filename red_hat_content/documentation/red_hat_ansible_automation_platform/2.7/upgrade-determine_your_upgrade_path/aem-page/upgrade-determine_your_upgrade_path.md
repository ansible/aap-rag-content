+++
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/upgrade-determine_your_upgrade_path"
title = "Determine your upgrade path - Red Hat Ansible Automation Platform 2.7"
template = "docs/aem-title.html"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/upgrade-determine_your_upgrade_path/", "Determine your upgrade path"]]
category = "Upgrade"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/upgrade-determine_your_upgrade_path/aem-page/upgrade-determine_your_upgrade_path.html"
last_crumb = "Determine your upgrade path"
modified = "2026-06-05T07:48:10.594Z"
multi_page_path = ""
name = "Determine your upgrade path"
oversized = "false"
page_slug = "upgrade-determine_your_upgrade_path"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/upgrade-determine_your_upgrade_path"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/upgrade-determine_your_upgrade_path/toc/toc.json"
type = "aem-page"
+++

# Determine your upgrade path

Use these reference tables to find the supported upgrade paths for your Ansible Automation Platform deployment.

Review Red Hat Enterprise Linux version compatibility and supported processes for containerized and OpenShift Container Platform deployment types.

Note:

In-place upgrades of major Red Hat Enterprise Linux versions are not supported. You must migrate your existing deployment of Ansible Automation Platform to a new Red Hat Enterprise Linux environment.

## Supported RHEL versions by deployment type

Supported RHEL versions differ among deployment types, as shown in the following table.

| Deployment type and version                                         | Supported RHEL version                                                                                                                                                      |
| ------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <br>Containerized 2.7                                               | <br>RHEL 9.6 or later minor versions of RHEL 9, RHEL 10 or later minor versions of RHEL 10                                                                                  |
| <br>Ansible Automation Platform 2.7 on OpenShift Container Platform | <br>For RHEL versions included with OpenShift Container Platform, see [Red Hat OpenShift Container Platform Life Cycle Policy](https://access.redhat.com/articles/6907891). |

## Container-based upgrade scenarios

Find the supported upgrade paths for your container-based Ansible Automation Platform deployment.

**Container-based Ansible Automation Platform 2.6 on RHEL 9**

| Source                                                        | Target                                                              | Process                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| ------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <br>Container-based Ansible Automation Platform 2.6 on RHEL 9 | <br>Container-based Ansible Automation Platform 2.7 on RHEL 9       | [Upgrade your container deployment](/documentation/en-us/red_hat_ansible_automation_platform/2.7/upgrade-proc_update_aap_container "Perform an upgrade of containerized Ansible Automation Platform.") from 2.6 to 2.7.                                                                                                                                                                                                                                                                                                                                                                                                                     |
| <br>Container-based Ansible Automation Platform 2.6 on RHEL 9 | <br>Container-based Ansible Automation Platform 2.7 on RHEL 10      | [Upgrade your container deployment](/documentation/en-us/red_hat_ansible_automation_platform/2.7/upgrade-proc_update_aap_container "Perform an upgrade of containerized Ansible Automation Platform.") from 2.6 to 2.7.[Back up your deployment of container 2.7](/documentation/en-us/red_hat_ansible_automation_platform/2.7/administer-back_up_and_restore_your_containerized_deployment#backing-up-containerized-ansible-automation-platform "Perform a backup of your container-based installation of Ansible Automation Platform.")on RHEL 9, then restore to a RHEL 10 environment running a fresh container installation 2.7.       |
| <br>Container-based Ansible Automation Platform 2.6 on RHEL 9 | <br>Ansible Automation Platform 2.7 on OpenShift Container Platform | [Upgrade your container deployment](/documentation/en-us/red_hat_ansible_automation_platform/2.7/upgrade-proc_update_aap_container "Perform an upgrade of containerized Ansible Automation Platform.") from 2.6 to 2.7.[Migration process overview](/documentation/en-us/red_hat_ansible_automation_platform/2.7/migrate-con_migration_process_overview "Understand the complete migration workflow including preparation, export, artifact creation, import, reconciliation, and validation steps for moving between Ansible Automation Platform installation types.") 2.7 to Ansible Automation Platform on OpenShift Container Platform. |


**Container-based Ansible Automation Platform 2.6 on RHEL 10**

| Source                                                         | Target                                                              | Process                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| -------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <br>Container-based Ansible Automation Platform 2.6 on RHEL 10 | <br>Container-based Ansible Automation Platform 2.7 on RHEL 10      | [Upgrade your container deployment](/documentation/en-us/red_hat_ansible_automation_platform/2.7/upgrade-proc_update_aap_container "Perform an upgrade of containerized Ansible Automation Platform.") from 2.6 to 2.7.                                                                                                                                                                                                                                                                                                                                                                                                                     |
| <br>Container-based Ansible Automation Platform 2.6 on RHEL 10 | <br>Ansible Automation Platform 2.7 on OpenShift Container Platform | [Upgrade your container deployment](/documentation/en-us/red_hat_ansible_automation_platform/2.7/upgrade-proc_update_aap_container "Perform an upgrade of containerized Ansible Automation Platform.") from 2.6 to 2.7.[Migration process overview](/documentation/en-us/red_hat_ansible_automation_platform/2.7/migrate-con_migration_process_overview "Understand the complete migration workflow including preparation, export, artifact creation, import, reconciliation, and validation steps for moving between Ansible Automation Platform installation types.") 2.7 to Ansible Automation Platform on OpenShift Container Platform. |

## OpenShift Container Platform upgrade scenarios

Find the supported upgrade paths for Ansible Automation Platform deployments that use OpenShift Container Platform.

**Ansible Automation Platform 2.6 on OpenShift Container Platform**

| Source                                                              | Target                                                              | Process                                                                                                                                                                                                                                                                                                                                                                        |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| <br>Ansible Automation Platform 2.6 on OpenShift Container Platform | <br>Ansible Automation Platform 2.7 on OpenShift Container Platform | [Upgrade your OpenShift Container Platform deployment](/documentation/en-us/red_hat_ansible_automation_platform/2.7/upgrade-assembly_operator_upgrade "The Ansible Automation Platform Operator simplifies the installation, upgrade, and deployment of new Red Hat Ansible Automation Platform instances in your OpenShift Container Platform environment.") from 2.6 to 2.7. |

+++
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.6/upgrade-con_upgrade_controller_hub_eda_unified_ui"
template = "docs/aem-title.html"
title = "Mixed-version upgrades with pre-gateway components - Red Hat Ansible Automation Platform 2.6"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6", "2.6"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6/upgrade-ansible_automation_platform_upgrade/", "Upgrade your RPM deployment of Ansible Automation Platform"]]
category = "Upgrade"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/upgrade-con_upgrade_controller_hub_eda_unified_ui/aem-page/upgrade-con_upgrade_controller_hub_eda_unified_ui.html"
last_crumb = "Mixed-version upgrades with pre-gateway components"
modified = "2026-05-21T14:12:12.122Z"
multi_page_path = ""
name = "Mixed-version upgrades with pre-gateway components"
oversized = "false"
page_slug = "upgrade-con_upgrade_controller_hub_eda_unified_ui"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.6"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/upgrade-con_upgrade_controller_hub_eda_unified_ui"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/upgrade-con_upgrade_controller_hub_eda_unified_ui/toc/toc.json"
type = "aem-page"
+++

# Mixed-version upgrades with pre-gateway components

Ansible Automation Platform supports upgrades from pre-gateway environments for all components except Event-Driven Ansible. Configure a mixed environment with Event-Driven Ansible and the platform gateway connected to a pre-gateway cluster.

Combining installation methods (OpenShift Container Platform, RPM, containerized) within such a topology is not supported.

Note:

If you are running a pre-gateway version of Event-Driven Ansible in production, contact Red Hat support or your account representative before you upgrade for guidance on migrating to the current version.

Supported topologies described in this document assume that:

- Pre-gateway services include only automation controller and automation hub.
- Current-version services include Event-Driven Ansible and the platform gateway.
- Combining installation methods for these topologies is not supported.


## Upgrade considerations

- You must have two inventory files as a starting point: one for the pre-gateway services and one for the current-version services.
- Before running the upgrade, you must merge the pre-gateway inventory into the current-version inventory. The platform gateway host must be included in the inventory for the installation program to run successfully.
- Run the upgrade on the merged current-version inventory file only.
- You must be using an external database for both inventories.
- If you are using managed database instances for either inventory, you must migrate to an external database before upgrading.

## Use migration path for 2.4 instances with managed databases

Migrate Ansible Automation Platform 2.4 instances with managed databases to 2.6 by upgrading automation controller and automation hub before enabling unified UI and Event-Driven Ansible.

### Before you begin

- An inventory from 2.4 for automation controller and automation hub and a 2.6 inventory for unified UI (platform gateway) and Event-Driven Ansible. You must merge both inventories into a single 2.6 inventory file before running the upgrade. The platform gateway host must be included in the inventory for the installation program to run successfully.


Important:

Ensure you have upgraded to the latest version of Ansible Automation Platform2.4 before merging inventories and running the 2.6 upgrade.

### Procedure

-   **For standalone node managed database**   * Convert the database node to an external one, removing it from the inventory. The PostgreSQL node will continue working and will not lose the Ansible Automation Platform-provided setup, but you are responsible for managing its configuration afterward.

-   **For collocated managed database**   1.  Back up
  2.  Restore with standalone managed database node instead of collocated
  3.  Unmanaged standalone database

## Use migration path for 2.4 services with 2.6 services

If you installed Ansible Automation Platform 2.6 to use Event-Driven Ansible in a supported scenario, you can upgrade your Ansible Automation Platform 2.4 automation controller and automation hub to Ansible Automation Platform 2.6 by following this procedure.

### Before you begin

- An inventory from 2.4 for automation controller and automation hub and a 2.6 inventory for unified UI (platform gateway) and Event-Driven Ansible. You must merge both inventories into a single 2.6 inventory file before running the upgrade. The platform gateway host must be included in the inventory for the installation program to run successfully.


Important:

Ensure you have upgraded to the latest version of Ansible Automation Platform 2.4 before merging inventories and running the 2.6 upgrade.

### Procedure

1.  Merge 2.4 inventory data into the 2.6 inventory. The example below shows the inventory file for automation controller and automation hub for 2.4 and the inventory file for Event-Driven Ansible and the unified UI (platform gateway) for 2.6, respectively, as the starting point, and what the merged inventory looks like.

     **Inventory files from 2.4**

```bash
[automationcontroller]
controller-1
controller-2

    [automationhub]
hub-1
hub-2

    [all:vars]
# Here we have the admin passwd, db credentials, etc.
```
     **Inventory files from 2.6**

```
[automationedacontroller]
eda-1
eda-2

    [automationgateway]
gw-1
gw-2

    [all:vars]
# Here we have admin passwd, db credentials etc.
```
     **Merged Inventory**

```
[automationcontroller]
controller-1
controller-2

    [automationhub]
hub-1
hub-2

    [automationedacontroller]
eda-1
eda-2

    [automationgateway]
gw-1
gw-2

    [all:vars]
# Here we have admin passwd, db credentials etc from both inventories above
```

2.  Run `setup.sh`
      The installation program upgrades all services to the latest version of Ansible Automation Platform 2.6 and connects them to the unified UI (platform gateway).

### Results

- Verify that everything has upgraded to 2.6 and is working properly in one of two ways:
  * Perform an SSH to automation controller and Event-Driven Ansible.
  * In the unified UI, go to Help> (and then)About to verify the RPM versions are at 2.6.

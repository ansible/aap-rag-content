+++
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/configure-configure_static_storage_for_ansible_automation_platform"
title = "Configure static storage for Ansible Automation Platform - Red Hat Ansible Automation Platform 2.7"
template = "docs/aem-title.html"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/configure-configure_static_storage_for_ansible_automation_platform/", "Configure static storage for Ansible Automation Platform"]]
category = "Configure"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/configure-configure_static_storage_for_ansible_automation_platform/aem-page/configure-configure_static_storage_for_ansible_automation_platform.html"
last_crumb = "Configure static storage for Ansible Automation Platform"
modified = "2026-06-05T07:48:10.594Z"
multi_page_path = ""
name = "Configure static storage for Ansible Automation Platform"
oversized = "false"
page_slug = "configure-configure_static_storage_for_ansible_automation_platform"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/configure-configure_static_storage_for_ansible_automation_platform"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/configure-configure_static_storage_for_ansible_automation_platform/toc/toc.json"
type = "aem-page"
+++

# Configure static storage for Ansible Automation Platform

Configure static storage when your environment does not support dynamic volume provisioning. This process ensures the Ansible Automation Platform Operator adopts manually created Persistent Volume Claims by using specific naming conventions.

## Understand static provisioning in the Ansible Automation Platform Operator

By default, the Ansible Automation Platform Operator uses dynamic provisioning to create the required storage for components such as the database and automation hub. If your environment does not allow dynamic provisioning, you must use static provisioning.

 With static provisioning, you manually create Persistent Volumes (PVs) and Persistent Volume Claims (PVCs) before you deploy the `AnsibleAutomationPlatform` custom resource. When the Operator starts the deployment, it searches the namespace for PVCs that match its internal naming conventions. If a matching PVC exists, the Operator binds to that claim instead of attempting to provision new storage.

Static provisioning also enables data persistence during redeployments. If you delete an `AnsibleAutomationPlatform` instance, the Operator does not delete the associated PVCs. You can redeploy the instance using the same name to reconnect to the existing data.

## Pre-create Persistent Volume Claims for manual provisioning

Follow this process to manually prepare storage for an Ansible Automation Platform installation when dynamic provisioning is disabled.

### Before you begin

- You have an active OpenShift Container Platform CLI (`oc`) session.
- You have defined Persistent Volumes (PVs) that meet the minimum size and access mode requirements for your components.

### Procedure

1.  Identify the name you intend to use for your `AnsibleAutomationPlatform` deployment (for example, myaap).
2.  Create a PVC manifest for the PostgreSQL database using the required naming convention: `postgres-15-<deployment_name>-0`,
3.  Ensure the `accessModes` and `resources.requests.storage` match your manually provisioned PV.
4.  Apply the PVC manifest:
  

```
oc apply -f postgres-pvc.yaml
```

5.  Repeat these steps for other components, such as automation Hub, using the correct naming conventions.
6.  Leave the `storage_class` fields empty or omit them from the specification. This forces the Operator to use the pre-created PVCs.
  
  Note:
  Unlike core components, the `AnsibleAutomationPlatformBackup` and `Restore` custom resources provide a `backup_pvc` parameter. You must use this parameter to specify your custom PVC name instead of relying on naming conventions.

### Results

Check the status of the PVCs to ensure they are in a Bound state:

```
oc get pvc -n <namespace>
```

## PVC naming conventions for Ansible Automation Platform components

The Operator must find PVCs with exact names to adopt them for static provisioning. Replace `<instance_name>` with the name of your `AnsibleAutomationPlatform` custom resource.

| Component                            | Required PVC name                                                                         | Default access mode |
| ------------------------------------ | ----------------------------------------------------------------------------------------- | ------------------- |
| Ansible Automation Platform database | `postgres-15-<aap_cr_name>-postgres-15-0`                                                 | ReadWriteOnce       |
| Automation hub storage               | <br>`<instance_name>-hub-file-storage`<br>(Required when `storage_type` is set to `file`) | ReadWriteMany       |
| Automation Hub Redis persistence     | `<instance_name>-hub-redis-data`                                                          | ReadWriteOnce       |

+++
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-proc_operator_link_components"
template = "docs/aem-title.html"
title = "Deploy a new Ansible Automation Platform instance with components - Red Hat Ansible Automation Platform 2.7"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-assembly_operator_install_operator/", "Install on OpenShift Container Platform"]]
category = "Install"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/install-proc_operator_link_components/aem-page/install-proc_operator_link_components.html"
last_crumb = "Deploy a new Ansible Automation Platform instance with components"
modified = "2026-06-05T07:48:10.594Z"
multi_page_path = ""
name = "Deploy a new Ansible Automation Platform instance with components"
oversized = "false"
page_slug = "install-proc_operator_link_components"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/install-proc_operator_link_components"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/install-proc_operator_link_components/toc/toc.json"
type = "aem-page"
+++

# Deploy a new Ansible Automation Platform instance with components

After installing the Ansible Automation Platform Operator in your namespace you can set up your **Ansible Automation Platform** instance. Then link all the platform components to a single user interface.

## About this task

## Procedure

1.  Log in to Red Hat OpenShift Container Platform.
2.  Navigate to Operators> (and then)Installed Operators.
3.  Select your Ansible Automation Platform Operator deployment.
4.  Select the **Details** tab.
5.  On the **Ansible Automation Platform** tile click Create instance.
6.  From the **Create Ansible Automation Platform** page enter a name for your instance in the **Name** field.
7.  Click YAML view and replace the `spec` section with the following:
  

```
spec:
  database:
    resource_requirements:
      requests:
        cpu: 200m
        memory: 512Mi
    storage_requirements:
      requests:
        storage: 100Gi

    controller:
    disabled: false

    eda:
    disabled: false

    hub:
    disabled: false
    storage_type: file
    file_storage_storage_class: <read-write-many-storage-class>
    file_storage_size: 10Gi
```

8.  You must specify your desired value for the `<read-write-many-storage-class>` placeholder.
9.  Click Create.

## Results

 **Verify instance deployment (UI):**

1. Navigate to Operators> (and then)Installed Operators.
2. Select your Ansible Automation Platform Operator deployment.
3. Select the **All instances** tab.
4. Verify that the **Ansible Automation Platform** instance, **Automation Controller**, **Event-Driven Ansible**, and **Automation Hub** instances are listed.


 **Verify pod status (UI):**

1. Navigate to Workloads> (and then)Pods.
2. Switch to the project (namespace) where you deployed the instance.
3. Verify that all related pods display a **Running** or **Completed** status.


 **Verify Platform Route (CLI):**

Run the following command to confirm the URL for accessing the platform gateway:

```
oc get route
```

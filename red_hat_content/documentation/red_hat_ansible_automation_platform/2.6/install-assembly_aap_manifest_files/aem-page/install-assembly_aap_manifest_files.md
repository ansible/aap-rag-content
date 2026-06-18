+++
title = "Obtain a manifest file - Red Hat Ansible Automation Platform 2.6"
template = "docs/aem-title.html"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.6/install-assembly_aap_manifest_files"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6", "2.6"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6/install-assembly_operator_install_operator/", "Install on OpenShift Container Platform"]]
category = "Install"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/install-assembly_aap_manifest_files/aem-page/install-assembly_aap_manifest_files.html"
last_crumb = "Obtain a manifest file"
modified = "2026-05-21T14:12:12.122Z"
multi_page_path = ""
name = "Obtain a manifest file"
oversized = "false"
page_slug = "install-assembly_aap_manifest_files"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.6"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/install-assembly_aap_manifest_files"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/install-assembly_aap_manifest_files/toc/toc.json"
type = "aem-page"
+++

# Obtain a manifest file

You can obtain a subscription manifest in the **Subscription Allocations** section of Red Hat Subscription Management.

After you obtain a subscription allocation, you can download its manifest file and upload it to activate Ansible Automation Platform.

To begin, log in to the **Red Hat Customer Portal** by using your administrator user account and follow the procedures listed.

## Create a subscription allocation

With a new subscription allocation you can set aside subscriptions and entitlements for a system that is currently offline or air-gapped. This is necessary before you download its manifest and upload it to Ansible Automation Platform.

### About this task

### Procedure

1.  From the [Subscription Allocations](https://access.redhat.com/management/subscription_allocations/) page, click New Subscription Allocation.
2.  Enter a name for the allocation so that you can find it later.
3.  Select **Type: Satellite 6.16** as the management application.
4.  Click Create.

## Add subscriptions to a subscription allocation

After you create an allocation, you can add the subscriptions you need for Ansible Automation Platform to run properly. This is necessary before you download the manifest and add it to Ansible Automation Platform.

### About this task

### Procedure

1.  From the [Subscription Allocations](https://access.redhat.com/management/subscription_allocations/) page, click the name of the **Subscription Allocation** to which you want to add a subscription.
2.  Click the **Subscriptions** tab.
3.  Click Add Subscriptions.
4.  Enter the number of Ansible Automation Platform Entitlements you plan to add.
5.  Click Submit.

## Download a manifest file

After you create an allocation with the appropriate subscriptions on it, you can download the manifest file from Red Hat Subscription Management.

### About this task

### Procedure

1.  From the [Subscription Allocations](https://access.redhat.com/management/subscription_allocations/) page, click the name of the **Subscription Allocation** to which you want to generate a manifest.
2.  Click the **Subscriptions** tab.
3.  Click Export Manifest to download the manifest file.

### Results

This downloads a file `manifest_<allocation name>_<date>.zip` to your default downloads folder.

+++
title = "Sync content collections - Red Hat Ansible Automation Platform 2.6"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.6/administer-proc_create_synclist"
template = "docs/aem-title.html"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6", "2.6"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6/administer-manage_your_organization_s_automation_content/", "Manage your organization's automation content"]]
category = "Administer"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/administer-proc_create_synclist/aem-page/administer-proc_create_synclist.html"
last_crumb = "Sync content collections"
modified = "2026-05-21T14:12:12.122Z"
multi_page_path = ""
name = "Sync content collections"
oversized = "false"
page_slug = "administer-proc_create_synclist"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.6"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/administer-proc_create_synclist"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/administer-proc_create_synclist/toc/toc.json"
type = "aem-page"
+++

# Sync content collections

You can sync certified and validated collections in Ansible automation hub from console.redhat.com.

## Before you begin

- You have a valid Ansible Automation Platform subscription.
- You have organization administrator permissions for console.redhat.com.
- You have created a requirements file.
- The following domain names are part of either the firewall or the proxy’s allowlist. They are required for successful connection and download of collections from automation hub or Galaxy server:
  * `galaxy.ansible.com`
  * `cloud.redhat.com`
  * `console.redhat.com`
  * `sso.redhat.com`
  * `ansible-galaxy-ng.s3.dualstack.us-east-1.amazonaws.com`
- Ansible automation hub resources are stored in Amazon Simple Storage. The following domain names must be in the allow list:
  * `automation-hub-prd.s3.us-east-2.amazonaws.com`
  * `ansible-galaxy.s3.amazonaws.com`
- SSL inspection is disabled either when using self signed certificates or for the Red Hat domains.


 Important:

Before you begin your content sync, ensure that you have the resources to sync the collections you need.

## About this task

 Note:

When syncing content, keep in mind that automation hub does not check other repositories for dependencies. To avoid an error, turn off dependency downloading by editing your remote settings.

## Procedure

1.  From the navigation panel, select Automation Content> (and then)Remotes.
2.  Find the remote you want to sync from and click the pencil icon ![Edit](/webassets/aem/red_hat_ansible_automation_platform/2.6/images/leftpencil.png) to edit.
3.  Find the field labeled **Requirements file**. There, you can either paste the contents of your requirements file, or upload the file from your hard drive by selecting the upload button.
4.  Click Save remote.
5.  To begin synchronization, from the navigation panel select Automation Content> (and then)Repositories.
6.  In the row containing the repository you want to sync, click the ⋮ icon and select the ![Sync repository](/webassets/aem/red_hat_ansible_automation_platform/2.6/images/sync.png)**Sync repository** icon to initiate the remote repository synchronization to your private automation hub.
7.  On the modal that appears, you can toggle the following options:

  - **Mirror**: Select if you want your repository content to mirror the remote repository’s content.
  - **Optimize**: Select if you want to sync only when changes are reported by the remote server.

8.  Click Sync to complete the sync.

## Results

The **Sync status** column updates to notify you whether the synchronization is successful.

- Navigate to Automation Content> (and then)Collections to confirm that your collections content has synchronized successfully.

+++
template = "docs/aem-title.html"
title = "Sync content collections - Red Hat Ansible Automation Platform 2.7"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/administer-proc_create_synclist"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/administer-manage_your_organization_s_automation_content/", "Manage your organization's automation content"]]
category = "Administer"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/administer-proc_create_synclist/aem-page/administer-proc_create_synclist.html"
last_crumb = "Sync content collections"
modified = "2026-07-30T17:12:56.473Z"
multi_page_path = ""
name = "Sync content collections"
oversized = "false"
page_slug = "administer-proc_create_synclist"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/administer-proc_create_synclist"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/administer-proc_create_synclist/toc/toc.json"
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
2.  Find the remote you want to sync from and click the pencil icon ![Edit](/webassets/aem/red_hat_ansible_automation_platform/2.7/images/leftpencil.png) to edit.
3.  Find the field labeled **Requirements file**. There, you can either paste the contents of your requirements file, or upload the file from your hard drive by selecting the upload button.
4.  Click Save remote.
5.  To begin synchronization, from the navigation panel select Automation Content> (and then)Repositories.
6.  In the row containing the repository you want to sync, click the ⋮ icon and select the ![Sync repository](/webassets/aem/red_hat_ansible_automation_platform/2.7/images/sync.png)**Sync repository** icon to initiate the remote repository synchronization to your private automation hub.
7.  On the modal that appears, you can toggle the following options:

  - **Mirror**: Select if you want your repository content to mirror the remote repository’s content.
  - **Optimize**: Select if you want to sync only when changes are reported by the remote server.

8.  Click Sync to complete the sync.

## Results

After you initiate a sync, the **Sync status** column on the Automation Content> (and then)Repositories page updates to show the current state of the operation.

| Sync status | Description                                                                           |
| ----------- | ------------------------------------------------------------------------------------- |
| Completed   | The sync finished successfully. The repository content is up to date with the remote. |
| Failed      | The sync encountered an error. Check the sync task details for more information.      |
| Syncing     | The sync is in progress.                                                              |
| No sync     | The repository has never been synced.                                                 |

To verify the sync results, navigate to Automation Content> (and then)Collections and confirm that the expected content appears.

**Check when a repository was last synced**

The Automation Content> (and then)Remotes page shows the "Last updated" timestamp for each remote configuration. The timestamp also reflects the most recent successful sync for that remote. You can also retrieve the last sync time from the API. Send a GET request to `/api/galaxy/pulp/api/v3/repositories/ansible/ansible/` and check the` last_synced_metadata_time` field in the response. The field is null if the repository has never been synced.

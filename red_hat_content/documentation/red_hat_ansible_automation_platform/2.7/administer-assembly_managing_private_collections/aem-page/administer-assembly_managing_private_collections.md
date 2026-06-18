+++
title = "Upload, group, and approve your organization?s content collections - Red Hat Ansible Automation Platform 2.7"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/administer-assembly_managing_private_collections"
template = "docs/aem-title.html"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/administer-assembly_working_with_namespaces/", "Manage collection access and permissions with namespaces"]]
category = "Administer"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/administer-assembly_managing_private_collections/aem-page/administer-assembly_managing_private_collections.html"
last_crumb = "Upload, group, and approve your organization?s content collections"
modified = "2026-06-05T07:48:10.594Z"
multi_page_path = ""
name = "Upload, group, and approve your organization?s content collections"
oversized = "false"
page_slug = "administer-assembly_managing_private_collections"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/administer-assembly_managing_private_collections"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/administer-assembly_managing_private_collections/toc/toc.json"
type = "aem-page"
+++

# Upload, group, and approve your organization’s content collections

Use automation hub to manage and publish content collections developed within your organization.

Upload and group collections in namespaces. Uploaded collections need administrative approval to appear in the **Published** content repository. When the collection is published, your users can access and download it for use.

You can also reject submitted collections that do not meet organizational certification criteria.

## Approve collections

You can approve collections uploaded to individual namespaces for internal publication and use.

### Before you begin

- You have **Modify Ansible repo content** permissions.

### About this task

All collections awaiting review are located in Automation Content> (and then)Collection Approvals.

### Procedure

1.  From the navigation panel, select Automation Content> (and then)Collection Approvals. Collections requiring approval have the status **Needs review**.

2.  Find the collection you want to review in the list. You can also filter collections by Namespace, Repository, and Status using the search bar.
3.  Click the thumbs up icon to approve and sign the collection. Confirm your choice in the modal that appears.

### Results

Approved collections are moved to the **Published** repository where users can view and download them for use.

## Reject collections uploaded for review

You can reject collections uploaded to individual namespaces.

### Before you begin

- You have **Modify Ansible repo content** permissions.

### About this task

All collections awaiting review are located in Automation Content> (and then)Collection Approvals.

Collections requiring approval have the status **Needs review**.

### Procedure

1.  From the navigation panel, select Automation Content> (and then)Collection Approvals.
2.  Find the collection you want to review in the list. You can also filter collections by Namespace, Repository, and Status using the search bar.
3.  Click the thumbs down icon to reject the collection. Confirm your choice in the modal that appears.

### Results

Collections you decline for publication are moved to the **Rejected** repository.

## Repository management with automation hub

As a platform administrator, you can create, edit, delete, and move automation content collections between repositories.

### Types of repositories in automation hub

In automation hub you can publish collections to two types of repositories, depending on whether you want your collection to be verified:

Staging repositories
Any user with permission to upload to a namespace can publish collections into these repositories. Collections in these repositories are not available in the search page. Instead, they are displayed on the approval dashboard for an administrator to verify. Staging repositories are marked with the `pipeline=staging` label.

Custom repositories
Any user with write permissions on the repository can publish collections to these repositories. Custom repositories can be public where all users can see them, or private where only users with view permissions can see them. These repositories are not displayed on the approval dashboard. If the repository owner enables search, the collection can appear in search results.

By default, automation hub includes one staging repository that is automatically used when a repository is not specified for uploading collections.

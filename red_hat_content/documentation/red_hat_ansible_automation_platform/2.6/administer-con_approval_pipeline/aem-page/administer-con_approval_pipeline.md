+++
title = "Approve content for custom repositories in automation hub - Red Hat Ansible Automation Platform 2.6"
template = "docs/aem-title.html"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.6/administer-con_approval_pipeline"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6", "2.6"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6/administer-assembly_working_with_namespaces/", "Manage collection access and permissions with namespaces"]]
category = "Administer"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/administer-con_approval_pipeline/aem-page/administer-con_approval_pipeline.html"
last_crumb = "Approve content for custom repositories in automation hub"
modified = "2026-05-21T14:12:12.122Z"
multi_page_path = ""
name = "Approve content for custom repositories in automation hub"
oversized = "false"
page_slug = "administer-con_approval_pipeline"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.6"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/administer-con_approval_pipeline"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/administer-con_approval_pipeline/toc/toc.json"
type = "aem-page"
+++

# Approve content for custom repositories in automation hub

In automation hub you can approve collections into any repository marked with the `pipeline=approved` label.

By default, automation hub includes one repository for approved content, but you have the option to add more from the repository creation screen. You cannot directly publish into a repository marked with the `pipeline=approved` label. A collection must first go through a staging repository and be approved before being published into a `pipeline=approved` repository.

Auto approval
When auto approve is enabled, any collection you upload to a staging repository is automatically promoted to all of the repositories marked as `pipeline=approved`.

Approval required
When auto approve is disabled, the administrator can view the approval dashboard and see collections that have been uploaded into any of the staging repositories. Sorting by **Approved** displays a list of approved repositories. From this list, the administrator can select one or more repositories to which the content should be promoted.

If only one approved repository exists, the collection is automatically promoted into it and the administrator is not prompted to select a repository.

Rejection
Rejected collections are automatically placed into the rejected repository, which is pre-installed.

## Manage access to custom content with role based access control

Use Role Based Access Control (RBAC) to restrict user access to custom repositories by defining access permissions based on user roles.

By default, users can view all public repositories in their automation hub, but they cannot modify a repository unless their role allows them access to do so. The same logic applies to other operations on the repository. For example, you can remove a user’s ability to download content from a custom repository by changing their role permissions.

## Create a custom repository

When you create a repository in Ansible Automation Platform, you can configure the repository to be private or hide it from search results.

### Procedure

1.  Log in to Ansible Automation Platform.
2.  From the navigation panel, select Automation Content> (and then)Repositories.
3.  Click Create repository.
4.  Enter a **Name** for your repository.
5.  In the **Description** field, describe the purpose of the repository.
6.  To retain previous versions of your repository each time you make a change, enter a figure in the field labeled **Retained number of versions**. The number of retained versions can range anywhere between 0 and unlimited. To save all versions, leave this set to null. Note:
      If you have a problem with a change to your custom repository, you can [revert to a different repository version](/documentation/en-us/red_hat_ansible_automation_platform/2.6/administer-con_approval_pipeline#proc-revert-repository-version "When automation content is added or removed from a repository, a new version is created. If a change to your repository causes a problem, you can revert to a previous version.") that you have retained.

7.  In the **Pipeline** field, select a pipeline for the repository. This option defines who can publish a collection into the repository.

Staging
Anyone is allowed to publish automation content into the repository.

Approved
Collections added to this repository are required to go through the approval process by way of the staging repository. When auto approve is enabled, any collection uploaded to a staging repository is automatically promoted to all of the approved repositories.

None
Any user with permissions on the repository can publish to the repository directly, and the repository is not part of the approval pipeline.

8.  Optional: To hide the repository from search results, select **Hide from search**.
9.  Optional: To make the repository private, select **Make private**. This hides the repository from anyone who does not have permissions to view the repository.
10.  To sync the content from a remote repository into this repository, in the **Remote** field select the remote that contains the collections you want included in your custom repository.
11.  Click Create repository.

### What to do next

- After the repository is created, the details page is displayed. From here, you can provide access to your repository, review or add collections, and work with the saved versions of your custom repository.

## Configure access to a custom automation hub repository

Use role-based access control to assign users to a repository so they can interact with it.

### About this task

By default, private repositories and the automation content collections are hidden from all users in the system. Public repositories can be viewed by all users, but cannot be modified. You must configure a custom repository to grant users access to it.

### Procedure

1.  Log in to private automation hub.
2.  From the navigation panel, select Automation Content> (and then)Repositories.
3.  Click into your repository in the list and select the **Team Access** tab.
4.  Click Assign teams.
5.  Select the team to which you want to grant a role, then click Next.
6.  Select the roles you want to apply to the selected team, and then click Next.
7.  Review your selections and click Finish.
8.  Click Close to complete the process.

## Add automation content to an automation hub repository

After you create your repository, you can add automation content to it.

### Procedure

1.  From the navigation panel, select Automation Content> (and then)Repositories.
2.  Click into your repository in the list.
3.  Select the **Collection versions** tab.
4.  Click Add Collections and select the collections that you want to add to your repository.
5.  Click Select.

## Manage automation hub repository versions

When automation content is added or removed from a repository, a new version is created. If a change to your repository causes a problem, you can revert to a previous version.

### About this task

Reverting is a safe operation and does not delete content from the system, but rather changes the content associated with the repository. The number of versions saved is defined in the **Retained number of versions** setting when a repository is created.

### Procedure

1.  Log in to Ansible Automation Platform.
2.  From the navigation panel, select Automation Content> (and then)Repositories.
3.  Click into your repository in the list and then select the **Versions** tab.
4.  Locate the version you want to revert to and click the More Actions icon **⋮**, and select **Revert to this version**.
5.  Check the box confirming your selection, and then click Revert to repository version.

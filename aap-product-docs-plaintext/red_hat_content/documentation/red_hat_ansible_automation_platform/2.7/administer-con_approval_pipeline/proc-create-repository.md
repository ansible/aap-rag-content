# Approve content for custom repositories in automation hub
## Create a custom repository

When you create a repository in Ansible Automation Platform, you can configure the repository to be private or hide it from search results.

### Procedure

1.  Log in to Ansible Automation Platform.
2.  From the navigation panel, select Automation Content> (and then)Repositories.
3.  Click Create repository.
4.  Enter a **Name** for your repository.
5.  In the **Description** field, describe the purpose of the repository.
6.  To retain previous versions of your repository each time you make a change, enter a figure in the field labeled **Retained number of versions**. The number of retained versions can range anywhere between 0 and unlimited. To save all versions, leave this set to null. Note:
If you have a problem with a change to your custom repository, you can [revert to a different repository version](/documentation/en-us/red_hat_ansible_automation_platform/2.7/administer-con_approval_pipeline#proc-revert-repository-version "When automation content is added or removed from a repository, a new version is created. If a change to your repository causes a problem, you can revert to a previous version.") that you have retained.

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


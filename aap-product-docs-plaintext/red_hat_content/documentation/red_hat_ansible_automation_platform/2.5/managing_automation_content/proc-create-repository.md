# 2. Managing collections in automation hub
## 2.3. Repository management with automation hub
### 2.3.4. Creating a custom repository in automation hub




When you use Red Hat Ansible Automation Platform to create a repository, you can configure the repository to be private or hide it from search results.

**Procedure**

1. Log in to Ansible Automation Platform.
1. From the navigation panel, selectAutomation Content→Repositories.
1. ClickCreate repository.
1. Enter a **Name** for your repository.
1. In the **Description** field, describe the purpose of the repository.
1. To retain previous versions of your repository each time you make a change, enter a figure in the field labeled **Retained number of versions** . The number of retained versions can range anywhere between 0 and unlimited. To save all versions, leave this set to null.

Note
If you have a problem with a change to your custom repository, you can [revert to a different repository version](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/managing_automation_content/index#proc-revert-repository-version) that you have retained.




1. In the **Pipeline** field, select a pipeline for the repository. This option defines who can publish a collection into the repository.


1. Optional: To hide the repository from search results, select **Hide from search** .
1. Optional: To make the repository private, select **Make private** . This hides the repository from anyone who does not have permissions to view the repository.
1. To sync the content from a remote repository into this repository, in the **Remote** field select the remote that contains the collections you want included in your custom repository. For more information, see [Repository sync](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/managing_automation_content/index#proc-basic-repo-sync) .
1. ClickCreate repository.


**Next steps**

- After the repository is created, the details page is displayed.

From here, you can provide access to your repository, review or add collections, and work with the saved versions of your custom repository.





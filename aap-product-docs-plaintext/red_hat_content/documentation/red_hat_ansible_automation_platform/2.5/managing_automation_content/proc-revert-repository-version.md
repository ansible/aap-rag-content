# 2. Managing collections in automation hub
## 2.3. Repository management with automation hub
### 2.3.7. Revert to a different automation hub repository version




When automation content collections are added or removed from a repository, a new version is created. If a change to your repository causes a problem, you can revert to a previous version. Reverting is a safe operation and does not delete collections from the system, but rather, changes the content associated with the repository. The number of versions saved is defined in the **Retained number of versions** setting when a [repository is created](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/managing_automation_content/index#proc-create-repository) .

**Procedure**

1. Log in to Ansible Automation Platform.
1. From the navigation panel, selectAutomation Content→Repositories.
1. Click into your repository in the list and then select the **Versions** tab.
1. Locate the version you want to revert to and click theMore Actionsicon **⋮** , and select **Revert to this version** .
1. Check the box confirming your selection, and then clickRevert to repository version.



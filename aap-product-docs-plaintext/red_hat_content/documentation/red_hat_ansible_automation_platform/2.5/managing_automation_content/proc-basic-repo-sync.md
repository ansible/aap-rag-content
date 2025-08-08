# 2. Managing collections in automation hub
## 2.5. Synchronizing repositories in automation hub
### 2.5.1. Synchronizing repositories in automation hub




**Procedure**

1. Log in to Ansible Automation Platform.
1. From the navigation panel, selectAutomation Content→Repositories.
1. Locate your repository in the list and clickMore Actionsicon **⋮** , then select **Sync repository** .

All collections in the configured remote are downloaded to your custom repository. To check the status of the collection sync, selectAutomation Content→Task Managementfrom the navigation panel.

Note
To limit repository synchronization to specific collections within a remote, you can identify specific collections to be pulled by using a requirements.yml file. See [Create a remote](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/managing_automation_content/index#proc-create-remote_remote-management) for more information.






**Additional resources**

For more information about using requirements files, see [Creating a requirements file](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/managing_automation_content/managing-cert-valid-content#create-requirements-file_managing-cert-validated-content) .



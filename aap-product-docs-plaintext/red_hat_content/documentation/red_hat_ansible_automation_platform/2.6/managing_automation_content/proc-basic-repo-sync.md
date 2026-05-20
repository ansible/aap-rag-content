# 2. Managing collections in automation hub
## 2.5. Synchronizing repositories in automation hub
### 2.5.1. Synchronizing repositories in automation hub

**Procedure**

1. Log in to Ansible Automation Platform.

2. From the navigation panel, select Automation Content → Repositories.

3. Locate your repository in the list and click More Actions icon **⋮**, then select **Sync repository**.

All collections in the configured remote are downloaded to your custom repository. To check the status of the collection sync, select Automation Content → Task Management from the navigation panel.


Note
To limit repository synchronization to specific collections within a remote, you can identify specific collections to be pulled by using a requirements.yml file. See [Create a remote](#proc-create-remote_remote-management "2.4.1.&nbsp;Creating a remote configuration in automation hub") for more information.

**Additional resources**

- [Creating a requirements file](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/managing_automation_content/managing-cert-valid-content#create-requirements-file_managing-cert-validated-content)


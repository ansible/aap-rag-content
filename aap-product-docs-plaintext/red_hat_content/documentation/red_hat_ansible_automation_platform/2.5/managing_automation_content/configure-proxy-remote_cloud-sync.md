# 1. Red Hat Certified, validated, and Ansible Galaxy content in automation hub
## 1.1. Configuring remote repositories for content syncing
### 1.1.7. Configuring proxy settings




If your private automation hub is behind a network proxy, you can configure proxy settings on the remote to sync content located outside of your local network.

**Prerequisites**

- You have valid **Modify Ansible repo content** permissions. For more information on permissions, see [Access management and authentication](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/access_management_and_authentication)
- You have a proxy URL and credentials from your local network administrator.


**Procedure**

1. Log in to Ansible Automation Platform.
1. From the navigation panel, selectAutomation Content→Remotes.
1. In either the **rh-certified** or **Community** remote, click theMore Actionsicon **⋮** and select **Edit remote** .
1. Expand the **Show advanced options** drop-down menu.
1. Enter your proxy URL, proxy username, and proxy password in the appropriate fields.
1. ClickSave remote.



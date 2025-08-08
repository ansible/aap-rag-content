# 1. Red Hat Certified, validated, and Ansible Galaxy content in automation hub
## 1.1. Configuring Ansible automation hub remote repositories to synchronize content
### 1.1.5. Configuring the rh-certified remote repository to sync Ansible Certified Content Collections




You can edit the **rh-certified** remote repository to synchronize collections from automation hub hosted on console.redhat.com to your private automation hub. By default, your private automation hub `rh-certified` repository includes the URL for the entire group of Ansible Certified Content Collections.

To use only those collections specified by your organization, a private automation hub administrator can upload manually-created requirements files from the `rh-certified` remote.

If you have collections `A` , `B` , and `C` in your requirements file, and a new collection `X` is added to console.redhat.com that you want to use, you must add `X` to your requirements file for private automation hub to synchronize it.

**Prerequisites**

- You have valid **Modify Ansible repo content** permissions. For more information on permissions, see [Access management and authentication](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/access_management_and_authentication) .
- You have retrieved the Sync URL and API Token from the automation hub hosted service on console.redhat.com.
- You have configured access to port 443. This is required for synchronizing certified collections. For more information, see the automation hub table in the [Network ports and protocols](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/planning_your_installation/ref-network-ports-protocols_planning) chapter of Planning your installation.


**Procedure**

1. Log in to your Ansible Automation Platform.
1. From the navigation panel, selectAutomation Content→Remotes.
1. In the **rh-certified** remote repository, clickEdit remote.
1. In the **URL** field, paste the **Sync URL** .
1. In the **Token** field, paste the token you acquired from console.redhat.com.
1. ClickSave remote.


**Result**

You can now synchronize collections from console.redhat.com to your private automation hub.


**Next steps**

See [Synchronizing Ansible content collections in automation hub](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/managing_automation_content/managing-cert-valid-content#assembly-synclists) for syncing steps.



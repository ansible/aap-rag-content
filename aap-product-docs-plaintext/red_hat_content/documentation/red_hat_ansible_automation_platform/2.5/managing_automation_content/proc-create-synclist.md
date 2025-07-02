# 1. Red Hat Certified, validated, and Ansible Galaxy content in automation hub
## 1.2. Synchronizing Ansible Content Collections in automation hub
### 1.2.1. Syncing Ansible content collections




You can sync certified and validated collections in Ansible automation hub on console.redhat.com.

Note
When syncing content, keep in mind that automation hub does not check other repositories for dependencies. To avoid an error, turn off dependency downloading by editing your remote settings. See [Creating a remote configuration in automation hub](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/managing_automation_content/managing-collections-hub#proc-create-remote_remote-management) for more information.



**Prerequisites**

- You have a valid Ansible Automation Platform subscription.
- You have organization administrator permissions for console.redhat.com.
- You have created a [requirements file](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/managing_automation_content/managing-cert-valid-content#create-requirements-file_cloud-sync) .
- The following domain names are part of either the firewall or the proxy’s allowlist. They are required for successful connection and download of collections from automation hub or Galaxy server:


-  `        galaxy.ansible.com`
-  `        cloud.redhat.com`
-  `        console.redhat.com`
-  `        sso.redhat.com`

- Ansible automation hub resources are stored in Amazon Simple Storage. The following domain names must be in the allow list:


-  `        automation-hub-prd.s3.us-east-2.amazonaws.com`
-  `        ansible-galaxy.s3.amazonaws.com`

- SSL inspection is disabled either when using self signed certificates or for the Red Hat domains.


Important
Before you begin your content sync, consult the Knowledgebase article [Resource requirements for syncing automation content](https://access.redhat.com/articles/7118757) to ensure that you have the resources to sync the collections you need.



**Procedure**

1. From the navigation panel, selectAutomation Content→Remotes.
1. Find the remote you want to sync from and click the pencil icon![Edit](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.5-Managing_automation_content-en-US/images/e5cb7f9b0cfe60ab5ba421bd17ecbb6a/leftpencil.png)
to edit.
1. Find the field labeled **Requirements file** . There, you can either paste the contents of your requirements file, or upload the file from your hard drive by selecting the upload button.
1. ClickSave remote.
1. To begin synchronization, from the navigation panel selectAutomation Content→Repositories.
1. In the row containing the repository you want to sync, click the ⋮ icon and select the![Sync repository](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.5-Managing_automation_content-en-US/images/8ca24410ba90c880998d13dfe67a52b0/sync.png)
**Sync repository** icon to initiate the remote repository synchronization to your private automation hub.
1. On the modal that appears, you can toggle the following options:


-  **Mirror** : Select if you want your repository content to mirror the remote repository’s content.
-  **Optimize** : Select if you want to sync only when no changes are reported by the remote server.

1. ClickSyncto complete the sync.


**Verification**

The **Sync status** column updates to notify you whether the synchronization is successful.


- Navigate toAutomation Content→Collectionsto confirm that your collections content has synchronized successfully.



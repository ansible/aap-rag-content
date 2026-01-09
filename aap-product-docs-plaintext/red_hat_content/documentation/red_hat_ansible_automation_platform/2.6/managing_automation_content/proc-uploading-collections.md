# 2. Managing collections in automation hub
## 2.1. Managing namespaces
### 2.1.4. Uploading collections to a namespace




Upload internally-developed collections in `tar.gz` file format to your private automation hub namespace for review and approval by an automation hub administrator. When approved, the collection moves to the **Published** content repository where automation hub users can view and download it.

Note
Format your collection file name as follows: <my_namespace-my_collection-1.0.0.tar.gz>



**Prerequisites**

- You have a namespace to which you can upload the collection.


Important
Attempting to upload very large collections will result in an error.

Limit collection size to 20 mb when uploading to Ansible Galaxy or console.redhat.com. For private automation hub avoid uploading collections sized 200 mb or more.

In scenarios that require a complete environment with multiple collections and dependencies, use an execution environment. See [Pulling execution environments for use in automation hub](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/managing_automation_content/managing-containers-hub#obtain-images) for more information.



**Procedure**

1. Log in to Ansible Automation Platform.
1. From the navigation panel, selectAutomation Content→Namespacesand select a namespace.
1. Select the **Collections** tab.
1. ClickUpload collection.
1. ClickBrowsenext to the **Collection file** field.
1. Select the collection to upload.
1. Select one of the following options:


-  **Staging repos**
-  **Repositories without pipeline**

1. ClickUpload collection.


**Verification**

To verify whether the collection uploaded successfully or if it failed, navigate toAutomation Content→Namespacesand click theMore Actionsicon **⋮** , then select **Imports** . There you will find a summary of tests indicating whether the import was successful.



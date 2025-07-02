# 2. Managing collections in automation hub
## 2.1. Using namespaces to manage collections in automation hub
### 2.1.4. Uploading collections to your namespaces




You can upload internally developed collections in `tar.gz` file format to your private automation hub namespace for review and approval by an automation hub administrator. When approved, the collection moves to the **Published** content repository where automation hub users can view and download it.

Note
Format your collection file name as follows: <my_namespace-my_collection-1.0.0.tar.gz>



**Prerequisites**

- You have a namespace to which you can upload the collection.


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



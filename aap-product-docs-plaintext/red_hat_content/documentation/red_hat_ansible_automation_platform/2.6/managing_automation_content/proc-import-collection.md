# 2. Managing collections in automation hub
## 2.6. Exporting and importing collections in automation hub
### 2.6.2. Importing an automation content collection in automation hub




As an automation content creator, you can import a collection to use in a custom repository. To use a collection in your custom repository, you must first import the collection into your namespace so the automation hub administrator can approve it.

**Procedure**

1. Log in to Ansible Automation Platform.
1. From the navigation panel, selectAutomation Content→Namespaces. The **Namespaces** page displays all of the namespaces available.
1. Select the namespace to which you want to add your collection.
1. Select the **Collections** tab.
1. ClickUpload Collection.
1. Enter or browse to select a collection file.
1. Select the repository pipeline to add the collection. The choices are **Staging repos** and **Repositories without pipeline** .
1. ClickUpload collection.

The **Imports** screen displays a summary of tests and notifies you if the collection upload is successful or has failed. To find your imports, on your namespace click theMore Actionsicon **⋮** and select **Imports** .

Note
If the collection is not approved, it is not displayed in the published repository.






**Additional resources**

-  [Approval pipeline for custom repositories in automation hub](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/managing_automation_content/managing-collections-hub#con-approval-pipeline)



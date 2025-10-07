# 2. Managing collections in automation hub
## 2.1. Using namespaces to manage collections in automation hub
### 2.1.6. Deleting a collection




You can further manage your collections by deleting unwanted collections, if the collection is not dependent on other collections. The **Dependencies** tab on a collection displays a list of other collections that use the current collection.

**Prerequisites**

- The collection being deleted does not have dependencies with other collections.
- You have **Delete Collections** permissions.


**Procedure**

1. Log in to your Ansible Automation Platform.
1. From the navigation panel, selectAutomation Content→Collections.
1. Before deleting the collection, check to see if it has collections that are dependent on it:


- Click the **Dependencies** tab for that collection. If it is blank, you will be able to delete the collection. If the **Dependencies** tab is not blank, you must delete these dependencies before you can delete the collection.

1. Click the collection to delete.
1. Click theMore Actionsicon **⋮** , and then select an option:


1.  **Delete version from system** removes the specific version of the collection from the entire instance, including all repositories and namespaces.
1.  **Delete version from repository** removes the specific version of the collection from the repository where it was uploaded. This does not affect the collection in other repositories or namespaces.
1.  **Delete entire collection from repository** removes all versions of the entire collection from the repository where it was uploaded, but does not affect other repositories or namespaces.
1.  **Delete entire collection from system** removes all versions of the entire collection from the instance, including all repositories and namespaces.

1. When the confirmation window opens, verify that the collection or version number is correct, and then select **Delete** .



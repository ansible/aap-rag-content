# Manage collection access and permissions with namespaces
## Delete a collection

You can further manage your collections by deleting content, if the content has no dependencies.

### Before you begin

- The content being deleted does not have dependencies with other content.
- You have **Delete Collections** permissions.

### About this task

The **Dependencies** tab on a collection displays a list of other collections that use the current collection.

### Procedure

1.  Log in to your Ansible Automation Platform.
2.  From the navigation panel, select Automation Content> (and then)Collections.
3.  Before deleting the collection, check to see if it has collections that are dependent on it:

- Click the **Dependencies** tab for that collection. If it is blank, you will be able to delete the collection. If the **Dependencies** tab is not blank, you must delete these dependencies before you can delete the collection.

4.  Click the collection to delete.
5.  Click the More Actions icon **⋮**, and then select an option:
1.  **Delete version from system** removes the specific version of the collection from the entire instance, including all repositories and namespaces.
2.  **Delete version from repository** removes the specific version of the collection from the repository where it was uploaded. This does not affect the collection in other repositories or namespaces.
3.  **Delete entire collection from repository** removes all versions of the entire collection from the repository where it was uploaded, but does not affect other repositories or namespaces.
4.  **Delete entire collection from system** removes all versions of the entire collection from the instance, including all repositories and namespaces.
6.  When the confirmation window opens, verify that the collection or version number is correct, and then select **Delete**.


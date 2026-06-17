# 2. Managing collections in automation hub
## 2.1. Managing namespaces
### 2.1.7. Deleting a namespace

You can delete unwanted namespaces to manage storage on your automation hub server. You must first ensure that the namespace you want to delete does not contain a collection with dependencies.

**Prerequisites**

- The namespace you are deleting does not have a collection with dependencies.
- You have **Delete namespace** permissions.

**Procedure**

1. Log in to your Ansible Automation Platform.

2. From the navigation panel, select Automation Content → Namespaces.

3. Click the namespace to be deleted.

4. Click the More Actions icon **⋮**, then click Delete namespace.


Note
If the Delete namespace button is disabled, the namespace contains a collection with dependencies. Review the collections in this namespace, and delete any dependencies.

**Result**

The namespace that you deleted, as well as its associated collections, is now deleted and removed from the namespace list view.


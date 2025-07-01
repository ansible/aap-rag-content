# 3. Getting started as an automation developer
## 3.6. Publishing to a collection
### 3.6.1. Uploading a collection to automation hub




If you want to share a collection that you have created with the rest of the Ansible community, you can upload it to automation hub.

Note
Sharing a collection with the Ansible community requires getting the collection certified or validated by our Partner Engineering team. This action is available only to partner clients. For more about becoming a partner, see our [documentation on software certification](https://connect.redhat.com/en/partner-resources/software-certification-documentation) .



You can upload your collection by using either the automation hub user interface or the `ansible-galaxy` client.

**Prerequisites**

- You have configured the `    ansible-galaxy` client for automation hub.
- You have at least one namespace.
- You have run all content through `    ansible-test sanity`


**Procedure**

1. From the navigation panel, selectAutomation Content→Namespaces.
1. Within the My namespaces tab, locate and click into the namespace to which you want to upload a collection.
1. Select the **Collections** tab, and then clickUpload collection.
1. In the New collection modal, click **Select file** . Locate the file on your system.
1. ClickUpload.


Using the `ansible-galaxy` client, enter the following command:

```
$ ansible-galaxy collection publish path/to/my_namespace-my_collection-1.0.0.tar.gz --api-key=SECRET
```


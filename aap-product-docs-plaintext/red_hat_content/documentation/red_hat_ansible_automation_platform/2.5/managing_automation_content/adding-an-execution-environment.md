# 3. Manage containers in private automation hub
## 3.6. Working with signed containers
### 3.6.3. Adding and signing an execution environment




Automation execution environments are container images that make it possible to incorporate system-level dependencies and collection-based content. Each execution environment allows you to have a customized image to run jobs, and each of them contain only what you need when running the job.

**Procedure**

1. From the navigation panel, selectAutomation Content→Execution Environments.
1. ClickCreate execution environmentand enter the relevant information in the fields that appear.


1. The **Name** field displays the name of the execution environment on your local registry.
1. The **Upstream name** field is the name of the image on the remote server.
1. Under **Registry** , select the name of the registry from the drop-down menu.
1. Optional: Enter tags in the **Add tag(s) to include** field. If the field is blank, all the tags are passed. You must specify which repository-specific tags to pass.
1. Optional: Enter tags to exclude in the **Add tag(s) to exclude** field.

1. ClickCreate execution environment. You should see your new execution environment in the list that appears.
1. Sync and sign your new automation execution environment.


1. Click theMore Actionsicon **⋮** and select **Sync execution environment** .
1. Click theMore Actionsicon **⋮** and select **Sign execution environment** .

1. Click on your new execution environment. On the Details page, find the **Signed** label to determine that your execution environment has been signed.



# 5. Inventory File Importing
## 5.1. Source control management inventory source fields




You can use a source control management (SCM) system, such as Git, to manage your inventory files in automation controller. You can use an SCM system to version control your inventory files and manage them in a collaborative manner.

The source fields used are:

-  `    source_project` : the project to use.
-  `    source_path` : the relative path inside the project indicating a directory or a file. If left blank, "" is still a relative path indicating the root directory of the project.
-  `    source_vars` : if set on a "file" type inventory source then they are passed to the environment variables when running.


Additionally:

- An update of the project automatically triggers an inventory update where it is used.
- An update of the project is scheduled immediately after creation of the inventory source.
- Neither inventory nor project updates are blocked while a related job is running.
- In cases where you have a large project (around 10 GB), disk space on `    /tmp` can be an issue.


You can specify a location manually in the automation controller UI from the **Add source** page of an inventory. Refer to [Adding a source](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/using_automation_execution/controller-inventories#proc-controller-add-source) for instructions on creating an inventory source.

When you update a project, refresh the listing to use the latest source control management (SCM) information. If no inventory sources use a project as an SCM inventory source, then the inventory listing might not be refreshed on update.

For inventories with SCM sources, the job **Details** page for inventory updates displays a status indicator for the project update and the name of the project.

The status indicator links to the project update job.

The project name links to the project.

You can perform an inventory update while a related job is running.


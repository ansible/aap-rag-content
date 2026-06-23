# Delete an Ansible development workspace
## Delete an Ansible development workspace

To delete the contents of an Ansible development workspace, you delete the workspace itself. This action removes all the pods, storage, and other resources associated with that specific workspace, effectively wiping its contents.

### Before you begin

- You know the name of the workspace you want to delete.

### About this task

### Procedure

1.  Stop the Ansible development workspace that you want to delete.

- To stop the workspace in the Dev Spaces dashboard, select the workspace that you want to delete and select actions> (and then)Stop Workspace.
- To stop the workspace using OpenShift `oc` commands, follow the steps in [Stopping workspaces](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/latest/html-single/user_guide/index#managing-workspaces-with-apis-stopping-workspaces) in the Red Hat OpenShift Dev Spaces *User Guide*.

2.  Delete the workspace:

- To delete the workspace from the Dev Spaces dashboard, select the workspace that you want to delete and select actions> (and then)Delete Workspace.
- To delete a workspace using OpenShift `oc` commands, follow the steps in [Removing workspaces](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/latest/html-single/user_guide/index#managing-workspaces-with-apis-removing-workspaces) in the Red Hat OpenShift Dev Spaces *User Guide*.


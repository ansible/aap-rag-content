# Deprovision individual nodes or groups
## Deprovision instance groups in a containerized deployment
### Before you begin

Deprovisioning nodes removes them from the mesh. For instance groups, you unregister the group from the controller's cluster registry by using the `awx-manage unregister_queue `command. This removes the group definition but does not deprovision its member nodes

**Prerequisites**

- You have root or sudo access to the host running the automation controller containers.
- You know the name of the instance group to remove.
- No active jobs are running on nodes that are members of the instance group.

### Procedure

1. Ensure that no jobs are currently running on instances in the group. In the automation controller UI, navigate to Automation execution> (and then)Jobsand confirm that no jobs with a status of Running or Pending are assigned to instances in the group.
2. On the primary automation controller node, run the unregister command inside the automation controller task container. Replace `<group_name>` with the name of the instance group:
`podman exec -it automation-controller-task awx-manage unregister_queue --queuename=<group_name>`

For example:

`podman exec -it automation-controller-task awx-manage unregister_queue --queuename=remote_execution_group`

3. (Optional) If the instance group contains nodes that should also be deprovisioned, deprovision each node using the procedure in <xref here>. Deprovisioning a node automatically removes its membership from any instance groups, so no specific order of operations is required.
4. Verify the instance group has been removed by checking the Instance Groups list in the automation controller UI:
Navigate to Automation execution> (and then)Infrastructure> (and then)Instance groups and confirm the group no longer appears.


# View details about mesh nodes with topology viewer

Use the **Topology View** to view node type, node health, and specific details about each node if you already have a mesh topology deployed.

To access the topology viewer from the automation controller UI, you must have **System Administrator** permissions.

For more information about automation mesh on an operator-based installation, see *Automation mesh for managed cloud or operator environments* in the Related Links section.

## Access the topology viewer

Use the following procedure to access the topology viewer from the automation controller UI.

### Procedure

1.  From the navigation panel, select Automation Execution> (and then)Infrastructure> (and then)Topology View. The **Topology View** opens and displays a graphical representation of how each receptor node links together.
2.  To adjust the zoom levels, or manipulate the graphic views, use the control icons: zoom-in (![Examine](/webassets/aem/red_hat_ansible_automation_platform/2.7/images/examine.png)), zoom-out (![Reduce](/webassets/aem/red_hat_ansible_automation_platform/2.7/images/reduce.png)), expand (![Expand](/webassets/aem/red_hat_ansible_automation_platform/2.7/images/expand.png)), and reset (![Reset](/webassets/aem/red_hat_ansible_automation_platform/2.7/images/reset.png)) on the toolbar. You can also click and drag to pan around; and scroll using your mouse or trackpad to zoom. The fit-to-screen feature automatically scales the graphic to fit on the screen and repositions it in the center. It is particularly useful when you want to see a large mesh in its entirety.

To reset the view to its default view, click the **Reset view** (![Reset](/webassets/aem/red_hat_ansible_automation_platform/2.7/images/reset.png)) icon.

3.  Refer to the **Legend** to identify the type of nodes that are represented. For VM-based installations, see [Control and execution planes](/documentation/en-us/red_hat_ansible_automation_platform/2.7/administer-assembly_planning_mesh#con-automation-mesh-node-types "Automation mesh makes use of unique node types to create both the control and execution plane. Learn more about the control and execution plane and their node types before designing your automation mesh topology.").

For operator-based installations, see [Control and execution planes](/documentation/en-us/red_hat_ansible_automation_platform/2.7/administer-assembly_planning_mesh#con-automation-mesh-node-types "Automation mesh makes use of unique node types to create both the control and execution plane. Learn more about the control and execution plane and their node types before designing your automation mesh topology.") for more information about each type of node.

The Legend shows the `node status <node_statuses>` by color, which is indicative of the health of the node. An **Error** status in the Legend includes the **Unavailable** state (as displayed in the Instances list view) plus any future error conditions encountered in later versions of automation controller.

The following link statuses are also shown in the Legend:

- **Established**: This is a link state that indicates a peer connection between nodes that are either ready, unavailable, or disabled.
- **Adding**: This is a link state indicating a peer connection between nodes that were selected to be added to the mesh topology.
- **Removing**: This is a link state indicating a peer connection between nodes that were selected to be removed from the topology.

4.  Hover over a node and the connectors highlight to show its immediate connected nodes (peers) or click a node to retrieve details about it, such as its hostname, node type, and status.
5.  Click the link for instance hostname from the details displayed to be redirected to its **Details** page that provides more information about that node, most notably for information about an `Error` status, as in the following example. You can use the **Details** page to remove the instance, run a health check on the instance on an as-needed basis, or unassign jobs from the instance. By default, jobs can be assigned to each node. However, you can disable it to exclude the node from having any jobs running on it.

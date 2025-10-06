# 13. Topology View
## 13.1. Accessing the topology viewer




Use the following procedure to access the topology viewer from the automation controller UI.

**Procedure**

1. From the navigation panel, selectAutomation Execution→Infrastructure→Topology View. The **Topology View** opens and displays a graphical representation of how each receptor node links together.
1. To adjust the zoom levels, or manipulate the graphic views, use the control icons: zoom-in (![Examine](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.6-Using_automation_execution-en-US/images/4e440067d24ca0b7a2a91901d3b3778f/examine.png)
), zoom-out (![Reduce](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.6-Using_automation_execution-en-US/images/a869019c522e92f9e0b2274236ad130d/reduce.png)
), expand (![Expand](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.6-Using_automation_execution-en-US/images/bf7534829ee13dfb84e75b5772eff8b0/expand.png)
), and reset (![Reset](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.6-Using_automation_execution-en-US/images/bf3f8223a6edfa7d88bd7ff95e57f7cc/reset.png)
) on the toolbar.

You can also click and drag to pan around; and scroll using your mouse or trackpad to zoom. The fit-to-screen feature automatically scales the graphic to fit on the screen and repositions it in the center. It is particularly useful when you want to see a large mesh in its entirety.

To reset the view to its default view, click the **Reset view** (![Reset](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.6-Using_automation_execution-en-US/images/bf3f8223a6edfa7d88bd7ff95e57f7cc/reset.png)
) icon.


1. Refer to the **Legend** to identify the type of nodes that are represented.

For VM-based installations, see [Control and execution planes](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/automation_mesh_for_vm_environments/assembly-planning-mesh#con-automation-mesh-node-types) .

For operator-based installations, see [Control and execution planes](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/automation_mesh_for_managed_cloud_or_operator_environments/assembly-planning-mesh#con-automation-mesh-node-types) for more information about each type of node.

The Legend shows the `    node status &lt;node_statuses&gt;` by color, which is indicative of the health of the node. An **Error** status in the Legend includes the **Unavailable** state (as displayed in the Instances list view) plus any future error conditions encountered in later versions of automation controller.

The following link statuses are also shown in the Legend:


-  **Established** : This is a link state that indicates a peer connection between nodes that are either ready, unavailable, or disabled.
-  **Adding** : This is a link state indicating a peer connection between nodes that were selected to be added to the mesh topology.
-  **Removing** : This is a link state indicating a peer connection between nodes that were selected to be removed from the topology.

1. Hover over a node and the connectors highlight to show its immediate connected nodes (peers) or click a node to retrieve details about it, such as its hostname, node type, and status.
1. Click the link for instance hostname from the details displayed to be redirected to its **Details** page that provides more information about that node, most notably for information about an `    Error` status, as in the following example.

You can use the **Details** page to remove the instance, run a health check on the instance on an as-needed basis, or unassign jobs from the instance. By default, jobs can be assigned to each node. However, you can disable it to exclude the node from having any jobs running on it.


1. Additional resources For more information about creating new nodes and scaling the mesh, see [Managing capacity with Instances](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/using_automation_execution/assembly-controller-instances) .



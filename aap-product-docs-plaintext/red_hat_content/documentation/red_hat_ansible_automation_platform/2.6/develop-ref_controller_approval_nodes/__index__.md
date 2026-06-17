# Configure nodes in workflow visualizer

Use an Approval node to manually pause a workflow between playbooks. This allows you to review and approve the next step within a set timeframe or advance the process immediately.

The default for the timeout is none, but you can specify the length of time before the request expires and is automatically denied. After you select and supply the information for the approval node, it displays on the graphical view with a pause icon beside it.


![Approval node](/webassets/aem/red_hat_ansible_automation_platform/2.6/images/ug-wf-approval-node.png)


The approver is anyone who meets the following criteria:

- A user that can execute the workflow job template containing the approval nodes.
- A user who has organization administrator or above privileges (for the organization associated with that workflow job template).
- A user who has the **Approve** permission explicitly assigned to them within that specific workflow job template.


If pending approval nodes are not approved within the specified time limit (if an expiration was assigned) or they are denied, then they are marked as "timed out" or "failed", and move on to the next "on fail node" or "always node". If approved, the "on success" path is taken. If you try to `POST` in the API to a node that has already been approved, denied or timed out, an error message notifies you that this action is redundant, and no further steps are taken.

The following table shows the various levels of permissions allowed on approval workflows:


![Node approval rbac](/webassets/aem/red_hat_ansible_automation_platform/2.6/images/ug-wf-node-approval-rbac.png)

## Build nodes scenarios

Learn how to manage nodes in the following scenarios.

### Procedure

1.  Click the (![Plus icon](/webassets/aem/red_hat_ansible_automation_platform/2.6/images/options_menu.png)) icon on the parent node and **Add step and link** to add a sibling node:
![Create sibling node](/webassets/aem/red_hat_ansible_automation_platform/2.6/images/ug-wf-create-sibling-node.png)
2.  Click Add step or Start (![Plus icon](/webassets/aem/red_hat_ansible_automation_platform/2.6/images/options_menu.png)) and **Add step**, to add a root node to depict a split scenario.
3.  At any node where you want to create a split scenario, hover over the node from which the split scenario begins and click the plus (![Plus icon](/webassets/aem/red_hat_ansible_automation_platform/2.6/images/options_menu.png)) icon on the parent node and **Add step and link**. This adds multiple nodes from the same parent node, creating sibling nodes.
4.  Refer to the key by clicking Legend to identify the meaning of the symbols and colors associated with the graphical depiction.  Note:
If you remove a node that has a follow-on node attached to it in a workflow with a set of sibling nodes that has varying edge types, the attached node automatically joins the set of sibling nodes and retains its edge type:

## Edit a node

Learn how to edit a node’s details or link edge type (Run on success/fail/always) and remove links within a workflow, and how to adjust the workflow diagram’s view.

### Procedure

-  Edit a node by using one of these methods:

* If you want to edit a node, click the icon of the node. The pane displays the current selections, click Edit to change these. Make your changes and click Finish to apply them to the graphical view.
* To edit the edge type for an existing link, (**Run on success**, **Run on fail**, **Run always**), click (![Plus icon](/webassets/aem/red_hat_ansible_automation_platform/2.6/images/options_menu.png)) on the existing status.
* To remove a link, click (![Plus icon](/webassets/aem/red_hat_ansible_automation_platform/2.6/images/options_menu.png)) for the link and click Remove link. This option only appears in the pane if the target or child node has more than one parent. All nodes must be linked to at least one other node at all times so you must create a new link before removing an old one.

-  Edit the view of the workflow diagram by using one of these methods:

* Click the examine icon (![Examine icon 15](/webassets/aem/red_hat_ansible_automation_platform/2.6/images/examine.png)) to zoom in, the reduce icon (![Reduce icon 15](/webassets/aem/red_hat_ansible_automation_platform/2.6/images/reduce.png)) to zoom out, the expand icon (![Expand icon 15](/webassets/aem/red_hat_ansible_automation_platform/2.6/images/expand.png)) to fit to screen or the reset icon (![Reset icon 15](/webassets/aem/red_hat_ansible_automation_platform/2.6/images/reset.png)) to reposition the view.
* Drag the workflow diagram to reposition it on the screen or use the scroll on your mouse to zoom.

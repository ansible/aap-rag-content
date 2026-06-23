# Configure nodes in workflow visualizer

Use an Approval node to manually pause a workflow between playbooks. This allows you to review and approve the next step within a set timeframe or advance the process immediately.

The default for the timeout is none, but you can specify the length of time before the request expires and is automatically denied. After you select and supply the information for the approval node, it displays on the graphical view with a pause icon beside it.


![Approval node](/webassets/aem/red_hat_ansible_automation_platform/2.7/images/ug-wf-approval-node.png)


The approver is anyone who meets the following criteria:

- A user that can execute the workflow job template containing the approval nodes.
- A user who has organization administrator or above privileges (for the organization associated with that workflow job template).
- A user who has the **Approve** permission explicitly assigned to them within that specific workflow job template.


If pending approval nodes are not approved within the specified time limit (if an expiration was assigned) or they are denied, then they are marked as "timed out" or "failed", and move on to the next "on fail node" or "always node". If approved, the "on success" path is taken. If you try to `POST` in the API to a node that has already been approved, denied or timed out, an error message notifies you that this action is redundant, and no further steps are taken.

The following table shows the various levels of permissions allowed on approval workflows:


![Node approval rbac](/webassets/aem/red_hat_ansible_automation_platform/2.7/images/ug-wf-node-approval-rbac.png)


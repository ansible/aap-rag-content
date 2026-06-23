# Understand how to configure workflows
## Workflow scenarios and considerations

Workflows in automation controller allow you to string together multiple job templates and other workflows into a single job run. This section describes several workflow scenarios and considerations to remember when building workflows.

When building workflows, consider the following:

- A root node is set to **ALWAYS** by default and cannot be edited.

![Node always](/webassets/aem/red_hat_ansible_automation_platform/2.7/images/ug-wf-root-node-always.png)


- A node can have multiple parents, and children can be linked to any of the states of success, failure, or always. If always, then the state is neither success nor failure. States apply at the node level, not at the workflow job template level. A workflow job is marked as successful unless it is canceled or encounters an error.

![Sibling nodes all edge types](/webassets/aem/red_hat_ansible_automation_platform/2.7/images/ug-wf-sibling-nodes-all-edge-types.png)


- If you remove a job or workflow template within the workflow, the nodes previously connected to those deleted, automatically get connected upstream and retain the edge type as in the following example:

![Node delete scenario](/webassets/aem/red_hat_ansible_automation_platform/2.7/images/ug-wf-node-delete-scenario.png)


- You can have a convergent workflow, where multiple jobs converge into one. In this scenario, any of the jobs or all of them must complete before the next one runs, as shown in the following example:
![Node convergence](/webassets/aem/red_hat_ansible_automation_platform/2.7/images/ug-wf-node-convergence.png)
* In this example, automation controller runs the first two job templates in parallel. When they both finish and succeed as specified, the third downstream (convergence node), triggers.
- Prompts for inventory and surveys apply to workflow nodes in workflow job templates.
- If you launch from the API, running a `get` command displays a list of warnings and highlights missing components. The following image illustrates a basic workflow for a workflow job template:

![Workflow diagram](/webassets/aem/red_hat_ansible_automation_platform/2.7/images/ug-workflow-diagram.png)


- It is possible to launch several workflows simultaneously, and set a schedule for when to launch them. You can set notifications on workflows, such as when a job completes, similar to that of job templates.


Note:

Job slicing is intended to scale job executions horizontally.

If you enable job slicing on a job template, it divides the inventory to be acted on in the number of slices configured at launch time. Then starts a job for each slice.

For more information see the Job slicing section.

- You can build a recursive workflow, but if automation controller detects an error, it stops at the time the nested workflow attempts to run.
- Artifacts gathered in jobs in the sub-workflow are passed to downstream nodes.
- An inventory can be set at the workflow level, or prompt for inventory on launch.
- When launched, all job templates in the workflow that have `ask_inventory_on_launch=true` use the workflow level inventory.
- Job templates that do not prompt for inventory ignore the workflow inventory and run against their own inventory.
- If a workflow prompts for inventory, schedules and other workflow nodes can provide the inventory.
- In a workflow convergence scenario, `set_stats` data is merged in an undefined way, therefore you must set unique keys.


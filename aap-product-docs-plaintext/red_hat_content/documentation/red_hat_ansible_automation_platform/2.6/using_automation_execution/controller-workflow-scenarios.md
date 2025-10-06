# 9. Workflows in automation controller
## 9.1. Workflow scenarios and considerations




When building workflows, consider the following:

- A root node is set to **ALWAYS** by default and cannot be edited.


![Node always](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.6-Using_automation_execution-en-US/images/71c6075603f005b4b10ea880c15ba7c7/ug-wf-root-node-always.png)


- A node can have multiple parents, and children can be linked to any of the states of success, failure, or always. If always, then the state is neither success nor failure. States apply at the node level, not at the workflow job template level. A workflow job is marked as successful unless it is canceled or encounters an error.


![Sibling nodes all edge types](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.6-Using_automation_execution-en-US/images/e92956b67c87f6a8dec17f19f0282599/ug-wf-sibling-nodes-all-edge-types.png)


- If you remove a job or workflow template within the workflow, the nodes previously connected to those deleted, automatically get connected upstream and retain the edge type as in the following example:


![Node delete scenario](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.6-Using_automation_execution-en-US/images/dba76ade8b6f5d084840518c9f400c56/ug-wf-node-delete-scenario.png)


- You can have a convergent workflow, where multiple jobs converge into one. In this scenario, any of the jobs or all of them must complete before the next one runs, as shown in the following example:

![Node convergence](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.6-Using_automation_execution-en-US/images/02c5e7a0d70768afa79cd69cf9b2e756/ug-wf-node-convergence.png)



- In this example, automation controller runs the first two job templates in parallel. When they both finish and succeed as specified, the third downstream (convergence node), triggers.

- Prompts for inventory and surveys apply to workflow nodes in workflow job templates.
- If you launch from the API, running a `    get` command displays a list of warnings and highlights missing components. The following image illustrates a basic workflow for a workflow job template:


![Workflow diagram](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.6-Using_automation_execution-en-US/images/59ef716602a45c64711d56684d20c4a3/ug-workflow-diagram.png)


- It is possible to launch several workflows simultaneously, and set a schedule for when to launch them. You can set notifications on workflows, such as when a job completes, similar to that of job templates.


Note
Job slicing is intended to scale job executions horizontally.

If you enable job slicing on a job template, it divides the inventory to be acted on in the number of slices configured at launch time. Then starts a job for each slice.

For more information see the [Job slicing](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html-single/using_automation_execution/index#controller-job-slicing) section.



- You can build a recursive workflow, but if automation controller detects an error, it stops at the time the nested workflow attempts to run.
- Artifacts gathered in jobs in the sub-workflow are passed to downstream nodes.
- An inventory can be set at the workflow level, or prompt for inventory on launch.
- When launched, all job templates in the workflow that have `    ask_inventory_on_launch=true` use the workflow level inventory.
- Job templates that do not prompt for inventory ignore the workflow inventory and run against their own inventory.
- If a workflow prompts for inventory, schedules and other workflow nodes can provide the inventory.
- In a workflow convergence scenario, `    set_stats` data is merged in an undefined way, therefore you must set unique keys.



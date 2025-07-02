# 8. Workflow job templates
## 8.7. Workflow visualizer
### 8.7.1. Building a workflow




You can set up any combination of two or more of the following node types to build a workflow:

- Template (Job Template or Workflow Job Template)
- Project Sync
- Inventory Sync
- Approval


**Procedure**

1. To launch the workflow visualizer, use one of these methods:


- From the navigation panel, selectAutomation Execution→Templates.


- Select a workflow template and clickView workflow visualizer.

- From the **Automation Templates** list view, click the![Visualizer](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.5-Using_automation_execution-en-US/images/1dca9a5e84ebe1b6ed13d956d77cca6e/visualizer.png)
icon next to a workflow job template.

1. ClickAdd stepto display a list of nodes to add to your workflow.
1. From the **Node type** list, select the type of node that you want to add.


- If you select an **Approval** node, see [Approval nodes](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/using_automation_execution/index#controller-approval-nodes) for more information.

Selecting a node provides the available valid options associated with it.

Note
If you select a job template that does not have a default inventory when populating a workflow graph, the inventory of the parent workflow is used. Though a credential is not required in a job template, you cannot select a job template for your workflow if it has a credential that requires a password, unless the credential is replaced by a prompted credential.





1. When you select a node type, the workflow begins to build, and you must specify the type of action to be taken for the selected node. This action is also referred to as edge type.
1. If the node is a root node, the edge type defaults to **Always** and is non-editable. For subsequent nodes, you can select one of the following scenarios (edge type) to apply to each:


-  **Always run** : Continue to execute regardless of success or failure.
-  **Run on success** : After successful completion, execute the next template.
-  **Run on fail** : After failure, execute a different template.

1. Select the behavior of the node if it is a convergent node from the **Convergence** field:


-  **Any** is the default behavior, allowing any of the nodes to complete as specified, before triggering the next converging node. If the status of one parent meets one of those run conditions, an **any** child node will run. An **any** node requires all nodes to complete, but only one node must complete with the expected outcome.
- Choose **All** to ensure that all nodes complete as specified, before converging and triggering the next node. The purpose of **all** * nodes is to make sure that every parent meets its expected outcome to run the child node. The workflow checks to make sure every parent behaves as expected to run the child node. Otherwise, it will not run the child node.

If selected, the node is labeled as **ALL** in the graphical view:

![Convergent node all](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.5-Using_automation_execution-en-US/images/8d554f3c21bf7ce4a995a923fcc6be47/ug-wf-editor-convergent-node-all.png)


Note
If a node is a root node, or a node that does not have any nodes converging into it, setting the Convergence rule does not apply, as its behavior is dictated by the action that triggers it.





1. If a job template used in the workflow has **Prompt on launch** selected for any of its parameters, aPROMPToption appears, enabling you to change those values at the node level. Use the wizard to change the values in each of the tabs and clickConfirmin the **Preview** tab.

If a workflow template used in the workflow has **Prompt on launch** selected for the inventory option, use the wizard to supply the inventory at the prompt. If the parent workflow has its own inventory, it overrides any inventory that is supplied here.

Note
For workflow job templates with required fields that prompt details, but do not have a default, you must give those values when creating a node before the **SELECT** option is enabled.

The following two cases disable theSELECToption until a value is provided by thePROMPToption:


1. When you select the **Prompt on launch** checkbox in a workflow job template, but do not give a default.
1. When you create a survey question that is required but do not give a default answer.
However, this is not the case with credentials. Credentials that require a password on launch are not permitted when creating a workflow node, because everything required to launch the node must be provided when the node is created. If you are prompted for credentials in a workflow job template, it is not possible to select a credential that requires a password in automation controller.

You must also clickSELECTwhen the prompt wizard closes, to apply the changes at that node. Otherwise, any changes you make revert back to the values set in the job template.



When the node is created, it is labeled with its job type. A template that is associated with each workflow node runs based on the selected run scenario as it proceeds. ClickLegendto display the legend for each run scenario and their job types.

![Workflow dropdown list](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.5-Using_automation_execution-en-US/images/44457cc9bbd0a536ece1605d7fa5d34c/ug-wf-dropdown-list.png)



1. Hover over a node to edit the node, add step and link, or delete the selected node:

Note
If you hover over a step when adding a link and a red border appears, this means that you cannot connect those two steps together. This is a preventive measure to avoid users creating "circular dependencies", which can result in a workflow that ends up in an infinite loop and never finishes.



![Node options](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.5-Using_automation_execution-en-US/images/684d806593055c5c5771359665d8ca15/ug-wf-add-template.png)



1. When you have added or edited a node, clickFinishto save any modifications and render it on the graphical view. For possible ways to build your workflow, see [Building nodes scenarios](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/using_automation_execution/index#controller-building-nodes-scenarios) .
1. When you have built your workflow job template, clickSaveto save your entire workflow template and return to the new workflow job template details page.


Important
ClickingClosedoes not save your work, but instead, it closes the entire Workflow Visualizer so that you have to start again.




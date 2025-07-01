# 1. Automation controller overview
## 1.16. Workflow enhancements




To model your complex provisioning, deployment, and orchestration workflows, you can use automation controller expanded workflows in several ways:

-  **Inventory overrides for Workflows** You can override an inventory across a workflow at workflow definition time, or at launch time. Use automation controller to define your application deployment workflows, and then re-use them in many environments.
-  **Convergence nodes for Workflows** When modeling complex processes, you must sometimes wait for many steps to finish before proceeding. Automation controller workflows can replicate this; workflow steps can wait for any number of earlier workflow steps to complete properly before proceeding.
-  **Workflow Nesting** You can re-use individual workflows as components of a larger workflow. Examples include combining provisioning and application deployment workflows into a single workflow.
-  **Workflow Pause and Approval** You can build workflows containing approval nodes that require user intervention. This makes it possible to pause workflows in between playbooks so that a user can give approval (or denial) for continuing on to the next step in the workflow.


For more information, see [Workflows in automation controller](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/using_automation_execution/index#controller-workflows) .


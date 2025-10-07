# 3. Ansible Automation Platform security automation use cases
## 3.2. Patch automation with Ansible Automation Platform
### 3.2.3. Complex patching scenarios




In Ansible Automation Platform, multiple automation jobs can be chained together into workflows, which can be used to coordinate multiple steps in a complex patching scenario.

The following example complex patching scenario demonstrates taking virtual machine snapshots, patching the virtual machines, and creating tickets when an error is encountered in the workflow.

1. Run a project sync to ensure the latest playbooks are available. In parallel, run an inventory sync to make sure the latest list of target hosts is available.
1. Take a snapshot of each target host.


1. If the snapshot task fails, submit a ticket with the relevant information.

1. Patch each of the target hosts.


1. If the patching task fails, restore the snapshot and submit a ticket with the relevant information.

1. Delete each snapshot where the patching task was successful.


The following workflow visualization shows how the components of the example complex patching scenario are executed:

![Workflow representation](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.5-Implementing_security_automation-en-US/images/12acc5e4d3f82e24ae62e14736879c6e/workflow.png)


**Additional resources**

-  [Workflows in automation controller](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/using_automation_execution/controller-workflows)



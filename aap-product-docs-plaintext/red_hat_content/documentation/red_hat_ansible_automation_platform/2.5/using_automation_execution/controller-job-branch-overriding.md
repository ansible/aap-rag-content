# 5. Jobs in automation controller
## 5.5. Job branch overriding




Projects specify the branch, tag, or reference to use from source control in the `scm_branch` field. These are represented by the values specified in the **Type Details** fields:

![Project branching emphasized](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.5-Using_automation_execution-en-US/images/0ba4c940a0b89d4fffe04a22f80d5094/ug-scm-project-branching-emphasized.png)


When creating or editing a job you have the option to **Allow branch override** . When this option is checked, project administrators can delegate branch selection to the job templates that use that project, requiring only project `use_role` .


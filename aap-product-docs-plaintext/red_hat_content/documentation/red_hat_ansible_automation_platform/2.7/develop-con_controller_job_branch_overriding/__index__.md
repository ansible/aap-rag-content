# Advanced configuration for jobs tied to source control management systems

In automation controller, you can configure projects to allow job templates to override the branch, tag, or reference used for source control.

Projects specify the branch, tag, or reference to use from source control in the `scm_branch` field. These are represented by the values specified in the **Type Details** fields:


![Project branching emphasized](/webassets/aem/red_hat_ansible_automation_platform/2.7/images/ug-scm-project-branching-emphasized.png)


When creating or editing a job you have the option to **Allow branch override**. When this option is checked, project administrators can delegate branch selection to the job templates that use that project, requiring only project `use_role`.


# 2. Automation mesh for operator-based Red Hat Ansible Automation Platform
## 2.6. Running jobs on execution nodes




You must specify where jobs are run, or they default to running in the control cluster.

To do this, set up a Job Template.

For more information on Job Templates, see [Job templates](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/using_automation_execution/controller-job-templates) in _Using automation execution_ .

**Procedure**

1. The **Templates** list view shows job templates that are currently available. From this screen you can launch![Launch](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.6-Automation_mesh_for_managed_cloud_or_operator_environments-en-US/images/15376a8ac10d1efa9ec8cb3d4c707dfd/rightrocket.png)
, edit![Edoit](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.6-Automation_mesh_for_managed_cloud_or_operator_environments-en-US/images/e5cb7f9b0cfe60ab5ba421bd17ecbb6a/leftpencil.png)
, and duplicate![Duplicate](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.6-Automation_mesh_for_managed_cloud_or_operator_environments-en-US/images/df17e3afcfb728d4887b97e8605bd65c/copy.png)
a workflow job template.
1. Select the job you want and click the![Launch](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.6-Automation_mesh_for_managed_cloud_or_operator_environments-en-US/images/15376a8ac10d1efa9ec8cb3d4c707dfd/rightrocket.png)
icon.
1. Select the **Instance Group** on which you want to run the job. Note that a System Administrator must grant you or your team permissions to be able to use an instance group in a job template. If you select multiple jobs templates, the order in which you select them sets the execution precedence.
1. ClickNext.
1. ClickLaunch.



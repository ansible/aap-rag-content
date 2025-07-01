# 4. Management Jobs
## 4.2. Cleanup Expired OAuth2 Tokens
### 4.2.2. Removing Old Job History




To remove job history older than a specified number of days, click the launch![Launch](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.5-Configuring_automation_execution-en-US/images/15376a8ac10d1efa9ec8cb3d4c707dfd/rightrocket.png)
icon beside **Cleanup Job Details** .

![management jobs - cleanup job launch](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.5-Configuring_automation_execution-en-US/images/230d4569158709df3f1afd0706549ee9/management-jobs-cleanup-job-launch.png)


Enter the number of days of data you want to save and clickLaunch.

Note
The initial job run for an automation controller resource, such as Projects, or Job Templates, are excluded from **Cleanup Job Details** , regardless of retention value.



You can review or set a schedule for cleaning up old job history by performing the same procedure described for activity stream management jobs.

For more information, see [Scheduling deletion](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/configuring_automation_execution/index#proc-controller-scheduling-deletion) .

You can also set or review notifications associated with this management job in the same way as described in [Notifications](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/configuring_automation_execution/index#proc-controller-management-notifications) for activity stream management jobs, or for more information, see [Notifiers](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/using_automation_execution/controller-notifications) in _Using automation execution_ .


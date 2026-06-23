# Determine where automation runs with instance groups
## Create an instance group

You can create instance groups with Automation controller to organize and manage your instances.

### About this task

Use the following procedure to create a new instance group.

### Procedure

1.  From the navigation panel, select Automation Execution> (and then)Infrastructure> (and then)Instance Groups.
2.  Click Create group and select **Create instance group** from the list.
3.  Enter the appropriate details into the following fields:

- **Name**: Names must be unique and must not be named "controller".
- **Policy instance minimum**: Enter the minimum number of instances to automatically assign to this group when new instances come online.
- **Policy instance percentage**: Use the slider to select a minimum percentage of instances to automatically assign to this group when new instances come online.  Note:
Policy instance fields are not required to create a new instance group. If you do not specify values, then the **Policy instance minimum** and **Policy instance percentage** default to 0.

- **Max concurrent jobs**: Specify the maximum number of forks that can be run for any given job.
- **Max forks**: Specify the maximum number of concurrent jobs that can be run for any given job.  Note:
The default value of 0 for **Max concurrent jobs** and **Max forks** denotes no limit. For more information, see [Instance group capacity limits](/documentation/en-us/red_hat_ansible_automation_platform/2.7/administer-con_controller_configure_instance_groups#controller-instance-group-capacity "There is external business logic that can drive the need to limit the concurrency of jobs sent to an instance group, or the maximum number of forks to be consumed.").

4.  Click Create instance group, or, if you have edited an existing Instance Group click Save instance group

### What to do next

When you have successfully created the instance group the **Details** tab of the newly created instance group enables you to review and edit your instance group information.

You can also edit **Instances** and review **Jobs** associated with this instance group:


![Instance group successfully created](/webassets/aem/red_hat_ansible_automation_platform/2.7/images/ug-instance-group-created.png)


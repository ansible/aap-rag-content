# 2. Automation mesh for operator-based Red Hat Ansible Automation Platform
## 2.4. Creating an instance group




You can create instance groups with Automation controller to organize and manage your instances.

Use the following procedure to create a new instance group.

**Procedure**

1. From the navigation panel, selectAutomation Execution→Infrastructure→Instance Groups.
1. ClickCreate groupand select **Create instance group** from the list.
1. Enter the appropriate details into the following fields:


-  **Name** : Names must be unique and must not be named "controller".
-  **Policy instance minimum** : Enter the minimum number of instances to automatically assign to this group when new instances come online.
-  **Policy instance percentage** : Use the slider to select a minimum percentage of instances to automatically assign to this group when new instances come online.

Note
Policy instance fields are not required to create a new instance group. If you do not specify values, then the **Policy instance minimum** and **Policy instance percentage** default to 0.




-  **Max concurrent jobs** : Specify the maximum number of forks that can be run for any given job.
-  **Max forks** : Specify the maximum number of concurrent jobs that can be run for any given job.

Note
The default value of 0 for **Max concurrent jobs** and **Max forks** denotes no limit. For more information, see [Instance group capacity limits](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/using_automation_execution/index#controller-instance-group-capacity) .





1. ClickCreate instance group, or, if you have edited an existing Instance Group clickSave instance group


**Next steps**

When you have successfully created the instance group the **Details** tab of the newly created instance group enables you to review and edit your instance group information.


You can also edit **Instances** and review **Jobs** associated with this instance group:

![Instance group successfully created](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.6-Automation_mesh_for_managed_cloud_or_operator_environments-en-US/images/25e41a55f53db73a847cf8df31d972ca/ug-instance-group-created.png)



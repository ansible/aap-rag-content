# Configure instance groups from the API
## Deprovision instance groups

Re-running the setup playbook won't deprovision instances, as clusters can't distinguish between intentional offline status or failure. Instead, shut down all services on the automation controller instance, then run the deprovisioning tool from another instance.

### Procedure

1.  Shut down the instance or stop the service with the following command:


```
automation-controller-service stop
```

2.  Run the following deprovision command from another instance to remove it from the controller cluster registry:


```
awx-manage deprovision_instance --hostname=<name used in inventory file>
```
For example:

```
awx-manage deprovision_instance --hostname=hostB
```

### What to do next

Deprovisioning instance groups in automation controller does not automatically deprovision or remove instance groups, even though re-provisioning often causes these to be unused. They can still show up in API endpoints and stats monitoring. You can remove these groups with the following command:

```
awx-manage unregister_queue --queuename=<name>
```
Removing an instance’s membership from an instance group in the inventory file and re-running the setup playbook does not ensure that the instance is not added back to a group. To be sure that an instance is not added back to a group, remove it through the API and also remove it in your inventory file. You can also stop defining instance groups in the inventory file. You can manage instance group topology through the automation controller UI. For more information about managing instance groups in the UI, see [Managing Instance Groups](/documentation/en-us/red_hat_ansible_automation_platform/2.7/administer-assembly_ug_controller_instance_groups#controller-instance-groups "An Instance Group enables you to group instances in a clustered environment. Policies dictate how instance groups behave and how jobs are executed. The following view displays the capacity levels based on policy algorithms:").

Note:

If you have isolated instance groups created in older versions of automation controller (3.8.x and earlier) and want to migrate them to execution nodes to make them compatible for use with the automation mesh architecture, see [Migrate isolated instances to execution nodes](https://legacy-controller-docs.ansible.com/automation-controller/4.4/html/upgrade-migration-guide/upgrade_to_ees.html#migrate-iso-to-exe) in the *Ansible Automation Platform Upgrade and Migration Guide*.

# Determine where automation runs with instance groups

An Instance Group enables you to group instances in a clustered environment. Policies dictate how instance groups behave and how jobs are executed. The following view displays the capacity levels based on policy algorithms:


![Instance groups list view](/webassets/aem/red_hat_ansible_automation_platform/2.7/images/ug-instance-groups-list-view.png)

## Instance groups

Instances can be grouped into one or more instance groups. Instance groups can be assigned to one or more of the following listed resources:

- Organizations
- Inventories
- Job templates


When a job associated with one of the resources executes, it is assigned to the instance group associated with the resource. During the execution process, instance groups associated with job templates are checked before those associated with inventories. Instance groups associated with inventories are checked before those associated with organizations. Therefore, instance group assignments for the three resources form the hierarchy:

**Job Template > Inventory > Organization**

Consider the following when working with instance groups:

- You can define other groups and group instances in those groups. These groups must be prefixed with `instance_group_`. Instances are required to be in the `automationcontroller` or `execution_nodes` group alongside other `instance_group_` groups. In a clustered setup, at least one instance must be present in the `automationcontroller` group, which is displayed as `controlplane` in the API instance groups.

- You cannot modify the `controlplane` instance group, and attempting to do so results in a permission denied error for any user. Therefore, the **Disassociate** option is not available in the **Instances** tab of `controlplane`.

- A `default` API instance group is automatically created with all nodes capable of running jobs. This is similar to any other instance group but if a specific instance group is not associated with a specific resource, then the job execution always falls back to the default instance group. The default instance group always exists, and you cannot delete or rename it.

- Do not create a group named `instance_group_default`.

- Do not name any instance the same as a group name.

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

## Associate instances to an instance group

Learn how to associate instances to an instance group in automation controller.

### Procedure

1.  Select the **Instances** tab on the **Details** page of an Instance Group.
2.  Click Associate instance.
3.  Click the checkbox next to one or more available instances from the list to select the instances you want to associate with the instance group and click Confirm

## View jobs associated with an instance group

You can view jobs associated with an instance group to monitor their status and details.

### Procedure

1.  Select the **Jobs** tab of the **Instance Group** window.
2.  Click the arrow ![Arrow](/webassets/aem/red_hat_ansible_automation_platform/2.7/images/arrow.png) icon next to a job to expand the view and show details about each job. Each job displays the following details:

- The job status
- The ID and name
- The type of job
- The time it started and completed
- Who started the job and applicable resources associated with it, such as the template, inventory, project, and execution environment

## Control where an automation job runs

Use instance groups to control job execution locations. While the controller automatically selects groups based on capacity, you can override this by associating groups with job templates, inventories, or organizations.

When a job is launched, automation controller checks for any instance groups associated with the job template, inventory, or organization (by way of project) in that order.

If you associate instance groups with a job template, inventory, or organization, a job run from that job template is not eligible for the default behavior. This means that if all of the instances inside of the instance groups associated with these three resources are out of capacity, the job remains in the pending state until capacity becomes available.

The order of preference in determining which instance group to submit the job to is as follows:

1. Job template
2. Inventory
3. Organization (by way of project)


If you associate instance groups with the job template, and all of these are at capacity, then the job is submitted to instance groups specified on the inventory, and then the organization. Jobs must run in those groups in preferential order as resources are available.

You can still associate the global `default` group with a resource, such as any of the custom instance groups defined in the playbook. You can use this to specify a preferred instance group on the job template or inventory, but still enable the job to be submitted to any instance if those are out of capacity.

- If you associate `group_a` with a job template and also associate the `default` group with its inventory, you enable the `default` group to be used as a fallback in case `group_a` gets out of capacity.
- In addition, it is possible to not associate an instance group with one resource but choose another resource as the fallback. For example, not associating an instance group with a job template and having it fall back to the inventory or the organization’s instance group.


This presents the following possibilities:

1. Associating instance groups with an inventory (omitting assigning the job template to an instance group) ensures that any playbook run against a specific inventory runs only on the group associated with it. This is useful in the situation where only those instances have a direct link to the managed nodes.

2. An administrator can assign instance groups to organizations. This enables the administrator to segment out the entire infrastructure and guarantee that each organization has capacity to run jobs without interfering with any other organization’s ability to run jobs.

An administrator can assign multiple groups to each organization, similar to the following scenario:

- There are three instance groups: *A*, *B*, and *C*. There are two organizations: *Org1* and *Org2*.
- The administrator assigns group *A* to *Org1*, group *B* to *Org2* and then assigns group *C* to both *Org1* and *Org2* as an overflow for any extra capacity that might be needed.
- The organization administrators are then free to assign inventory or job templates to whichever group they want, or let them inherit the default order from the organization.


![Instance groups scenarios](/webassets/aem/red_hat_ansible_automation_platform/2.7/images/ag-instance-groups-scenarios.png)


Arranging resources this way offers you flexibility. You can also create instance groups with only one instance, enabling you to direct work towards a very specific Host in the automation controller cluster.

## Define instance groups in the inventory file

Define custom instance groups in the inventory file to organize nodes in your automation mesh. By correctly assigning nodes to the `automationcontroller` or `execution_nodes` groups, you ensure the installer validates the mesh topology and prevents configuration errors.

Use the following criteria when defining nodes:

- Nodes in the `automationcontroller` group can define `node_type` hostvar to be `hybrid` (default) or `control`.
- Nodes in the `execution_nodes group` can define `node_type` hostvar to be `execution` (default) or `hop`.


You can define custom groups in the inventory file by naming groups with `instance_group_*` where `*` becomes the name of the group in the API. You can also create custom instance groups in the API after the install has finished.

The current behavior expects a member of an `instance_group_*` to be part of `automationcontroller` or `execution_nodes` group.

### Define instance groups

```
[automationcontroller]
126-addr.tatu.home ansible_host=192.168.111.126  node_type=control

[automationcontroller:vars]
peers=execution_nodes

[execution_nodes]

[instance_group_test]
110-addr.tatu.home ansible_host=192.168.111.110 receptor_listener_port=8928
```

After you run the installation program, the following error is displayed:

```
TASK [ansible.automation_platform_installer.check_config_static : Validate mesh topology] ***
fatal: [126-addr.tatu.home -> localhost]: FAILED! => {"msg": "The host '110-addr.tatu.home' is not present in either [automationcontroller] or [execution_nodes]"}
```
To fix this, move the box `110-addr.tatu.home` to an `execution_node` group, as follows:

```
[automationcontroller]
126-addr.tatu.home ansible_host=192.168.111.126  node_type=control

[automationcontroller:vars]
peers=execution_nodes

[execution_nodes]
110-addr.tatu.home ansible_host=192.168.111.110 receptor_listener_port=8928

[instance_group_test]
110-addr.tatu.home
```
This results in:

```
TASK [ansible.automation_platform_installer.check_config_static : Validate mesh topology] ***
ok: [126-addr.tatu.home -> localhost] => {"changed": false, "mesh": {"110-addr.tatu.home": {"node_type": "execution", "peers": [], "receptor_control_filename": "receptor.sock", "receptor_control_service_name": "control", "receptor_listener": true, "receptor_listener_port": 8928, "receptor_listener_protocol": "tcp", "receptor_log_level": "info"}, "126-addr.tatu.home": {"node_type": "control", "peers": ["110-addr.tatu.home"], "receptor_control_filename": "receptor.sock", "receptor_control_service_name": "control", "receptor_listener": false, "receptor_listener_port": 27199, "receptor_listener_protocol": "tcp", "receptor_log_level": "info"}}}
```
After upgrading from automation controller 4.0 or earlier, the legacy `instance_group_` member likely has the awx code installed. This places that node in the `automationcontroller` group.

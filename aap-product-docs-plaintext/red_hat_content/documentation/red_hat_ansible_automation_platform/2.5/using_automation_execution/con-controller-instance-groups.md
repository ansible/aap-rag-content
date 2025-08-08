# 18. Instance and container groups
## 18.1. Instance groups




Instances can be grouped into one or more instance groups. Instance groups can be assigned to one or more of the following listed resources:

- Organizations
- Inventories
- Job templates


When a job associated with one of the resources executes, it is assigned to the instance group associated with the resource. During the execution process, instance groups associated with job templates are checked before those associated with inventories. Instance groups associated with inventories are checked before those associated with organizations. Therefore, instance group assignments for the three resources form the hierarchy:

**Job Template > Inventory > Organization**

Consider the following when working with instance groups:

- You can define other groups and group instances in those groups. These groups must be prefixed with `    instance_group_` . Instances are required to be in the `    automationcontroller` or `    execution_nodes` group alongside other `    instance_group_` groups. In a clustered setup, at least one instance must be present in the `    automationcontroller` group, which appears as `    controlplane` in the API instance groups. For more information and example scenarios, see [Group policies for automationcontroller](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/using_automation_execution/controller-instance-and-container-groups.xml#controller-group-policies-automationcontroller) .
- You cannot modify the `    controlplane` instance group, and attempting to do so results in a permission denied error for any user.

Therefore, the **Disassociate** option is not available in the **Instances** tab of `    controlplane` .


- A `    default` API instance group is automatically created with all nodes capable of running jobs. This is like any other instance group but if a specific instance group is not associated with a specific resource, then the job execution always falls back to the default instance group. The default instance group always exists, and you cannot delete or rename it.
- Do not create a group named `    instance_group_default` .
- Do not name any instance the same as a group name.


### 18.1.1. Group policies for `automationcontroller`




Use the following criteria when defining nodes:

- Nodes in the `    automationcontroller` group can define `    node_type` hostvar to be `    hybrid` (default) or `    control` .
- Nodes in the `    execution_nodes group` can define `    node_type` hostvar to be `    execution` (default) or `    hop` .


You can define custom groups in the inventory file by naming groups with `instance_group_*` where `*` becomes the name of the group in the API. You can also create custom instance groups in the API after the install has finished.

The current behavior expects a member of an `instance_group_*` to be part of `automationcontroller` or `execution_nodes` group.


<span id="idm140389991662192"></span>
**Example 18.1. Define instance groups**

```
[automationcontroller]
126-addr.tatu.home ansible_host=192.168.111.126  node_type=control

[automationcontroller:vars]
peers=execution_nodes

[execution_nodes]

[instance_group_test]
110-addr.tatu.home ansible_host=192.168.111.110 receptor_listener_port=8928
```




After you run the installation program, the following error appears:

```
TASK [ansible.automation_platform_installer.check_config_static : Validate mesh topology] ***
fatal: [126-addr.tatu.home -&gt; localhost]: FAILED! =&gt; {"msg": "The host '110-addr.tatu.home' is not present in either [automationcontroller] or [execution_nodes]"}
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
ok: [126-addr.tatu.home -&gt; localhost] =&gt; {"changed": false, "mesh": {"110-addr.tatu.home": {"node_type": "execution", "peers": [], "receptor_control_filename": "receptor.sock", "receptor_control_service_name": "control", "receptor_listener": true, "receptor_listener_port": 8928, "receptor_listener_protocol": "tcp", "receptor_log_level": "info"}, "126-addr.tatu.home": {"node_type": "control", "peers": ["110-addr.tatu.home"], "receptor_control_filename": "receptor.sock", "receptor_control_service_name": "control", "receptor_listener": false, "receptor_listener_port": 27199, "receptor_listener_protocol": "tcp", "receptor_log_level": "info"}}}
```

After upgrading from automation controller 4.0 or earlier, the legacy `instance_group_` member likely has the awx code installed. This places that node in the `automationcontroller` group.

### 18.1.2. Configure instance groups from the API




You can create instance groups by POSTing to `/api/v2/instance_groups` as a system administrator.

Once created, you can associate instances with an instance group using:

```
HTTP POST /api/v2/instance_groups/x/instances/ {'id': y}`
```

An instance that is added to an instance group automatically reconfigures itself to listen on the group’s work queue. For more information, see [Instance group policies](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/using_automation_execution/controller-instance-and-container-groups#controller-instance-group-policies) .

### 18.1.3. Instance group policies




You can configure automation controller instances to automatically join instance groups when they come online by defining a policy. These policies are evaluated for every new instance that comes online.

Instance group policies are controlled by the following three optional fields on an `Instance Group` :

-  `    policy_instance_percentage` : This is a number between 0 - 100. It guarantees that this percentage of active automation controller instances are added to this instance group. As new instances come online, if the number of instances in this group relative to the total number of instances is less than the given percentage, then new ones are added until the percentage condition is satisfied.
-  `    policy_instance_minimum` : This policy attempts to keep at least this many instances in the instance group. If the number of available instances is lower than this minimum, then all instances are placed in this instance group.
-  `    policy_instance_list` : This is a fixed list of instance names to always include in this instance group.


The **Instance Groups** list view from the automation controller user interface (UI) provides a summary of the capacity levels for each instance group according to instance group policies:

![Instance Groups list view](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.5-Using_automation_execution-en-US/images/90794892ff0f11c2385ec26264fdf7eb/ug-instance-groups_list_view.png)


**Additional resources**

For more information, see the [Managing Instance Groups](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/using_automation_execution/index#controller-instance-groups) section.


### 18.1.4. Notable policy considerations




Take the following policy considerations into account:

- Both `    policy_instance_percentage` and `    policy_instance_minimum` set minimum allocations. The rule that results in more instances assigned to the group takes effect.

For example, if you have a `    policy_instance_percentage` of 50% and a `    policy_instance_minimum` of 2 and you start 6 instances, 3 of them are assigned to the instance group.

If you reduce the number of total instances in the cluster to 2, then both of them are assigned to the instance group to satisfy `    policy_instance_minimum` . This enables you to set a lower limit on the amount of available resources.


- Policies do not actively prevent instances from being associated with multiple instance groups, but this can be achieved by making the percentages add up to 100.

If you have 4 instance groups, assign each a percentage value of 25 and the instances are distributed among them without any overlap.




### 18.1.5. Pinning instances manually to specific groups




If you have a special instance which needs to be only assigned to a specific instance group but do not want it to automatically join other groups by "percentage" or "minimum" policies:

**Procedure**

1. Add the instance to one or more instance groups' `    policy_instance_list` .
1. Update the instance’s `    managed_by_policy` property to be `    False` .


This prevents the instance from being automatically added to other groups based on percentage and minimum policy. It only belongs to the groups you have manually assigned it to:

```
HTTP PATCH /api/v2/instance_groups/N/
{
"policy_instance_list": ["special-instance"]
}
HTTP PATCH /api/v2/instances/X/
{
"managed_by_policy": False
}
```

### 18.1.6. Job runtime behavior




When you run a job associated with an instance group, note the following behaviors:

- If you divide a cluster into separate instance groups, then the behavior is similar to the cluster as a whole.
- If you assign two instances to a group then either one is as likely to receive a job as any other in the same group.
- As automation controller instances are brought online, it effectively expands the work capacity of the system.
- If you place those instances into instance groups, then they also expand that group’s capacity.
- If an instance is performing work and it is a member of multiple groups, then capacity is reduced from all groups for which it is a member.
- De-provisioning an instance removes capacity from the cluster wherever that instance was assigned. For more information, see the [Deprovisioning instance groups](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/using_automation_execution/controller-instance-and-container-groups#controller-deprovision-instance-group) section.


Note
Not all instances are required to be provisioned with an equal capacity.



### 18.1.7. Control where a job runs




If you associate instance groups with a job template, inventory, or organization, a job run from that job template is not eligible for the default behavior. This means that if all of the instances inside of the instance groups associated with these three resources are out of capacity, the job remains in the pending state until capacity becomes available.

The order of preference in determining which instance group to submit the job to is as follows:

1. Job template
1. Inventory
1. Organization (by way of project)


If you associate instance groups with the job template, and all of these are at capacity, then the job is submitted to instance groups specified on the inventory, and then the organization. Jobs must execute in those groups in preferential order as resources are available.

You can still associate the global `default` group with a resource, such as any of the custom instance groups defined in the playbook. You can use this to specify a preferred instance group on the job template or inventory, but still enable the job to be submitted to any instance if those are out of capacity.

- If you associate `    group_a` with a job template and also associate the `    default` group with its inventory, you enable the `    default` group to be used as a fallback in case `    group_a` gets out of capacity.
- In addition, it is possible to not associate an instance group with one resource but choose another resource as the fallback. For example, not associating an instance group with a job template and having it fall back to the inventory or the organization’s instance group.


This presents the following possibilites:

1. Associating instance groups with an inventory (omitting assigning the job template to an instance group) ensures that any playbook run against a specific inventory runs only on the group associated with it. This is useful in the situation where only those instances have a direct link to the managed nodes.
1. An administrator can assign instance groups to organizations.

This enables the administrator to segment out the entire infrastructure and guarantee that each organization has capacity to run jobs without interfering with any other organization’s ability to run jobs.

An administrator can assign multiple groups to each organization, similar to the following scenario:


- There are three instance groups: _A_ , _B_ , and _C_ . There are two organizations: _Org1_ and _Org2_ .
- The administrator assigns group _A_ to _Org1_ , group _B_ to _Org2_ and then assigns group _C_ to both _Org1_ and _Org2_ as an overflow for any extra capacity that might be needed.
- The organization administrators are then free to assign inventory or job templates to whichever group they want, or let them inherit the default order from the organization.



![Instance groups scenarios](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.5-Using_automation_execution-en-US/images/9005be8db10fa90f02db83c07c3e96ca/ag-instance-groups-scenarios.png)


Arranging resources this way offers you flexibility. You can also create instance groups with only one instance, enabling you to direct work towards a very specific Host in the automation controller cluster.

### 18.1.8. Instance group capacity limits




There is external business logic that can drive the need to limit the concurrency of jobs sent to an instance group, or the maximum number of forks to be consumed.

For traditional instances and instance groups, you might want to enable two organizations to run jobs on the same underlying instances, but limit each organization’s total number of concurrent jobs. This can be achieved by creating an instance group for each organization and assigning the value for `max_concurrent_jobs` .

For automation controller groups, automation controller is generally not aware of the resource limits of the OpenShift cluster. You can set limits on the number of pods on a namespace, or only resources available to schedule a certain number of pods at a time if no auto-scaling is in place. In this case, you can adjust the value for `max_concurrent_jobs` .

Another parameter available is `max_forks` . This provides additional flexibility for capping the capacity consumed on an instance group or container group. You can use this if jobs with a wide variety of inventory sizes and "forks" values are being run. You can limit an organization to run up to 10 jobs concurrently, but consume no more than 50 forks at a time:

```
max_concurrent_jobs: 10
max_forks: 50
```

If 10 jobs that use 5 forks each are run, an eleventh job waits until one of these finishes to run on that group (or be scheduled on a different group with capacity).

If 2 jobs are running with 20 forks each, then a third job with a `task_impact` of 11 or more waits until one of these finishes to run on that group (or be scheduled on a different group with capacity).

For container groups, using the `max_forks` value is useful given that all jobs are submitted using the same `pod_spec` with the same resource requests, irrespective of the "forks" value of the job. The default `pod_spec` sets requests and not limits, so the pods can "burst" above their requested value without being throttled or reaped. By setting the `max_forks value` , you can help prevent a scenario where too many jobs with large forks values get scheduled concurrently and cause the OpenShift nodes to be oversubscribed with multiple pods using more resources than their requested value.

To set the maximum values for the concurrent jobs and forks in an instance group, see [Creating an instance group](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/using_automation_execution/controller-instance-groups#controller-create-instance-group) .

### 18.1.9. Deprovisioning instance groups




Re-running the setup playbook does not deprovision instances since clusters do not currently distinguish between an instance that you took offline intentionally or due to failure. Instead, shut down all services on the automation controller instance and then run the deprovisioning tool from any other instance.

**Procedure**

1. Shut down the instance or stop the service with the following command:


```
automation-controller-service stop
```


1. Run the following deprovision command from another instance to remove it from the controller cluster registry:


```
awx-manage deprovision_instance --hostname=&lt;name used in inventory file&gt;
```

For example




```
awx-manage deprovision_instance --hostname=hostB
```

Deprovisioning instance groups in automation controller does not automatically deprovision or remove instance groups, even though re-provisioning often causes these to be unused. They can still show up in API endpoints and stats monitoring. You can remove these groups with the following command:

```
awx-manage unregister_queue --queuename=&lt;name&gt;
```

Removing an instance’s membership from an instance group in the inventory file and re-running the setup playbook does not ensure that the instance is not added back to a group. To be sure that an instance is not added back to a group, remove it through the API and also remove it in your inventory file. You can also stop defining instance groups in the inventory file. You can manage instance group topology through the automation controller UI. For more information about managing instance groups in the UI, see [Managing Instance Groups](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/using_automation_execution/index#controller-instance-groups) .

Note
If you have isolated instance groups created in older versions of automation controller (3.8.x and earlier) and want to migrate them to execution nodes to make them compatible for use with the automation mesh architecture, see [Migrate isolated instances to execution nodes](https://docs.ansible.com/automation-controller/4.4/html/upgrade-migration-guide/upgrade_to_ees.html#migrate-iso-to-exe) in the _Ansible Automation Platform Upgrade and Migration Guide_ .



## 18.2. Container groups




Ansible Automation Platform supports container groups, which enable you to run jobs in automation controller regardless of whether automation controller is installed as a standalone, in a virtual environment, or in a container.

Container groups act as a pool of resources within a virtual environment.

You can create instance groups to point to an OpenShift container. These are job environments that are provisioned on-demand as a pod that exists only for the duration of the playbook run. This is known as the ephemeral execution model and ensures a clean environment for every job run.

In some cases, you might want to set container groups to be "always-on", which you can configure through the creation of an instance.

Note
Container groups upgraded from versions before automation controller 4.0 revert back to default and remove the old pod definition, clearing out all custom pod definitions in the migration.



Container groups are different from execution environments in that execution environments are container images and do not use a virtual environment. For more information, see [Execution environments](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/using_automation_execution/assembly-controller-execution-environments) .

### 18.2.1. Creating a container group




A `ContainerGroup` is a type of `InstanceGroup` that has an associated credential that enables you to connect to an OpenShift cluster.

**Prerequisites**

- A namespace that you can launch into. Every cluster has a "default" namespace, but you can use a specific namespace.
- A service account that has the roles that enable it to launch and manage pods in this namespace. For more information, see [Creating a service account in OpenShift Container Platform or Kubernetes](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/using_automation_execution/controller-instance-and-container-groups#controller-create-service-account) .
- If you are using execution environments in a private registry, and have a container registry credential associated with them in automation controller, the service account also needs the roles to get, create, and delete secrets in the namespace. If you do not want to give these roles to the service account, you can pre-create the `    ImagePullSecrets` and specify them on the pod spec for the `    ContainerGroup` . In this case, the execution environment must not have a container registry credential associated, or automation controller attempts to create the secret for you in the namespace.
- A token associated with that service account. An OpenShift or Kubernetes Bearer Token.
- A CA certificate associated with the cluster.


**Procedure**

1. From the navigation panel, selectAutomation Execution→Infrastructure→Instance Groups.
1. ClickCreate groupand select **Create container group** .
1. Enter a name for your new container group and select the credential you created before to associate it to the container group.
1. ClickCreate container group.
1. Check the **Customize pod spec** box and edit the **Pod spec override** to include the namespace and service account name that you used in the previous steps.


### 18.2.2. Creating a service account in OpenShift Container Platform or Kubernetes




Use service accounts in an OpenShift cluster or Kubernetes to run jobs in a container group through automation controller. After the service account is created, its credentials are provided to automation controller in the form of an OpenShift or Kubernetes API Bearer Token credential.

**Procedure**

1. To create a service account, download and use the following sample service account example, `    containergroup sa` and change it as required to obtain the credentials:


```
---    apiVersion: v1    kind: ServiceAccount    metadata:      name: containergroup-service-account      namespace: containergroup-namespace    ---    kind: Role    apiVersion: rbac.authorization.k8s.io/v1    metadata:      name: role-containergroup-service-account      namespace: containergroup-namespace    rules:      - verbs:          - get          - list          - watch          - create          - update          - patch          - delete        apiGroups:          - ''        resources:          - pods      - verbs:          - get        apiGroups:          - ''        resources:          - pods/log      - verbs:          - create        apiGroups:          - ''        resources:          - pods/attach      - verbs:          - get          - create          - delete        apiGroups:          - ''        resources:          - secrets    ---    kind: RoleBinding    apiVersion: rbac.authorization.k8s.io/v1    metadata:      name: role-containergroup-service-account-binding      namespace: containergroup-namespace    subjects:    - kind: ServiceAccount      name: containergroup-service-account      namespace: containergroup-namespace    roleRef:      kind: Role      name: role-containergroup-service-account      apiGroup: rbac.authorization.k8s.io
```


1. Apply the configuration from `    containergroup-sa.yml` :


```
oc apply -f containergroup-sa.yml
```


1. Get an API token by generating a service account token:


```
oc create token containergroup-service-account --duration=$((365*24))h &gt; containergroup-sa.token
```


1. Get the CA certificate:


```
oc get secret -n openshift-ingress wildcard-tls -o jsonpath='{.data.ca\.crt}' | base64 -d &gt; containergroup-ca.crt
```


1. Use the contents of `    containergroup-sa.token` and `    containergroup-ca.crt` to provide the information for the [OpenShift or Kubernetes API Bearer Token](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/using_automation_execution/controller-instance-and-container-groups#controller-create-service-account) required for the container group.


To create a container group, create a [OpenShift or Kubernetes API Bearer Token](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/using_automation_execution/controller-instance-and-container-groups#controller-create-service-account) credential to use with your container group. For more information, see [Creating new credentials](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/using_automation_execution/controller-credentials#controller-create-credential) .

### 18.2.3. Customizing the pod specification




Ansible Automation Platform provides a simple default pod specification, however, you can provide a custom YAML or JSON document that overrides the default pod specification. This field uses any custom fields such as `ImagePullSecrets` , that can be "serialized" as valid pod JSON or YAML. A full list of options can be found in the [Pods and Services](https://docs.openshift.com/online/pro/architecture/core_concepts/pods_and_services.html) section of the OpenShift documentation.

**Procedure**

1. From the navigation panel, selectAutomation Execution→Infrastructure→Instance Groups.
1. ClickCreate groupand select **Create container group** .
1. Check the option for **Customize pod spec** .
1. Enter a custom Kubernetes or OpenShift Pod specification in the **Pod spec override** field.

![Customize pod specification](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.5-Using_automation_execution-en-US/images/d996389a7a5466c2db742bc8e29cbef4/ag-instance-group-customize-cg-pod.png)



1. ClickCreate container group.


Note
The image when a job launches is determined by which execution environment is associated with the job. If you associate a container registry credential with the execution environment, then automation controller attempts to make an `ImagePullSecret` to pull the image. If you prefer not to give the service account permission to manage secrets, you must pre-create the `ImagePullSecret` and specify it on the pod specification, and omit any credential from the execution environment used.

For more information, see the [Allowing Pods to Reference Images from Other Secured Registries](https://access.redhat.com/RegistryAuthentication#allowing-pods-to-reference-images-from-other-secured-registries-8) section of the _Red Hat Container Registry Authentication_ article.



Once you have created the container group successfully, the **Details** tab of the newly created container group remains, which enables you to review and edit your container group information. This is the same menu that is opened if you click the![Edit](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.5-Using_automation_execution-en-US/images/e5cb7f9b0cfe60ab5ba421bd17ecbb6a/leftpencil.png)
icon from the **Instance Groups** list view.

You can also edit **Instances** and review **Jobs** associated with this instance group.

![Instance group successfully created](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.5-Using_automation_execution-en-US/images/dadcc869d6759fdd4454ca5dad03c70b/ag-instance-group-successfully-created.png)


Container groups and instance groups are labeled accordingly.

### 18.2.4. Verifying container group functions




To verify the deployment and termination of your container:

**Procedure**

1. Create a mock inventory and associate the container group to it by populating the name of the container group in the **Instance groups** field. For more information, see [Add a new inventory](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/using_automation_execution/controller-inventories#proc-controller-adding-new-inventory) .

![Create test inventory](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.5-Using_automation_execution-en-US/images/cb9aa2b00da6b771e9bbb2f738186dd0/ag-inventories-create-new-test-inventory.png)



1. Create the `    localhost` host in the inventory with the following variables:


```
{'ansible_host': '127.0.0.1', 'ansible_connection': 'local'}
```


1. Launch an ad hoc job against the localhost using the _ping_ or _setup_ module. Even though the **Machine Credential** field is required, it does not matter which one is selected for this test:

![Launch ad hoc localhost](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.5-Using_automation_execution-en-US/images/848e6b0b251411a13de50917cc60483c/ag-inventories-launch-adhoc-localhost.png)


![Launch ad hoc localhost 2](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.5-Using_automation_execution-en-US/images/439e92914965f2dd56e80a9fc615aaaf/ag-inventories-launch-adhoc-localhost2.png)





You can see in the **Jobs** details view that the container was reached successfully by using one of the ad hoc jobs.

If you have an OpenShift UI, you can see pods appear and disappear as they deploy and end. You can also use the CLI to perform a `get pod` operation on your namespace to watch these same events occurring in real-time.

### 18.2.5. Viewing container group jobs




When you run a job associated with a container group, you can see the details of that job in the **Details** tab. You can also view its associated container group and the execution environment that spun up.

**Procedure**

1. From the navigation panel, selectAutomation Execution→Jobs.
1. Click a job for which you want to view a container group job.
1. Click the **Details** tab.


![Instance group job details](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.5-Using_automation_execution-en-US/images/5bb0843f3f72143000f0fe6dcf123e4a/ag-instance-group-job-details.png)


### 18.2.6. Kubernetes API failure conditions




When running a container group and the Kubernetes API responds that the resource quota has been exceeded, automation controller keeps the job in pending state. Other failures result in the traceback of the **Error Details** field showing the failure reason, similar to the following example:

```
Error creating pod: pods is forbidden: User "system: serviceaccount: aap:example" cannot create resource "pods" in API group "" in the namespace "aap"
```

### 18.2.7. Container capacity limits




Capacity limits and quotas for containers are defined by objects in the Kubernetes API:

- To set limits on all pods within a given namespace, use the `    LimitRange` object. For more information see the [Quotas and Limit Ranges](https://docs.openshift.com/online/pro/dev_guide/compute_resources.html#overview) section of the OpenShift documentation.
- To set limits directly on the pod definition launched by automation controller, see [Customizing the pod specification](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/using_automation_execution/controller-instance-and-container-groups#controller-customize-pod-spec) and the [Compute Resources](https://docs.openshift.com/online/pro/dev_guide/compute_resources.html#dev-compute-resources) section of the OpenShift documentation.


Note
Container groups do not use the capacity algorithm that normal nodes use. You need to set the number of forks at the job template level. If you configure forks in automation controller, that setting is passed along to the container.



# Chapter 19. Managing capacity with Instances




Scaling your automation mesh is available on OpenShift deployments of Red Hat Ansible Automation Platform and is possible through adding or removing nodes from your cluster dynamically, using the **Instances** resource of the UI, without running the installation script.

Instances serve as nodes in your mesh topology. Automation mesh enables you to extend the footprint of your automation. The location where you launch a job can be different from the location where the ansible-playbook runs.

To manage instances from the UI, you must have System Administrator or System Auditor permissions.

In general, the more processor cores (CPU) and memory (RAM) a node has, the more jobs that can be scheduled to run on that node at once.

For more information, see [Automation controller capacity determination and job impact](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/using_automation_execution/index#controller-capacity-determination) .

## 19.1. Prerequisites




The automation mesh is dependent on hop and execution nodes running on _Red Hat Enterprise Linux_ (RHEL). Your Red Hat Ansible Automation Platform subscription grants you ten Red Hat Enterprise Linux licenses that can be used for running components of Ansible Automation Platform.

For more information about Red Hat Enterprise Linux subscriptions, see [Registering the system and managing subscriptions](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/configuring_basic_system_settings/assembly_registering-the-system-and-managing-subscriptions_configuring-basic-system-settings) in the Red Hat Enterprise Linux documentation.

The following steps prepare the RHEL instances for deployment of the automation mesh.

1. You require a Red Hat Enterprise Linux operating system. Each node in the mesh requires a static IP address, or a resolvable DNS hostname that Ansible Automation Platform can access.
1. Ensure that you have the minimum requirements for the RHEL virtual machine before proceeding. For more information, see the [System requirements](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/planning_your_installation/platform-system-requirements) .
1. Deploy the RHEL instances within the remote networks where communication is required. For information about creating virtual machines, see [Creating Virtual Machines](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/configuring_and_managing_virtualization/assembly_creating-virtual-machines_configuring-and-managing-virtualization) in the _Red Hat Enterprise Linux_ documentation. Remember to scale the capacity of your virtual machines sufficiently so that your proposed tasks can run on them.


- RHEL ISOs can be obtained from access.redhat.com.
- RHEL cloud images can be built using Image Builder from console.redhat.com.



## 19.2. Pulling the secret




If you are using the default execution environment (provided with automation controller) to run on remote execution nodes, you must add a pull secret in the automation controller that contains the credential for pulling the execution environment image.

To do this, create a pull secret on the automation controller namespace and configure the `ee_pull_credentials_secret` parameter in the Operator as follows:

**Procedure**

1. Create a secret:


```
oc create secret generic ee-pull-secret \         --from-literal=username=&lt;username&gt; \         --from-literal=password=&lt;password&gt; \         --from-literal=url=registry.redhat.io            oc edit automationcontrollers &lt;instance name&gt;
```


1. Add `    ee_pull_credentials_secret ee-pull-secret` to the specification:


```
spec.ee_pull_credentials_secret=ee-pull-secret
```




Note
To manage instances from the automation controller UI, you must have System administrator permissions.



## 19.3. Setting up Virtual Machines for use in an automation mesh




**Procedure**

1. SSH into each of the RHEL instances and perform the following steps. Depending on your network access and controls, SSH proxies or other access models might be required.

Use the following command:


```
ssh [username]@[host_ip_address]
```

For example, for an Ansible Automation Platform instance running on Amazon Web Services.


```
ssh ec2-user@10.0.0.6
```


1. Create or copy an SSH key that can be used to connect from the hop node to the execution node in later steps. This can be a temporary key used just for the automation mesh configuration, or a long-lived key. The SSH user and key are used in later steps.
1. Enable your RHEL subscription with `    baseos` and `    appstream` repositories. Ansible Automation Platform RPM repositories are only available through subscription-manager, not the _Red Hat Update Infrastructure_ (RHUI). If you attempt to use any other Linux footprint, including RHEL with RHUI, this causes errors.


```
sudo subscription-manager register --auto-attach
```

If Simple Content Access is enabled for your account, use:


```
sudo subscription-manager register
```

For more information about Simple Content Access, see [Getting started with simple content access](https://docs.redhat.com/en/documentation/subscription_central/1-latest/html/getting_started_with_simple_content_access/index) .


1. Enable Ansible Automation Platform subscriptions and the proper Red Hat Ansible Automation Platform channel:

For RHEL 8


```
# subscription-manager repos --enable ansible-automation-platform-2.5-for-rhel-8-x86_64-rpms
```

For RHEL 9


```
# subscription-manager repos --enable ansible-automation-platform-2.5-for-rhel-9-x86_64-rpms
```

For ARM


```
# subscription-manager repos --enable ansible-automation-platform-2.5-for-rhel-aarch64-rpms
```


1. Ensure the packages are up to date:


```
sudo dnf upgrade -y
```


1. Install the ansible-core packages on the machine where the downloaded bundle is to run:


```
sudo dnf install -y ansible-core
```

Note
Ansible core is required on the machine that runs the automation mesh configuration bundle playbooks. This document assumes that happens on the execution node. However, this step can be omitted if you run the playbook from a different machine. You cannot run directly from the control node, this is not currently supported, but future support expects that the control node has direct connectivity to the execution node.






## 19.4. Managing instances




To expand job capacity, create a standalone **execution node** that can be added to run alongside a deployment of automation controller. These execution nodes are not part of the automation controller Kubernetes cluster.

The control nodes run in the cluster connect and submit work to the execution nodes through Receptor.

These execution nodes are registered in automation controller as type `execution` instances, meaning they are only used to run jobs, not dispatch work or handle web requests as control nodes do.

**Hop nodes** can be added to sit between the control plane of automation controller and standalone execution nodes. These hop nodes are not part of the Kubernetes cluster and are registered in automation controller as an instance of type `hop` , meaning they only handle inbound and outbound traffic for otherwise unreachable nodes in different or more strict networks.

The following procedure demonstrates how to set the node type for the hosts.

**Procedure**

1. From the navigation panel, selectAutomation Execution→Infrastructure→Instances.
1. On the **Instances** list page, clickAdd instance. The **Add Instance** window opens.

![Create new Instance](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.5-Using_automation_execution-en-US/images/3355dec0d74db565c318375fabb769dc/instances_create_new.png)


An instance requires the following attributes:


-  **Host name** : (required) Enter a fully qualified domain name (public DNS) or IP address for your instance. This field is equivalent to `        hostname` for installer-based deployments.

Note
If the instance uses private DNS that cannot be resolved from the control cluster, DNS lookup routing fails, and the generated SSL certificates is invalid. Use the IP address instead.




- Optional: **Description** : Enter a description for the instance.
-  **Instance state** : This field is auto-populated, indicating that it is being installed, and cannot be modified.
-  **Listener port** : This port is used for the receptor to listen on for incoming connections. You can set the port to one that is appropriate for your configuration. This field is equivalent to `        listener_port` in the API. The default value is 27199, though you can set your own port value.
-  **Instance type** : Only `        execution` and `        hop` nodes can be created. Operator based deployments do not support Control or Hybrid nodes.

Options:


-  **Enable instance** : Check this box to make it available for jobs to run on an execution node.
- Check the **Managed by policy** box to enable policy to dictate how the instance is assigned.
-  **Peers from control nodes** :


- If you are configuring a hop node:


- If the hop node needs to have requests pushed directly from automation controller, then check the **Peers from Control** box.
- If the hop node is peered to another hop node, then make sure **Peers from Control** is not checked.

- If you are configuring an execution node:


- If the execution node needs to have requests pushed directly from automation controller, then check the **Peers from Control** box.
- If the execution node is peered to a hop node, then make sure that **Peers from Control** is not checked.




1. ClickAssociate peers.
1. To view a graphical representation of your updated topology, see [Topology view](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/using_automation_execution/index#assembly-controller-topology-viewer) .

Note
Complete the following steps from any computer that has SSH access to the newly created instance.




1. Click the![Download](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.5-Using_automation_execution-en-US/images/8a61e20c21c53f44e207c84d454159ec/download.png)
icon next to **Download Bundle** to download the tar file that includes this new instance and the files necessary to install the created node into the automation mesh.

The install bundle has TLS certificates and keys, a certificate authority, and a proper Receptor configuration file.


```
receptor-ca.crt    work-public-key.pem    receptor.key    install_receptor.yml    inventory.yml    group_vars/all.yml    requirements.yml
```


1. Extract the downloaded `    tar.gz` Install Bundle from the location where you downloaded it. To ensure that these files are in the correct location on the remote machine, the install bundle includes the `    install_receptor.yml` playbook.
1. Before running the `    ansible-playbook` command, edit the following fields in the `    inventory.yml` file:


```
all:      hosts:        remote-execution:          ansible_host: localhost # change to the mesh node host name              ansible_user: &lt;username&gt; # user provided              ansible_ssh_private_key_file: ~/.ssh/&lt;id_rsa&gt;
```


- Ensure `        ansible_host` is set to the IP address or DNS of the node.
- Set `        ansible_user` to the username running the installation.
- Set `        ansible_ssh_private_key_file` to contain the filename of the private key used to connect to the instance.
- The content of the `        inventory.yml` file serves as a template and contains variables for roles that are applied during the installation and configuration of a receptor node in a mesh topology. You can modify some of the other fields, or replace the file in its entirety for advanced scenarios. For more information, see [Role Variables](https://github.com/ansible/receptor-collection/blob/main/README.md) .

1. For a node that uses a private DNS, add the following line to `    inventory.yml` :


```
ansible_ssh_common_args: &lt;your ssh ProxyCommand setting&gt;
```

This instructs the `    install-receptor.yml` playbook to use the proxy command to connect through the local DNS node to the private node.


1. When the attributes are configured, clickSave. The **Details** page of the created instance opens.
1. Save the file to continue.
1. The system that is going to run the install bundle to setup the remote node and run `    ansible-playbook` requires the `    ansible.receptor` collection to be installed:


```
ansible-galaxy collection install ansible.receptor
```

or


```
ansible-galaxy install -r requirements.yml
```


- Installing the receptor collection dependency from the `        requirements.yml` file consistently retrieves the receptor version specified there. Additionally, it retrieves any other collection dependencies that might be needed in the future.
- Install the receptor collection on all nodes where your playbook will run, otherwise an error occurs.

1. If `    receptor_listener_port` is defined, the machine also requires an available open port on which to establish inbound TCP connections, for example, 27199. Run the following command to open port 27199 for receptor communication (Make sure you have port 27199 open in your firewall):


```
sudo firewall-cmd --permanent --zone=public --add-port=27199/tcp
```


1. Run the following playbook on the machine where you want to update your automation mesh:


```
ansible-playbook -i inventory.yml install_receptor.yml
```

+

Note
OpenSSL is required for this playbook. You can install it by running the following command:

```
openssl -v
```

If it returns then a version OpenSSL is installed. Otherwise you need to install OpenSSL with:

```
sudo dnf install -y openssl
```



+ After this playbook runs, your automation mesh is configured.

![Instances list view](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.5-Using_automation_execution-en-US/images/043e594ac0d2f7fcb63c477c4603dcc3/instances_list_view2.png)


Note
It might be the case that some servers do not listen on the receptor port (the default is 27199)

Suppose you have a Control plane with nodes A, B, and C

The following is a peering set up for three controller nodes:

Controller node A -→ Controller node B

Controller node A -→ Controller node C

Controller node B -→ Controller node C

You can force the listener by setting

`receptor_listener=True`

However, a connection Controller B -→ A is likely to be rejected as that connection already exists.

This means that nothing connects to Controller A as Controller A is creating the connections to the other nodes, and the following command does not return anything on Controller A:

`[root@controller1 ~]# ss -ntlp | grep 27199 [root@controller1 ~]#`

The RPM installer creates a strongly connected peering between the control plane nodes with a least privileged approach and opens the tcp listener only on those nodes where it is required. All the receptor connections are bidirectional, so once the connection is created, the receptor can communicate in both directions.



To remove an instance from the mesh, see [Removing instances](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/using_automation_execution/assembly-controller-instances#ref-removing-instances) . r

## 19.5. Removing Instances




From the **Instances** page, you can add, remove or run health checks on your nodes.

Note
You must follow the procedures for installing RHEL packages for any additional nodes you create. If you peer this additional node to an existing hop node, you must also install the Install Bundle on each node.



Use the check boxes next to an instance to select it to remove it, or run a health check against it.

Note
- If a node is removed using the UI, then the node is "removed" and does not show a status. If you delete the VM of the node before it is removed in the UI, it will show an error.
- You only need to reinstall the Install Bundle if the topology changes the communication pattern, that is, hop nodes change or you add nodes.




When a button is disabled, you do not have permission for that particular action. Contact your Administrator to grant you the required level of access.

If you are able to remove an instance, you receive a prompt for confirmation.

Note
You can still remove an instance even if it is active and jobs are running on it. Automation controller waits for jobs running on this node to complete before removing it.



# Chapter 20. Execution environments




execution environments are container images that make it possible to incorporate system-level dependencies and collection-based content. Each execution environment enables you to have a customized image to run jobs and has only what is necessary when running the job.

The default view for the **Execution Environments** page is collapsed ( **Compact** ) with the execution environment name and its image name. Selecting the execution environment name expands the entry for more information.

For each execution environment listed, you can use the![Edit](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.5-Using_automation_execution-en-US/images/e5cb7f9b0cfe60ab5ba421bd17ecbb6a/leftpencil.png)
to edit the properties for the selected execution environment or the ⋮ to duplicate the execution environment. These are also avilable from the **Details** page.

## 20.1. Build an execution environment




If your Ansible content depends on custom virtual environments instead of a default environment, you must take additional steps. You must install packages on each node that interact well with other software installed on the host system, and keep them in synchronization.

To simplify this process, you can build container images that serve as Ansible [Control nodes](https://docs.ansible.com/ansible/latest/network/getting_started/basic_concepts.html#control-node) . These container images are referred to as automation execution environments, which you can create with ansible-builder. Ansible-runner can then make use of those images.

### 20.1.1. Install ansible-builder




To build images, you must have Podman or Docker installed, along with the `ansible-builder` Python package.

The `--container-runtime` option must correspond to the Podman or Docker executable you intend to use.

When building an execution environment image, it must support the architecture that Ansible Automation Platform is deployed with.

For more information, see [Quickstart for Ansible Builder](https://ansible.readthedocs.io/projects/builder/en/latest/#quickstart-for-ansible-builder) , or [Creating and consuming execution environments](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/creating_and_using_execution_environments/index) .

### 20.1.2. Content needed for an execution environment




Ansible-builder is used to create an execution environment.

An execution environment must contain:

- Ansible
- Ansible Runner
- Ansible Collections
- Python and system dependencies of:


- modules or plugins in collections
- content in ansible-base
- custom user needs



Building a new execution environment involves a definition that specifies which content you want to include in your execution environment, such as collections, Python requirements, and system-level packages. The definition must be a .yml file

The content from the output generated from migrating to execution environments has some of the required data that can be piped to a file or pasted into this definition file.

**Additional resources**

-  [Migrate legacy venvs to execution environments](https://docs.ansible.com/automation-controller/4.4/html/upgrade-migration-guide/upgrade_to_ees.html#migrate-new-venv)
-  [Execution Environment Setup Reference](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/creating_and_using_execution_environments/index#assembly-controller-ee-setup-reference)
-  [Dependencies](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/using_automation_execution/assembly-controller-ee-setup-reference#ref-controller-dependencies)


### 20.1.3. Example YAML file to build an image




The `ansible-builder build` command takes an execution environment definition as an input. It outputs the build context necessary for building an execution environment image, and then builds that image. The image can be re-built with the build context elsewhere, and produces the same result. By default, the builder searches for a file named `execution-environment.yml` in the current directory.

The following example `execution-environment.yml` file can be used as a starting point:

```
---
version: 3
dependencies:
galaxy: requirements.yml
```

The content of `requirements.yml` :

```
---
collections:
- name: awx.awx
```

To build an execution environment using the preceding files and run the following command:

```
ansible-builder build
...
STEP 7: COMMIT my-awx-ee
--&gt; 09c930f5f6a
09c930f5f6ac329b7ddb321b144a029dbbfcc83bdfc77103968b7f6cdfc7bea2
Complete! The build context can be found at: context
```

In addition to producing a ready-to-use container image, the build context is preserved. This can be rebuilt at a different time or location with the tools of your choice, such as `docker build` or `podman build` .

**Additional resources**

For additional information about the `ansible-builder build` command, see Ansible’s [CLI Usage](https://ansible.readthedocs.io/projects/builder/en/latest/usage/#cli-usage) documentation.


### 20.1.4. Execution environment mount options




Rebuilding an execution environment is one way to add certificates, but inheriting certificates from the host provides a more convenient solution. For VM-based installations, automation controller automatically mounts the system truststore in the execution environment when jobs run.

You can customize execution environment mount options and mount paths in the **Paths to expose to isolated jobs** field of the **Job Settings** page, where Podman-style volume mount syntax is supported.

**Additional resources**

For more information, see the [Podman documentation](https://docs.podman.io/en/latest/markdown/podman-run.1.html#volume-v-source-volume-host-dir-container-dir-options) .


#### 20.1.4.1. Troubleshooting execution environment mount options




In some cases where the `/etc/ssh/*` files were added to the execution environment image due to customization of an execution environment, an SSH error can occur.

For example, exposing the `/etc/ssh/ssh_config.d:/etc/ssh/ssh_config.d:O` path enables the container to be mounted, but the ownership permissions are not mapped correctly.

Use the following procedure if you meet this error, or have upgraded from an older version of automation controller:

**Procedure**

1. Change the container ownership on the mounted volume to `    root` .
1. From the navigation panel, selectSettings→Automation Execution→Job.
1. ClickEdit.
1. Expose the path in the **Paths to expose to isolated jobs** field, using the current example:


```
[      "/ssh_config:/etc/ssh/ssh_config.d/:0"    ]
```

Note
The `    :O` option is only supported for directories. Be as detailed as possible, especially when specifying system paths. Mounting `    /etc` or `    /usr` directly has an impact that makes it difficult to troubleshoot.



This informs Podman to run a command similar to the following example, where the configuration is mounted and the `    ssh` command works as expected:


```
podman run -v /ssh_config:/etc/ssh/ssh_config.d/:O ...
```




To expose isolated paths in OpenShift or Kubernetes containers as HostPath, use the following configuration:

```
[
"/mnt2:/mnt2",
"/mnt3",
"/mnt4:/mnt4:0"
]
```

Set **Expose host paths for Container Groups** to **On** to enable it.

When the playbook runs, the resulting Pod specification is similar to the following example. Note the details of the `volumeMounts` and `volumes` sections.

![Pod specification](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.5-Using_automation_execution-en-US/images/b6af54079d861f5652516179412150d9/mount-containers-playbook-run-podspec.png)


#### 20.1.4.2. Mounting the directory in the execution node to the execution environment container




This procedure describes how to configure paths exposed to isolated jobs, allowing volumes to be mounted from execution or hybrid nodes to job containers.

**Procedure**

1. From the navigation panel, selectSettings→Automation Execution→Job.
1. Edit the **Paths to expose to isolated jobs** field:


- Enter a list of paths that volumes are mounted from the execution node or the hybrid node to the container.
- Enter one path per line.
- The supported format is `        HOST-DIR[:CONTAINER-DIR[:OPTIONS]` . The allowed paths are `        z` , `        O` , `        ro` , and `        rw` .

**Example**


```
[          "/var/lib/awx/.ssh:/root/.ssh:O"        ]
```



- For the `        rw` option, configure the SELinux label correctly. For example, to mount the `        /foo` directory, complete the following commands:


```
sudo su
```


```
mkdir /foo
```


```
chmod 777 /foo
```


```
semanage fcontext -a -t container_file_t "/foo(/.*)?"
```


```
restorecon -vvFR /foo
```





The `awx` user must be permitted to read or write in this directory at least. Set the permissions as `777` at this time.

**Additional resources**

For more information about mount volumes, see the [--volume option of the podman-run(1)](https://docs.podman.io/en/stable/markdown/podman-run.1.html#volume-v-source-volume-host-dir-container-dir-options) section of the Podman documentation.


## 20.2. Adding an execution environment to a job template




**Prerequisites**

- You must build an execution environment as described in [Build an execution environment](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/using_automation_execution/assembly-controller-execution-environments#ref-controller-build-exec-envs) before you can create it using automation controller.

After building it, you must push it to a repository (such as quay) and then, when creating an execution environment in the UI with automation controller, you must point to that repository to use it in Ansible Automation Platform to use it, for example, in a job template.


- Depending on whether an execution environment is made available for global use or tied to an organization, you must have the appropriate level of administrator privileges to use an execution environment in a job. Execution environments tied to an organization require Organization administrators to be able to run jobs with those execution environments.
- Before running a job or job template that uses an execution environment that has a credential assigned to it, ensure that the credential contains a username, host, and password.


**Procedure**

1. From the navigation panel, selectAutomation Execution→Infrastructure→Execution Environments.
1. ClickCreate execution environmentto add an execution environment.
1. Enter the appropriate details into the following fields:


-  **Name** (required): Enter a name for the execution environment.
-  **Image** (required): Enter the image name. The image name requires its full location (repository), the registry, image name, and version tag in the example format of `        quay.io/ansible/awx-ee:latestrepo/project/image-name:tag` .
- Optional: **Pull** : Choose the type of pull when running jobs:


-  **Always pull container before running** : Pulls the latest image file for the container.
-  **Only pull the image if not present before running** : Only pulls the latest image if none is specified.
-  **Never pull container before running** : Never pull the latest version of the container image.

Note
If you do not set a type for pull, the value defaults to **Only pull the image if not present before running** .





- Optional: **Description** :
- Optional: **Organization** : Assign the organization to specifically use this execution environment. To make the execution environment available for use across multiple organizations, leave this field blank.
-  **Registry Credential** : If the image has a protected container registry, give the credential to access it.

1. ClickCreate execution environment.

Your newly added execution environment is ready to be used in a job template.


1. To add an execution environment to a job template, specify it in the **Execution Environment** field of the job template.


When you have added an execution environment to a job template, those templates are listed in the **Templates** tab of the execution environment:

# Chapter 21. Execution Environment Setup Reference




This section contains reference information associated with the definition of an execution environment. You define the content of your execution environment in a YAML file. By default, this file is called `execution_environment.yml` . This file tells Ansible Builder how to create the build instruction file (Containerfile for Podman, Dockerfile for Docker) and build context for your container image.

Note
The definition schema for Ansible Builder 3.x is documented here. If you are running an older version of Ansible Builder, you need an older schema version. For more information, see older versions of [this](https://ansible.readthedocs.io/projects/builder/en/latest/) documentation. We recommend using version 3, which offers substantially more configurable options and functionality than previous versions.



## 21.1. Execution environment definition example




You must create a definition file to build an image for an execution environment. The file is in YAML format.

You must specify the version of Ansible Builder in the definition file. The default version is 1.

The following definition file is using Ansible Builder version 3:

```
version: 3
build_arg_defaults:
ANSIBLE_GALAXY_CLI_COLLECTION_OPTS: '--pre'
dependencies:
galaxy: requirements.yml
python:
- six
- psutil
system: bindep.txt
images:
base_image:
name: registry.redhat.io/ansible-automation-platform-24/ee-minimal-rhel8:latest
additional_build_files:
- src: files/ansible.cfg
dest: configs
additional_build_steps:
prepend_galaxy:
- ADD _build/configs/ansible.cfg /home/runner/.ansible.cfg
prepend_final: |
RUN whoami
RUN cat /etc/os-release
append_final:
- RUN echo This is a post-install command!
- RUN ls -la /etc
```

## 21.2. Configuration options




Use the following configuration YAML keys in your definition file.

The Ansible Builder 3.x execution environment definition file accepts seven top-level sections:

-  [additional_build_files](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/using_automation_execution/assembly-controller-ee-setup-reference#ref-controller-additional-build-files)
-  [additional_build_steps](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/using_automation_execution/assembly-controller-ee-setup-reference#ref-controller-additional-build-steps)
-  [build_arg_defaults](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/using_automation_execution/assembly-controller-ee-setup-reference#ref-controller-build-arg-defaults)
-  [dependencies](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/using_automation_execution/assembly-controller-ee-setup-reference#ref-controller-dependencies)
-  [images](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/using_automation_execution/assembly-controller-ee-setup-reference#ref-controller-images)


-  [image verification](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/using_automation_execution/assembly-controller-ee-setup-reference#ref-controller-image-verification)

-  [options](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/using_automation_execution/assembly-controller-ee-setup-reference#ref-controller-config-options)
-  [version](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/using_automation_execution/assembly-controller-ee-setup-reference#ref-controller-config-version)


### 21.2.1. additional_build_files




The build files specify what are to be added to the build context directory. These can then be referenced or copied by `additional_build_steps` during any build stage.

The format is a list of dictionary values, each with a `src` and `dest` key and value.

Each list item must be a dictionary containing the following required keys:

|  **src** | Specifies the source files to copy into the build context directory.

This can be an absolute path, for example, `/home/user/.ansible.cfg` , or a path that is relative to the file. Relative paths can be a glob expression matching one or more files, for example, `files/\*.cfg` . Note that an absolute path must not include a regular expression. If `src` is a directory, the entire contents of that directory are copied to `dest` . |
| --- | --- |
|  **dest** | Specifies a subdirectory path underneath the `_build` subdirectory of the build context directory that contains the source files, for example, `files/configs` .

This cannot be an absolute path or contain `..` within the path. This directory is created for you if it does not exist.

Note
When using an `ansible.cfg` file to pass a token and other settings for a private account to an automation hub server, listing the configuration file path here as a string enables it to be included as a build argument in the initial phase of the build. |


### 21.2.2. additional_build_steps




The build steps specify custom build commands for any build phase. These commands are inserted directly into the build instruction file for the container runtime, for example, Containerfile or Dockerfile. The commands must conform to any rules required by the containerization tool.

You can add build steps before or after any stage of the image creation process. For example, if you need `git` to be installed before you install your dependencies, you can add a build step at the end of the base build stage.

The following are the valid keys. Each supports either a multi-line string, or a list of strings.

|  **append_base** | Commands to insert after building of the base image. |
| --- | --- |
|  **append_builder** | Commands to insert after building of the builder image. |
|  **append_final** | Commands to insert after building of the final image. |
|  **append_galaxy** | Commands to insert after building of the galaxy image. |
|  **prepend_base** | Commands to insert before building of the base image. |
|  **prepend_builder** | Commands to insert before building of the builder image. |
|  **prepend_final** | Commands to insert before building of the final image. |
|  **prepend_galaxy** | Commands to insert before building of the galaxy image. |


### 21.2.3. build_arg_defaults




This specifies the default values for build arguments as a dictionary.

This is an alternative to using the `--build-arg` CLI flag.

Ansible Builder uses the following build arguments:

|  **ANSIBLE_GALAXY_CLI_COLLECTION_OPTS** | Enables the user to pass the `-pre` flag and other flags to enable the installation of pre-release collections. |
| --- | --- |
|  **ANSIBLE_GALAXY_CLI_ROLE_OPTS** | This enables the user to pass any flags, such as `--no-deps` , to the role installation. |
|  **PKGMGR_PRESERVE_CACHE** | This controls how often the package manager cache is cleared during the image build process.

If this value is not set, which is the default, the cache is cleared frequently. If the value is `always` , the cache is never cleared. Any other value forces the cache to be cleared only after the system dependencies are installed in the final build stage. |


Ansible Builder hard-codes values given inside of `build_arg_defaults` into the build instruction file, so they persist if you run your container build manually.

If you specify the same variable in the definition and at the command line with the CLI `build-arg` flag, the CLI value overrides the value in the definition.

### 21.2.4. Dependencies




Specifies dependencies to install into the final image, including `ansible-core` , `ansible-runner` , Python packages, system packages, and collections. Ansible Builder automatically installs dependencies for any Ansible collections you install.

In general, you can use standard syntax to constrain package versions. Use the same syntax you would pass to `dnf` , `pip` , `ansible-galaxy` , or any other package management utility. You can also define your packages or collections in separate files and reference those files in the `dependencies` section of your definition file.

The following keys are valid:

|  **ansible_core** | The version of the `ansible-core` Python package to be installed.

This value is a dictionary with a single key, `package_pip` . The `package_pip` value is passed directly to pip for installation and can be in any format that pip supports. The following are some example values:

```
ansible_core:
package_pip: ansible-core
ansible_core:
package_pip: ansible-core==2.14.3
ansible_core:
package_pip: https://github.com/example_user/ansible/archive/refs/heads/ansible.tar.gz
``` |
| --- | --- |
|  **ansible_runner** | The version of the Ansible Runner Python package to be installed.

This value is a dictionary with a single key, `package_pip` . The `package_pip` value is passed directly to pip for installation and can be in any format that pip supports. The following are some example values:

```
ansible_runner:
package_pip: ansible-runner
ansible_runner:
package_pip: ansible-runner==2.3.2
ansible_runner:
package_pip: https://github.com/example_user/ansible-runner/archive/refs/heads/ansible-runner.tar.gz
``` |
|  **galaxy** | Collections to be installed from Ansible Galaxy.

This can be a filename, a dictionary, or a multi-line string representation of an Ansible Galaxy `requirements.yml` file. For more information about the requirements file format, see the [Galaxy User Guide](https://docs.ansible.com/ansible/latest/galaxy/user_guide.html#install-multiple-collections-with-a-requirements-file) . |
|  **python** | The Python installation requirements.

This can be a filename, or a list of requirements. Ansible Builder combines all the Python requirements files from all collections into a single file using the `requirements-parser` library.

This library supports complex syntax, including references to other files. If many collections require the same _package name_ , Ansible Builder combines them into a single entry and combines the constraints.

Ansible Builder excludes some packages in the combined file of Python dependencies even if a collection lists them as dependencies. These include test packages and packages that provide Ansible itself. The full list can is available under `EXCLUDE_REQUIREMENTS` in `src/ansible_builder/_target_scripts/introspect.py` .

If you need to include one of these excluded package names, use the `--user-pip` option of the `introspect` command to list it in the user requirements file.

Packages supplied this way are not processed against the list of excluded Python packages. |
|  **python_interpreter** | A dictionary that defines the Python system package name to be installed by dnf ( `package_system` ) or a path to the Python interpreter to be used ( `python_path)` . |
|  **system** | The system packages to be installed, in bindep format. This can be a filename or a list of requirements.

For more information about bindep, see the [OpenDev documentation](https://docs.opendev.org/opendev/bindep/latest/readme.html) .

For system packages, use the `bindep` format to specify cross-platform requirements, so they can be installed by whichever package management system the execution environment uses. Collections must specify necessary requirements for `[platform:rpm]` . Ansible Builder combines system package entries from multiple collections into a single file. Only requirements with no profiles (runtime requirements) are installed to the image. Entries from many collections which are duplicates of each other can be consolidated in the combined file. |


The following example uses filenames that contain the various dependencies:

```
dependencies:
python: requirements.txt
system: bindep.txt
galaxy: requirements.yml
ansible_core:
package_pip: ansible-core==2.14.2
ansible_runner:
package_pip: ansible-runner==2.3.1
python_interpreter:
package_system: "python310"
python_path: "/usr/bin/python3.10"
```

This example uses inline values:

```
dependencies:
python:
- pywinrm
system:
- iputils [platform:rpm]
galaxy:
collections:
- name: community.windows
- name: ansible.utils
version: 2.10.1
ansible_core:
package_pip: ansible-core==2.14.2
ansible_runner:
package_pip: ansible-runner==2.3.1
python_interpreter:
package_system: "python310"
python_path: "/usr/bin/python3.10"
```

Note
If any of these dependency files ( `requirements.txt, bindep.txt, and requirements.yml` ) are in the `build_ignore` of the collection, the build fails.

Collection maintainers can verify that ansible-builder recognizes the requirements they expect by using the `introspect` command:

```
ansible-builder introspect --sanitize ~/.ansible/collections/
```



The `--sanitize` option reviews all of the collection requirements and removes duplicates. It also removes any Python requirements that are normally excluded (see **python** dependencies).

Use the `-v3` option to `introspect` to see logging messages about requirements that are being excluded.

### 21.2.5. images




Specifies the base image to be used. At a minimum you must specify a source, image, and tag for the base image. The base image provides the operating system and can also provide some packages. Use the standard `host/namespace/container:tag` syntax to specify images. You can use Podman or Docker shortcut syntax instead, but the full definition is more reliable and portable.

Valid keys for this section are:

|  **base_image** | A dictionary defining the parent image for the execution environment.

A `name` key must be supplied with the container image to use. Use the `signature_original_name` key if the image is mirrored within your repository, but signed with the original image’s signature key. |
| --- | --- |


### 21.2.6. Image verification




You can verify signed container images if you are using the `podman` container runtime.

Set the `container-policy` CLI option to control how this data is used in relation to a Podman `policy.json` file for container image signature validation.

-  ** `    ignore_all` ** policy: Generate a `    policy.json` file in the build `    context directory &lt;context&gt;` where no signature validation is performed.
-  ** `    system` ** policy: Signature validation is performed using pre-existing `    policy.json` files in standard system locations. `    ansible-builder` assumes no responsibility for the content within these files, and the user has complete control over the content.
-  ** `    signature_required` ** policy: `    ansible-builder` uses the container image definitions to generate a `    policy.json` file in the build `    context directory &lt;context&gt;` that is used during the build to validate the images.


### 21.2.7. options




A dictionary of keywords or options that can affect the runtime functionality Ansible Builder.

Valid keys for this section are:

-  **container_init** : A dictionary with keys that allow for customization of the container `    ENTRYPOINT` and `    CMD` directives (and related behaviors). Customizing these behaviors is an advanced task, and can result failures that are difficult to debug. Because the provided defaults control several intertwined behaviors, overriding any value skips all remaining defaults in this dictionary.

Valid keys are:


-  **cmd** : Literal value for the `        CMD` Containerfile directive. The default value is `        ["bash"]` .
-  **entrypoint** : Literal value for the `        ENTRYPOINT` Containerfile directive. The default entrypoint behavior handles signal propagation to subprocesses, as well as attempting to ensure at runtime that the container user has a proper environment with a valid writeable home directory, represented in `        /etc/passwd` , with the `        HOME` environment variable set to match. The default entrypoint script can emit warnings to `        stderr` in cases where it is unable to suitably adjust the user runtime environment. This behavior can be ignored or elevated to a fatal error; consult the source for the `        entrypoint` target script for more details.

The default value is `        ["/opt/builder/bin/entrypoint", "dumb-init"]` .


-  **package_pip** : Package to install with pip for entrypoint support. This package is installed in the final build image.

The default value is `        dumb-init==1.2.5` .



-  **package_manager_path** : string with the path to the package manager (dnf or microdnf) to use. The default is `    /usr/bin/dnf` . This value is used to install a Python interpreter, if specified in `    dependencies` , and during the build phase by the `    assemble` script.
-  **skip_ansible_check** : This boolean value controls whether or not the check for an installation of Ansible and Ansible Runner is performed on the final image.

Set this value to `    True` to not perform this check.

The default is `    False` .


-  **relax_passwd_permissions** : This boolean value controls whether the `    root` group (GID 0) is explicitly granted write permission to `    /etc/passwd` in the final container image. The default entrypoint script can attempt to update `    /etc/passwd` under some container runtimes with dynamically created users to ensure a fully-functional POSIX user environment and home directory. Disabling this capability can cause failures of software features that require users to be listed in `    /etc/passwd` with a valid and writeable home directory, for example, `    async` in ansible-core, and the `    ~username` shell expansion.

The default is `    True` .


-  **workdir** : Default current working directory for new processes started under the final container image. Some container runtimes also use this value as `    HOME` for dynamically-created users in the `    root` (GID 0) group. When this value is specified, if the directory does not already exist, it is created, set to `    root` group ownership, and `    rwx` group permissions are recursively applied to it.

The default value is `    /runner` .


-  **user** : This sets the username or UID to use as the default user for the final container image.

The default value is `    1000` .




**Example options:**

```
options:
container_init:
package_pip: dumb-init&gt;=1.2.5
entrypoint: '["dumb-init"]'
cmd: '["csh"]'
package_manager_path: /usr/bin/microdnf
relax_password_permissions: false
skip_ansible_check: true
workdir: /myworkdir
user: bob
```


### 21.2.8. version




An integer value that sets the schema version of the execution environment definition file.

Defaults to `1` .

The value must be `3` if you are using Ansible Builder 3.x.

## 21.3. Default execution environment for AWX




The example in `test/data/pytz` requires the `awx.awx` collection in the definition. The lookup plugin `awx.awx.tower_schedule_rrule` requires the PyPI `pytz` and another library to work. If the `test/data/pytz/execution-environment.yml` file is provided to the `ansible-builder build` command, it installs the collection inside the image, reads the `requirements.txt` file inside of the collection, and then installs `pytz` into the image.

The image produced can be used inside of an `ansible-runner` project by placing these variables inside the `env/settings` file, inside the private data directory.

```
---
container_image: image-name
process_isolation_executable: podman # or docker
process_isolation: true
```

The `awx.awx` collection is a subset of content included in the default AWX .

For further information, see the [awx-ee repository](https://github.com/ansible/awx-ee) .

# Chapter 22. Managing user credentials




Credentials authenticate the automation controller user when launching jobs against machines, synchronizing with inventory sources, and importing project content from a version control system.

You can grant users and teams the ability to use these credentials, without exposing the credential to the user. If a user moves to a different team or leaves the organization, you do not have to re-key all of your systems just because that credential was available in automation controller.

Note
Automation controller encrypts passwords and key information in the database and never makes secret information visible through the API. For further information, see [Configuring automation execution](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/configuring_automation_execution) .



## 22.1. How credentials work




Automation controller uses SSH to connect to remote hosts. To pass the key from automation controller to SSH, the key must be decrypted before it can be written to a named pipe. Automation controller uses that pipe to send the key to SSH, so that the key is never written to disk. If passwords are used, automation controller handles them by responding directly to the password prompt and decrypting the password before writing it to the prompt.

The **Credentials** page shows credentials that are currently available. The default view is collapsed (Compact), showing the credential name, and credential type.

From this screen you can edit![Edit](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.5-Using_automation_execution-en-US/images/e5cb7f9b0cfe60ab5ba421bd17ecbb6a/leftpencil.png)
, duplicate![Copy](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.5-Using_automation_execution-en-US/images/df17e3afcfb728d4887b97e8605bd65c/copy.png)
or delete ⋮ a credential.

Note
It is possible to create duplicate credentials with the same name and without an organization. However, it is not possible to create two duplicate credentials in the same organization.

**Example**

1. Create two machine credentials with the same name but without an organization.
1. Use the module `    ansible.controller.export` to export the credentials.
1. Use the module `    ansible.controller.import` in a different automation execution node.
1. Check the imported credentials.


When you export two duplicate credentials and then import them in a different node, only one credential is imported.



## 22.2. Creating new credentials




Credentials added to a team are made available to all members of the team. You can also add credentials to individual users.

As part of the initial setup, two credentials are available for your use: Demo Credential and Ansible Galaxy. Use the Ansible Galaxy credential as a template. You can copy this credential, but not edit it. Add more credentials as needed.

**Procedure**

1. From the navigation panel, selectAutomation Execution→Infrastructure→Credentials.
1. On the **Credentials** page, clickCreate credential.
1. Enter the following information:


-  **Name** : the name for your new credential.
- (Optional) **Description** : a description for the new credential.
- Optional **Organization** : The name of the organization with which the credential is associated. The default is **Default** .
-  **Credential type** : enter or select the credential type you want to create.

1. Enter the appropriate details depending on the type of credential selected, as described in [Credential types](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/using_automation_execution/controller-credentials#ref-controller-credential-types) .

![Credential types drop down list](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.5-Using_automation_execution-en-US/images/64863eaf88acdfbaf537933f0cf14cb7/credential-types-drop-down-menu.png)



1. ClickCreate credential.


## 22.3. Adding new users and job templates to existing credentials




**Procedure**

1. From the navigation panel, selectAutomation Execution→Infrastructure→Credentials.
1. Select the credential that you want to assign to additional users.
1. Click the **User Access** tab. You can see users and teams associated with this credential and their roles. If no users exist, add them from the **Users** menu. For more information, see [Users](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/access_management_and_authentication/gw-managing-access#assembly-controller-users_gw-manage-rbac) .
1. ClickAdd roles.
1. Select the user(s) that you want to give access to the credential and clickNext.
1. From the **Select roles to apply** page, select the roles you want to add to the User.
1. ClickNext.
1. Review your selections and clickFinishto add the roles or clickBackto make changes.

The **Add roles** window displays stating whether the action was successful.

If the action is not successful, a warning displays.


1. ClickClose.
1. The **User Access** page displays the summary information.
1. Select the **Job templates** tab to select a job template to which you want to assign this credential.
1. Chose a job template or select **Create job template** from the **Create template** list to assign the credential to additional job templates.

For more information about creating new job templates, see [Job templates](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/using_automation_execution/controller-job-templates) .




## 22.4. Credential types




Automation controller supports the following credential types:

-  [Amazon Web Services](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/using_automation_execution/controller-credentials#ref-controller-credential-aws)
-  [Ansible Galaxy/Automation Hub API Token](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/using_automation_execution/controller-credentials#ref-controller-credential-galaxy-hub)
-  [AWS Secrets Manager Lookup](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/using_automation_execution/controller-credentials#ref-controller-aws-secrets-lookup)
-  [Bitbucket Data Center HTTP Access Token](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/using_automation_execution/controller-credentials#ref-controller-credential-bitbucket)
-  [Centrify Vault Credential Provider Lookup](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/using_automation_execution/controller-credentials#ref-controller-credential-centrify-vault)
-  [Container Registry](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/using_automation_execution/controller-credentials#ref-controller-credential-container-registry)
-  [CyberArk Central Credential Provider Lookup](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/using_automation_execution/controller-credentials#ref-controller-credential-cyberark-central)
-  [CyberArk Conjur Secrets Manager Lookup](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/using_automation_execution/controller-credentials#ef-controller-credential-cyberark-conjur)
-  [GitHub Personal Access Token](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/using_automation_execution/controller-credentials#ref-controller-credential-gitHub-pat)
-  [GitLab Personal Access Token](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/using_automation_execution/controller-credentials#ref-controller-credential-gitLab-pat)
-  [Google Compute Engine](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/using_automation_execution/controller-credentials#ref-controller-credential-GCE)
-  [GPG Public Key](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/using_automation_execution/controller-credentials#ref-controller-credential-GPG-public-key)
-  [HashiCorp Vault Secret Lookup](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/using_automation_execution/controller-credentials#ref-controller-credential-hasiCorp-secret)
-  [HashiCorp Vault Signed SSH](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/using_automation_execution/controller-credentials#ref-controller-credential-hashiCorp-vault)
-  [Insights](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/using_automation_execution/controller-credentials#ref-controller-credential-insights)
-  [Machine](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/using_automation_execution/controller-credentials#ref-controller-credential-machine)
-  [Microsoft Azure Key Vault](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/using_automation_execution/controller-credentials#ref-controller-credential-azure-key)
-  [Microsoft Azure Resource Manager](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/using_automation_execution/controller-credentials#ref-controller-credential-azure-resource)
-  [Network](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/using_automation_execution/controller-credentials#ref-controller-credential-network)
-  [OpenShift or Kubernetes API Bearer Token](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/using_automation_execution/controller-credentials#ref-controller-credential-openShift)
-  [OpenStack](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/using_automation_execution/controller-credentials#ref-controller-credential-openstack)
-  [Red Hat Ansible Automation Platform](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/using_automation_execution/controller-credentials#ref-controller-credential-aap)
-  [Red Hat Satellite 6](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/using_automation_execution/controller-credentials#ref-controller-credential-satellite)
-  [Red Hat Virtualization](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/using_automation_execution/controller-credentials#ref-controller-credential-virtualization)
-  [Source Control](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/using_automation_execution/controller-credentials#ref-controller-credential-source-control)
-  [Terraform Backend Configuration](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/using_automation_execution/controller-credentials#ref-controller-credential-terraform)
-  [Thycotic DevOps Secrets Vault](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/using_automation_execution/controller-credentials#ref-controller-credential-thycotic-vault)
-  [Thycotic Secret Server](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/using_automation_execution/controller-credentials#ref-controller-credential-thycotic-server)
-  [Vault](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/using_automation_execution/controller-credentials#ref-controller-credential-vault)
-  [VMware vCenter](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/using_automation_execution/controller-credentials#ref-controller-credential-vmware-vcenter)


The credential types associated with AWS Secrets Manager, Centrify, CyberArk, HashiCorp Vault, Microsoft Azure Key Vault, and Thycotic are part of the credential plugins capability that enables an external system to lookup your secrets information.

For more information, see [Secrets Management System](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/configuring_automation_execution/assembly-controller-secret-management) .

### 22.4.1. Amazon Web Services credential type




Select this credential to enable synchronization of cloud inventory with Amazon Web Services.

Automation controller uses the following environment variables for AWS credentials:

```
AWS_ACCESS_KEY_ID
AWS_SECRET_ACCESS_KEY
AWS_SECURITY_TOKEN
```

These are fields prompted in the user interface.

Amazon Web Services credentials consist of the AWS **Access Key** and **Secret Key** .

Automation controller provides support for EC2 STS tokens, also known as _Identity and Access Management_ (IAM) STS credentials. _Security Token Service_ (STS) is a web service that enables you to request temporary, limited-privilege credentials for AWS IAM users.

Note
If the value of your tags in EC2 contain Booleans ( `yes/no/true/false` ), you must quote them.



Warning
To use implicit IAM role credentials, do not attach AWS cloud credentials in automation controller when relying on IAM roles to access the AWS API.

Attaching your AWS cloud credential to your job template forces the use of your AWS credentials, not your IAM role credentials.



**Additional resources**

For more information about the IAM/EC2 STS Token, see [Temporary security credentials in IAM](http://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp.html) .


#### 22.4.1.1. Access Amazon EC2 credentials in an Ansible Playbook




You can get AWS credential parameters from a job runtime environment:

```
vars:
aws:
access_key: '{{ lookup("env", "AWS_ACCESS_KEY_ID") }}'
secret_key: '{{ lookup("env", "AWS_SECRET_ACCESS_KEY") }}'
security_token: '{{ lookup("env", "AWS_SECURITY_TOKEN") }}'
```

### 22.4.2. Ansible Galaxy/automation hub API token credential type




Select this credential to access Ansible Galaxy or use a collection published on an instance of private automation hub.

Enter the Galaxy server URL on this screen.

Populate the **Galaxy Server URL** field with the contents of the **Server URL** field at [Red Hat Hybrid Cloud Console](https://console.redhat.com/ansible/automation-hub/token) . Populate the **Auth Server URL** field with the contents of the **SSO URL** field at [Red Hat Hybrid Cloud Console](https://console.redhat.com/ansible/automation-hub/token) .

**Additional resources**

For more information, see [Using Collections with automation hub](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/using_automation_execution/controller-projects#proc-projects-using-collections-with-hub) .


### 22.4.3. AWS secrets manager lookup




This is considered part of the secret management capability. For more information, see [AWS Secrets Manager Lookup](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/configuring_automation_execution/assembly-controller-secret-management#ref-aws-secrets-manager-lookup)

### 22.4.4. BitBucket data center HTTP access token




Bitbucket Data Center is a self-hosted Git repository for collaboration and management. Select this credential type to enable you to use HTTP access tokens in place of passwords for Git over HTTPS.

For further information, see [HTTP access tokens](https://confluence.atlassian.com/bitbucketserver/http-access-tokens-939515499.html) in the Bitbucket Data Center documentation..

### 22.4.5. Centrify Vault Credential Provider Lookup credential type




This is considered part of the secret management capability.

For more information, see [Centrify Vault Credential Provider Lookup](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/configuring_automation_execution/assembly-controller-secret-management#ref-centrify-vault-lookup) .

### 22.4.6. Container Registry credential type




Select this credential to enable automation controller to access a collection of container images. For more information, see [What is a container registry?](https://www.redhat.com/en/topics/cloud-native-apps/what-is-a-container-registry) .

You must specify a name. The **Authentication URL** field is pre-populated with a default value. You can change the value by specifying the authentication endpoint for a different container registry.

### 22.4.7. CyberArk Central Credential Provider Lookup credential type




This is considered part of the secret management capability.

For more information, see [CyberArk Central Credential Provider (CCP) Lookup](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/configuring_automation_execution/assembly-controller-secret-management#ref-cyberark-ccp-lookup) .

### 22.4.8. CyberArk Conjur Secrets Manager Lookup credential type




This is considered part of the secret management capability.

For more information, see [CyberArk Conjur Secrets Manager Lookup](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/configuring_automation_execution/assembly-controller-secret-management#ref-cyberark-conjur-lookup) .

### 22.4.9. GitHub Personal Access Token credential type




Select this credential to enable you to access GitHub by using a _Personal Access Token_ (PAT), which you can get through GitHub.

For more information, see [Setting up a GitHub webhook](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/using_automation_execution/index#controller-set-up-github-webhook) .

GitHub PAT credentials require a value in the **Token** field, which is provided in your GitHub profile settings.

Use this credential to establish an API connection to GitHub for use in webhook listener jobs, to post status updates.

### 22.4.10. GitLab Personal Access Token credential type




Select this credential to enable you to access GitLab by using a _Personal Access Token_ (PAT), which you can get through GitLab.

For more information, see [Setting up a GitLab webhook](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/using_automation_execution/index#controller-set-up-gitlab-webhook) .

GitLab PAT credentials require a value in the **Token** field, which is provided in your GitLab profile settings.

Use this credential to establish an API connection to GitLab for use in webhook listener jobs, to post status updates.

### 22.4.11. Google Compute Engine credential type




Select this credential to enable synchronization of a cloud inventory with Google Compute Engine (GCE).

Automation controller uses the following environment variables for GCE credentials:

```
GCE_EMAIL
GCE_PROJECT
GCE_CREDENTIALS_FILE_PATH
```

These are fields prompted in the user interface:

GCE credentials require the following information:

-  **Service Account Email Address** : The email address assigned to the Google Compute Engine **service account** .
- Optional: **Project** : Provide the GCE assigned identification or the unique project ID that you provided at project creation time.
- Optional: **Service Account JSON File** : Upload a GCE service account file. ClickBrowseto browse for the file that has the special account information that can be used by services and applications running on your GCE instance to interact with other Google Cloud Platform APIs. This grants permissions to the service account and virtual machine instances.
-  **RSA Private Key** : The PEM file associated with the service account email.


#### 22.4.11.1. Access Google Compute Engine credentials in an Ansible Playbook




You can get GCE credential parameters from a job runtime environment:

```
vars:
gce:
email: '{{ lookup("env", "GCE_EMAIL") }}'
project: '{{ lookup("env", "GCE_PROJECT") }}'
pem_file_path: '{{ lookup("env", "GCE_PEM_FILE_PATH") }}'
```

### 22.4.12. GPG Public Key credential type




Select this credential type to enable automation controller to verify the integrity of the project when synchronizing from source control.

For more information about how to generate a valid keypair, use the CLI tool to sign content, and how to add the public key to the controller, see [Project Signing and Verification](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/using_automation_execution/index#assembly-controller-project-signing) .

### 22.4.13. HashiCorp Vault Secret Lookup credential type




This is considered part of the secret management capability.

For more information, see [HashiCorp Vault Secret Lookup](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/configuring_automation_execution/assembly-controller-secret-management#ref-hashicorp-vault-lookup) .

### 22.4.14. HashiCorp Vault Signed SSH credential type




This is considered part of the secret management capability.

For more information, see [HashiCorp Vault Signed SSH](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/configuring_automation_execution/controller-credentials#ref-controller-credential-hasiCorp-secret) .

### 22.4.15. Insights credential type




Select this credential type to enable synchronization of cloud inventory with Red Hat Insights.

Insights credentials are the Insights **Username** and **Password** , which are the user’s Red Hat Customer Portal Account username and password.

The `extra_vars` and `env` injectors for Insights are as follows:

```
ManagedCredentialType(
namespace='insights',
....
....
....

injectors={
'extra_vars': {
"scm_username": "{{username}}",
"scm_password": "{{password}}",
},
'env': {
'INSIGHTS_USER': '{{username}}',
'INSIGHTS_PASSWORD': '{{password}}',
},
```

### 22.4.16. Machine credential type




Machine credentials enable automation controller to call Ansible on hosts under your management. You can specify the SSH username, optionally give a password, an SSH key, a key password, or have automation controller prompt the user for their password at deployment time. They define SSH and user-level privilege escalation access for playbooks, and are used when submitting jobs to run playbooks on a remote host.

The following network connections use **Machine** as the credential type: `httpapi` , `netconf` , and `network_cli`

Machine and SSH credentials do not use environment variables. They pass the username through the ansible `-u` flag, and interactively write the SSH password when the underlying SSH client prompts for it.

Machine credentials require the following inputs:

-  **Username** : The username to use for SSH authentication.
-  **Password** : The password to use for SSH authentication. This password is stored encrypted in the database, if entered. Alternatively, you can configure automation controller to ask the user for the password at launch time by selecting **Prompt on launch** . In these cases, a dialog opens when the job is launched, promoting the user to enter the password and password confirmation.
-  **SSH Private Key** : Copy or drag-and-drop the SSH private key for the machine credential.
-  **Private Key Passphrase** : If the SSH Private Key used is protected by a password, you can configure a Key Passphrase for the private key. This password is stored encrypted in the database, if entered. You can also configure automation controller to ask the user for the key passphrase at launch time by selecting **Prompt on launch** . In these cases, a dialog opens when the job is launched, prompting the user to enter the key passphrase and key passphrase confirmation.
-  **Privilege Escalation Method** : Specifies the type of escalation privilege to assign to specific users. This is the same as specifying the `    --become-method=BECOME_METHOD` parameter, where `    BECOME_METHOD` is any of the existing methods, or a custom method you have written. Begin entering the name of the method, and the appropriate name auto-populates.


-  **empty selection** : If a task or play has `        become` set to `        yes` and is used with an empty selection, then it will default to `        sudo` .
-  **sudo** : Performs single commands with superuser (root user) privileges.
-  **su** : Switches to the superuser (root user) account (or to other user accounts).
-  **pbrun** : Requests that an application or command be run in a controlled account and provides for advanced root privilege delegation and keylogging.
-  **pfexec** : Executes commands with predefined process attributes, such as specific user or group IDs.
-  **dzdo** : An enhanced version of sudo that uses RBAC information in Centrify’s Active Directory service. For more information, see Centrify’s [site on DZDO](https://docs.delinea.com/online-help/server-suite/reports-events/events/server-suite/dzdo.htm) .
-  **pmrun** : Requests that an application is run in a controlled account. See [Privilege Manager for Unix 6.0](https://support.oneidentity.com/privilege-manager-for-unix/7.2.3/technical-documents) .
-  **runas** : Enables you to run as the current user.
-  **enable** : Switches to elevated permissions on a network device.
-  **doas** : Enables your remote/login user to run commands as another user through the _doas_ ("Do as user") utility.
-  **ksu** : Enables your remote/login user to run commands as another user through Kerberos access.
-  **machinectl** : Enables you to manage containers through the `        systemd` machine manager.
-  **sesu** : Enables your remote/login user to run commands as another user through the CA Privileged Access Manager.



Note
Custom `become` plugins are available from Ansible 2.8+. For more information, see [Understanding Privilege Escalation](https://docs.ansible.com/ansible/latest/playbook_guide/playbooks_privilege_escalation.html) and the list of [Become plugins](https://docs.ansible.com/ansible/latest/plugins/become.html#plugin-list)



-  **Privilege Escalation Username** : You see this field only if you selected an option for privilege escalation. Enter the username to use with escalation privileges on the remote system.
-  **Privilege Escalation Password** : You see this field only if you selected an option for privilege escalation. Enter the password to use to authenticate the user through the selected privilege escalation type on the remote system. This password is stored encrypted in the database. You can also configure automation controller to ask the user for the password at launch time by selecting **Prompt on launch** . In these cases, a dialog opens when the job is launched, promoting the user to enter the password and password confirmation.


Note
You must use sudo password must in combination with SSH passwords or SSH Private Keys, because automation controller must first establish an authenticated SSH connection with the host before invoking `sudo` to change to the sudo user.



Warning
Credentials that are used in scheduled jobs must not be configured as **Prompt on launch** .



#### 22.4.16.1. Access machine credentials in an ansible playbook




You can get username and password from Ansible facts:

```
vars:
machine:
username: '{{ ansible_user }}'
password: '{{ ansible_password }}'
```

### 22.4.17. Microsoft Azure Key Vault credential type




This is considered part of the secret management capability.

For more information, see [Microsoft Azure Key Vault](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/configuring_automation_execution/assembly-controller-secret-management#ref-azure-key-vault-lookup) .

### 22.4.18. Microsoft Azure Resource Manager credential type




Select this credential type to enable synchronization of cloud inventory with Microsoft Azure Resource Manager.

Microsoft Azure Resource Manager credentials require the following inputs:

-  **Subscription ID** : The Subscription UUID for the Microsoft Azure account.
-  **Username** : The username to use to connect to the Microsoft Azure account.
-  **Password** : The password to use to connect to the Microsoft Azure account.
-  **Client ID** : The Client ID for the Microsoft Azure account.
-  **Client Secret** : The Client Secret for the Microsoft Azure account.
-  **Tenant ID** : The Tenant ID for the Microsoft Azure account.
-  **Azure Cloud Environment** : The variable associated with Azure cloud or Azure stack environments.


These fields are equivalent to the variables in the API.

To pass service principal credentials, define the following variables:

```
AZURE_CLIENT_ID
AZURE_SECRET
AZURE_SUBSCRIPTION_ID
AZURE_TENANT
AZURE_CLOUD_ENVIRONMENT
```

To pass an Active Directory username and password pair, define the following variables:

```
AZURE_AD_USER
AZURE_PASSWORD
AZURE_SUBSCRIPTION_ID
```

You can also pass credentials as parameters to a task within a playbook. The order of precedence is parameters, then environment variables, and finally a file found in your home directory.

To pass credentials as parameters to a task, use the following parameters for service principal credentials:

```
client_id
secret
subscription_id
tenant
azure_cloud_environment
```

Alternatively, pass the following parameters for Active Directory username/password:

```
ad_user
password
subscription_id
```

#### 22.4.18.1. Access Microsoft Azure resource manager credentials in an ansible playbook




You can get Microsoft Azure credential parameters from a job runtime environment:

```
vars:
azure:
client_id: '{{ lookup("env", "AZURE_CLIENT_ID") }}'
secret: '{{ lookup("env", "AZURE_SECRET") }}'
tenant: '{{ lookup("env", "AZURE_TENANT") }}'
subscription_id: '{{ lookup("env", "AZURE_SUBSCRIPTION_ID") }}'
```

### 22.4.19. Network credential type




Note
Select the Network credential type if you are using a _local_ connection with _provider_ to use Ansible networking modules to connect to and manage networking devices.

When connecting to network devices, the credential type must match the connection type:



- For `    local` connections using `    provider` , credential type should be **Network** .
- For all other network connections ( `    httpapi` , `    netconf` , and `    network_cli` ), the credential type should be **Machine** .


For more information about connection types available for network devices, see [Multiple Communication Protocols](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/using_automation_execution/using_automation_execution/controller-credentials#ref-controller-multiple-connection-protocols) .

Automation controller uses the following environment variables for Network credentials:

```
ANSIBLE_NET_USERNAME
ANSIBLE_NET_PASSWORD
```

Provide the following information for network credentials:

-  **Username** : The username to use in conjunction with the network device.
-  **Password** : The password to use in conjunction with the network device.
-  **SSH Private Key** : Copy or drag-and-drop the actual SSH Private Key to be used to authenticate the user to the network through SSH.
-  **Private Key Passphrase** : The passphrase for the private key to authenticate the user to the network through SSH.
-  **Authorize** : Select this to control whether or not to enter privileged mode.


- If **Authorize** is checked, enter a password in the **Authorize Password** field to access privileged mode.



For more information, see [Porting Ansible Network Playbooks with New Connection Plugins](https://www.ansible.com/blog/porting-ansible-network-playbooks-with-new-connection-plugins) .

#### 22.4.19.1. Access network credentials in an ansible playbook




You can get the username and password parameters from a job runtime environment:

```
vars:
network:
username: '{{ lookup("env", "ANSIBLE_NET_USERNAME") }}'
password: '{{ lookup("env", "ANSIBLE_NET_PASSWORD") }}'
```

#### 22.4.19.2. Multiple communication protocols




Because network modules execute on the control node instead of on the managed nodes, they can support multiple communication protocols. The communication protocols (XML over SSH, CLI over SSH, or API over HTTPS) selected for each network module depend on the platform and the purpose of the module. Some network modules support only one protocol, while some offer a choice.

The most common protocol is CLI over SSH. You set the communication protocol with the ansible_connection variable:

| Value of ansible_connection | Protocol | Requires | Persistent? |
| --- | --- | --- | --- |
|  `ansible.netcommon.network_cli` | CLI over SSH | network_os setting | yes |
|  `ansible.netcommon.netconf` | XML over SSH | network_os setting | yes |
|  `ansible.netcommon.httpapi` | API over HTTP/HTTPS | network_os setting | yes |
|  `local` | depends on provider | provider setting | no |


The `ansible_connection: local` is deprecated. Use one of the persistent connection types listed above instead. With persistent connections, you can define the hosts and credentials only once, rather than in every task. You must also set the `network_os` variable for the specific network platform you are communicating with.

### 22.4.20. OpenShift or Kubernetes API Bearer Token credential type




Select this credential type to create instance groups that point to a Kubernetes or OpenShift container.

For more information, see [Instance and container groups](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/using_automation_execution/controller-instance-and-container-groups) .

Provide the following information for container credentials:

-  **OpenShift or Kubernetes API Endpoint** (required): The endpoint used to connect to an OpenShift or Kubernetes container.
-  **API authentication bearer token** (required): The token used to authenticate the connection.
- Optional: **Verify SSL** : You can check this option to verify the server’s SSL/TLS certificate is valid and trusted. Environments that use internal or private _Certificate Authority_ (CA) must leave this option unchecked to disable verification.
-  **Certificate Authority data** : Include the `    BEGIN CERTIFICATE` and `    END CERTIFICATE` lines when pasting the certificate, if provided.


A container group is a type of instance group that has an associated credential that enables connection to an OpenShift cluster. To set up a container group, you must have the following items:

- A namespace you can start into. Although every cluster has a default namespace, you can use a specific namespace.
- A service account that has the roles that enable it to start and manage pods in this namespace.
- If you use execution environments in a private registry, and have a container registry credential associated with them in automation controller, the service account also requires the roles to get, create, and delete secrets in the namespace.

If you do not want to give these roles to the service account, you can pre-create the `    ImagePullSecrets` and specify them on the pod spec for the container group. In this case, the execution environment must not have a Container Registry credential associated, or automation controller attempts to create the secret for you in the namespace.


- A token associated with that service account (OpenShift or Kubernetes Bearer Token)
- A CA certificate associated with the cluster


#### 22.4.20.1. Creating a service account in an Openshift cluster




Creating a service account in an Openshift or Kubernetes cluster to be used to run jobs in a container group through automation controller. After you create the service account, its credentials are provided to automation controller in the form of an Openshift or Kubernetes API bearer token credential.

After you create a service account, use the information in the new service account to configure automation controller.

**Procedure**

1. To create a service account, download and use the sample service account, `    containergroup sa` , and change it as needed to obtain the credentials:


```
---    apiVersion: v1    kind: ServiceAccount    metadata:      name: containergroup-service-account      namespace: containergroup-namespace    ---    kind: Role    apiVersion: rbac.authorization.k8s.io/v1    metadata:      name: role-containergroup-service-account      namespace: containergroup-namespace    rules:    - apiGroups: [""]      resources: ["pods"]      verbs: ["get", "list", "watch", "create", "update", "patch", "delete"]    - apiGroups: [""]      resources: ["pods/log"]      verbs: ["get"]    - apiGroups: [""]      resources: ["pods/attach"]      verbs: ["get", "list", "watch", "create"]    ---    kind: RoleBinding    apiVersion: rbac.authorization.k8s.io/v1    metadata:      name: role-containergroup-service-account-binding      namespace: containergroup-namespace    subjects:    - kind: ServiceAccount      name: containergroup-service-account      namespace: containergroup-namespace    roleRef:      kind: Role      name: role-containergroup-service-account      apiGroup: rbac.authorization.k8s.io
```


1. Apply the configuration from `    containergroup-sa.yml` :


```
oc apply -f containergroup-sa.yml
```


1. Get the secret name associated with the service account:


```
export SA_SECRET=$(oc get sa containergroup-service-account -o json | jq '.secrets[0].name' | tr -d '"')
```


1. Get the token from the secret:


```
oc get secret $(echo ${SA_SECRET}) -o json | jq '.data.token' | xargs | base64 --decode &gt; containergroup-sa.token
```


1. Get the CA cert:


```
oc get secret $SA_SECRET -o json | jq '.data["ca.crt"]' | xargs | base64 --decode &gt; containergroup-ca.crt
```


1. Use the contents of `    containergroup-sa.token` and `    containergroup-ca.crt` to provide the information for the [OpenShift or Kubernetes API Bearer Token](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/using_automation_execution/index#ref-controller-credential-openShift) required for the container group.


### 22.4.21. OpenStack credential type




Select this credential type to enable synchronization of cloud inventory with OpenStack.

Enter the following information for OpenStack credentials:

-  **Username** : The username to use to connect to OpenStack.
-  **Password (API Key)** : The password or API key to use to connect to OpenStack.
-  **Host (Authentication URL)** : The host to be used for authentication.
-  **Project (Tenant Name)** : The Tenant name or Tenant ID used for OpenStack. This value is usually the same as the username.
- Optional: **Project (Domain Name)** : Give the project name associated with your domain.
- Optional: **Domain Name** : Give the FQDN to be used to connect to OpenStack.
- Optional: **Region Name** : Give the region name. For some cloud providers, like OVH, the region must be specified.


If you are interested in using OpenStack Cloud Credentials, see [Use Cloud Credentials with a cloud inventory](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/using_automation_execution/controller-job-templates#controller-cloud-credentials) , which includes a sample playbook.

### 22.4.22. Red Hat Ansible Automation Platform credential type




Select this credential to access another automation controller instance.

Ansible Automation Platform credentials require the following inputs:

-  **Red Hat Ansible Automation Platform** : The base URL or IP address of the other instance to connect to.
-  **Username** : The username to use to connect to it.
-  **Password** : The password to use to connect to it.
-  **Oauth Token** : If username and password are not used, provide an OAuth token to use to authenticate.


The `env` injectors for Ansible Automation Platform are as follows:

```
ManagedCredentialType(
namespace='controller',

....
....
....

injectors={
'env': {
'TOWER_HOST': '{{host}}',
'TOWER_USERNAME': '{{username}}',
'TOWER_PASSWORD': '{{password}}',
'TOWER_VERIFY_SSL': '{{verify_ssl}}',
'TOWER_OAUTH_TOKEN': '{{oauth_token}}',
'CONTROLLER_HOST': '{{host}}',
'CONTROLLER_USERNAME': '{{username}}',
'CONTROLLER_PASSWORD': '{{password}}',
'CONTROLLER_VERIFY_SSL': '{{verify_ssl}}',
'CONTROLLER_OAUTH_TOKEN': '{{oauth_token}}',
}
```

#### 22.4.22.1. Access automation controller credentials in an Ansible Playbook




You can get the host, username, and password parameters from a job runtime environment:

```
vars:
controller:
host: '{{ lookup("env", "CONTROLLER_HOST") }}'
username: '{{ lookup("env", "CONTROLLER_USERNAME") }}'
password: '{{ lookup("env", "CONTROLLER_PASSWORD") }}'
```

### 22.4.23. Red Hat Satellite 6 credential type




Select this credential type to enable synchronization of cloud inventory with Red Hat Satellite 6.

Automation controller writes a Satellite configuration file based on fields prompted in the user interface. The absolute path to the file is set in the following environment variable:

`FOREMAN_INI_PATH`

Satellite credentials have the following required inputs:

-  **Satellite 6 URL** : The Satellite 6 URL or IP address to connect to.
-  **Username** : The username to use to connect to Satellite 6.
-  **Password** : The password to use to connect to Satellite 6.


### 22.4.24. Red Hat Virtualization credential type




Select this credential to enable automation controller to access Ansible’s `oVirt4.py` dynamic inventory plugin, which is managed by _Red Hat Virtualization_ .

Automation controller uses the following environment variables for Red Hat Virtualization credentials. These are fields in the user interface:

```
OVIRT_URL
OVIRT_USERNAME
OVIRT_PASSWORD
```

Provide the following information for Red Hat Virtualization credentials:

-  **Host (Authentication URL)** : The host URL or IP address to connect to. To sync with the inventory, the credential URL needs to include the `    ovirt-engine/api` path.
-  **Username** : The username to use to connect to oVirt4. This must include the domain profile to succeed, for example `    username@ovirt.host.com` .
-  **Password** : The password to use to connect to it.
- Optional: **CA File** : Provide an absolute path to the oVirt certificate file (it might end in `    .pem` , `    .cer` and `    .crt` extensions, but preferably `    .pem` for consistency)


#### 22.4.24.1. Access virtualization credentials in an Ansible Playbook




You can get the Red Hat Virtualization credential parameter from a job runtime environment:

```
vars:
ovirt:
ovirt_url: '{{ lookup("env", "OVIRT_URL") }}'
ovirt_username: '{{ lookup("env", "OVIRT_USERNAME") }}'
ovirt_password: '{{ lookup("env", "OVIRT_PASSWORD") }}'
```

The `file` and `env` injectors for Red Hat Virtualization are as follows:

```
ManagedCredentialType(
namespace='rhv',

....
....
....

injectors={
# The duplication here is intentional; the ovirt4 inventory plugin
# writes a .ini file for authentication, while the ansible modules for
# ovirt4 use a separate authentication process that support
# environment variables; by injecting both, we support both
'file': {
'template': '\n'.join(
[
'[ovirt]',
'ovirt_url={{host}}',
'ovirt_username={{username}}',
'ovirt_password={{password}}',
'{% if ca_file %}ovirt_ca_file={{ca_file}}{% endif %}',
]
)
},
'env': {'OVIRT_INI_PATH': '{{tower.filename}}', 'OVIRT_URL': '{{host}}', 'OVIRT_USERNAME': '{{username}}', 'OVIRT_PASSWORD': '{{password}}'},
},
)
```

### 22.4.25. Source Control credential type




_Source Control_ credentials are used with projects to clone and update local source code repositories from a remote revision control system such as Git or Subversion.

Source Control credentials require the following inputs:

-  **Username** : The username to use in conjunction with the source control system.
-  **Password** : The password to use in conjunction with the source control system.
-  **SCM Private Key** : Copy or drag-and-drop the actual SSH Private Key to be used to authenticate the user to the source control system through SSH.
-  **Private Key Passphrase** : If the SSH Private Key used is protected by a passphrase, you can configure a Key Passphrase for the private key.


Note
You cannot configure Source Control credentials as **Prompt on launch** .

If you are using a GitHub account for a Source Control credential and you have _Two Factor Authentication_ (2FA) enabled on your account, you must use your Personal Access Token in the password field rather than your account password.



### 22.4.26. Terraform backend configuration




Terraform is a HashiCorp tool used to automate various infrastructure tasks. Select this credential type to enable synchronization with the Terraform inventory source.

The Terraform credential requires the **Backend configuration** attribute which must contain the data from a [Terraform backend block](https://developer.hashicorp.com/terraform/language/backend) . You can paste, drag a file, browse to upload a file, or click the![Key](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.5-Using_automation_execution-en-US/images/fc669abfeec02bb8bda89a0de40c0391/leftkey.png)
icon to populate the field from an external [Secret Management System](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/configuring_automation_execution/assembly-controller-secret-management) .

Terraform backend configuration requires the following inputs:

-  **Name**
- Credential type: Select **Terraform backend configuration** .
- Optional: **Organization**
- Optional: **Description**
-  **Backend configuration** : Drag a file here or browse to upload.

Example configuration for an S3 backend:


```
bucket = "my-terraform-state-bucket"    key = "path/to/terraform-state-file"    region = "us-east-1"    access_key = "my-aws-access-key"    secret_key = "my-aws-secret-access-key"
```


- Optional: **Google Cloud Platform account credentials**


### 22.4.27. Thycotic DevOps Secrets Vault credential type




This is considered part of the secret management capability.

For more information, see [Thycotic DevOps Secrets Vault](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/configuring_automation_execution/assembly-controller-secret-management#ref-thycotic-devops-vault) .

### 22.4.28. Thycotic secret server credential type




This is considered part of the secret management capability.

For more information, see [Thycotic Secret Server](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/configuring_automation_execution/assembly-controller-secret-management#ref-thycotic-secret-server) .

### 22.4.29. Ansible Vault credential type




Select this credential type to enable synchronization of inventory with Ansible Vault.

Vault credentials require the **Vault Password** and an optional **Vault Identifier** if applying multi-Vault credentialing.

You can configure automation controller to ask the user for the password at launch time by selecting **Prompt on launch** .

When you select **Prompt on launch** , a dialog opens when the job is launched, prompting the user to enter the password.

Warning
Credentials that are used in scheduled jobs must not be configured as **Prompt on launch** .



For more information about Ansible Vault, see [Protecting sensitive data with Ansible vault](http://docs.ansible.com/ansible/playbooks_vault.html) .

### 22.4.30. VMware vCenter credential type




Select this credential type to enable synchronization of inventory with VMware vCenter.

Automation controller uses the following environment variables for VMware vCenter credentials:

```
VMWARE_HOST
VMWARE_USER
VMWARE_PASSWORD
VMWARE_VALIDATE_CERTS
```

These are fields prompted in the user interface.

VMware credentials require the following inputs:

-  **vCenter Host** : The vCenter hostname or IP address to connect to.
-  **Username** : The username to use to connect to vCenter.
-  **Password** : The password to use to connect to vCenter.


Note
If the VMware guest tools are not running on the instance, VMware inventory synchronization does not return an IP address for that instance.



#### 22.4.30.1. Access VMware vCenter credentials in an ansible playbook




You can get VMware vCenter credential parameters from a job runtime environment:

```
vars:
vmware:
host: '{{ lookup("env", "VMWARE_HOST") }}'
username: '{{ lookup("env", "VMWARE_USER") }}'
password: '{{ lookup("env", "VMWARE_PASSWORD") }}'
```

## 22.5. Use automation controller credentials in a playbook




The following playbook is an example of how to use automation controller credentials in your playbook.

```
- hosts: all

vars:
machine:
username: '{{ ansible_user }}'
password: '{{ ansible_password }}'
controller:
host: '{{ lookup("env", "CONTROLLER_HOST") }}'
username: '{{ lookup("env", "CONTROLLER_USERNAME") }}'
password: '{{ lookup("env", "CONTROLLER_PASSWORD") }}'
network:
username: '{{ lookup("env", "ANSIBLE_NET_USERNAME") }}'
password: '{{ lookup("env", "ANSIBLE_NET_PASSWORD") }}'
aws:
access_key: '{{ lookup("env", "AWS_ACCESS_KEY_ID") }}'
secret_key: '{{ lookup("env", "AWS_SECRET_ACCESS_KEY") }}'
security_token: '{{ lookup("env", "AWS_SECURITY_TOKEN") }}'
vmware:
host: '{{ lookup("env", "VMWARE_HOST") }}'
username: '{{ lookup("env", "VMWARE_USER") }}'
password: '{{ lookup("env", "VMWARE_PASSWORD") }}'
gce:
email: '{{ lookup("env", "GCE_EMAIL") }}'
project: '{{ lookup("env", "GCE_PROJECT") }}'
azure:
client_id: '{{ lookup("env", "AZURE_CLIENT_ID") }}'
secret: '{{ lookup("env", "AZURE_SECRET") }}'
tenant: '{{ lookup("env", "AZURE_TENANT") }}'
subscription_id: '{{ lookup("env", "AZURE_SUBSCRIPTION_ID") }}'

tasks:
- debug:
var: machine

- debug:
var: controller

- debug:
var: network

- debug:
var: aws

- debug:
var: vmware

- debug:
var: gce

- shell: 'cat {{ gce.pem_file_path }}'
delegate_to: localhost

- debug:
var: azure
```


<span id="use_delegate_to_and_any_lookup_variable"></span>
#### Use 'delegate_to' and any lookup variable


```
- command: somecommand
environment:
USERNAME: '{{ lookup("env", "USERNAME") }}'
PASSWORD: '{{ lookup("env", "PASSWORD") }}'
delegate_to: somehost
```

# Chapter 23. Custom credential types




As a system administrator, you can define a custom credential type in a standard format by using a YAML or JSON-like definition. You can define a custom credential type that works in ways similar to existing credential types. For example, a custom credential type can inject an API token for a third-party web service into an environment variable, for your playbook or custom inventory script to consume.

Custom credentials support the following ways of injecting their authentication information:

- Environment variables
- Ansible extra variables
- File-based templating, which means generating `    .ini` or `    .conf` files that contain credential values


You can attach one SSH and multiple cloud credentials to a job template. Each cloud credential must be of a different type. Only one of each type of credential is permitted. Vault credentials and machine credentials are separate entities.

Note
- When creating a new credential type, you must avoid collisions in the `    extra_vars` , `    env` , and file namespaces.
- Environment variable or extra variable names must not start with `    ANSIBLE_` because they are reserved.
- You must have System administrator (superuser) permissions to be able to create and edit a credential type ( `    CredentialType` ) and to be able to view the `    CredentialType.injection` field.




## 23.1. Content sourcing from collections




A "managed" credential type of `kind=galaxy` represents a content source for fetching collections defined in `requirements.yml` when project updates are run. Examples of content sources are galaxy.ansible.com, console.redhat.com, or on-premise automation hub. This new credential type represents a URL and (optional) authentication details necessary to construct the environment variables when a project update runs `ansible-galaxy collection install` as described in the Ansible documentation, [Configuring the ansible-galaxy client](https://docs.ansible.com/ansible/latest/collections_guide/collections_installing.html#configuring-the-ansible-galaxy-client) . It has fields that map directly to the configuration options exposed to the Ansible Galaxy CLI, for example, per-server.

An endpoint in the API reflects an ordered list of these credentials at the Organization level:

```
/api/v2/organizations/N/galaxy_credentials/
```

When installations of automation controller migrate existing Galaxy-oriented setting values, post-upgrade proper credentials are created and attached to every Organization. After upgrading to the latest version, every organization that existed before upgrade now has a list of one or more "Galaxy" credentials associated with it.

Additionally, post-upgrade, these settings are not visible (or editable) from the `/api/v2/settings/jobs/` endpoint.

Automation controller continues to fetch roles directly from public Galaxy even if `galaxy.ansible.com` is not the first credential in the list for the organization. The global Galaxy settings are no longer configured at the jobs level, but at the organization level in the user interface.

The organization’s **Create organization** and **Edit organization** windows have an optional **Galaxy credentials** lookup field for credentials of `kind=galaxy` .

![Create organization](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.5-Using_automation_execution-en-US/images/f359bc6f601642bb36cf0c1f0e57a5c7/organizations-galaxy-credentials.png)


It is important to specify the order of these credentials as order sets precedence for the sync and lookup of the content. For more information, see [Creating an organization](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/access_management_and_authentication/gw-managing-access#proc-controller-create-organization) .

For more information about how to set up a project by using collections, see [Using Collections with automation hub](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/using_automation_execution/index#proc-projects-using-collections-with-hub) .

## 23.2. Backwards-Compatible API considerations




Support for version 2 of the API ( `api/v2/` ) means a one-to-many relationship for job templates to credentials (including multicloud support).

You can filter credentials the v2 API:

```
curl "https://controller.example.org/api/v2/credentials/?credential_type__namespace=aws"
```

In the V2 Credential Type model, the relationships are defined as follows:

| Machine | SSH |
| --- | --- |
| Vault | Vault |
| Network | Sets environment variables, for example `ANSIBLE_NET_AUTHORIZE` |
| SCM | Source Control |
| Cloud | EC2, AWS |
| Cloud | Lots of others |
| Insights | Insights |
| Galaxy | galaxy.ansible.com, console.redhat.com |
| Galaxy | on-premise automation hub |


## 23.3. Content verification




Automation controller uses GNU Privacy Guard (GPG) to verify content.

For more information, see [The GNU Privacy Handbook](https://www.gnupg.org/gph/en/manual/c14.html#:~:text=GnuPG%20uses%20public%2Dkey%20cryptography,the%20user%20wants%20to%20communicate) .

## 23.4. Getting started with credential types




**Procedure**

1. From the navigation panel, selectAutomation Execution→Infrastructure→Credentials. If no custom credential types have been created, the **Credential Types** page prompts you to add one.

If credential types have been created, this page displays a list of existing and available Credential Types.


1. Select the name of a credential or the Edit![Edit](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.5-Using_automation_execution-en-US/images/e5cb7f9b0cfe60ab5ba421bd17ecbb6a/leftpencil.png)
icon to view more information about a credential type, .
1. On the **Details** tab, each credential type displays its own unique configurations in the **Input Configuration** field and the **Injector Configuration** field, if applicable. Both YAML and JSON formats are supported in the configuration fields.


## 23.5. Creating a new credential type




To create a new credential type:

**Procedure**

1. From the navigation panel, selectAutomation Execution→Infrastructure→Credentials.
1. In the **Credential Types** view, clickCreate credential type.
1. Enter the appropriate details in the **Name** and **Description** field.

Note
When creating a new credential type, do not use reserved variable names that start with `    ANSIBLE_` for the **INPUT** and **INJECTOR** names and IDs, as they are invalid for custom credential types.




1. In the **Input configuration** field, specify an input schema that defines a set of ordered fields for that type. The format can be in YAML or JSON:

**YAML**


```
fields:      - type: string        id: username        label: Username      - type: string        id: password        label: Password        secret: true    required:      - username      - password
```

View more YAML examples at the [YAML page](https://yaml.org/spec/1.2.2/) .

**JSON**


```
{    "fields": [      {      "type": "string",      "id": "username",      "label": "Username"      },      {      "secret": true,      "type": "string",      "id": "password",      "label": "Password"       }      ],     "required": ["username", "password"]    }
```

View more JSON examples at [The JSON website](https://www.json.org/json-en.html) .

The following configuration in JSON format shows each field and how they are used:


```
{      "fields": [{        "id": "api_token",    # required - a unique name used to reference the field value            "label": "API Token", # required - a unique label for the field            "help_text": "User-facing short text describing the field.",            "type": ("string" | "boolean")   # defaults to 'string'            "choices": ["A", "B", "C"]   # (only applicable to `type=string`)            "format": "ssh_private_key"  # optional, can be used to enforce data format validity                                     for SSH private key data (only applicable to `type=string`)            "secret": true,       # if true, the field value will be encrypted            "multiline": false    # if true, the field should be rendered as multi-line for input entry                              # (only applicable to `type=string`)    },{        # field 2...    },{        # field 3...    }],        "required": ["api_token"]   # optional; one or more fields can be marked as required    },
```

When `    type=string` , fields can optionally specify multiple choice options:


```
{      "fields": [{          "id": "api_token",    # required - a unique name used to reference the field value          "label": "API Token", # required - a unique label for the field          "type": "string",          "choices": ["A", "B", "C"]      }]    },
```


1. In the **Injector configuration** field, enter environment variables or extra variables that specify the values a credential type can inject. The format can be in YAML or JSON (see examples in the previous step).

The following configuration in JSON format shows each field and how they are used:


```
{      "file": {          "template": "[mycloud]\ntoken={{ api_token }}"      },      "env": {          "THIRD_PARTY_CLOUD_API_TOKEN": "{{ api_token }}"      },      "extra_vars": {          "some_extra_var": "{{ username }}:{{ password }}"      }    }
```

Credential Types can also generate temporary files to support `    .ini` files or certificate or key data:


```
{      "file": {          "template": "[mycloud]\ntoken={{ api_token }}"      },      "env": {          "MY_CLOUD_INI_FILE": "{{ tower.filename }}"      }    }
```

In this example, automation controller writes a temporary file that has:


```
[mycloud]\ntoken=SOME_TOKEN_VALUE
```

The absolute file path to the generated file is stored in an environment variable named `    MY_CLOUD_INI_FILE` .

The following is an example of referencing many files in a custom credential template:

**Inputs**


```
{      "fields": [{        "id": "cert",        "label": "Certificate",        "type": "string"      },{        "id": "key",        "label": "Key",        "type": "string"      }]    }
```

**Injectors**


```
{      "file": {        "template.cert_file": "[mycert]\n{{ cert }}",        "template.key_file": "[mykey]\n{{ key }}"    },    "env": {        "MY_CERT_INI_FILE": "{{ tower.filename.cert_file }}",        "MY_KEY_INI_FILE": "{{ tower.filename.key_file }}"    }    }
```


1. ClickCreate credential type.

Your newly created credential type is displayed on the list of credential types:

![New credential type](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.5-Using_automation_execution-en-US/images/30ad01fa860543fbf7afb3891f9a05c3/credential-types-new-listed.png)



1. Click the Edit![Edit](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.5-Using_automation_execution-en-US/images/e5cb7f9b0cfe60ab5ba421bd17ecbb6a/leftpencil.png)
icon to modify the credential type options.

Note
In the **Edit** screen, you can modify the details or delete the credential. If the **Delete** option is disabled, this means that the credential type is being used by a credential, and you must delete the credential type from all the credentials that use it before you can delete it.






**Verification**

- Verify that the newly created credential type can be selected from the **Credential Type** selection window when creating a new credential:


![Verify new credential type](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.5-Using_automation_execution-en-US/images/68f0dca37079402faddd543992a8a7bb/credential-types-new-listed-verify.png)


**Additional resources**

For information about how to create a new credential, see [Creating a credential](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/using_automation_execution/index#controller-create-credential) .


# Chapter 24. Activity stream




- From the navigation panel, selectAutomation Execution→Administration→Activity Stream.

![Activity stream page](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.5-Using_automation_execution-en-US/images/b90ef2c5030b58f9f3a2ac43d4917b66/activity_stream_page.png)





An Activity Stream shows all changes for a particular object. For each change, the Activity Stream shows the time of the event, the user that initiated the event, and the action. The information displayed varies depending on the type of event.

- Click the![Examine](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.5-Using_automation_execution-en-US/images/4e440067d24ca0b7a2a91901d3b3778f/examine.png)
icon to display the event log for the change.

![Activity stream details](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.5-Using_automation_execution-en-US/images/59488102ba43ff93fae36485beea8d10/activity_stream_details.png)





You can filter the Activity Stream by the initiating user, by system (if it was system initiated), or by any related object, such as a credential, job template, or schedule. The Activity Stream shows the Activity Stream for the entire instance. Most pages permit viewing an activity stream filtered for that specific object.

You can view the activity stream on any page by clicking theActivity Stream![activitystream](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.5-Using_automation_execution-en-US/images/a9296649c2fd7d36e8f259ff55d08821/activitystream.png)
icon.

# Chapter 25. Notifiers




A [Notification type](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/using_automation_execution/index#controller-notification-types) such as Email, Slack or a Webhook, is an instance of a Notification Template, and has a name, description and configuration defined in the Notification template.

The following include examples of details needed to add a notification template:

- A username, password, server, and recipients are needed for an Email notification template
- The token and a list of channels are needed for a Slack notification template
- The URL and Headers are needed for a Webhook notification template


When a job fails, a notification is sent using the configuration that you define in the notification template.

The following shows the typical flow for the notification system:

- You create a notification template to the `    REST API` at the `    /api/v2/notification_templates endpoint` , either through the API or through the UI.
- You assign the notification template to any of the various objects that support it (all variants of job templates as well as organizations and projects) and at the appropriate trigger level for which you want the notification (started, success, or error). For example, you might want to assign a particular notification template to trigger when Job Template 1 fails. In this case, you associate the notification template with the job template at `    /api/v2/job_templates/n/notification_templates_error` API endpoint.
- You can set notifications on job start and job end. Users and teams are also able to define their own notifications that can be attached to arbitrary jobs.


## 25.1. Notification hierarchy




Notification templates inherit templates defined on parent objects, such as the following:

- Job templates use notification templates defined for them. Additionally, they can inherit notification templates from the project used by the job template, and from the organization that it is listed under.
- Project updates use notification templates defined on the project and inherit notification templates from the organization associated with it.
- Inventory updates use notification templates defined on the organization that it is listed under.
- Ad hoc commands use notification templates defined on the organization that the inventory is associated with.


## 25.2. Notification workflow




When a job succeeds or fails, the error or success handler pulls a list of relevant notification templates using the procedure defined in the [Notifiers](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/using_automation_execution/index#controller-notifications) section.

It then creates a notification object for each one, containing relevant details about the job and sends it to the destination. These include email addresses, slack channels, and SMS numbers.

These notification objects are available as related resources on job types (jobs, inventory updates, project updates), and also at `/api/v2/notifications` . You can also see what notifications have been sent from a notification template by examining its related resources.

If a notification fails, it does not impact the job associated with it or cause it to fail. The status of the notification can be viewed at its detail endpoint `/api/v2/notifications/&lt;n&gt;` .

## 25.3. Creating a notification template




Use the following procedure to create a notification template.

**Procedure**

1. From the navigation panel, selectAutomation Execution→Administration→Notifiers.
1. ClickAdd notifier.
1. Complete the following fields:


-  **Name** : Enter the name of the notification.
-  **Description** : Enter a description for the notification. This field is optional.
-  **Organization** : Specify the organization that the notification belongs to.
-  **Type** : Choose a type of notification from the drop-down menu. For more information, see the [Notification types](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/using_automation_execution/index#controller-notification-types) section.

1. ClickSave notifier.


## 25.4. Notification types




The following notification types are supported with automation controller:

-  [Email](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/using_automation_execution/index#controller-notification-email)
-  [Grafana](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/using_automation_execution/index#controller-notification-grafana)
-  [IRC](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/using_automation_execution/index#controller-notification-irc)
-  [Mattermost](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/using_automation_execution/index#controller-notification-mattermost)
-  [PagerDuty](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/using_automation_execution/index#controller-notification-pagerduty)
-  [Rocket.Chat](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/using_automation_execution/index#controller-notification-rocketchat)
-  [Slack](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/using_automation_execution/index#controller-notification-slack)
-  [Twilio](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/using_automation_execution/index#controller-notification-twilio)
-  [Webhook](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/using_automation_execution/index#controller-notification-webhook)


-  [Webhook payloads](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/using_automation_execution/index#controller-notification-webhook-payloads)



Each notification type has its own configuration and behavioral semantics. You might need to test them in different ways. Additionally, you can customize each type of notification down to a specific detail or a set of criteria to trigger a notification.

**Additional resources**

-  [Create custom notifications](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/using_automation_execution/index#controller-create-custom-notifications)


### 25.4.1. Email




The email notification type supports a wide variety of SMTP servers and has support for SSL/TLS connections.

Provide the following details to set up an email notification:

-  **Host**
-  **Recipient list**
-  **Sender e-mail**
-  **Port**
-  **Timeout** (in seconds): You can set this up to 120 seconds. This is the length of time that automation controller tries to connect to the email server before failure.


![Notification template email](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.5-Using_automation_execution-en-US/images/107174efcf8ed047bb31ba86a527376d/ug-notification-template-email.png)


### 25.4.2. Grafana




To integrate Grafana, you must first create an API key in the [Grafana system](http://docs.grafana.org/tutorials/api_org_token_howto/) . This is the token that is given to automation controller.

Provide the following details to set up a Grafana notification:

-  **Grafana URL** : The URL of the Grafana API service, such as: http://yourcompany.grafana.com.
-  **Grafana API key** : You must first create an API key in the Grafana system.
- Optional: **ID of the dashboard** : When you create an API key for the Grafana account, you can set up a dashboard with a unique ID.
- Optional: **ID of the panel** : If you added panels and graphs to your Grafana interface, you can give its ID here.
- Optional: **Tags for the annotation** : Enter keywords to identify the types of events of the notification that you are configuring.
-  **Disable SSL verification** : SSL verification is on by default, but you can turn off verification of the authenticity of the target’s certificate. Select this option to disable verification for environments that use internal or private CA’s.


![Notification template Grafana](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.5-Using_automation_execution-en-US/images/c2abefe8c5bbce0fbc94e7148ec659b9/ug-notification-template-grafana.png)


### 25.4.3. IRC




The IRC notification takes the form of an IRC bot that connects, delivers its messages to channels or individual users, and then disconnects. The notification bot also supports SSL authentication. The bot does not currently support Nickserv identification. If a channel or user does not exist or is not online then the notification fails. The failure scenario is reserved specifically for connectivity.

Provide the following details to set up an IRC notification:

- Optional: **IRC server password** : IRC servers can require a password to connect. If the server does not require one leave it blank. **IRC Server Port** : The IRC server port. **IRC Server Address** : The hostname or address of the IRC server. **IRC Nick** : The bot’s nickname once it connects to the server. **Destination Channels or Users** : A list of users or channels to which the notification is sent.
- Optional: **Disable SSL verification** : Check if you want the bot to use SSL when connecting.


![Notification template IRC](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.5-Using_automation_execution-en-US/images/741058afb6c29014c154d0608e891a9c/ug-notification-template-irc.png)


### 25.4.4. Mattermost




The Mattermost notification type provides a simple interface to Mattermost’s messaging and collaboration workspace.

Provide the following details to set up a Mattermost notification:

-  **Target URL** : The full URL that is posted to.
- Optional: **Username** : Enter a username for the notification.
- Optional: **Channel** : Enter a channel for the notification.
-  **Icon URL** : Specifies the icon to display for this notification.
-  **Disable SSL verification** : Turns off verification of the authenticity of the target’s certificate. Select this option to disable verification for environments that use internal or private CA’s.


![Notification template Mattermost](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.5-Using_automation_execution-en-US/images/ba256c9e8d464a3ceba578e0cfc06cdb/ug-notification-template-mattermost.png)


### 25.4.5. Pagerduty




To integrate Pagerduty, you must first create an API key in the [PagerDuty system](http://docs.grafana.org/tutorials/api_org_token_howto/) . This is the token that is given to automation controller. Then create a **Service** which provides an **Integration Key** that is also given to automation controller.

Provide the following details to set up a Pagerduty notification:

-  **API Token** : You must first create an API key in the Pagerduty system. This is the token that is given to automation controller.
-  **PagerDuty subdomain** : When you sign up for the Pagerduty account, you receive a unique subdomain to communicate with. For example, if you signed up as "testuser", the web dashboard is at `    testuser.pagerduty.com` and you give the API `    testuser` as the subdomain, not the full domain.
-  **API service/Integration Key** : Enter the API service/integration key created in Pagerduty.
-  **Client Identifier** : This is sent along with the alert content to the Pagerduty service to help identify the service that is using the API key and service. This is helpful if multiple integrations are using the same API key and service.


![Notification template Pagerduty](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.5-Using_automation_execution-en-US/images/1a568ec6a0960a28156d9bf0592f8c26/ug-notification-template-pagerduty.png)


### 25.4.6. Rocket.Chat




The Rocket.Chat notification type provides an interface to Rocket.Chat’s collaboration and communication platform.

Provide the following details to set up a Rocket.Chat notification:

-  **Target URL** : The full URL that is `    POSTed` to.
- Optional: **Username** : Enter a username.
- Optional: **Icon URL** : Specifies the icon to display for this notification
-  **Disable SSL Verification** : Turns off verification of the authenticity of the target’s certificate. Select this option to disable verification for environments that use internal or private CA’s.


![Notification template rocketchat](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.5-Using_automation_execution-en-US/images/c3960d16948f438ba52ddf70a7903196/ug-notification-template-rocketchat.png)


### 25.4.7. Slack




Slack is a collaborative team communication and messaging tool.

Provide the following details to set up a Slack notification:

- A Slack application. For more information, see the [Quickstart](https://api.slack.com/authentication/basics) page of the Slack documentation on how to create one.
-  **Token** : A token. For more information, see [Legacy bots](https://api.slack.com/legacy/enabling-bot-users) and specific details on bot tokens on the [Current token types](https://api.slack.com/authentication/token-types#bot) documentation page.
-  **Destination Channel** : One Slack channel per line. The pound symbol (#) is required for channels. To respond to or start a thread to a specific message add the parent message Id to the channel where the parent message Id is 16 digits. A dot (.) must be manually inserted after the 10th digit. For example, :#destination-channel, 1231257890.006423.
-  **Notification color** : Specify a notification color. Acceptable colors are hex color code, for example: #3af or #789abc. When you have a bot or app set up, you must complete the following steps:


1. Go to **Apps** .
1. Click the newly-created app and then go to **Add features and functionality** , which enables you to configure incoming webhooks, bots, and permissions, as well as **Install your app to your workspace** .



![Notification template slack](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.5-Using_automation_execution-en-US/images/b7fcfb3a2b47bc25ade124cabd5ebb6f/ug-notification-template-slack.png)


### 25.4.8. Twilio




Twilio is a voice and SMS automation service. When you are signed in, you must create a phone number from which the messages are sent. You can then define a **Messaging Service** under **Programmable SMS** and associate the number you previously created with it.

You might need to verify this number or some other information before you are permitted to use it to send to any numbers. The **Messaging Service** does not require a status callback URL and it does not need the ability to process inbound messages.

Under your individual (or sub) account settings, you have API credentials. Twilio uses two credentials to determine which account an API request is coming from. The **Account SID** , which acts as a username, and the **Auth Token** which acts as a password.

Provide the following details to set up a Twilio notification:

-  **Account SID** : Enter the account SID.
-  **Account Token** : Enter the account token.
-  **Source Phone Number** : Enter the number associated with the messaging service in the form of "+15556667777".
-  **Destination SMS Numbers** : Enter the list of numbers you want to receive the SMS. It must be a 10 digit phone number.


![Notification template Twilio](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.5-Using_automation_execution-en-US/images/a49b3099e8ab18dec06ee08b5194d0fa/ug-notification-template-twilio.png)


### 25.4.9. Webhook




The webhook notification type provides a simple interface for sending `POSTs` to a predefined web service. Automation controller `POSTs` to this address by using application and JSON content type with the data payload containing the relevant details in JSON format. Some web service APIs expect HTTP requests to be in a certain format with certain fields.

Configure the webhook notification with the following:

- Configure the HTTP method, usingBasic authentication `    PUT` .
- The body of the outgoing request.
- Configure authentication, using Basic authentication.


Provide the following details to set up a webhook notification:

- Optional: **Username** : Enter a username.
- Optional: **Basic auth password** :
-  **Target URL** : Enter the full URL to which the webhook notification is `    PUT` or `    POSTed` .
-  **HTTP Headers** : Enter Headers in JSON format where the keys and values are strings. For example:


```
{"Authentication": "988881adc9fc3655077dc2d4d757d480b5ea0e11", "MessageType": "Test"}`.
```

-  **Disable SSL Verification** : SSL verification is on by default, but you can choose to turn off verification of the authenticity of the target’s certificate. Select this option to disable verification for environments that use internal or private CA’s.
-  **HTTP Method** : Select the method for your webhook:
-  **POST** : Creates a new resource. It also acts as a catch-all for operations that do not fit into the other categories. It is likely that you need to **POST** unless you know your webhook service expects a **PUT** .
-  **PUT** : Updates a specific resource (by an identifier) or a collection of resources. You can also use **PUT** to create a specific resource if the resource identifier is known beforehand.


![Notification template webhook](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.5-Using_automation_execution-en-US/images/32ba24d9c77a2d82ba1afee9a5e9e65c/ug-notification-template-webhook.png)


#### 25.4.9.1. Webhook payloads




The following data is sent by automation controller at the webhook endpoint:

```
job id
name
url
created_by
started
finished
status
traceback
inventory
project
playbook
credential
limit
extra_vars
hosts
http method
```

The following is an example of a `started` notification through a webhook message as returned by automation controller:

```
{"id": 38, "name": "Demo Job Template", "url": "https://host/#/jobs/playbook/38", "created_by": "bianca", "started":
"2020-07-28T19:57:07.888193+00:00", "finished": null, "status": "running", "traceback": "", "inventory": "Demo Inventory",
"project": "Demo Project", "playbook": "hello_world.yml", "credential": "Demo Credential", "limit": "", "extra_vars": "{}",
"hosts": {}}POST / HTTP/1.1
```

The following data is returned by automation controller at the webhook endpoint for a `success/fail` status:

```
job id
name
url
created_by
started
finished
status
traceback
inventory
project
playbook
credential
limit
extra_vars
hosts
```

The following is an example of a `success/fail` notification as returned by automation controller through a webhook message:

```
{"id": 46, "name": "AWX-Collection-tests-awx_job_wait-long_running-XVFBGRSAvUUIrYKn", "url": "https://host/#/jobs/playbook/46",
"created_by": "bianca", "started": "2020-07-28T20:43:36.966686+00:00", "finished": "2020-07-28T20:43:44.936072+00:00", "status": "failed",
"traceback": "", "inventory": "Demo Inventory", "project": "AWX-Collection-tests-awx_job_wait-long_running-JJSlglnwtsRJyQmw", "playbook":
"fail.yml", "credential": null, "limit": "", "extra_vars": "{\"sleep_interval\": 300}", "hosts": {"localhost": {"failed": true, "changed": 0,
"dark": 0, "failures": 1, "ok": 1, "processed": 1, "skipped": 0, "rescued": 0, "ignored": 0}}}
```

## 25.5. Creating custom notifications




You can [customize the text content](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/using_automation_execution/index#controller-attributes-custom-notifications) of each [Notification type](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/using_automation_execution/index#controller-notification-types) on the notification form.

**Procedure**

1. From the navigation panel, selectAutomation Execution→Administration→Notifiers.
1. ClickCreate notifier.
1. Choose a notification type from the **Type** list.
1. Enable **Customize messages** by using the toggle.

![Customize notification](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.5-Using_automation_execution-en-US/images/39d4ef8e4d673259ea2aebb6f58f663c/ug-notification-template-customize.png)



1. You can provide a custom message for various job events, such as the following:


-  **Start message body**
-  **success message body**
-  **Error message body**
-  **Workflow approved body**
-  **Workflow denied message body**
-  **Workflow pending message body**
-  **Workflow timed out message body**

The message forms vary depending on the type of notification that you are configuring. For example, messages for Email and PagerDuty notifications appear to be a typical email, with a body and a subject, in which case, automation controller displays the fields as **Message** and **Message Body** . Other notification types only expect a **Message** for each type of event.

The **Message** fields are pre-populated with a template containing a top-level variable, `        job` coupled with an attribute, such as `        id` or `        name` . Templates are enclosed in curly brackets and can draw from a fixed set of fields provided by automation controller, shown in the pre-populated message fields:

This pre-populated field suggests commonly displayed messages to a recipient who is notified of an event. You can customize these messages with different criteria by adding your own attributes for the job as needed. Custom notification messages are rendered using Jinja; the same templating engine used by Ansible playbooks.

Messages and message bodies have different types of content, as the following points outline:


- Messages are always just strings, one-liners only. New lines are not supported.
- Message bodies are either a dictionary or a block of text:


- The message body for Webhooks and PagerDuty uses dictionary definitions. The default message body for these is `            {{ job_metadata }}` , you can either leave that as it is or provide your own dictionary.
- The message body for email uses a block of text or a multi-line string. The default message body is:


```
{{ job_friendly_name }} #{{ job.id }} had status {{ job.status }}, view details at {{ url }} {{ job_metadata }}
```

You can edit this text leaving `            {{ job_metadata }}` in, or drop `            {{ job_metadata }}` . Since the body is a block of text, it can be any string you want. `            {{ job_metadata }}` is rendered as a dictionary containing fields that describe the job being executed. In all cases, `            {{ job_metadata }}` includes the following fields:


-  `                id`
-  `                name`
-  `                url`
-  `                created_by`
-  `                started`
-  `                finished`
-  `                status`
-  `                traceback`

You cannot query individual fields within `                {{ job_metadata }}` . When you use `                {{ job_metadata }}` in a notification template, all data is returned.

The resulting dictionary looks like the following:


```
{"id": 18,                 "name": "Project - Space Procedures",                 "url": "https://host/#/jobs/project/18",                 "created_by": "admin",                 "started": "2019-10-26T00:20:45.139356+00:00",                 "finished": "2019-10-26T00:20:55.769713+00:00",                 "status": "successful",                 "traceback": ""                }
```

If `                {{ job_metadata }}` is rendered in a job, it includes the following additional fields:


-  `                inventory`
-  `                project`
-  `                playbook`
-  `                credential`
-  `                limit`
-  `                extra_vars`
-  `                hosts`

The resulting dictionary is similar to the following:


```
{"id": 12,                 "name": "JobTemplate - Launch Rockets",                 "url": "https://host/#/jobs/playbook/12",                 "created_by": "admin",                 "started": "2019-10-26T00:02:07.943774+00:00",                 "finished": null,                 "status": "running",                 "traceback": "",                 "inventory": "Inventory - Fleet",                 "project": "Project - Space Procedures",                 "playbook": "launch.yml",                 "credential": "Credential - Mission Control",                 "limit": "",                 "extra_vars": "{}",                 "hosts": {}                }
```

If `                {{ job_metadata }}` is rendered in a workflow job, it includes the following additional field:


-  `                body` (This enumerates the nodes in the workflow job and includes a description of the job associated with each node)

The resulting dictionary is similar to the following:


```
{"id": 14,                 "name": "Workflow Job Template - Launch Mars Mission",                 "url": "https://host/#/workflows/14",                 "created_by": "admin",                 "started": "2019-10-26T00:11:04.554468+00:00",                 "finished": "2019-10-26T00:11:24.249899+00:00",                 "status": "successful",                 "traceback": "",                 "body": "Workflow job summary:                                         node #1 spawns job #15, \"Assemble Fleet JT\", which finished with status successful.                         node #2 spawns job #16, \"Mission Start approval node\", which finished with status successful.\n                         node #3 spawns job #17, \"Deploy Fleet\", which finished with status successful."                }
```







If you create a notification template that uses invalid syntax or references unusable fields, an error message displays indicating the nature of the error. If you delete a notification’s custom message, the default message is shown in its place.

Important
If you save the notifications template without editing the custom message (or edit and revert back to the default values), the **Details** screen assumes the defaults and does not display the custom message tables. If you edit and save any of the values, the entire table displays in the **Details** screen.



**Additional resources**

-  [Using variables with Jinja2](https://docs.ansible.com/ansible/latest/user_guide/playbooks_variables.html#using-variables-with-jinja2)
-  [Supported attributes for custom notifications](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/using_automation_execution/index#controller-attributes-custom-notifications)


## 25.6. Enable and disable notifications




You can set up notifications to notify you when a specific job starts, as well as on the success or failure at the end of the job run. Note the following behaviors:

- If a workflow job template has notification on start enabled, and a job template within that workflow also has notification on start enabled, you receive notifications for both.
- You can enable notifications to run on many job templates within a workflow job template.
- You can enable notifications to run on a sliced job template start and each slice generates a notification.
- When you enable a notification to run on job start, and that notification gets deleted, the job template continues to run, but results in an error message.


You can enable notifications on job start, job success, and job failure, or a combination of these, from the **Notifications** tab of the **Details** page for the following resources:

- Job Templates
- Workflow Templates
- Projects


For workflow templates that have approval nodes, in addition to **Start** , **Success** , and **Failure** , you can enable or disable certain approval-related events:

**Additional resources**

-  [Approval nodes](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/using_automation_execution/index#controller-approval-nodes)


## 25.7. Configure the host hostname for notifications




In [System settings](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/configuring_automation_execution/controller-config#controller-configure-system) , you can replace the default value in the **Base URL of the service** field with your preferred hostname to change the notification hostname.

Refreshing your license also changes the notification hostname. New installations of automation controller do not have to set the hostname for notifications.

### 25.7.1. Resetting TOWER_URL_BASE




Automation controller determines how the base URL ( `TOWER_URL_BASE` ) is defined by looking at an incoming request and setting the server address based on that incoming request.

Automation controller takes settings values from the database first. If no settings values are found, it uses the values from the settings files. If you post a license by navigating to the automation controller host’s IP address, the posted license is written to the settings entry in the database.

Use the following procedure to reset `TOWER_URL_BASE` if the wrong address has been picked up:

**Procedure**

1. From the navigation panel, selectSettings→System.
1. ClickEdit.
1. Enter the address in the **Base URL of the service** field for the DNS entry you want to appear in notifications.


## 25.8. Notifications API




Use the `started` , `success` , or `error` endpoints:

```
/api/v2/organizations/N/notification_templates_started/
/api/v2/organizations/N/notification_templates_success/
/api/v2/organizations/N/notification_templates_error/
```

Additionally, the `../../../N/notification_templates_started` endpoints have `GET` and `POST` actions for:

- Organizations
- Projects
- Inventory Sources
- Job Templates
- System Job Templates
- Workflow Job Templates


# Chapter 26. Supported attributes for custom notifications




Learn about the list of supported job attributes and the proper syntax for constructing the message text for notifications.


<span id="controller-supported-attributes"></span>
The following are the supported job attributes:


-  `    allow_simultaneous` - (boolean) Indicates if multiple jobs can run simultaneously from the job template associated with this job.
-  `    controller_node` - (string) The instance that manages the isolated execution environment.
-  `    created` - (datetime) The timestamp when this job was created.
-  `    custom_virtualenv` - (string) The custom virtual environment used to run the job.
-  `    description` - (string) An optional description of the job.
-  `    diff_mode` - (boolean) If enabled, textual changes made to any templated files on the host are shown in the standard output.
-  `    elapsed` - (decimal) The elapsed time in seconds that the job has run.
-  `    execution_node` - (string) The node that the job executes on.
-  `    failed` - (boolean) True if the job failed.
-  `    finished` - (datetime) The date and time the job finished execution.
-  `    force_handlers` - (boolean) When handlers are forced, they run when notified even if a task fails on that host. Note that some conditions, such as unreachable hosts can still prevent handlers from running.
-  `    forks` - (int) The number of forks requested for this job.
-  `    id` - (int) The database ID for this job.
-  `    job_explanation` - (string) The status field to indicate the state of the job if it was not able to run and capture `    stdout` .
-  `    job_slice_count` - (integer) If run as part of a sliced job, this is the total number of slices (if 1, job is not part of a sliced job).
-  `    job_slice_number` - (integer) If run as part of a sliced job, this is the ID of the inventory slice operated on (if not part of a sliced job, attribute is not used).
-  `    job_tags` - (string) Only tasks with specified tags run.
-  `    job_type` - (choice) This can be `    run` , `    check` , or `    scan` .
-  `    launch_type` - (choice) This can be `    manual` , `    relaunch` , `    callback` , `    scheduled` , `    dependency` , `    workflow` , `    sync` , or `    scm` .
-  `    limit` - (string) The playbook execution limited to this set of hosts, if specified.
-  `    modified` - (datetime) The timestamp when this job was last modified.
-  `    name` - (string) The name of this job.
-  `    playbook` - (string) The playbook executed.
-  `    scm_revision` - (string) The scm revision from the project used for this job, if available.
-  `    skip_tags` - (string) The playbook execution skips over this set of tags, if specified.
-  `    start_at_task` - (string) The playbook execution begins at the task matching this name, if specified.
-  `    started` - (datetime) The date and time the job was queued for starting.
-  `    status` - (choice) This can be `    new` , `    pending` , `    waiting` , `    running` , `    successful` , `    failed` , `    error` , or `    canceled` .
-  `    timeout` - (int) The amount of time, in seconds, to run before the task is canceled.
-  `    type` - (choice) The data type for this job.
-  `    url` - (string) The URL for this job.
-  `    use_fact_cache` - (boolean) If enabled for the job, automation controller acts as an Ansible Fact Cache Plugin at the end of a playbook run to the database and caches facts for use by Ansible.
-  `    verbosity` - (choice) 0 through 5 (corresponding to Normal through WinRM Debug).


-  `        host_status_counts` (The count of hosts uniquely assigned to each status)


-  `            skipped` (integer)
-  `            ok` (integer)
-  `            changed` (integer)
-  `            failures` (integer)
-  `            dark` (integer)
-  `            processed` (integer)
-  `            rescued` (integer)
-  `            ignored` (integer)
-  `            failed` (boolean)

-  `        summary_fields` :


-  `            inventory`


-  `                id` - (integer) The database ID for the inventory.
-  `                name` - (string) The name of the inventory.
-  `                description` - (string) An optional description of the inventory.
-  `                has_active_failures` - (boolean) (deprecated) flag indicating whether any hosts in this inventory have failed.
-  `                total_hosts` - (deprecated) (int) The total number of hosts in this inventory.
-  `                hosts_with_active_failures` - (deprecated) (int) The number of hosts in this inventory with active failures.
-  `                total_groups` - (deprecated) (int) The total number of groups in this inventory.
-  `                groups_with_active_failures` - (deprecated) (int) The number of hosts in this inventory with active failures.
-  `                has_inventory_sources` - (deprecated) (boolean) The flag indicating whether this inventory has external inventory sources.
-  `                total_inventory_sources` - (int) The total number of external inventory sources configured within this inventory.
-  `                inventory_sources_with_failures` - (int) The number of external inventory sources in this inventory with failures.
-  `                organization_id` - (id) The organization containing this inventory.
-  `                kind` - (choice) (empty string) (indicating hosts have direct link with inventory) or `                smart`

-  `            project`


-  `                id` - (int) The database ID for the project.
-  `                name` - (string) The name of the project.
-  `                description` (string) An optional description of the project.
-  `                status` - (choices) One of `                new` , `                pending` , `                waiting` , `                running` , `                successful` , `                failed` , `                error` , `                canceled` , `                never updated` , `                ok` , or `                missing` .
-  `                scm_type` (choice) One of (empty string), `                git` , `                hg` , `                svn` , `                insights` .

-  `            job_template`


-  `                id` - (int) The database ID for the job template.
-  `                description` - (string) The optional description of the project.
-  `                status` - (choices) One of `                new` , `                pending` , `                waiting` , `                running` , `                successful` , `                failed` , `                error` , `                canceled` , `                never updated` , `                ok` , or `                missing` .

-  `            job_template`


-  `                id` - (int) The database ID for the job template.
-  `                name` - (string) The name of the job template.
-  `                description` - (string) An optional description for the job template.

-  `            unified_job_template`


-  `                id` - (int) The database ID for the unified job template.
-  `                name` - (string) The name of the unified job template.
-  `                description` - (string) An optional description for the unified job template.
-  `                unified_job_type` - (choice) The unified job type, such as `                job` , `                workflow_job` , or `                project_update` .

-  `            instance_group`


-  `                id` - (int) The database ID for the instance group.
-  `                name` - (string) The name of the instance group.

-  `            created_by`


-  `                id` - (int) The database ID of the user that launched the operation.
-  `                username` - (string) The username that launched the operation.
-  `                first_name` - (string) The first name.
-  `                last_name` - (string) The last name.

-  `            labels`


-  `                count` - (int) The number of labels.
-  `                results` - The list of dictionaries representing labels. For example, {"id": 5, "name": "database jobs"}.





You can reference information about a job in a custom notification message by using grouped curly brackets {{ }}. Access specific job attributes by using dotted notation, for example, {{ job.summary_fields.inventory.name }}. You can add any characters used in front or around the braces, or plain text, for clarification, such as "#" for job ID and single-quotes to denote some descriptor. Custom messages can include several variables throughout the message:

```
{{ job_friendly_name }} {{ job.id }} ran on {{ job.execution_node }} in {{ job.elapsed }} seconds.
```

The following are additional variables that can be added to the template:

-  `    approval_node_name` - (string) The approval node name.
-  `    approval_status` - (choice) One of `    approved` , `    denied` , and `    timed_out` .
-  `    url` - (string) The URL of the job for which the notification is emitted (this applies to `    start` , `    success` , `    fail` , and `    approval notifications` ).
-  `    workflow_url` - (string) The URL to the relevant approval node. This allows the notification recipient to go to the relevant workflow job page to examine the situation. For example, `    This node can be viewed at: {{workflow_url }}` . In cases of approval-related notifications, both `    url` and `    workflow_url` are the same.
-  `    job_friendly_name` - (string) The friendly name of the job.
-  `    job_metadata` - (string) The job metadata as a JSON string, for example:


```
{'url': 'https://automationcontroller.example.com/$/jobs/playbook/13',     'traceback': '',     'status': 'running',     'started': '2019-08-07T21:46:38.362630+00:00',     'project': 'Stub project',     'playbook': 'ping.yml',     'name': 'Stub Job Template',     'limit': '',     'inventory': 'Stub Inventory',     'id': 42,     'hosts': {},     'friendly_name': 'Job',     'finished': False,     'credential': 'Stub credential',     'created_by': 'admin'}
```




# Chapter 27. Working with Webhooks




Use webhooks to run specified commands between applications over the web. Automation controller currently provides webhook integration with GitHub and GitLab.

Set up a webhook by using the following services:

-  [Setting up a GitHub webhook](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/using_automation_execution/index#controller-set-up-github-webhook)
-  [Setting up a GitLab webhook](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/using_automation_execution/index#controller-set-up-gitlab-webhook)
-  [Viewing the payload output](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/using_automation_execution/index#controller-view-payload-output)


The webhook post-status-back functionality for GitHub and GitLab is designed to work only under certain CI events. Receiving another kind of event results in messages such as the following in the service log:

`awx.main.models.mixins Webhook event did not have a status API endpoint associated, skipping.`

## 27.1. Setting up a GitHub webhook




Automation controller has the ability to run jobs based on a triggered webhook event coming in. Job status information (pending, error, success) can be sent back only for pull request events. If you do not need automation controller to post job statuses back to the webhook service, go directly to step 3.

**Procedure**

1. Generate a _Personal Access Token_ (PAT) for use with automation controller:


1. In the profile settings of your GitHub account, select **Settings** .
1. From the navigation panel, select<> Developer Settings.
1. On the **Developer Settings** page, select **Personal access tokens** .
1. Select **Tokens (classic)**
1. From the **Personal access tokens** screen, clickGenerate a personal access token.
1. When prompted, enter your GitHub account password to continue.
1. In the **Note** field, enter a brief description about what this PAT is used for.
1. In the **Select scopes** fields, check the boxes next to **repo:status** , **repo_deployment** , and **public_repo** . The automation webhook only needs repository scope access, with the exception of invites. For more information, see [Scopes for OAuth apps documentation](https://docs.github.com/en/apps/oauth-apps/building-oauth-apps/scopes-for-oauth-apps) .
1. ClickGenerate token.

Important
When the token is generated, ensure that you copy the PAT, as you need it in step 2. You cannot access this token again in GitHub.





1. Use the PAT to optionally create a GitHub credential:


1. Go to your instance and create a new credential for the GitHub PAT, using the generated token.
1. Make note of the name of this credential, as you use it in the job template that posts back to GitHub.

![GitHub PAT token](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.5-Using_automation_execution-en-US/images/f1178df4817793e7e13e78e51c34c190/ug-webhooks-github-PAT-token.png)



1. Go to the job template with which you want to enable webhooks, and select the webhook service and credential you created in the preceding step.

![GitLab webhook credential](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.5-Using_automation_execution-en-US/images/8f70d3fad47e82e19b7d366cde04bd36/ug-webhooks-webhook-credential.png)



1. ClickSave. Your job template is set up to post back to GitHub.

1. Go to a GitHub repository where you want to configure webhooks and selectSettings.
1. From the navigation panel, selectWebhooks→Add webhook.
1. To complete the **Add webhook** page, you must check the **Enable Webhook** option in a job template or workflow job template. For more information, see step 3 in both [Creating a job template](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/using_automation_execution/index#controller-create-job-template) and [Creating a workflow job template](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/using_automation_execution/index#controller-create-workflow-template) .
1. Complete the following fields:


-  **Payload URL** : Copy the contents of the **Webhook URL** from the job template and paste it here. The results are sent to this address from GitHub.
-  **Content type** : Set it to **application/json** .
-  **Secret** : Copy the contents of the **Webhook Key** from the job template and paste it here.
-  **Which events would you like to trigger this webhook?** : Select the types of events you want to trigger a webhook. Any such event will trigger the job or workflow. To have the job status (pending, error, success) sent back to GitHub, you must select **Pull requests** in the **Let me select individual events** section.

![Github repo choose events](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.5-Using_automation_execution-en-US/images/5e51e67876219fa5a9bb6c2520b8cb87/ug-webhooks-github-repo-choose-events.png)



-  **Active** : Leave this checked.

1. ClickAdd webhook.
1. When your webhook is configured, it is displayed in the list of webhooks active for your repository, along with the ability to edit or delete it. Click a webhook, to go to the **Manage webhook** screen.
1. Scroll to view the delivery attempts made to your webhook and whether they succeeded or failed.


**Additional resources**

-  [Webhooks documentation](https://docs.github.com/en/webhooks)


## 27.2. Setting up a GitLab webhook




Automation controller has the ability to run jobs based on a triggered webhook event coming in. Job status information (pending, error, success) can be sent back only for pull request events. If automation controller is not required to post job statuses back to the webhook service, go directly to step 3.

**Procedure**

1. Generate a _Personal Access Token_ (PAT) for use with automation controller:


1. From the navigation panel in GitLab, select your avatar andEdit profile.
1. From the navigation panel, selectAccess tokens.
1. Complete the following fields:


-  **Token name** : Enter a brief description about what this PAT is used for.
-  **Expiration date** : Skip this field unless you want to set an expiration date for your webhook.
-  **Select scopes** : Select those that are applicable to your integration. For automation controller, **api** is the only selection necessary.

1. ClickCreate personal access token.

Important
When the token is generated, ensure that you copy the PAT, as you need it in step 2. You cannot access this token again in GitLab.





1. Use the PAT to optionally create a GitLab credential:


1. Go to your instance, and create a new credential for the GitLab PAT, using the generated token.
1. Make note of the name of this credential, as you use it in the job template that posts back to GitLab.

![GitLab PAT token](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.5-Using_automation_execution-en-US/images/08d0556825411e6d2987f4f946d9be22/ug-webhooks-create-credential-gitlab-PAT-token.png)



1. Go to the job template with which you want to enable webhooks, and select the webhook service and credential you created in the preceding step.

![GitLab webhook credential](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.5-Using_automation_execution-en-US/images/4c15cb5c38b69f6dec23a362a018b519/ug-gitlab-webhook-credential.png)



1. ClickSave. Your job template is set up to post back to GitLab.

1. Go to a GitLab repository where you want to configure webhooks.
1. From the navigation panel, selectSettings→Integrations.
1. To complete the **Add webhook** page, you must check the **Enable Webhook** option in a job template or workflow job template. For more information, see step 3 in both [Creating a job template](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/using_automation_execution/index#controller-create-job-template) and [Creating a workflow job template](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/using_automation_execution/index#controller-create-workflow-template) .
1. Complete the following fields:


-  **URL** : Copy the contents of the **Webhook URL** from the job template and paste it here. The results are sent to this address from GitLab.
-  **Secret Token** : Copy the contents of the **Webhook Key** from the job template and paste it here.
-  **Trigger** : Select the types of events you want to trigger a webhook. Any such event will trigger the job or workflow. To have job status (pending, error, success) sent back to GitLab, you must select **Merge request events** in the **Trigger** section.
-  **SSL verification** : Leave **Enable SSL verification** selected.

1. ClickAdd webhook.
1. When your webhook is configured, it is displayed in the list **Project Webhooks** for your repository, along with the ability to test events, edit or delete the webhook. Testing a webhook event displays the results on each page whether it succeeded or failed.


**Additional resources**

-  [Webhooks](https://docs.gitlab.com/ee/user/project/integrations/webhooks.html)


## 27.3. Viewing the payload output




You can view the entire payload exposed as an extra variable.

**Procedure**

1. From the navigation panel, selectAutomation Execution→Jobs.
1. Select the job template with the webhook enabled.
1. Select the **Details** tab.
1. In the **Extra Variables** field, view the payload output from the `    awx_webhook_payload` variable, as shown in the following example:

![Webhooks extra variables payload](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.5-Using_automation_execution-en-US/images/f534a94752ebb695bb4a4e0c8dfb5310/ug-webhooks-jobs-extra-vars-payload.png)


![Webhook extra variables payload expanded](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.5-Using_automation_execution-en-US/images/8cef14342dfd738ae40fca1c770950ec/ug-webhooks-jobs-extra-vars-payload-expanded.png)





# Chapter 28. Setting up Red Hat Insights for Red Hat Ansible Automation Platform Remediations




Automation controller supports integration with Red Hat Insights.

When a host is registered with Red Hat Insights, it is scanned continually for vulnerabilities and known configuration conflicts. Each problem identified can have an associated fix in the form of an Ansible Playbook.

Red Hat Insights users create a maintenance plan to group the fixes and can create a playbook to mitigate the problems. Automation controller tracks the maintenance plan playbooks through a Red Hat Insights project.

Authentication to Red Hat Insights through Basic Authorization is backed by a special credential, which must first be established in automation controller.

To run a Red Hat Insights maintenance plan, you need a Red Hat Insights project and inventory.

## 28.1. Creating Red Hat Insights credentials




To create a Red Hat Insights credential, use the following procedure:

**Procedure**

1. From the navigation panel, selectAutomation Execution→Infrastructure→Credentials.
1. ClickCreate credential.
1. Enter the appropriate details in the following fields:


-  **Name** : Enter the name of the credential.
- Optional: **Description** : Enter a description for the credential.
- Optional: **Organization** : Enter the name of the organization with which the credential is associated, or click the search![Search](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.5-Using_automation_execution-en-US/images/74841a45a98b4160b7576724a8f4c038/search.png)
icon and select it from the **Select organization** window.
-  **Credential type** : Enter **Insights** or select it from the list.

![Credentials insights pop up](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.5-Using_automation_execution-en-US/images/2b259cb713ff79de481a59c82f8772ad/ug-credential-types-popup-window-insights.png)



-  **Username** : Enter a valid Red Hat Insights credential.
-  **Password** : Enter a valid Red Hat Insights credential.

The Insights for Ansible Automation Platform credentials are the user’s [Red Hat Customer Portal](https://access.redhat.com/) account username and password.



1. ClickCreate credential.


## 28.2. Creating a Red Hat Insights project




Use the following steps to create a new project for use with Red Hat Insights:

**Procedure**

1. From the navigation panel, selectAutomation Execution→Projects.
1. ClickCreate project.
1. Enter the appropriate details in the following fields. Note that the following fields require specific Red Hat Insights related entries:


-  **Name** : Enter the name for your Red Hat Insights project.
- Optional: **Description** : Enter a description for the project.
-  **Organization** : Enter the name of the organization with which the credential is associated, or click the search![Search](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.5-Using_automation_execution-en-US/images/74841a45a98b4160b7576724a8f4c038/search.png)
icon and select it from the **Select organization** window.
- Optional: **Execution environment** : The execution environment that is used for jobs that use this project.
-  **Source control type** : Select **Red Hat Insights** .
- Optional: **Content signature validation credential** : Enable content signing to verify that the content has remained secure when a project is synced.
-  **Insights credential** : This is pre-populated with the Red Hat Insights credential you created before. If not, enter the credential, or click the search![Search](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.5-Using_automation_execution-en-US/images/74841a45a98b4160b7576724a8f4c038/search.png)
icon and select it from the **Select Insights Credential** window.

1. Select the update options for this project from the **Options** field and provide any additional values, if applicable. For more information about each option click the tooltip![Tooltip](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.5-Using_automation_execution-en-US/images/0c17081b1d1293156a760e9a6e06634a/question_circle.png)
icon next to each one.

![Insights create project](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.5-Using_automation_execution-en-US/images/36ff3c474fcbf02cc9b2425d470ef05d/ug-insights-create-project-insights-form.png)



1. ClickCreate project.


All SCM and project synchronizations occur automatically the first time you save a new project. If you want them to be updated to what is current in Red Hat Insights, manually update the SCM-based project by clicking the update![Update](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.5-Using_automation_execution-en-US/images/3d77a9f541616ea047f39ea929579274/ug-update-button.png)
icon under the project’s available actions.

This process syncs your Red Hat Insights project with your Red Hat Insights account solution. Note that the status dot beside the name of the project updates once the sync has run.

## 28.3. Create an Insights inventory




The Insights playbook contains a `hosts:` line where the value is the host name supplied to red Hat insights, which can be different from the host name supplied to automation controller

## 28.4. Remediating a Red Hat Insights inventory




Remediation of a Red Hat Insights inventory enables automation controller to run Red Hat Insights playbooks with a single click.

You can do this by creating a job template to run the Red Hat Insights remediation.

**Procedure**

1. From the navigation menu, selectAutomation Execution→Templates.
1. On the **Templates** list view, clickCreate templateand select from the list.
1. Enter the appropriate details in the following fields. Note that the following fields require specific Red Hat Insights related entries:


-  **Name** : Enter the name of your Maintenance Plan.
- Optional: **Description** : Enter a description for the job template.
-  **Job Type** : If not already populated, select **Run** from the job type list.
-  **Inventory** : Select the Red Hat Insights inventory that you previously created.
-  **Project** : Select the Red Hat Insights project that you previously created.
- Optional: **Execution Environment** : The container image to be used for execution.
-  **Playbook** : Select a playbook associated with the Maintenance Plan that you want to run from the playbook list.
- Optional: **Credentials** : Enter the credential to use for this project or click the search (![Search](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.5-Using_automation_execution-en-US/images/9e5c25fe4be71dcba8b8d063ae0fc7f9/magnify.png)
) icon and select it from the pop-up window. The credential does not have to be a Red Hat Insights credential.
-  **Verbosity** : Keep the default setting, or select the desired verbosity from the list.

![Insights job template](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.5-Using_automation_execution-en-US/images/c4e4f3e6570148ef4dbcb806edfc21c1/ug-insights-create-job-template.png)




1. ClickCreate job template.
1. Click the launch![Launch](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.5-Using_automation_execution-en-US/images/15376a8ac10d1efa9ec8cb3d4c707dfd/rightrocket.png)
icon to launch the job template.


When complete, the job results in the **Job Details** page.

# Chapter 29. Best practices for automation controller




The following describes best practice for the use of automation controller:

## 29.1. Use source control




Automation controller supports playbooks stored directly on the server. Therefore, you must store your playbooks, roles, and any associated details in source control. This way you have an audit trail describing when and why you changed the rules that are automating your infrastructure. Additionally, it permits sharing of playbooks with other parts of your infrastructure or team.

## 29.2. Ansible file and directory structure




If you are creating a common set of roles to use across projects, these should be accessed through source control submodules, or a common location such as `/opt` . Projects should not expect to import roles or content from other projects.

For more information, see the link [General tips](https://docs.ansible.com/ansible/latest/tips_tricks/ansible_tips_tricks.html) from the Ansible documentation.

Note
- Avoid using the playbooks `    vars_prompt` feature, as automation controller does not interactively permit `    vars_prompt` questions. If you cannot avoid using `    vars_prompt` , see the [Surveys in job templates](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/using_automation_execution/index#controller-surveys-in-job-templates) functionality.
- Avoid using the playbooks `    pause` feature without a timeout, as automation controller does not permit canceling a pause interactively. If you cannot avoid using `    pause` , you must set a timeout.




Jobs use the playbook directory as the current working directory, although jobs must be coded to use the `playbook_dir` variable rather than relying on this.

## 29.3. Use Dynamic Inventory Sources




If you have an external source of truth for your infrastructure, whether it is a cloud provider or a local CMDB, it is best to define an inventory sync process and use the support for dynamic inventory (including cloud inventory sources). This ensures your inventory is always up to date.

Note
Edits and additions to Inventory host variables persist beyond an inventory synchronization as long as `--overwrite_vars` is **not** set.



## 29.4. Variable Management for Inventory




Keep variable data with the hosts and groups definitions (see the inventory editor), rather than using `group_vars/` and `host_vars/` . If you use dynamic inventory sources, automation controller can synchronize such variables with the database as long as the **Overwrite Variables** option is not set.

## 29.5. Autoscaling




Use the "callback" feature to permit newly booting instances to request configuration for auto-scaling scenarios or provisioning integration.

## 29.6. Larger Host Counts




Set "forks" on a job template to larger values to increase parallelism of execution runs.

## 29.7. Continuous integration / Continuous Deployment




For a Continuous Integration system, such as Jenkins, to spawn a job, it must make a `curl` request to a job template. The credentials to the job template must not require prompting for any particular passwords. For configuration and use instructions, see [Installation](https://docs.ansible.com/automation-controller/latest/html/controllercli/usage.html) in the Ansible documentation.

# Chapter 30. Glossary




See also, **Node** .


<span id="idm140390005286128"></span>
# Legal Notice

Copyright© 2025 Red Hat, Inc.
The text of and illustrations in this document are licensed by Red Hat under a Creative Commons Attribution–Share Alike 3.0 Unported license ("CC-BY-SA"). An explanation of CC-BY-SA is available at [http://creativecommons.org/licenses/by-sa/3.0/](http://creativecommons.org/licenses/by-sa/3.0/) . In accordance with CC-BY-SA, if you distribute this document or an adaptation of it, you must provide the URL for the original version.
Red Hat, as the licensor of this document, waives the right to enforce, and agrees not to assert, Section 4d of CC-BY-SA to the fullest extent permitted by applicable law.
Red Hat, Red Hat Enterprise Linux, the Shadowman logo, the Red Hat logo, JBoss, OpenShift, Fedora, the Infinity logo, and RHCE are trademarks of Red Hat, Inc., registered in the United States and other countries.
Linux® is the registered trademark of Linus Torvalds in the United States and other countries.
Java® is a registered trademark of Oracle and/or its affiliates.
XFS® is a trademark of Silicon Graphics International Corp. or its subsidiaries in the United States and/or other countries.
MySQL® is a registered trademark of MySQL AB in the United States, the European Union and other countries.
Node.js® is an official trademark of Joyent. Red Hat is not formally related to or endorsed by the official Joyent Node.js open source or commercial project.
TheOpenStack® Word Mark and OpenStack logo are either registered trademarks/service marks or trademarks/service marks of the OpenStack Foundation, in the United States and other countries and are used with the OpenStack Foundation's permission. We are not affiliated with, endorsed or sponsored by the OpenStack Foundation, or the OpenStack community.
All other trademarks are the property of their respective owners.






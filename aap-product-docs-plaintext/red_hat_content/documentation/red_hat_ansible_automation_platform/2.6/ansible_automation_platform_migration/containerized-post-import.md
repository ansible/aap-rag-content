# 7. Target environment
## 7.1. Container-based Ansible Automation Platform
### 7.1.3. Reconciling the target environment post-import




Perform the following post-import reconciliation steps to verify your target environment functions correctly.

**Procedure**

1. Deprovision the platform gateway configuration.


- To deprovision platform gateway configuration, SSH to the host serving an `        automation-gateway` container as the same rootless user from 4.2.6 and run the following to remove the platform gateway proxy configuration:


```
$ podman exec -it automation-gateway bash        $ aap-gateway-manage migrate        $ aap-gateway-manage shell_plus        &gt;&gt;&gt; HTTPPort.objects.all().delete(); ServiceNode.objects.all().delete(); ServiceCluster.objects.all().delete()
```



1. Transfer custom configurations and settings.


- Edit the inventory file and apply any relevant `        extra_settings` to each component by using the `        component_extra_settings` .

1. Remove all resource server key secrets to be repopulated by the installation program:


```
$ for i in `podman secret ls | egrep 'resource_server' | awk '{print $2}'`; do podman secret rm $i; done
```


1. Re-run the installation program on the target environment by using the same inventory from the installation.
1. Sync platform gateway resources if Event-Driven Ansible is present:


```
$ podman exec -it automation-eda-api bash    $ aap-eda-manage resource_sync
```


1. Validate instances for automation execution.


1. SSH to the host serving an `        automation-controller-task` container as the rootless user, and run the following commands to validate and remove instances that are orphaned from the source artifact:


```
$ podman exec -it automation-controller-task bash
```


```
$ awx-manage list_instances
```


1. Find nodes that are no longer part of this cluster. A good indicator is nodes with 0 capacity as they have failed their health checks:


```
[ungrouped capacity=0]        	[DISABLED] node1.example.org capacity=0 node_type=hybrid version=X.Y.Z heartbeat="..."        	[DISABLED] node2.example.org capacity=0 node_type=execution version=ansible-runner-X.Y.Z heartbeat="..."
```


1. Remove those nodes with `        awx-manage` , leaving only the `        aap-controller-task` instance:


```
awx-manage deprovision_instance --host=node1.example.org        awx-manage deprovision_instance --host=node2.example.org
```



1. Repair orphaned automation hub content links for Pulp.


- Run the following command from any host that has direct access to the automation hub address:


```
$ curl -d '{\"verify_checksums\": true }' -X POST -k https://&lt;gateway url&gt;/api/galaxy/pulp/api/v3/repair/ -u &lt;gateway_admin_user&gt;:&lt;gateway_admin_password&gt;
```



1. Reconcile instance groups configuration:


1. Go toAutomation Execution→Infrastructure→Instance Groups.
1. Select the **Instance Group** and then select the **Instances** tab.
1. Associate or disassociate instances as required.

1. Reconcile decision environments and credentials:


1. Go toAutomation Decisions→Decision Environments.
1. Edit each decision environment which references a registry URL either unrelated or no longer accessible to this new environment. For example, the automation hub decision environment might require modification for the target automation hub environment.
1. Select each associated credential to these decision environments and ensure their addresses align with the new environment.

1. Reconcile execution environments and credentials:


1. Go toAutomation Execution→Infrastructure→Execution Environments.
1. Check each execution environment image and verify their addresses against the new environment.
1. Go toAutomation Execution→Infrastructure→Credentials.
1. Edit each credential and ensure that all environment specific information aligns with the new environment.

1. Verify any further customizations or configurations after the migration, such as RBAC rules with instance groups.



# 4. Deprovisioning individual nodes or groups
## 4.2. Deprovisioning isolated nodes




You have the option to manually remove any isolated nodes using the `awx-manage` deprovisioning utility.

Warning
Use the deprovisioning command to remove only isolated nodes that have not migrated to execution nodes. To deprovision execution nodes from your automation mesh architecture, use the [Deprovisioning individual nodes using the installer](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html-single/automation_mesh_for_vm_environments/index#proc-deprovisioning-nodes) method instead.



**Procedure**

1. Shut down the instance:


```
$ automation-controller-service stop
```


1. Run the deprovision command from another instance, replacing `    <span class="emphasis"><em><span class="Role ARG Spec Role ARG Spec">host_name</span></em></span>` with the name of the node as listed in the inventory file:


```
$ awx-manage deprovision_instance --hostname=<span class="emphasis"><em><span class="Role ARG Spec Role ARG Spec">&lt;host_name&gt;</span></em></span>
```





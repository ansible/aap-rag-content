# 4. Deprovisioning individual nodes or groups
## 4.4. Deprovisioning isolated instance groups




You have the option to manually remove any isolated instance groups using the `awx-manage` deprovisioning utility.

Warning
Use the deprovisioning command to only remove isolated instance groups. To deprovision instance groups from your automation mesh architecture, use the [Deprovisioning groups using the installer](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/automation_mesh_for_vm_environments/index#proc-deprovisioning-groups) method instead.



**Procedure**

- Run the following command, replacing `    <span class="emphasis"><em><span class="Role ARG Spec Role ARG Spec">&lt;name&gt;</span></em></span>` with the name of the instance group:


```
$ awx-manage unregister_queue --queuename=<span class="emphasis"><em><span class="Role ARG Spec Role ARG Spec">&lt;name&gt;</span></em></span>
```





<span id="idm140138491277488"></span>

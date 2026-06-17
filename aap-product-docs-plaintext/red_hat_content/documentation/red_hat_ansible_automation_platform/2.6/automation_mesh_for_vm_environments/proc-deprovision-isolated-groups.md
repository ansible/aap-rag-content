# 4. Deprovisioning individual nodes or groups
## 4.4. Deprovisioning isolated instance groups

You have the option to manually remove any isolated instance groups using the `awx-manage` deprovisioning utility.

Warning

Use the deprovisioning command to only remove isolated instance groups. To deprovision instance groups from your automation mesh architecture, use the [Deprovisioning groups using the installer](#proc-deprovisioning-groups "4.3.&nbsp;Deprovisioning groups using the installer") method instead.

**Procedure**

- Run the following command, replacing `<name>` with the name of the instance group:

$ awx-manage unregister_queue --queuename=<name>


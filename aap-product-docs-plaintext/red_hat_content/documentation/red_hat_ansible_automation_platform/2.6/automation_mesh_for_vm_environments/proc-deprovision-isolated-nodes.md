# 4. Deprovisioning individual nodes or groups
## 4.2. Deprovisioning isolated nodes

You have the option to manually remove any isolated nodes using the `awx-manage` deprovisioning utility.

Warning

Use the deprovisioning command to remove only isolated nodes that have not migrated to execution nodes. To deprovision execution nodes from your automation mesh architecture, use the [Deprovisioning individual nodes using the installer](#proc-deprovisioning-nodes "4.1.&nbsp;Deprovisioning individual nodes using the installer") method instead.

**Procedure**

1. Shut down the instance:

$ automation-controller-service stop

2. Run the deprovision command from another instance, replacing `host_name` with the name of the node as listed in the inventory file:

$ awx-manage deprovision_instance --hostname=<host_name>


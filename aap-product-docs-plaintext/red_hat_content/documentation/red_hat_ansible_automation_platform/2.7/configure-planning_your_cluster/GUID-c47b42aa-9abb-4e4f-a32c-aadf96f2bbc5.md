# Planning your cluster environment
## Deprovision cluster instances

Deprovision an instance from an automation controller cluster.

### About this task

Re-running the setup playbook does not automatically deprovision instances because clusters do not currently distinguish between an instance that was taken offline intentionally or due to failure. Instead, shut down all services on the automation controller instance and then run the deprovisioning tool from any other instance.

### Procedure

1.  Shut down the instance or stop the service with the command: `automation-controller-service stop `.
2.  Run the following deprovision command from another instance to remove it from the automation controller cluster: $ awx-manage deprovision_instance --hostname=<name used in inventory file.
3.  The following is an example deprovision command:`$ awx-manage deprovision_instance --hostname=hostB`
4.  Restart the services on the remaining instances with the command:`automation-controller-service start`.


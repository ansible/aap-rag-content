# 6. Clustering
## 6.6. Deprovisioning instances




Re-running the setup playbook does not automatically deprovision instances since clusters do not currently distinguish between an instance that was taken offline intentionally or due to failure. Instead, shut down all services on the automation controller instance and then run the deprovisioning tool from any other instance.

**Procedure**

1. Shut down the instance or stop the service with the command: `    automation-controller-service stop` .
1. Run the following deprovision command from another instance to remove it from the automation controller cluster:


```
$ awx-manage deprovision_instance --hostname=&lt;name used in inventory file&gt;
```




The following is an example deprovision command:

```
$ awx-manage deprovision_instance --hostname=hostB
```

Deprovisioning instance groups in automation controller does not automatically deprovision or remove instance groups. For more information, see the [Deprovisioning instance groups](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/using_automation_execution/controller-instance-and-container-groups#controller-deprovision-instance-group) section in _Using automation execution_ .


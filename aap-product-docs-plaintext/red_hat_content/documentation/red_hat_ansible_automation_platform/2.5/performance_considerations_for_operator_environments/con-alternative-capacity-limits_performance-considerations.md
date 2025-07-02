# 2. Control plane adjustments
## 2.3. Alternative capacity limiting with automation controller settings




The capacity of a control node in OpenShift is determined by the memory and CPU limits. However, if these are not set then the capacity is determined by the memory and CPU detected by the pod on the filesystem, which are actually the CPU and memory of the underlying Kubernetes node.

This can lead to issues with overwhelming the underlying Kubernetes pod if the automation controller pod is not the only pod on that node. If you do not want to set limits directly on the task container, you can use `extra_settings` , see _Extra Settings_ in [Custom pod timeouts](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/performance_considerations_for_operator_environments/index#proc-specify-nodes-job-execution) section for how to configure the following:

```
SYSTEM_TASK_ABS_MEM = 3gi
SYSTEM_TASK_ABS_CPU = 750m
```

This acts as a soft limit within the application that enables automation controller to control how much work it attempts to run, while not risking any CPU throttling from Kubernetes itself, or being reaped if memory usage peaks above the required limit. These settings accept the same format accepted by resource requests and limits in the Kubernetes resource definition.


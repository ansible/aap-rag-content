# Control where automation runs with container groups
## Container capacity limits

When using container groups in automation controller, you can set capacity limits for the containers that run the jobs.

Capacity limits and quotas for containers are defined by objects in the Kubernetes API:

- To set limits on all pods within a given namespace, use the `LimitRange` object. For more information see the [Quotas and Limit Ranges](https://docs.openshift.com/online/pro/dev_guide/compute_resources.html#overview) section of the OpenShift documentation.
- To set limits directly on the pod definition launched by automation controller, see [Customizing the pod specification](/documentation/en-us/red_hat_ansible_automation_platform/2.7/administer-con_controller_container_groups#controller-customize-pod-spec "Ansible Automation Platform provides a simple default pod specification, however, you can provide a custom YAML or JSON document that overrides the default pod specification.") and the [Compute Resources](https://docs.openshift.com/online/pro/dev_guide/compute_resources.html#dev-compute-resources) section of the OpenShift documentation.


Note:

Container groups do not use the capacity algorithm that normal nodes use. You need to set the number of forks at the job template level. If you configure forks in automation controller, that setting is passed along to the container.

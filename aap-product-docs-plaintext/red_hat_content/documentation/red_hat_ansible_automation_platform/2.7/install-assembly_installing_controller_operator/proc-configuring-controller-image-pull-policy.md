# Configure automation controller
## Configure your automation controller image pull policy

Use this procedure to configure the image pull policy on your automation controller.

### About this task

### Procedure

1.  Log in to Red Hat OpenShift Container Platform.
2.  Go to Operators> (and then)Installed Operators.
3.  Select your Ansible Automation Platform Operator deployment.
4.  Select the **Ansible Automation Platform** tab.
5.  Click the ⋮ icon next to your Ansible Automation Platform instance and select **Edit AnsibleAutomationPlatform**.
6.  Click **YAML view** and locate the `spec.controller:` section.

7.  Configure the image pull policy and resource requirements under the `controller:` section:


```
spec:
controller:
image_pull_policy: IfNotPresent  # Options: Always, Never, IfNotPresent
image_pull_secrets:
- pull-secret-name
web_resource_requirements:
limits:
cpu: 1000m
memory: 2Gi
requests:
cpu: 500m
memory: 1Gi
task_resource_requirements:
limits:
cpu: 2000m
memory: 4Gi
requests:
cpu: 1000m
memory: 2Gi
ee_resource_requirements:
limits:
cpu: 500m
memory: 1Gi
requests:
cpu: 250m
memory: 512Mi
redis_resource_requirements:
limits:
cpu: 500m
memory: 1Gi
requests:
cpu: 250m
memory: 512Mi
postgres_resource_requirements:
limits:
cpu: 1000m
memory: 2Gi
requests:
cpu: 500m
memory: 1Gi
postgres_storage_requirements:
limits:
storage: 10Gi
requests:
storage: 8Gi
replicas: 1
garbage_collect_secrets: false
create_preload_data: true
```

8.  Click **Save**.

Note:
These settings apply to the automation controller component managed by this Ansible Automation Platform instance. If you specified an existing controller under `controller.name`, these settings will update that instance.

For more examples of Ansible Automation Platform custom resources, see [Red Hat Ansible Automation Platform custom resources](/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-assembly_appendix_operator_crs#appendix-operator-crs_appendix-operator-crs "This appendix provides a reference for the Ansible Automation Platform custom resources for various deployment scenarios.")


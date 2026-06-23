# Configure automation controller
## Configure automation controller route options

The Red Hat Ansible Automation Platform operator installation form allows you to further configure your automation controller operator route options under **Advanced configuration**.

### About this task

Important:

You must assign a unique metadata.name to each custom resource (CR) in your namespace. If you assign an `AutomationControllerMeshIngress` the same name as your `AnsibleAutomationPlatform` installation, the operator overrides default routes and services. This conflict causes the platform installation to fail.

### Procedure

1.  Log in to Red Hat OpenShift Container Platform.
2.  Navigate to Operators> (and then)Installed Operators.
3.  Select your Ansible Automation Platform Operator deployment.
4.  Select the **Ansible Automation Platform** tab.
5.  Click the ⋮ icon next to your Ansible Automation Platform instance and select **Edit AnsibleAutomationPlatform** .
6.  Click **YAML view** and locate the `spec.controller:` section..
7.  Configure the route options under the `controller:` section:


```
spec:
controller:
ingress_type: Route
route_host: controller.example.com  # Custom hostname for the route
route_tls_termination_mechanism: Edge  # Options: Edge, Passthrough
route_tls_secret: controller-tls-secret  # Optional: TLS credential secret
projects_persistence: false  # Enable/disable persistence for /var/lib/projects
```

8.  Click **Save.**

Note:
Edge termination is recommended for most instances. After configuring your route, you can customize additional route settings by adding them to the `controller:` section in the Ansible Automation Platform custom resource.

For more examples of Ansible Automation Platform custom resources, see [Red Hat Ansible Automation Platform custom resources](/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-assembly_appendix_operator_crs#appendix-operator-crs_appendix-operator-crs "This appendix provides a reference for the Ansible Automation Platform custom resources for various deployment scenarios.") .


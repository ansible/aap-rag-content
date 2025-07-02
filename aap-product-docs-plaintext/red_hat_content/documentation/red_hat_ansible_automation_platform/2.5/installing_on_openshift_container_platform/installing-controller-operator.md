# 3. Configuring Red Hat Ansible Automation Platform components on Red Hat Ansible Automation Platform Operator
## 3.2. Configuring automation controller on Red Hat OpenShift Container Platform web console




You can use these instructions to configure the automation controller operator on Red Hat OpenShift Container Platform, specify custom resources, and deploy Ansible Automation Platform with an external database.

Automation controller configuration can be done through the automation controller extra_settings or directly in the user interface after deployment. However, it is important to note that configurations made in extra_settings take precedence over settings made in the user interface.

Note
When an instance of automation controller is removed, the associated PVCs are not automatically deleted. This can cause issues during migration if the new deployment has the same name as the previous one. Therefore, it is recommended that you manually remove old PVCs before deploying a new automation controller instance in the same namespace. See [Finding and deleting PVCs](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/installing_on_openshift_container_platform/index#proc-find-delete-PVCs_installing-controller-operator) for more information.




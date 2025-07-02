# Chapter 2. Configuring the Red Hat Ansible Automation Platform Operator on Red Hat OpenShift Container Platform




As a namespace administrator, you can use Ansible Automation Platform gateway to manage new Ansible Automation Platform components in your OpenShift environment.

The Ansible Automation Platform gateway uses the Ansible Automation Platform custom resource to manage and integrate the following Ansible Automation Platform components into a unified user interface:

- Automation controller
- Automation hub
- Event-Driven Ansible
- Red Hat Ansible Lightspeed (This feature is disabled by default, you must opt in to use it.)


Before you can deploy the platform gateway you must have Ansible Automation Platform Operator installed in a namespace. If you have not installed Ansible Automation Platform Operator see [Installing the Red Hat Ansible Automation Platform Operator on Red Hat OpenShift Container Platform](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/installing_on_openshift_container_platform/index#install-aap-operator_operator-platform-doc) .

Note
Platform gateway is only available under Ansible Automation Platform Operator version 2.5. Every component deployed under Ansible Automation Platform Operator 2.5 defaults to version 2.5.



If you have the Ansible Automation Platform Operator and some or all of the Ansible Automation Platform components installed see [Deploying the platform gateway with existing Ansible Automation Platform components](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/installing_on_openshift_container_platform/index#operator-deploy-central-config_install-aap-gateway) for how to proceed.


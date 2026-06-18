# Deploy Ansible Automation Platform

As a namespace administrator, you can use Ansible Automation Platform gateway to manage Ansible Automation Platform components in your OpenShift environment.

The Ansible Automation Platform gateway uses the Ansible Automation Platform custom resource to manage and integrate the following Ansible Automation Platform components into a unified user interface:

- Automation controller
- Automation hub
- Event-Driven Ansible
- Red Hat Ansible Lightspeed (This feature is disabled by default, you must opt in to use it.)


Before you can deploy the platform gateway you must have Ansible Automation Platform Operator installed in a namespace. If you have not installed Ansible Automation Platform Operator see **Installing the Red Hat Ansible Automation Platform Operator on Red Hat OpenShift Container Platform**.

If you have the Ansible Automation Platform Operator and some or all of the Ansible Automation Platform components installed see **Deploying the platform gateway with existing Ansible Automation Platform components** for how to proceed.

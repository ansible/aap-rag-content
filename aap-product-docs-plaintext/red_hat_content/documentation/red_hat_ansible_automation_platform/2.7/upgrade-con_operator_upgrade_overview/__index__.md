# Overview

Upgrade Ansible Automation Platform on Red Hat OpenShift Container Platform. You can perform full upgrades from supported previous versions or apply patch updates within your current version.

Important:

Upgrading from version 2.4 or 2.5 is not supported. Upgrade to Red Hat Ansible Automation Platform 2.6 before upgrading to version 2.7.

See the Upgrading Red Hat Ansible Automation Platform Operator in the version 2.6 documentation, for help updating to 2.6.

The Ansible Automation Platform Operator manages deployments, upgrades, backups, and restores of automation controller and automation hub. It also handles deployments of AnsibleJob and JobTemplate resources from the Ansible Automation Platform Resource Operator.

Each operator version has default automation controller and automation hub versions. When the operator is upgraded, it also upgrades the automation controller and automation hub deployments it manages, unless overridden in the spec.

OpenShift deployments of Ansible Automation Platform use the built-in Operator Lifecycle Management (OLM) functionality. For more information, see **Operator Lifecycle Manager concepts and resources**. OpenShift does this by using Subscription, CSV, InstallPlan, and OperatorGroup objects. Most users will not have to interact directly with these resources. They are created when the Ansible Automation Platform Operator is installed from **OperatorHub** and managed through the **Subscriptions** tab in the OpenShift console UI. For more information, refer to **Accessing the web console**.

![Subscription tab in the OpenShift console](/webassets/aem/red_hat_ansible_automation_platform/2.7/images/aap-operator-stable-2.7-deployment.png)

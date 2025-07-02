# 6. Upgrading Red Hat Ansible Automation Platform Operator on Red Hat OpenShift Container Platform
## 6.1. Overview




You can use this document for help with upgrading Ansible Automation Platform 2.4 to 2.5 on Red Hat OpenShift Container Platform. This document applies to upgrades of Ansible Automation Platform 2.5 to later versions of 2.5.

The Ansible Automation Platform Operator manages deployments, upgrades, backups, and restores of automation controller and automation hub. It also handles deployments of AnsibleJob and JobTemplate resources from the Ansible Automation Platform Resource Operator.

Each operator version has default automation controller and automation hub versions. When the operator is upgraded, it also upgrades the automation controller and automation hub deployments it manages, unless overridden in the spec.

OpenShift deployments of Ansible Automation Platform use the built-in Operator Lifecycle Management (OLM) functionality. For more information, see [Operator Lifecycle Manager concepts and resources](https://docs.openshift.com/container-platform/4.16/operators/understanding/olm/olm-understanding-olm.html) . OpenShift does this by using Subscription, CSV, InstallPlan, and OperatorGroup objects. Most users will not have to interact directly with these resources. They are created when the Ansible Automation Platform Operator is installed from **OperatorHub** and managed through the **Subscriptions** tab in the OpenShift console UI. For more information, refer to [Accessing the web console](https://docs.openshift.com/container-platform/4.16/web_console/web-console.html) .

![Subscription tab](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.5-Installing_on_OpenShift_Container_Platform-en-US/images/de823df4e26be639e0aecde38aa62805/Subscription_tab.png)



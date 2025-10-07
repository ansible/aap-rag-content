# 1. Installing Red Hat Ansible Automation Platform Operator on Red Hat OpenShift Container Platform
## 1.1. Planning your Red Hat Ansible Automation Platform Operator on Red Hat OpenShift Container Platform
### 1.1.3. Supported installation scenarios for Red Hat OpenShift Container Platform




You can use the OperatorHub on the Red Hat OpenShift Container Platform web console to install Ansible Automation Platform Operator.

Alternatively, you can install Ansible Automation Platform Operator from the OpenShift Container Platform command-line interface (CLI), `oc` . See [Installing Red Hat Ansible Automation Platform Operator from the OpenShift Container Platform CLI](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html-single/installing_on_openshift_container_platform/index#installing-aap-operator-cli_operator-platform-doc) for help with this.

After you have installed Ansible Automation Platform Operator you must create an **Ansible Automation Platform** custom resource (CR). This enables you to manage Ansible Automation Platform components from a single unified interface known as the platform gateway. In version 2.6, you must create an Ansible Automation Platform CR, even if you have an existing automation controller, automation hub, or Event-Driven Ansible, components.

If existing components have already been deployed, you must specify these components on the Ansible Automation Platform CR. You must create the custom resource in the same namespace as the existing components.

|  **Supported scenarios** |  **Supported scenarios with existing components** |
| --- | --- |
| - Ansible Automation Platform CR for blank slate install with automation controller, automation hub, and Event-Driven Ansible enabled
- Ansible Automation Platform CR with just automation controller enabled
- Ansible Automation Platform CR with just automation controller, automation hub enabled
- Ansible Automation Platform CR with just automation controller, Event-Driven Ansible enabled | - Ansible Automation Platform CR created in the same namespace as an existing automation controller CR with the automation controller name specified on the Ansible Automation Platform CR spec
- Same with automation controller and automation hub
- Same with automation controller, automation hub, and Event-Driven Ansible
- Same with automation controller and Event-Driven Ansible |



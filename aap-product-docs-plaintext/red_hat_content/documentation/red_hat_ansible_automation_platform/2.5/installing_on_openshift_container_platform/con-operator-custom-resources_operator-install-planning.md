# 1. Installing Red Hat Ansible Automation Platform Operator on Red Hat OpenShift Container Platform
## 1.1. Planning your Red Hat Ansible Automation Platform Operator on Red Hat OpenShift Container Platform
### 1.1.4. Custom resources




You can define custom resources for each primary installation workflows.

#### 1.1.4.1. Modifying the number of simultaneous rulebook activations during or after Event-Driven Ansible controller installation




- If you plan to install Event-Driven Ansible on OpenShift Container Platform and modify the number of simultaneous rulebook activations, add the required `    EDA_MAX_RUNNING_ACTIVATIONS` parameter to your custom resources. By default, Event-Driven Ansible controller allows 12 activations per node to run simultaneously. For an example see the [eda-max-running-activations.yml](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/installing_on_openshift_container_platform/index#eda_max_running_activations_yml) in the appendix section.


Note
`EDA_MAX_RUNNING_ACTIVATIONS` for OpenShift Container Platform is a global value since there is no concept of worker nodes when installing Event-Driven Ansible on OpenShift Container Platform.




# 11. Performance tuning for Event-Driven Ansible controller
## 11.1. Characterizing your workload
### 11.1.1. Modifying the number of simultaneous rulebook activations




By default, Event-Driven Ansible controller allows 12 rulebook activations per node. For example, with two worker or hybrid nodes, it results in a limit of 24 activations in total to run simultaneously. If more than 24 rulebook activations are created, the expected behavior is that subsequent rulebook activations wait until there is an available rulebook activation worker. In this case, the rulebook activation status is displayed as **Pending** even if there is enough free memory and CPU on your Event-Driven Ansible controller instance. To change this behavior, you must change the default maximum number of running rulebook activations.

Note
- The value for `    MAX_RUNNING_ACTIVATIONS` does not change when you modify the instance size, so it needs to be adjusted manually.
- If you are installing Event-Driven Ansible on OpenShift Container Platform, the 12 rulebook activations per node is a global value since there is no concept of worker nodes when installing Event-Driven Ansible on OpenShift Container Platform. For more information, see [Modifying the number of simultaneous rulebook activations during or after Event-Driven Ansible controller installation](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/installing_on_openshift_container_platform/operator-install-operator_operator-platform-doc#modifying_the_number_of_simultaneous_rulebook_activations_during_or_after_event_driven_ansible_controller_installation) in [Installing on OpenShift Container Platform](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/installing_on_openshift_container_platform) .




#### 11.1.1.1. Modifying the number of simultaneous rulebook activations during Event-Driven Ansible controller installation




By default, Event-Driven Ansible controller allows 12 rulebook activations per node. For example, with two worker or hybrid nodes, it results in a limit of 24 activations in total to run simultaneously. You can modify this default value during installation by using the following procedure:

**Procedure**

Provide a variable to the VM installer:


1. Navigate to the setup inventory file.
1. Add `    automationedacontroller_max_running_activations` in the [all:vars] section. For example, `    automationedacontroller_max_running_activations=16` .
1. Run the setup.


#### 11.1.1.2. Modifying the number of simultaneous rulebook activations after Event-Driven Ansible controller installation




By default, Event-Driven Ansible controller allows 12 rulebook activations per node. For example, with two worker or hybrid nodes, it results in a limit of 24 activations in total to run simultaneously. You can modify this default value after installation by using the following procedure:

**Procedure**

1. Navigate to the environment file at `    /etc/ansible-automation-platform/eda/settings.yaml` .
1. Choose the number of maximum running activations that you need. For example, `    MAX_RUNNING_ACTIVATIONS = 16`
1. Use the following command to restart Event-Driven Ansible services: `    automation-eda-controller-service restart`


**Additional Resources**

- For more information about rulebook activations, see the [Rulebook activations](https://access.redhat.com/documentation/en-us/red_hat_ansible_automation_platform/2.4/html-single/event-driven_ansible_controller_user_guide/index#eda-rulebook-activations) .
- For more information about modifying simultaneous rulebook activations during or after Event-Driven Ansible on OpenShift Container Platform, see the example in [eda_max_running_activations_yml](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/installing_on_openshift_container_platform/appendix-operator-crs_appendix-operator-crs#eda_max_running_activations_yml) .



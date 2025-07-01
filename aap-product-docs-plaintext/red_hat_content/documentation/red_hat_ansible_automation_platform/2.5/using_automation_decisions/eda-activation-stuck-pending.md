# 8. Rulebook activations troubleshooting
## 8.1. Activation stuck in Pending state




Perform the following steps if your rulebook activation is stuck in **Pending** state.

**Procedure**

1. Confirm whether there are other running activations and if you have reached the limits (for example, memory or CPU limits).


1. If there are other activations running, terminate one or more of them, if possible.
1. If not, check that the default worker, Redis, and activation worker are all running. If all systems are working as expected, check your eda-server internal logs in the worker, scheduler, API, and nginx containers and services to see if the problem can be determined.

Note
These logs reveal the source of the issue, such as an exception thrown by the code, a runtime error with network issues, or an error with the rulebook code. If your internal logs do not provide information that leads to resolution, report the issue to Red Hat support.




1. If you need to make adjustments, see the [Modifying the number of simultaneous rulebook activations](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/using_automation_decisions/eda-performance-tuning#modifying-simultaneous-activations) .

Note
To adjust the maximum number of simultaneous activations for Ansible Automation Platform Operator on OpenShift Container Platform deployments, see [Modifying the number of simultaneous rulebook activations during or after Event-Driven Ansible controller installation](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/installing_on_openshift_container_platform/operator-install-operator_operator-platform-doc#modifying_the_number_of_simultaneous_rulebook_activations_during_or_after_event_driven_ansible_controller_installation) in [Installing on OpenShift Container Platform](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/installing_on_openshift_container_platform) .








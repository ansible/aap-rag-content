# 1. Installing Red Hat Ansible Automation Platform Operator on Red Hat OpenShift Container Platform
## 1.1. Planning your Red Hat Ansible Automation Platform Operator on Red Hat OpenShift Container Platform
### 1.1.5. Ansible Automation Platform Operator CSRF management




In Ansible Automation Platform version 2.6 the Ansible Automation Platform Operator on OpenShift Container Platform creates OpenShift Routes and configures your Cross-site request forgery (CSRF) settings automatically.

When using external ingress, you must configure your CSRF on the ingress, for help with this see [Configuring your CSRF settings for your platform gateway operator ingress](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html-single/installing_on_openshift_container_platform/index#proc-operator-config-csrf-gateway_operator-configure-gateway) .

Important
In previous versions CSRF was configurable through the automation controller user interface, in version 2.6 automation controller settings are still present but have no impact on CSRF settings for the platform gateway.



The following table helps to clarify which settings are applicable for which component.

|  **UI setting** |  **Applicable for** |
| --- | --- |
| Subscription | automation controller |
| platform gateway | platform gateway |
| User Preferences | User interface |
| System | Automation controller |
| Job | Automation controller |
| Logging | Automation controller |
| Troubleshooting | Automation controller |



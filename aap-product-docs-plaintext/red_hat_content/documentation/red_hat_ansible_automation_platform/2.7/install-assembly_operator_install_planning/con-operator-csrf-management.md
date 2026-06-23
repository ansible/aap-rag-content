# Plan your installation of Ansible Automation Platform on Red Hat OpenShift Container Platform
## Ansible Automation Platform Operator CSRF management

In Ansible Automation Platform version 2.7 the Ansible Automation Platform Operator on OpenShift Container Platform creates OpenShift Routes and configures your Cross-site request forgery (CSRF) settings automatically.

When using external ingress, you must configure your CSRF on the ingress.

Important:

In previous versions CSRF was configurable through the automation controller user interface, in version 2.7 automation controller settings are still present but have no impact on CSRF settings for the platform gateway.

The following table helps to clarify which settings are applicable for which component.

| **UI setting**       | **Applicable for**        |
| -------------------- | ------------------------- |
| <br>Subscription     | <br>automation controller |
| <br>platform gateway | <br>platform gateway      |
| <br>User Preferences | <br>User interface        |
| <br>System           | <br>Automation controller |
| <br>Job              | <br>Automation controller |
| <br>Logging          | <br>Automation controller |
| <br>Troubleshooting  | <br>Automation controller |


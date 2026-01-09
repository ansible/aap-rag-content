# 8. Rulebook activations troubleshooting
## 8.7. Cannot connect to the 2.5 automation controller when running activations




You might experience a failed connection to automation controller when you run your activations.

**Procedure**

1. To help resolve the issue, confirm that you have set up a Red Hat Ansible Automation Platform credential and have obtained the correct automation controller URL.


1. If you have not set up a Red Hat Ansible Automation Platform credential, follow the procedures in [Setting up a Red Hat Ansible Automation Platform credential](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/using_automation_decisions/eda-set-up-rhaap-credential-type#eda-set-up-rhaap-credential) . Ensure that this credential has the host set to the following URL format: [https://<your_gateway>/api/controller](https://<your_gateway>/api/controller)
1. When you have completed this process, try setting up your rulebook activation again.




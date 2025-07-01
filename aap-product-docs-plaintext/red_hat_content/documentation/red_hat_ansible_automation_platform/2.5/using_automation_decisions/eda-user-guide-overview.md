# Chapter 1. Event-Driven Ansible controller overview




Event-Driven Ansible is a highly scalable, flexible automation capability that works with event sources such as other software vendors' monitoring tools. These tools monitor IT solutions and identify events and automatically implement the documented changes or response in a rulebook to handle that event.

The following procedures form the user configuration:

-  [Credentials](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/using_automation_decisions/index#eda-credentials)
-  [Credential types](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/using_automation_decisions/index#eda-credential-types)
-  [Projects](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/using_automation_decisions/index#eda-projects)
-  [Decision environments](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/using_automation_decisions/index#eda-decision-environments)
-  [Red Hat Ansible Automation Platform credential](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/using_automation_decisions/index#eda-set-up-rhaap-credential-type)
-  [Rulebook activations](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/using_automation_decisions/index#eda-rulebook-activations)
-  [Rulebook activations troubleshooting](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/using_automation_decisions/index#eda-rulebook-troubleshooting)
-  [Rule audit](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/using_automation_decisions/index#eda-rule-audit)
-  [Simplified event routing](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/using_automation_decisions/index#simplified-event-routing)
-  [Performance tuning for Event-Driven Ansible controller](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/using_automation_decisions/index#eda-performance-tuning)
-  [Event filter plugins](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/using_automation_decisions/index#eda-event-filter-plugins)
-  [Event-Driven Ansible logging strategy](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/using_automation_decisions/index#eda-logging-strategy)


Note
- API documentation for Event-Driven Ansible controller is available at https://<gateway-host>/api/eda/v1/docs
- To meet high availability demands, Event-Driven Ansible controller shares centralized [Redis (REmote DIctionary Server)](https://redis.io/) with the Ansible Automation Platform UI. When Redis is unavailable, you will not be able to create or sync projects, or enable rulebook activations.




**Additional resources**

- For information on how to set user permissions for Event-Driven Ansible controller, see the following in the [Access management and authentication guide](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/access_management_and_authentication/index) :


1.  [Adding roles for a user](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/access_management_and_authentication/gw-managing-access#ref-controller-user-roles)
1.  [Roles](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/access_management_and_authentication/assembly-gw-roles)

- If you plan to use Event-Driven Ansible 2.5 with a 2.4 Ansible Automation Platform, see [Using Event-Driven Ansible 2.5 with Ansible Automation Platform 2.4](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.4/html/using_event-driven_ansible_2.5_with_ansible_automation_platform_2.4/index) .



# Chapter 1. Event-Driven Ansible controller overview




Event-Driven Ansible is a highly scalable, flexible automation capability that works with event sources such as other software vendors' monitoring tools. These tools monitor IT solutions and identify events and automatically implement the documented changes or response in a rulebook to handle that event.

The following procedures form the user configuration:

-  [Credentials](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/using_automation_decisions/eda-credentials)
-  [Credential types](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/using_automation_decisions/eda-credential-types)
-  [Projects](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/using_automation_decisions/eda-projects)
-  [Decision environments](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/using_automation_decisions/eda-decision-environments)
-  [Red Hat Ansible Automation Platform credential](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/using_automation_decisions/eda-set-up-rhaap-credential-type)
-  [Rulebook activations](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/using_automation_decisions/eda-rulebook-activations)
-  [Rulebook activations troubleshooting](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/using_automation_decisions/eda-rulebook-troubleshooting)
-  [Rule audit](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/using_automation_decisions/eda-rule-audit)
-  [Simplified event routing](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/using_automation_decisions/simplified-event-routing)
-  [Performance tuning for Event-Driven Ansible controller](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/using_automation_decisions/eda-performance-tuning)
-  [Event filter plugins](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/using_automation_decisions/eda-event-filter-plugins)
-  [Event-Driven Ansible logging strategy](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/using_automation_decisions/eda-logging-strategy)


Note
- API documentation for Event-Driven Ansible controller is available at https://<gateway-host>/api/eda/v1/docs
- To meet high availability demands, Event-Driven Ansible controller shares centralized [Redis (REmote DIctionary Server)](https://redis.io/) with the Ansible Automation Platform UI. When Redis is unavailable, you will not be able to create or sync projects, or enable rulebook activations.




**Additional resources**

-  [Access management and authentication guide](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/access_management_and_authentication/index) :


-  [Adding roles for a user](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/access_management_and_authentication/gw-managing-access#ref-controller-user-roles)
-  [Roles](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/access_management_and_authentication/assembly-gw-roles)

-  [Using Event-Driven Ansible 2.5 with Ansible Automation Platform 2.4](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.4/html/using_event-driven_ansible_2.5_with_ansible_automation_platform_2.4/index) .



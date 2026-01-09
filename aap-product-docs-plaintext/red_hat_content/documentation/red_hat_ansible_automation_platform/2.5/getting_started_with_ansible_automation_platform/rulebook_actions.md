# 3. Getting started as an automation developer
## 3.4. Define events with rulebooks
### 3.4.1. Rulebook actions




Rulebooks use an "if-this-then-that” logic that tells Event-Driven Ansible what actions to activate when a rule is triggered. Event-Driven Ansible listens to the controller event stream and, when an event triggers a rule, activates an automation action in response.

Rulebooks can trigger the following activations:

-  `    run_job_template`
-  `    run_playbook` (only supported with ansible-rulebook CLI)
-  `    debug`
-  `    print_event`
-  `    set_fact`
-  `    post_event`
-  `    retract_fact`
-  `    shutdown`


To read more about rulebook activations, see [Actions](https://ansible.readthedocs.io/projects/rulebook/en/latest/actions.html) in the Ansible Rulebook documentation. For a complete guide to using Event-Driven Ansible, see [Using automation decisions](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/using_automation_decisions) .


# Chapter 7. Rulebook activations




A rulebook is a set of conditional rules that Event-Driven Ansible uses to perform IT actions in an event-driven automation model. Rulebooks are the means by which users tell Event-Driven Ansible which source to check for an event and when that event occurs what to do when certain conditions are met.

A rulebook specifies actions to be performed when a rule is triggered. A rule gets triggered when the events match the conditions for the rules. The following actions are currently supported:

-  `    run_playbook` (only supported with ansible-rulebook CLI)
-  `    run_module`
-  `    run_job_template`
-  `    run_workflow_template`
-  `    set_fact`
-  `    post_event`
-  `    retract_fact`
-  `    print_event`
-  `    shutdown`
-  `    debug`
-  `    none`


To view further details, see [Actions](https://ansible.readthedocs.io/projects/rulebook/en/latest/actions.html) .

A rulebook activation is a process running in the background defined by a decision environment executing a specific rulebook. You can set up your rulebook activation by following [Setting up a rulebook activation](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/using_automation_decisions/eda-rulebook-activations#eda-set-up-rulebook-activation) .

Warning
Red Hat does not recommend the use of a non-supported source plugin with 1 postgres database. This can pose a potential risk to your use of Ansible Automation Platform.



Important
To meet high availability demands, Event-Driven Ansible controller shares centralized [Redis (REmote DIctionary Server)](https://redis.io/) with the Ansible Automation Platform UI. When Redis is unavailable, the following functions will not be available:

- Creating an activation, if `    is_enabled` is True
- Deleting an activation
- Enabling an activation, if not already enabled
- Disabling an activation, if not already disabled
- Restarting an activation





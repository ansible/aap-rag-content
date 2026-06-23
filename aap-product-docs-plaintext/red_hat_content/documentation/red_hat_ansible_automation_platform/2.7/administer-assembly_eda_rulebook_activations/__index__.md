# Define rules that trigger automation from events

A rulebook is a set of conditional rules that Event-Driven Ansible uses to perform IT actions in an event-driven automation model. Rulebooks are the means that users tell Event-Driven Ansible which source to check for an event and when that event occurs what to do when certain conditions are met.

A rulebook specifies actions to be performed when a rule is triggered. A rule gets triggered when the events match the conditions for the rules. The following actions are currently supported:

- `run_playbook` (only supported with ansible-rulebook CLI)
-  `run_module`
-  `run_job_template`
-  `run_workflow_template`
-  `set_fact`
-  `post_event`
-  `retract_fact`
-  `print_event`
-  `shutdown`
-  `debug`
-  `none`


To view further details, see Ansible Actions.

A rulebook activation is a process running in the background defined by a decision environment executing a specific rulebook. You can set up your rulebook activation by following Set up a rulebook activation.

Warning:

Red Hat does not recommend the use of a non-supported source plugin with 1 postgres database. This can pose a potential risk to your use of Ansible Automation Platform.

Important:

Event-Driven Ansible controller uses PostgreSQL for data storage and background task workers via the `dispatcherd` service. When the workers are unavailable, you will not be able to create or sync projects, or enable rulebook activations.


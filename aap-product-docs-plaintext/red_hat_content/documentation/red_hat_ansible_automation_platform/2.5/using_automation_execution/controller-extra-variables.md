# 6. Job templates
## 6.21. Extra variables




When you pass survey variables, they are passed as extra variables ( `extra_vars` ) within automation controller. However, passing extra variables to a job template (as you would do with a survey) can override other variables being passed from the inventory and project.

By default, `extra_vars` are marked as `!unsafe` unless you specify them on the Job Template’s Extra Variables section. These are trusted, because they can only be added by users with enough privileges to add or edit a Job Template. For example, nested variables do not expand when entered as a prompt, as the Jinja brackets are treated as a string. For more information about unsafe variables, see [Unsafe or raw strings](https://docs.ansible.com/ansible/latest/playbook_guide/playbooks_advanced_syntax.html#unsafe-or-raw-strings) .

Note
`extra_vars` passed to the job launch API are only honored if one of the following is true:

- They correspond to variables in an enabled survey.
-  `    ask_variables_on_launch` is set to **True** .




**Example**

You have a defined variable for an inventory for `debug = true` . It is possible that this variable, `debug = true` , can be overridden in a job template survey.


To ensure the variables that you pass are not overridden, ensure they are included by redefining them in the survey. You can define extra variables at the inventory, group, and host levels.

If you are specifying the `ALLOW_JINJA_IN_EXTRA_VARS` parameter, see the [The ALLOW_JINJA_IN_EXTRA_VARS variable](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/configuring_automation_execution/controller-tips-and-tricks#ref-controller-allow-jinja-in-extra-vars) section of _Configuring automation execution_ to configure it.

The job template extra variables dictionary is merged with the survey variables.

The following are some simplified examples of `extra_vars` in YAML and JSON formats:

- The configuration in YAML format:


```
launch_to_orbit: true
satellites:
- sputnik
- explorer
- satcom
```

- The configuration in JSON format:


```
{
"launch_to_orbit": true,
"satellites": ["sputnik", "explorer", "satcom"]
}
```

The following table notes the behavior (hierarchy) of variable precedence in automation controller as it compares to variable precedence in Ansible.


<span id="idm140390006816320"></span>
**Table 6.1. Automation controller Variable Precedence Hierarchy (last listed wins)**

| Ansible | automation controller |
| --- | --- |
| role defaults | role defaults |
| dynamic inventory variables | dynamic inventory variables |
| inventory variables | automation controller inventory variables |
| inventory `group_vars` | automation controller group variables |
| inventory `host_vars` | automation controller host variables |
| playbook `group_vars` | playbook `group_vars` |
| playbook `host_vars` | playbook `host_vars` |
| host facts | host facts |
| registered variables | registered variables |
| set facts | set facts |
| play variables | play variables |
| play `vars_prompt` | (not supported) |
| play `vars_files` | play `vars_files` |
| role and include variables | role and include variables |
| block variables | block variables |
| task variables | task variables |
| extra variables | Job Template extra variables |
|  | Job Template Survey (defaults) |
|  | Job Launch extra variables |





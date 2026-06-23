# Set extra variables in job templates
## Extra variables

You can pass extra variables to a automation controller job template in several ways, including through surveys and the API.

When you pass survey variables, they are passed as extra variables (`extra_vars`) within automation controller. However, passing extra variables to a job template (as you would do with a survey) can override other variables being passed from the inventory and project.

By default, `extra_vars` are marked as `!unsafe` unless you specify them on the Job Template’s Extra Variables section. These are trusted, because they can only be added by users with enough privileges to add or edit a Job Template. For example, nested variables do not expand when entered as a prompt, as the Jinja brackets are treated as a string.

Note:

`extra_vars` passed to the job launch API are only honored if one of the following is true:

- They correspond to variables in an enabled survey.
- `ask_variables_on_launch` is set to **True**.

**Example** You have a defined variable for an inventory for `debug = true`. It is possible that this variable, `debug = true`, can be overridden in a job template survey.

To ensure the variables that you pass are not overridden, ensure they are included by redefining them in the survey. You can define extra variables at the inventory, group, and host levels.

If you are specifying the `ALLOW_JINJA_IN_EXTRA_VARS` parameter, which controls whether Jinja templating is allowed in extra variables for job templates in automation controller, you can configure the parameter in the UI Jobs Settings.

-
- Only on Template Definitions (default); Never (recommended); Always (strongly discouraged)
Setting The job template extra variables dictionary is merged with the survey variables.

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

**Automation controller Variable Precedence Hierarchy (last listed wins)**

| Ansible                         | automation controller                         |
| ------------------------------- | --------------------------------------------- |
| <br>role defaults               | <br>role defaults                             |
| <br>dynamic inventory variables | <br>dynamic inventory variables               |
| <br>inventory variables         | <br>automation controller inventory variables |
| <br>inventory `group_vars`      | <br>automation controller group variables     |
| <br>inventory `host_vars`       | <br>automation controller host variables      |
| <br>playbook `group_vars`       | <br>playbook `group_vars`                     |
| <br>playbook `host_vars`        | <br>playbook `host_vars`                      |
| <br>host facts                  | <br>host facts                                |
| <br>registered variables        | <br>registered variables                      |
| <br>set facts                   | <br>set facts                                 |
| <br>play variables              | <br>play variables                            |
| <br>play `vars_prompt`          | <br>(not supported)                           |
| <br>play `vars_files`           | <br>play `vars_files`                         |
| <br>role and include variables  | <br>role and include variables                |
| <br>block variables             | <br>block variables                           |
| <br>task variables              | <br>task variables                            |
| <br>extra variables             | <br>Job Template extra variables              |
|                                 | <br>Job Template Survey (defaults)            |
|                                 | <br>Job Launch extra variables                |

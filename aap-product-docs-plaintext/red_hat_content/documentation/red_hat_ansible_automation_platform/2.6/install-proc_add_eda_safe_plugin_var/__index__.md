# Add a safe plugin variable to Event-Driven Ansible controller

When using the `redhat.insights_eda` plugin for rulebook activations, add a safe plugin variable to a platform directory to ensure a secure connection and correct port mapping displays.

## Procedure

1.  Create a directory for the safe plugin variable: `mkdir -p ./group_vars/automationedacontroller`
2.  Create a file within that directory for your new setting (for example, `touch ./group_vars/automationedacontroller/custom.yml`)
3.  Add the variable `automationedacontroller_additional_settings` to extend the default `settings.yaml` template for Event-Driven Ansible controller and add the `SAFE_PLUGINS` field with a list of plugins to enable. For example:


```
automationedacontroller_additional_settings:
SAFE_PLUGINS:
- ansible.eda.webhook
- ansible.eda.alertmanager
```
Note:
You can also extend the `automationedacontroller_additional_settings` variable beyond `SAFE_PLUGINS` in the Django configuration file `/etc/ansible-automation-platform/eda/settings.yaml`.

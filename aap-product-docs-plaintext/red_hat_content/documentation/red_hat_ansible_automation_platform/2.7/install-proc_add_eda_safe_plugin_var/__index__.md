# Add a safe plugin variable to Event-Driven Ansible controller

When using the `redhat.insights_eda` plugin for rulebook activations, add a safe plugin variable to a platform directory to ensure a secure connection and correct port mapping displays.

## Procedure

1.  Create a directory for the safe plugin variable:


```
mkdir -p ./group_vars/automationeda
```

2.  Create a file within that directory for your new setting (for example, `touch ./group_vars/automationeda/custom.yml`)
3.  Add the variable `eda_safe_plugins` with a list of plugins to enable. For example:


```
eda_safe_plugins: ['ansible.eda.webhook', 'ansible.eda.alertmanager']
```

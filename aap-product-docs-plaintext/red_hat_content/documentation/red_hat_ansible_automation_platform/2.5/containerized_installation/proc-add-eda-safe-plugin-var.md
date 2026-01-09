# 5. Advanced containerized deployment
## 5.1. Adding a safe plugin variable to Event-Driven Ansible controller




When using `redhat.insights_eda` or similar plugins to run rulebook activations in Event-Driven Ansible controller, you must add a safe plugin variable to a directory in Ansible Automation Platform. This ensures connection between Event-Driven Ansible controller and the source plugin, and displays port mappings correctly.

**Procedure**

1. Create a directory for the safe plugin variable:


```
mkdir -p ./group_vars/automationeda
```


1. Create a file within that directory for your new setting (for example, `    touch ./group_vars/automationeda/custom.yml` )
1. Add the variable `    eda_safe_plugins` with a list of plugins to enable. For example:


```
eda_safe_plugins: ['ansible.eda.webhook', 'ansible.eda.alertmanager']
```





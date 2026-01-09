# 14. Appendix: Red Hat Ansible Automation Platform custom resources
## 14.1. Custom resources
### 14.1.5. aap-existing-hub-controller-eda.yml




```
---
apiVersion: aap.ansible.com/v1alpha1
kind: AnsibleAutomationPlatform
metadata:
name: myaap
spec:
# Development purposes only
no_log: false

controller:
name: existing-controller # &lt;-- this is the name of the existing AutomationController CR
disabled: false

eda:
name: existing-eda
disabled: false

hub:
name: existing-hub
disabled: false

# End state:
# * Controller: existing-controller registered with Ansible Automation Platform UI
# * * Event-Driven Ansible: existing-eda registered with Ansible Automation Platform UI
# * * Automation hub: existing-hub registered with Ansible Automation Platform UI
#
# Note: The automation controller, Event-Driven Ansible, and automation hub names must match the names of the existing.
# Automation controller, Event-Driven Ansible, and automation hub CRs in the same namespace as the Ansible Automation Platform CR. If the names do not match, the Ansible Automation Platform CR will not be able to register the existing automation controller, Event-Driven Ansible, and automation hub with the Ansible Automation Platform UI,and will instead deploy new automation controller, Event-Driven Ansible, and automation hub instances.
```


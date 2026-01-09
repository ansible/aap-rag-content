# 14. Appendix: Red Hat Ansible Automation Platform custom resources
## 14.1. Custom resources
### 14.1.4. aap-existing-hub-and-controller.yml




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
name: existing-controller
disabled: false

eda:
disabled: true

hub:
name: existing-hub
disabled: false

# End state:
# * Automation controller: existing-controller registered with Ansible Automation Platform UI
# * * Event-Driven Ansible deployed and named: myaap-eda
# * * Automation hub: existing-hub registered with Ansible Automation Platform UI
```


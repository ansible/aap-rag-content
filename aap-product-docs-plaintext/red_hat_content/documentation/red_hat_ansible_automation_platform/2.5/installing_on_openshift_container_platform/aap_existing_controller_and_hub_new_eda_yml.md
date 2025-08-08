# 11. Appendix: Red Hat Ansible Automation Platform custom resources
## 11.1. Custom resources
### 11.1.1. aap-existing-controller-and-hub-new-eda.yml




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
disabled: false

hub:
name: existing-hub
disabled: false
```


# 10. Appendix: Red Hat Ansible Automation Platform custom resources
## 10.1. Custom resources
### 10.1.18. gateway-only.yml




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
disabled: true

eda:
disabled: true

hub:
disabled: true

lightspeed:
disabled: true

# End state:
# * Platform gateway deployed and named: myaap-gateway
#   * UI is reachable at: https://myaap-gateway-gateway.apps.ocp4.example.com
# * Automation controller is not deployed
# * * Event-Driven Ansible is not deployed
# * * Automation hub is not deployed
# * Red Hat Ansible Lightspeed is not deployed
```


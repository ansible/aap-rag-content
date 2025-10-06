# 13. Appendix: Red Hat Ansible Automation Platform custom resources
## 13.1. Custom resources
### 13.1.18. eda-max-running-activations.yml




```
---
apiVersion: aap.ansible.com/v1alpha1
kind: AnsibleAutomationPlatform
metadata:
name: myaap
spec:
eda:
extra_settings:
- setting: EDA_MAX_RUNNING_ACTIVATIONS
value: "15" # Setting this value to "-1" means there will be no limit
```


<span id="idm139902298668736"></span>

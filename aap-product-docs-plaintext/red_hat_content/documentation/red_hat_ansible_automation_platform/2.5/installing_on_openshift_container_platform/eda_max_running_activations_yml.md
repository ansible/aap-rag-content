# 10. Appendix: Red Hat Ansible Automation Platform custom resources
## 10.1. Custom resources
### 10.1.19. eda-max-running-activations.yml




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


<span id="idm140127317995808"></span>

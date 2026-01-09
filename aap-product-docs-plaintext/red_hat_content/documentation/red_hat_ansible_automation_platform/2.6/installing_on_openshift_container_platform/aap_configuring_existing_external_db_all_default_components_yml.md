# 15. Appendix: Red Hat Ansible Automation Platform custom resources
## 15.1. Custom resources
### 15.1.10. aap-configuring-existing-external-db-all-default-components.yml




```
---
apiVersion: aap.ansible.com/v1alpha1
kind: AnsibleAutomationPlatform
metadata:
name: myaap
spec:
database:
database_secret: external-postgres-configuration-gateway
```

Note
The system uses the external database for platform gateway, and automation controller, automation hub, and Event-Driven Ansible continues to use the existing databases that were used in 2.4.




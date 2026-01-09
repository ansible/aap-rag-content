# 15. Appendix: Red Hat Ansible Automation Platform custom resources
## 15.1. Custom resources
### 15.1.9. aap-configuring-external-db-all-default-components.yml




```
---
apiVersion: aap.ansible.com/v1alpha1
kind: AnsibleAutomationPlatform
metadata:
name: myaap
spec:
database:
database_secret: external-postgres-configuration-gateway
controller:
postgres_configuration_secret: external-postgres-configuration-controller
hub:
postgres_configuration_secret: external-postgres-configuration-hub
eda:
database:
database_secret: external-postgres-configuration-eda
```


# 5. Migrating Red Hat Ansible Automation Platform to Red Hat Ansible Automation Platform Operator
## 5.3. Migrating data to the Ansible Automation Platform Operator
### 5.3.1. Creating an Ansible Automation Platform object




Use the following steps to create an **AnsibleAutomationPlatform** custom resource object.

**Procedure**

1. Log in to **Red Hat OpenShift Container Platform** .
1. Navigate toOperators→Installed Operators.
1. Select the Ansible Automation Platform Operator installed on your project namespace.
1. Select the **Ansible Automation Platform** tab.
1. ClickCreate AnsibleAutomationPlatform.
1. Select **YAML view** and paste in the following, modified accordingly:


```
---    apiVersion: aap.ansible.com/v1alpha1    kind: AnsibleAutomationPlatform    metadata:      name: myaap    spec:      postgres_configuration_secret: external-postgres-configuration          controller:        disabled: false        postgres_configuration_secret: external-controller-postgres-configuration        secret_key_secret: controller-secret-key          hub:        disabled: false        postgres_configuration_secret: external-hub-postgres-configuration        db_fields_encryption_secret: hub-db-fields-encryption-secret
```


1. ClickCreate.



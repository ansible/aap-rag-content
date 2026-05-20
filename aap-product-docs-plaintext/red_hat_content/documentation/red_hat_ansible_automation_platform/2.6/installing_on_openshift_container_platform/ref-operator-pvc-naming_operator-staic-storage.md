# 5. Configuring Red Hat Ansible Automation Platform components on Red Hat Ansible Automation Platform Operator
## 5.4. Configure static storage for Ansible Automation Platform
### 5.4.3. PVC naming conventions for Ansible Automation Platform components

The Operator must find PVCs with exact names to adopt them for static provisioning. Replace `<instance_name>` with the name of your `AnsibleAutomationPlatform` custom resource.

| Component | Required PVC Name | Default Access Mode |
| --- | --- | --- |
| <br>  Ansible Automation Platform Database | <br> `postgres-15-<aap_cr_name>-postgres-15-0` | <br>  ReadWriteOnce |
| <br>  Automation Hub Storage | <br> `<instance_name>-hub-file-storage`<br>  (Required when storage_type is set to file) | <br>  ReadWriteMany |
| <br>  Automation Hub Redis Persistence | <br> `<instance_name>-hub-redis-data` | <br>  ReadWriteOnce |


# Configure static storage for Ansible Automation Platform
## PVC naming conventions for Ansible Automation Platform components

The Operator must find PVCs with exact names to adopt them for static provisioning. Replace `<instance_name>` with the name of your `AnsibleAutomationPlatform` custom resource.

| Component                            | Required PVC name                                                                         | Default access mode |
| ------------------------------------ | ----------------------------------------------------------------------------------------- | ------------------- |
| Ansible Automation Platform database | `postgres-15-<aap_cr_name>-postgres-15-0`                                                 | ReadWriteOnce       |
| Automation hub storage               | <br>`<instance_name>-hub-file-storage`<br>(Required when `storage_type` is set to `file`) | ReadWriteMany       |
| Automation Hub Redis persistence     | `<instance_name>-hub-redis-data`                                                          | ReadWriteOnce       |

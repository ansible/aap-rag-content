# 5. Configuring Red Hat Ansible Automation Platform components on Red Hat Ansible Automation Platform Operator
## 5.4. Configure static storage for Ansible Automation Platform
### 5.4.3. PVC naming conventions for Ansible Automation Platform components




The Operator must find PVCs with exact names to adopt them for static provisioning. Replace `&lt;instance_name&gt;` with the name of your `AnsibleAutomationPlatform` custom resource.

| Component | Required PVC Name | Default Access Mode |
| --- | --- | --- |
| Ansible Automation Platform Database |  `postgres-15-<span class="emphasis"><em><span class="Role ARG Spec Role ARG Spec">&lt;aap_cr_name&gt;</span></em></span>-postgres-15-0` | ReadWriteOnce |
| Automation Hub Storage |  `<span class="emphasis"><em><span class="Role ARG Spec Role ARG Spec">&lt;instance_name&gt;</span></em></span>-hub-file-storage`

(Required when storage_type is set to file) | ReadWriteMany |
| Automation Hub Redis Persistence |  `<span class="emphasis"><em><span class="Role ARG Spec Role ARG Spec">&lt;instance_name&gt;</span></em></span>-hub-redis-data` | ReadWriteOnce |



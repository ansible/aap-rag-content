# 4. Configuring Red Hat Ansible Automation Platform components on Red Hat Ansible Automation Platform Operator
## 4.3. Configuring automation hub on Red Hat OpenShift Container Platform web console
### 4.3.5. Additional configurations




A collection download count can help you understand collection usage. To add a collection download count to automation hub, set the following configuration:

```
spec:
pulp_settings:
ansible_collect_download_count: true
```

When `ansible_collect_download_count` is enabled, automation hub will display a download count by the collection.


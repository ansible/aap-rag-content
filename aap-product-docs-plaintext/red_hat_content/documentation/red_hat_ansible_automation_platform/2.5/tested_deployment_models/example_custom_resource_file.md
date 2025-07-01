# 4. Operator topologies
## 4.1. Operator growth topology
### 4.1.3. Example custom resource file




Use the following example custom resource (CR) to add your Ansible Automation Platform instance to your project:

```
apiVersion: aap.ansible.com/v1alpha1
kind: AnsibleAutomationPlatform
metadata:
name: &lt;aap instance name&gt;
spec:
eda:
automation_server_ssl_verify: 'no'
hub:
storage_type: 's3'
object_storage_s3_secret: '&lt;name of the Secret resource holding s3 configuration&gt;'
```


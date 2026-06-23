# AnsibleAutomationPlatform [aap.ansible.com/v1alpha1]
## Example custom resource

The following example shows a basic `AnsibleAutomationPlatform` custom resource with an external database, S3 storage for automation hub, and Event-Driven Ansible SSL verification disabled:

```
apiVersion: aap.ansible.com/v1alpha1
kind: AnsibleAutomationPlatform
metadata:
name: aap
spec:
database:
database_secret: postgres-config-gateway
eda:
automation_server_ssl_verify: 'no'
hub:
storage_type: 's3'
object_storage_s3_secret: 'example-galaxy-object-storage'
```

# Operator growth topology
## Example custom resource file

Use this example custom resource (CR) to add your Ansible Automation Platform instance to your project:

```
apiVersion: aap.ansible.com/v1alpha1
kind: AnsibleAutomationPlatform
metadata:
name: <aap instance name>
spec:
eda:
automation_server_ssl_verify: 'no'
hub:
storage_type: 's3'
object_storage_s3_secret: '<name of the Secret resource holding s3 configuration>'
metrics:
disabled: false
```


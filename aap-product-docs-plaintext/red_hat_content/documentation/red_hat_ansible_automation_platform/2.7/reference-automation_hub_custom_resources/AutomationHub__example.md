# Automation hub custom resources
## AutomationHub [automationhub.ansible.com/v1beta1]
### Example custom resource

```
apiVersion: automationhub.ansible.com/v1beta1
kind: AutomationHub
metadata:
name: my-hub
spec:
storage_type: S3
object_storage_s3_secret: my-s3-secret
pulp_settings:
MAX_PAGE_SIZE: 501
cache_enabled: true
api:
replicas: 2
content:
replicas: 2
```


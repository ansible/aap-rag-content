# 15. Appendix: Red Hat Ansible Automation Platform custom resources
## 15.1. Custom resources
### 15.1.15. aap-fresh-only-hub.yml




```
---
apiVersion: aap.ansible.com/v1alpha1
kind: AnsibleAutomationPlatform
metadata:
name: myaap
spec:
# Development purposes only
no_log: false

controller:
disabled: true

eda:
disabled: true

hub:
disabled: false
## uncomment if using file storage for Content pod
storage_type: file
file_storage_storage_class: nfs-local-rwx
file_storage_size: 10Gi

# # AaaS Hub Settings
# pulp_settings:
#   cache_enabled: false

## uncomment if using S3 storage for Content pod
# storage_type: S3
# object_storage_s3_secret: example-galaxy-object-storage

## uncomment if using Azure storage for Content pod
# storage_type: azure
# object_storage_azure_secret: azure-secret-name

lightspeed:
disabled: false

# End state:
# * Automation controller disabled
# * * Event-Driven Ansible disabled
# * * Automation hub deployed and named: myaap-hub
# * Red Hat Ansible Lightspeed disabled
```


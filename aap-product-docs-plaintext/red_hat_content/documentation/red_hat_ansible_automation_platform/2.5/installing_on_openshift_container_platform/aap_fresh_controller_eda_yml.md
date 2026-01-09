# 14. Appendix: Red Hat Ansible Automation Platform custom resources
## 14.1. Custom resources
### 14.1.7. aap-fresh-controller-eda.yml




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
disabled: false

eda:
disabled: false

hub:
disabled: true
## uncomment if using file storage for Content pod
storage_type: file
file_storage_storage_class: nfs-local-rwx
file_storage_size: 10Gi

## uncomment if using S3 storage for Content pod
# storage_type: S3
# object_storage_s3_secret: example-galaxy-object-storage

## uncomment if using Azure storage for Content pod
# storage_type: azure
# object_storage_azure_secret: azure-secret-name

# End state:
# * Automation controller deployed and named: myaap-controller
# * * Event-Driven Ansible deployed and named: myaap-eda
# * * Automation hub disabled
# * Red Hat Ansible Lightspeed disabled
```


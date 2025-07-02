# 10. Appendix: Red Hat Ansible Automation Platform custom resources
## 10.1. Custom resources
### 10.1.13. aap-fresh-install-with-settings.yml




```
---
apiVersion: aap.ansible.com/v1alpha1
kind: AnsibleAutomationPlatform
metadata:
name: myaap
spec:
# Development purposes only
no_log: false
image_pull_policy: Always

# Platform
## uncomment to test bundle certs
# bundle_cacert_secret: gateway-custom-certs

# Components
controller:
disabled: false
image_pull_policy: Always

extra_settings:
- setting: MAX_PAGE_SIZE
value: '501'

eda:
disabled: false
image_pull_policy: Always

extra_settings:
- setting: EDA_MAX_PAGE_SIZE
value: '501'

hub:
disabled: false
image_pull_policy: Always

## uncomment if using file storage for Content pod
storage_type: file
file_storage_storage_class: rook-cephfs
file_storage_size: 10Gi

## uncomment if using S3 storage for Content pod
# storage_type: S3
# object_storage_s3_secret: example-galaxy-object-storage

## uncomment if using Azure storage for Content pod
# storage_type: azure
# object_storage_azure_secret: azure-secret-name

pulp_settings:
MAX_PAGE_SIZE: 501
cache_enabled: false

# lightspeed:
#   disabled: true

# End state:
# * Automation controller deployed and named: myaap-controller
# * * Event-Driven Ansible deployed and named: myaap-eda
# * * Automation hub deployed and named: myaap-hub
```


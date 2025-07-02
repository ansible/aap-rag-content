# 10. Appendix: Red Hat Ansible Automation Platform custom resources
## 10.1. Custom resources
### 10.1.12. aap-fresh-install-local-management.yml




```
---
apiVersion: aap.ansible.com/v1alpha1
kind: AnsibleAutomationPlatform
metadata:
name: myaap
spec:
# Development purposes only
no_log: false

# Platform
## uncomment to test bundle certs
# bundle_cacert_secret: gateway-custom-certs

# Components
controller:
disabled: false
extra_settings:
- setting: ALLOW_LOCAL_RESOURCE_MANAGEMENT
value: 'True'

eda:
disabled: false

extra_settings:
- setting: EDA_ALLOW_LOCAL_RESOURCE_MANAGEMENT
value: '@bool True'

hub:
disabled: false
## uncomment if using file storage for Content pod
storage_type: file
file_storage_storage_class: nfs-local-rwx
file_storage_size: 10Gi


pulp_settings:
ALLOW_LOCAL_RESOURCE_MANAGEMENT: True

# cache_enabled: false
# redirect_to_object_storage: "False"
# analytics: false
# galaxy_collection_signing_service: ""
# galaxy_container_signing_service: ""
# token_auth_disabled: 'False'
# token_signature_algorithm: 'ES256'

## uncomment if using S3 storage for Content pod
# storage_type: S3
# object_storage_s3_secret: example-galaxy-object-storage

## uncomment if using Azure storage for Content pod
# storage_type: azure
# object_storage_azure_secret: azure-secret-name

# Development purposes only
no_log: false

# lightspeed:
#   disabled: true

# End state:
# * Automation controller deployed and named: myaap-controller
# * * Event-Driven Ansible deployed and named: myaap-eda
# * * Automation hub deployed and named: myaap-hub
```


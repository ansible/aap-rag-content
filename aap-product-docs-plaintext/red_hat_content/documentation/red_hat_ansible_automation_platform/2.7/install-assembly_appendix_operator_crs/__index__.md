# Red Hat Ansible Automation Platform custom resources

This appendix provides a reference for the Ansible Automation Platform custom resources for various deployment scenarios.

Tip:

You can link in existing components by specifying the component name under the `name` variable. You can also use `name` to create a custom name for a new component.

## Custom resources

Refer to the following custom resources you can use for various Ansible Automation Platform deployment scenarios.

### aap-existing-controller-and-hub-new-eda.yml

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
name: existing-controller
disabled: false

eda:
disabled: false

hub:
name: existing-hub
disabled: false
```

### aap-all-defaults.yml

```
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

hub:
disabled: false
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

# lightspeed:
#   disabled: true

# End state:
# * Automation controller deployed and named: myaap-controller
# * * Event-Driven Ansible deployed and named: myaap-eda
# * * Automation hub deployed and named: myaap-hub
```

### aap-existing-controller-only.yml

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
name: existing-controller

eda:
disabled: true

hub:
disabled: true
## uncomment if using file storage for Content pod
# storage_type: file
# file_storage_storage_class: nfs-local-rwx
# file_storage_size: 10Gi

## uncomment if using S3 storage for Content pod
# storage_type: S3
# object_storage_s3_secret: example-galaxy-object-storage

## uncomment if using Azure storage for Content pod
# storage_type: azure
# object_storage_azure_secret: azure-secret-name


# End state:
# * Automation controller: existing-controller registered with Ansible Automation Platform UI
# * * Event-Driven Ansible deployed and named: myaap-eda
# * * Automation hub deployed and named: myaap-hub
```

### aap-existing-hub-and-controller.yml

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
name: existing-controller
disabled: false

eda:
disabled: true

hub:
name: existing-hub
disabled: false

# End state:
# * Automation controller: existing-controller registered with Ansible Automation Platform UI
# * * Event-Driven Ansible deployed and named: myaap-eda
# * * Automation hub: existing-hub registered with Ansible Automation Platform UI
```

### aap-existing-hub-controller-eda.yml

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
name: existing-controller # <-- this is the name of the existing AutomationController CR
disabled: false

eda:
name: existing-eda
disabled: false

hub:
name: existing-hub
disabled: false

# End state:
# * Controller: existing-controller registered with Ansible Automation Platform UI
# * * Event-Driven Ansible: existing-eda registered with Ansible Automation Platform UI
# * * Automation hub: existing-hub registered with Ansible Automation Platform UI
#
# Note: The automation controller, Event-Driven Ansible, and automation hub names must match the names of the existing.
# Automation controller, Event-Driven Ansible, and automation hub CRs in the same namespace as the Ansible Automation Platform CR. If the names do not match, the Ansible Automation Platform CR will not be able to register the existing automation controller, Event-Driven Ansible, and automation hub with the Ansible Automation Platform UI,and will instead deploy new automation controller, Event-Driven Ansible, and automation hub instances.
```

### aap-existing-hub-controller-eda.yml

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
name: existing-controller # <-- this is the name of the existing AutomationController CR
disabled: false

eda:
name: existing-eda
disabled: false

hub:
name: existing-hub
disabled: false

# End state:
# * Automation controller: existing-controller registered with Ansible Automation Platform UI
# * * Event-Driven Ansible: existing-eda registered with Ansible Automation Platform UI
# * * Automation hub: existing-hub registered with Ansible Automation Platform UI
#
# Note: The automation controller, Event-Driven Ansible, and automation hub names must match the names of the existing.
# Automation controller, Event-Driven Ansible, and automation hub CRs in the same namespace as the Ansible Automation Platform CR. If the names do not match, the Ansible Automation Platform CR will not be able to register the existing automation controller, Event-Driven Ansible, and automation hub with the Ansible Automation Platform UI,and will instead deploy new automation controller, Event-Driven Ansible, and automation hub instances.
```

### aap-fresh-controller-eda.yml

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

### aap-fresh-external-db.yml

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
disabled: false
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
# * * Automation hub deployed and named: myaap-hub
```

### aap-configuring-external-db-all-default-components.yml

```
---
apiVersion: aap.ansible.com/v1alpha1
kind: AnsibleAutomationPlatform
metadata:
name: myaap
spec:
database:
database_secret: external-postgres-configuration-gateway
controller:
postgres_configuration_secret: external-postgres-configuration-controller
hub:
postgres_configuration_secret: external-postgres-configuration-hub
eda:
database:
database_secret: external-postgres-configuration-eda
```

### aap-configuring-existing-external-db-all-default-components.yml

```
---
apiVersion: aap.ansible.com/v1alpha1
kind: AnsibleAutomationPlatform
metadata:
name: myaap
spec:
database:
database_secret: external-postgres-configuration-gateway
```


Note:

The system uses the external database for platform gateway, and automation controller, automation hub, and Event-Driven Ansible continues to use the existing databases that were used in 2.4.

### aap-configuring-external-db-with-lightspeed-enabled.yml

```
---
apiVersion: aap.ansible.com/v1alpha1
kind: AnsibleAutomationPlatform
metadata:
name: myaap
spec:
database:
database_secret: external-postgres-configuration-gateway
controller:
postgres_configuration_secret: external-postgres-configuration-controller
hub:
postgres_configuration_secret: external-postgres-configuration-hub
eda:
database:
database_secret: external-postgres-configuration-eda
lightspeed:
disabled: false
database:
database_secret: <secret-name>-postgres-configuration
auth_config_secret_name: 'auth-configuration-secret'
model_config_secret_name: 'model-configuration-secret'
```


Note:

You can follow the [Red Hat Ansible Lightspeed with IBM watsonx Code Assistant User Guide](https://docs.redhat.com/en/documentation/red_hat_ansible_lightspeed_with_ibm_watsonx_code_assistant/2.x_latest/html/red_hat_ansible_lightspeed_with_ibm_watsonx_code_assistant_user_guide/index) for help with creating the model and auth secrets.

### aap-fresh-install-with-settings.yml

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

### aap-fresh-install.yml

```
---
apiVersion: aap.ansible.com/v1alpha1
kind: AnsibleAutomationPlatform
metadata:
name: myaap
spec:
# Development purposes only
no_log: false

# Redis Mode
# redis_mode: cluster

# Platform
## uncomment to test bundle certs
# bundle_cacert_secret: gateway-custom-certs
# extra_settings:
#   - setting: MAX_PAGE_SIZE
#     value: '501'

# Components
controller:
disabled: false

eda:
disabled: false

hub:
disabled: false
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

# lightspeed:
#   disabled: true

# End state:
# * Automation controller deployed and named: myaap-controller
# * * Event-Driven Ansible deployed and named: myaap-eda
# * * Automation hub deployed and named: myaap-hub
```

### aap-fresh-only-controller.yml

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
disabled: true

hub:
disabled: true
## uncomment if using file storage for Content pod
# storage_type: file
# file_storage_storage_class: nfs-local-rwx
# file_storage_size: 10Gi

## uncomment if using S3 storage for Content pod
# storage_type: S3
# object_storage_s3_secret: example-galaxy-object-storage

## uncomment if using Azure storage for Content pod
# storage_type: azure
# object_storage_azure_secret: azure-secret-name


# End state:
# * Automation controller: existing-controller registered with Ansible Automation Platform UI
# * * Event-Driven Ansible deployed and named: myaap-eda
# * * Automation hub deployed and named: myaap-hub
```

### aap-fresh-only-hub.yml

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

### aap-lightspeed-enabled.yml

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
disabled: false
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

lightspeed:
disabled: false

# End state:
# * Automation controller deployed and named: myaap-controller
# * * Event-Driven Ansible deployed and named: myaap-eda
# * * Automation hub deployed and named: myaap-hub
# * Red Hat Ansible Lightspeed deployed and named: myaap-lightspeed
```

### gateway-only.yml

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
disabled: true

lightspeed:
disabled: true

# End state:
# * Platform gateway deployed and named: myaap-gateway
#   * UI is reachable at: https://myaap-gateway-gateway.apps.ocp4.example.com
# * Automation controller is not deployed
# * * Event-Driven Ansible is not deployed
# * * Automation hub is not deployed
# * Red Hat Ansible Lightspeed is not deployed
```

## Custom resources

Refer to the following custom resources you can use for various Ansible Automation Platform deployment scenarios.

### aap-existing-controller-and-hub-new-eda.yml

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
name: existing-controller
disabled: false

eda:
disabled: false

hub:
name: existing-hub
disabled: false
```

### aap-all-defaults.yml

```
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

hub:
disabled: false
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

# lightspeed:
#   disabled: true

# End state:
# * Automation controller deployed and named: myaap-controller
# * * Event-Driven Ansible deployed and named: myaap-eda
# * * Automation hub deployed and named: myaap-hub
```

### aap-existing-controller-only.yml

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
name: existing-controller

eda:
disabled: true

hub:
disabled: true
## uncomment if using file storage for Content pod
# storage_type: file
# file_storage_storage_class: nfs-local-rwx
# file_storage_size: 10Gi

## uncomment if using S3 storage for Content pod
# storage_type: S3
# object_storage_s3_secret: example-galaxy-object-storage

## uncomment if using Azure storage for Content pod
# storage_type: azure
# object_storage_azure_secret: azure-secret-name


# End state:
# * Automation controller: existing-controller registered with Ansible Automation Platform UI
# * * Event-Driven Ansible deployed and named: myaap-eda
# * * Automation hub deployed and named: myaap-hub
```

### aap-existing-hub-and-controller.yml

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
name: existing-controller
disabled: false

eda:
disabled: true

hub:
name: existing-hub
disabled: false

# End state:
# * Automation controller: existing-controller registered with Ansible Automation Platform UI
# * * Event-Driven Ansible deployed and named: myaap-eda
# * * Automation hub: existing-hub registered with Ansible Automation Platform UI
```

### aap-existing-hub-controller-eda.yml

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
name: existing-controller # <-- this is the name of the existing AutomationController CR
disabled: false

eda:
name: existing-eda
disabled: false

hub:
name: existing-hub
disabled: false

# End state:
# * Controller: existing-controller registered with Ansible Automation Platform UI
# * * Event-Driven Ansible: existing-eda registered with Ansible Automation Platform UI
# * * Automation hub: existing-hub registered with Ansible Automation Platform UI
#
# Note: The automation controller, Event-Driven Ansible, and automation hub names must match the names of the existing.
# Automation controller, Event-Driven Ansible, and automation hub CRs in the same namespace as the Ansible Automation Platform CR. If the names do not match, the Ansible Automation Platform CR will not be able to register the existing automation controller, Event-Driven Ansible, and automation hub with the Ansible Automation Platform UI,and will instead deploy new automation controller, Event-Driven Ansible, and automation hub instances.
```

### aap-existing-hub-controller-eda.yml

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
name: existing-controller # <-- this is the name of the existing AutomationController CR
disabled: false

eda:
name: existing-eda
disabled: false

hub:
name: existing-hub
disabled: false

# End state:
# * Automation controller: existing-controller registered with Ansible Automation Platform UI
# * * Event-Driven Ansible: existing-eda registered with Ansible Automation Platform UI
# * * Automation hub: existing-hub registered with Ansible Automation Platform UI
#
# Note: The automation controller, Event-Driven Ansible, and automation hub names must match the names of the existing.
# Automation controller, Event-Driven Ansible, and automation hub CRs in the same namespace as the Ansible Automation Platform CR. If the names do not match, the Ansible Automation Platform CR will not be able to register the existing automation controller, Event-Driven Ansible, and automation hub with the Ansible Automation Platform UI,and will instead deploy new automation controller, Event-Driven Ansible, and automation hub instances.
```

### aap-fresh-controller-eda.yml

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

### aap-fresh-external-db.yml

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
disabled: false
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
# * * Automation hub deployed and named: myaap-hub
```

### aap-configuring-external-db-all-default-components.yml

```
---
apiVersion: aap.ansible.com/v1alpha1
kind: AnsibleAutomationPlatform
metadata:
name: myaap
spec:
database:
database_secret: external-postgres-configuration-gateway
controller:
postgres_configuration_secret: external-postgres-configuration-controller
hub:
postgres_configuration_secret: external-postgres-configuration-hub
eda:
database:
database_secret: external-postgres-configuration-eda
```

### aap-configuring-existing-external-db-all-default-components.yml

```
---
apiVersion: aap.ansible.com/v1alpha1
kind: AnsibleAutomationPlatform
metadata:
name: myaap
spec:
database:
database_secret: external-postgres-configuration-gateway
```


Note:

The system uses the external database for platform gateway, and automation controller, automation hub, and Event-Driven Ansible continues to use the existing databases that were used in 2.4.

### aap-configuring-external-db-with-lightspeed-enabled.yml

```
---
apiVersion: aap.ansible.com/v1alpha1
kind: AnsibleAutomationPlatform
metadata:
name: myaap
spec:
database:
database_secret: external-postgres-configuration-gateway
controller:
postgres_configuration_secret: external-postgres-configuration-controller
hub:
postgres_configuration_secret: external-postgres-configuration-hub
eda:
database:
database_secret: external-postgres-configuration-eda
lightspeed:
disabled: false
database:
database_secret: <secret-name>-postgres-configuration
auth_config_secret_name: 'auth-configuration-secret'
model_config_secret_name: 'model-configuration-secret'
```


Note:

You can follow the [Red Hat Ansible Lightspeed with IBM watsonx Code Assistant User Guide](https://docs.redhat.com/en/documentation/red_hat_ansible_lightspeed_with_ibm_watsonx_code_assistant/2.x_latest/html/red_hat_ansible_lightspeed_with_ibm_watsonx_code_assistant_user_guide/index) for help with creating the model and auth secrets.

### aap-fresh-install-with-settings.yml

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

### aap-fresh-install.yml

```
---
apiVersion: aap.ansible.com/v1alpha1
kind: AnsibleAutomationPlatform
metadata:
name: myaap
spec:
# Development purposes only
no_log: false

# Redis Mode
# redis_mode: cluster

# Platform
## uncomment to test bundle certs
# bundle_cacert_secret: gateway-custom-certs
# extra_settings:
#   - setting: MAX_PAGE_SIZE
#     value: '501'

# Components
controller:
disabled: false

eda:
disabled: false

hub:
disabled: false
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

# lightspeed:
#   disabled: true

# End state:
# * Automation controller deployed and named: myaap-controller
# * * Event-Driven Ansible deployed and named: myaap-eda
# * * Automation hub deployed and named: myaap-hub
```

### aap-fresh-only-controller.yml

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
disabled: true

hub:
disabled: true
## uncomment if using file storage for Content pod
# storage_type: file
# file_storage_storage_class: nfs-local-rwx
# file_storage_size: 10Gi

## uncomment if using S3 storage for Content pod
# storage_type: S3
# object_storage_s3_secret: example-galaxy-object-storage

## uncomment if using Azure storage for Content pod
# storage_type: azure
# object_storage_azure_secret: azure-secret-name


# End state:
# * Automation controller: existing-controller registered with Ansible Automation Platform UI
# * * Event-Driven Ansible deployed and named: myaap-eda
# * * Automation hub deployed and named: myaap-hub
```

### aap-fresh-only-hub.yml

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

### aap-lightspeed-enabled.yml

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
disabled: false
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

lightspeed:
disabled: false

# End state:
# * Automation controller deployed and named: myaap-controller
# * * Event-Driven Ansible deployed and named: myaap-eda
# * * Automation hub deployed and named: myaap-hub
# * Red Hat Ansible Lightspeed deployed and named: myaap-lightspeed
```

### gateway-only.yml

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
disabled: true

lightspeed:
disabled: true

# End state:
# * Platform gateway deployed and named: myaap-gateway
#   * UI is reachable at: https://myaap-gateway-gateway.apps.ocp4.example.com
# * Automation controller is not deployed
# * * Event-Driven Ansible is not deployed
# * * Automation hub is not deployed
# * Red Hat Ansible Lightspeed is not deployed
```

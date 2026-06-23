# Ansible Lightspeed custom resources
## AnsibleLightspeed [lightspeed.ansible.com/v1alpha1]
### Example custom resource

```
apiVersion: lightspeed.ansible.com/v1alpha1
kind: AnsibleLightspeed
metadata:
name: my-lightspeed
spec:
disabled: false
auth_config_secret_name: lightspeed-auth-config
model_config_secret_name: lightspeed-model-config
database:
database_secret: lightspeed-db-secret
```

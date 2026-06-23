# Microsoft Azure Resource Manager credential type
## Access Microsoft Azure Resource Manager credentials in an Ansible Playbook

You can get Microsoft Azure credential parameters from a job runtime environment.

```
vars:
azure:
client_id: '{{ lookup("env", "AZURE_CLIENT_ID") }}'
secret: '{{ lookup("env", "AZURE_SECRET") }}'
tenant: '{{ lookup("env", "AZURE_TENANT") }}'
subscription_id: '{{ lookup("env", "AZURE_SUBSCRIPTION_ID") }}'
```

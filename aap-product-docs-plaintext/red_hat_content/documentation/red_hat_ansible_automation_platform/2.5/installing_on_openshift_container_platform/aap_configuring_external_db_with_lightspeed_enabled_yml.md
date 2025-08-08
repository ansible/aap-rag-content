# 11. Appendix: Red Hat Ansible Automation Platform custom resources
## 11.1. Custom resources
### 11.1.11. aap-configuring-external-db-with-lightspeed-enabled.yml




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
database_secret: &lt;secret-name&gt;-postgres-configuration
auth_config_secret_name: 'auth-configuration-secret'
model_config_secret_name: 'model-configuration-secret'
```

Note
You can follow the [Red Hat Ansible Lightspeed with IBM watsonx Code Assistant User Guide](https://docs.redhat.com/en/documentation/red_hat_ansible_lightspeed_with_ibm_watsonx_code_assistant/2.x_latest/html/red_hat_ansible_lightspeed_with_ibm_watsonx_code_assistant_user_guide/index) for help with creating the model and auth secrets.




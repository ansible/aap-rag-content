# 6. Deploying Red Hat Ansible Lightspeed on containerized Ansible Automation Platform
## 6.2. Configuring Red Hat Ansible Lightspeed variables in the inventory file




To deploy Red Hat Ansible Lightspeed, add the required installation variables to your inventory file under the `[all: vars]` group. You will also need to add specific variables to enable the Ansible Lightspeed coding assistant, the Ansible Lightspeed intelligent assistant, and the MCP server integration. Refer to the [Appendix: Red Hat Ansible Lightspeed variables](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/containerized_installation/appendix-inventory-files-vars#lightspeed-variables) for information about required and optional variables.

```
# This is the list of inventory file variables required to deploy Red Hat Ansible Lightspeed on a containerized installation.

# Consult the docs if you are unsure what to add.
# For information about required and optional variables, refer to the Appendix: Red Hat Ansible Lightspeed variables
# https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/containerized_installation/appendix-inventory-files-vars#lightspeed-variables

# This section is for your Red Hat Ansible Lightspeed host
# ---------------------------------------------------------
[ansiblelightspeed]
aap.example.com

# This section is for Red Hat Ansible Lightspeed deployment
# ----------------------------------------------------------
lightspeed_admin_user: &lt;set your own&gt;
lightspeed_admin_password: &lt;set your own&gt;
lightspeed_admin_email: &lt;set your own&gt;
lightspeed_pg_host: &lt;set your own&gt;
lightspeed_pg_password: &lt;set your own&gt;


# This section is to configure Ansible Lightspeed intelligent assistant
# ----------------------------------------------------------------------
lightspeed_chatbot_model_url: &lt;set your own&gt;
lightspeed_chatbot_model_api_key: &lt;set your own&gt;
lightspeed_chatbot_model_id: : &lt;set your own&gt;
lightspeed_chatbot_default_provider: 'rhoai'
lightspeed_chatbot_model_extra_settings: {}
# If you want to use {AzureOpenAI} as the LLM provider, specify the lightspeed_chatbot_model_extra_settings value as '{"api_type": ""}'.

# This section is to configure Ansible Lightspeed intelligent assistant with MCP server integration
# --------------------------------------------------------------------------------------------------
lightspeed_mcp_controller_enabled: false
lightspeed_mcp_lightspeed_enabled: false


# This section is to configure Ansible Lightspeed coding assistant
# -----------------------------------------------------------------
lightspeed_wca_model_type: 'wca'
lightspeed_wca_model_url: 'https://api.dataplatform.cloud.ibm.com'
lightspeed_wca_model_verify_ssl: true
lightspeed_wca_model_enable_anonymization: true
lightspeed_wca_health_check: true
```

**Next steps**

-  [Installing containerized Ansible Automation Platform](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html-single/containerized_installation/index#installing-containerized-aap)



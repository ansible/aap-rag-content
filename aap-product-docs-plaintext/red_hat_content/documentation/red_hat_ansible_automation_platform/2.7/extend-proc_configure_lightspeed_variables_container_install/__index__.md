# Configure Red Hat Ansible Lightspeed variables

To deploy Red Hat Ansible Lightspeed, configure the required installation variables in your inventory file.

## Procedure

1.  Add the required installation variables to your inventory file under the `[all: vars]` group.
2.  You will also need to add specific variables to enable the coding assistant, the intelligent assistant, and the MCP server integration. Refer to the [Appendix: Red Hat Ansible Lightspeed variables](/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-ref_lightspeed_variables "Configure Red Hat Ansible Lightspeed by setting inventory file variables during installation. Use this reference to determine which variables to set for your deployment requirements.") for information about required and optional variables.

```
# This is the list of inventory file variables required to deploy Red Hat Ansible Lightspeed on a containerized installation.

# Consult the docs if you are unsure what to add.
# For information about required and optional variables, refer to the Appendix: Red Hat Ansible Lightspeed variables
# https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/install-ref_lightspeed_variables

# This section is for your Red Hat Ansible Lightspeed host
# ---------------------------------------------------------
[ansiblelightspeed]
aap.example.com

# This section is for Red Hat Ansible Lightspeed deployment
# ----------------------------------------------------------
lightspeed_admin_user: <set your own>
lightspeed_admin_password: <set your own>
lightspeed_admin_email: <set your own>
lightspeed_pg_host: <set your own>
lightspeed_pg_password: <set your own>

# This section is to configure the automation intelligent assistant
# ----------------------------------------------------------------------
lightspeed_chatbot_model_url: <set your own>
lightspeed_chatbot_model_api_key: <set your own>
lightspeed_chatbot_model_id: : <set your own>
lightspeed_chatbot_default_provider: 'rhoai'
lightspeed_chatbot_model_extra_settings: {}
lightspeed_chatbot_agent_extra_settings: {}
# If you want to use Microsoft Azure OpenAI as the LLM provider, specify the lightspeed_chatbot_model_extra_settings value as '{"api_type": ""}', and the lightspeed_chatbot_model_url value to 'https://your_inference_api/openai/v1'.

# This section is to configure the automation intelligent assistant with MCP server integration
# --------------------------------------------------------------------------------------------------
lightspeed_mcp_controller_enabled: false
lightspeed_mcp_lightspeed_enabled: false

# This section is to configure the coding assistant
# -----------------------------------------------------------------
lightspeed_wca_model_type: 'wca'
lightspeed_wca_model_url: 'https://api.dataplatform.cloud.ibm.com'
lightspeed_wca_model_verify_ssl: true
lightspeed_wca_model_enable_anonymization: true
lightspeed_wca_health_check: true
```

## What to do next

-  [Installing containerized Ansible Automation Platform](/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-proc_installing_containerized_aap#installing-containerized-aap "Run the install playbook to install containerized Ansible Automation Platform after preparing the Red Hat Enterprise Linux host, downloading the installation program, and configuring the inventory file.")

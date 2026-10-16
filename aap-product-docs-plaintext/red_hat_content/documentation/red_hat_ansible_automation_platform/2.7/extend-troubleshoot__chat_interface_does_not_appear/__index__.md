# Troubleshoot: Chat interface does not appear

The automation intelligent assistant chat interface might not appear in the platform UI if the provider configuration does not match your LLM service endpoint.

## Before you begin

You have deployed the automation intelligent assistant following the installation procedures for your deployment type (OpenShift Container Platform or containerized installation).

## Procedure

1. Verify your inventory file configuration for the intelligent assistant variables. Check that `lightspeed_chatbot_default_provider` matches your LLM service deployment platform. See [Provider configuration values](/documentation/en-us/red_hat_ansible_automation_platform/2.7/extend-provider_configuration_values "Valid provider values for the automation intelligent assistant and when to use each one.") for the complete reference.
Incorrect configuration (provider does not match URL):

```
lightspeed_chatbot_model_url="https://litellm-litemaas.apps.prod.rhoai.rh-aiservices-bu.com/v1"
lightspeed_chatbot_default_provider="openai"  # WRONG - URL is RHOAI, not OpenAI
```

Correct configuration:

```
lightspeed_chatbot_model_url="https://litellm-litemaas.apps.prod.rhoai.rh-aiservices-bu.com/v1"
lightspeed_chatbot_default_provider="rhoai"  # CORRECT - matches the deployment platform
```

2. Update the `lightspeed_chatbot_default_provider` value in your inventory file to match your LLM service endpoint.
3. Rerun the installation playbook to apply the corrected configuration.
For containerized installations:

```
ansible-playbook -i inventory ansible.containerized_installer.install
```

For OpenShift Container Platform deployments, update the custom resource and allow the Operator to reconcile the changes.

4. Clear your browser cache and refresh the Ansible Automation Platform UI.

## Results

The automation intelligent assistant chat interface appears in the Ansible Automation Platform UI. You can click the chat icon to open the interface and ask questions about your automation environment.

## What to do next

If the chat interface still does not appear after correcting the provider setting, verify:

- The `lightspeed_chatbot_model_url`, `lightspeed_chatbot_model_api_key`, and `lightspeed_chatbot_model_id` values are correct for your LLM deployment
- Network connectivity exists between the Ansible Automation Platform instance and the LLM service endpoint
- The LLM service is running and accessible at the configured URL
- Check the intelligent assistant service logs for error messages related to LLM communication

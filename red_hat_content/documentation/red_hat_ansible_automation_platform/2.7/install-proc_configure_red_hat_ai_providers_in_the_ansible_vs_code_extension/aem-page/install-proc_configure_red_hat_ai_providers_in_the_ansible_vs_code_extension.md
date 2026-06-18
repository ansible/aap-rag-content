+++
title = "Configure Red Hat AI providers in the Ansible VS Code extension - Red Hat Ansible Automation Platform 2.7"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-proc_configure_red_hat_ai_providers_in_the_ansible_vs_code_extension"
template = "docs/aem-title.html"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-assembly_devtools_install/", "Install Ansible development tools"]]
category = "Install"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/install-proc_configure_red_hat_ai_providers_in_the_ansible_vs_code_extension/aem-page/install-proc_configure_red_hat_ai_providers_in_the_ansible_vs_code_extension.html"
last_crumb = "Configure Red Hat AI providers in the Ansible VS Code extension"
modified = "2026-06-05T07:48:10.594Z"
multi_page_path = ""
name = "Configure Red Hat AI providers in the Ansible VS Code extension"
oversized = "false"
page_slug = "install-proc_configure_red_hat_ai_providers_in_the_ansible_vs_code_extension"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/install-proc_configure_red_hat_ai_providers_in_the_ansible_vs_code_extension"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/install-proc_configure_red_hat_ai_providers_in_the_ansible_vs_code_extension/toc/toc.json"
type = "aem-page"
+++

# Configure Red Hat AI providers in the Ansible VS Code extension

You can configure the Ansible VS Code extension to interact with models hosted on Red Hat AI infrastructure such as the RHEL AI Inference Server and OpenShift AI.

## Before you begin

- You have installed the Ansible VS Code extension version 25.12.3 or later.
- You already deployed and can access the Red Hat AI infrastructure (RHEL AI Inference Server or OpenShift AI).
- You have the API endpoint URL for the inference server.
- You have a valid API key or credential for the target model.
- You know the specific Model Name.

## About this task

This integration enables you to use the "Bring Your Own LLM" (BYOLLM) capability to generate and explain Ansible playbooks and roles. You can use your own hosted models, such as Llama, Mistral, or OpenAI, without requiring external middleware.

## Procedure

1.  In Visual Studio Code, open the LLM provider settings:
  1.  In the Activity Bar, select the **Ansible** icon to open the Ansible Development Tools panel.
  2.  In the **GENERATIVE AI** section, select the settings icon (cog) to open the LLM provider configuration.
2.  In the **API Endpoint URL** field, enter the full address of your RHEL AI or OpenShift AI instance.
3.  In the **Model Name/ID** field, enter the specific identifier for the model you want to use (for example, `granite-13b-chat-v2`).
4.  In the **API Key** field, enter the credentials required to authenticate with your infrastructure.
  
  Note:
      The extension connects directly to the provider endpoint. It does not require the `c.ai.ansible.redhat.com` middleware or Red Hat authentication to enable this feature.

5.  Ensure that the Red Hat AI provider is selected as the active provider.
  
  Important:
      Only one provider can be active at a time. If you switch between providers, ensure you select the correct provider in the LLM provider configuration to enable the corresponding features.

## Results

1. Open an Ansible playbook or role file in the editor.
2. Check the status bar to verify that the Red Hat AI provider status is displayed and indicates a successful connection.
3. Right-click within the editor and trigger Ansible Lightspeed> (and then)Generate Playbook. If the configuration is correct, the extension generates content using the model hosted on your RHEL AI or OpenShift AI infrastructure.

- **Issue**: The extension fails to connect or times out. **Resolution**: Verify that the **API Endpoint URL** is reachable from your network. The extension has a default timeout of 30 seconds. Check the **Output** view in VS Code under the **Ansible Lightspeed** channel for specific error logs.

- **Issue**: Inline suggestions (ghost text) do not appear while typing. **Resolution**: This is expected behavior. Inline task suggestions and content source matching are not supported for Red Hat AI infrastructure providers.

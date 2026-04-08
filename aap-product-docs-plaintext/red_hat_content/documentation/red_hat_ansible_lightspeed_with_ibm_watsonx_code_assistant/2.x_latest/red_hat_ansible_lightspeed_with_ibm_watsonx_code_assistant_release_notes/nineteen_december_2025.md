# 2. New features and enhancements
## 2.1. 19 December 2025




This release features the following enhancement:

**Support for Bring Your Own LLM (BYOLLM) providers**

The Red Hat Ansible Lightspeed extension for VS Code now includes Bring-Your-Own-LLM (BYOLLM) functionality, decoupling the code generation experience from a single model provider (IBM watsonx Code Assistant).

Ansible users can now configure and select their preferred third-party Large Language Model (LLM), such as Google Gemini or custom {OpenAI}-compliant models, rather than relying exclusively on the default IBM watsonx Code Assistant (WCA). By allowing users to switch providers, Ansible developers can use the most current and capable AI models to create single or multitask recommendations, generate and explain playbooks and roles. This capability ensures high-quality outputs and improved accuracy without disrupting established development workflows.

Note
Red Hat Ansible Lightspeed no longer supports custom model creation.



For information about how to configure Google Gemini or IBM watsonx Code Assistant as the AI provider, see [Configuring the Ansible VS Code extension](https://docs.redhat.com/en/documentation/red_hat_ansible_lightspeed_with_ibm_watsonx_code_assistant/2.x_latest/html-single/red_hat_ansible_lightspeed_with_ibm_watsonx_code_assistant_user_guide/index#configure-vscode-extension_developing-ansible-content) .


# 5. Deploying the Ansible Lightspeed intelligent assistant on OpenShift Container Platform
## 5.1. Overview
### 5.1.1. Integration with MCP server




Ansible Lightspeed intelligent assistant integration with the Model Context Protocol (MCP) server is available as a Technology Preview release. This integration enhances the user experience by delivering relevant, dynamically sourced data results to your queries.

MCP is an open protocol that standardizes how applications provide context to LLMs. Using the protocol, an MCP server provides a standardized way for an LLM to increase context by requesting and receiving real-time information from external resources. The integration with an MCP server enables the Ansible Lightspeed intelligent assistant to offer an enhanced user experience by delivering relevant, dynamically sourced data results to your queries. You can configure a MCP server in the chatbot configuration secret. For more information, see [Creating a chatbot configuration secret](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html-single/installing_on_openshift_container_platform/index#proc-create-chatbot-config-secret_deploying-chatbot-operator) .

Note
Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process. For more information about the support scope of Red Hat Technology Preview features, see [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview/) .




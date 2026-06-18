+++
title = "Install Ansible Development Tools with the AI assistant - Red Hat Ansible Automation Platform 2.6"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.6/extend-install_ansible_development_tools_with_the_ai_assistant"
template = "docs/aem-title.html"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6", "2.6"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6/extend-enable_ai_in_the_ansible_vs_code_extension_with_the_mcp_server/", "Enable AI in the Ansible VS Code extension with the MCP server"]]
category = "Extend"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/extend-install_ansible_development_tools_with_the_ai_assistant/aem-page/extend-install_ansible_development_tools_with_the_ai_assistant.html"
last_crumb = "Install Ansible Development Tools with the AI assistant"
modified = "2026-05-21T14:12:12.122Z"
multi_page_path = ""
name = "Install Ansible Development Tools with the AI assistant"
oversized = "false"
page_slug = "extend-install_ansible_development_tools_with_the_ai_assistant"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.6"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/extend-install_ansible_development_tools_with_the_ai_assistant"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/extend-install_ansible_development_tools_with_the_ai_assistant/toc/toc.json"
type = "aem-page"
+++

# Install Ansible Development Tools with the AI assistant

If you do not have Ansible Development Tools installed, you can instruct the assistant to install them.

## Procedure

1.  Open GitHub Copilot Chat.
2.  Enter the prompt:
  

```

  
  
```
The assistant then triggers the `adt_check_env` tool.
  The system:
  - Checks if ADT is already installed. If so, it will report: "ADT (`ansible-dev-tools`) is already installed".
  - If ADT is not installed, it will attempt installation via `pip` or `pipx`.
If ADT is not already installed, the AI assistant chooses a package manager (`pip` or `pipx`) and installs ADT automatically.

## What to do next

When installation is complete, the assistant will return a message in the Copilot chat window confirming that ADT has been installed successfully. You can also prompt the assistant to `check my Ansible environment again`. If the installation was successful, the assistant will verify that ADT is in your environment.

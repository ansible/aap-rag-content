+++
title = "Install Ansible Development Tools with the AI assistant - Red Hat Ansible Automation Platform 2.7"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/develop-install_ansible_development_tools_with_the_ai_assistant"
template = "docs/aem-title.html"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/develop-assembly_lightspeed_intro/", "Build automation faster with Red Hat Ansible Lightspeed code assistant"]]
category = "Develop"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/develop-install_ansible_development_tools_with_the_ai_assistant/aem-page/develop-install_ansible_development_tools_with_the_ai_assistant.html"
last_crumb = "Install Ansible Development Tools with the AI assistant"
latest = "true"
modified = "2026-10-06T15:21:13.207Z"
multi_page_path = ""
name = "Install Ansible Development Tools with the AI assistant"
oversized = "false"
page_slug = "develop-install_ansible_development_tools_with_the_ai_assistant"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/develop-install_ansible_development_tools_with_the_ai_assistant"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/develop-install_ansible_development_tools_with_the_ai_assistant/toc/toc.json"
type = "aem-page"
+++

# Install Ansible Development Tools with the AI assistant

If you do not have Ansible Development Tools installed, you can instruct the assistant to install them.

## Procedure

1. Open GitHub Copilot Chat.
2. Enter the prompt:
  

```

  
  
```

The assistant then triggers the `adt_check_env` tool.
  The system:
  - Checks if ADT is already installed. If so, it will report: "ADT (`ansible-dev-tools`) is already installed".
  - If ADT is not installed, it will attempt installation via `pip` or `pipx`.
If ADT is not already installed, the AI assistant chooses a package manager (`pip` or `pipx`) and installs ADT automatically.

## What to do next

When installation is complete, the assistant will return a message in the Copilot chat window confirming that ADT has been installed successfully. You can also prompt the assistant to `check my Ansible environment again`. If the installation was successful, the assistant will verify that ADT is in your environment.

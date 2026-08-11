+++
template = "docs/aem-title.html"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/extend-remove_the_automation_intelligent_assistant_from_a_containerized_deployment"
title = "Remove the automation intelligent assistant from a containerized deployment - Red Hat Ansible Automation Platform 2.7"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/extend-disable_or_remove_the_automation_intelligent_assistant/", "Disable or remove the automation intelligent assistant"]]
category = "Extend"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/extend-remove_the_automation_intelligent_assistant_from_a_containerized_deployment/aem-page/extend-remove_the_automation_intelligent_assistant_from_a_containerized_deployment.html"
last_crumb = "Remove the automation intelligent assistant from a containerized deployment"
modified = "2026-07-30T17:12:56.473Z"
multi_page_path = ""
name = "Remove the automation intelligent assistant from a containerized deployment"
oversized = "false"
page_slug = "extend-remove_the_automation_intelligent_assistant_from_a_containerized_deployment"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/extend-remove_the_automation_intelligent_assistant_from_a_containerized_deployment"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/extend-remove_the_automation_intelligent_assistant_from_a_containerized_deployment/toc/toc.json"
type = "aem-page"
+++

# Remove the automation intelligent assistant from a containerized deployment

Use this procedure to remove the automation intelligent assistant from a containerized Ansible Automation Platform installation.

## Before you begin

- You have administrator access to the host where Ansible Automation Platform is installed.
- You have access to the inventory file used for the Ansible Automation Platform installation.

## About this task

Note:

**Important**: To stop the chatbot as quickly as possible, complete step 1 first. Stopping the chatbot services immediately prevents the assistant from responding to user queries while you complete the remaining steps.

Note:

Re-running the installer with the chatbot configuration removed disconnects the chatbot from the platform gateway, but does not stop or remove the chatbot containers. The manual cleanup steps in this procedure are required.

## Procedure

1.  Stop the chatbot services on the host to immediately prevent the assistant from responding to queries:
  

```
sudo systemctl stop ansible-lightspeed-chatbot.service
sudo systemctl stop ansible-lightspeed.service
```

2.  Disable the chatbot services to prevent them from restarting on reboot:
  

```
sudo systemctl disable ansible-lightspeed-chatbot.service
sudo systemctl disable ansible-lightspeed.service
```

3.  Open the inventory file that you used to install Ansible Automation Platform.
4.  Remove or comment out all chatbot variables from the inventory file. These are the variables that begin with `lightspeed_chatbot_`:

  - `lightspeed_chatbot_model_url`
  - `lightspeed_chatbot_model_api_key`
  - `lightspeed_chatbot_model_id`
  - `lightspeed_chatbot_default_provider`
  - `lightspeed_chatbot_model_extra_settings`
  - `lightspeed_chatbot_agent_extra_settings`

5.  Remove or comment out the Ansible Lightspeed host entry from the `[ansiblelightspeed] `group, if no other Lightspeed components are in use. Leave the group header in the inventory file.
6.  Save the inventory file.
7.  Re-run the Ansible Automation Platform installer with the updated inventory file:
  

```
ansible-playbook -i inventory
ansible.containerized_installer.install
```

The installer reconfigures the platform gateway to remove the chatbot proxy routes. The chatbot API endpoints return a 503 error and the chat interface is no longer accessible to users.

8.  Remove the stopped chatbot containers from the host:
  

```
podman rm ansible-lightspeed-chatbot
podman rm ansible-lightspeed
```

## What to do next

To verify:

1. Confirm that the chatbot containers are no longer present on the host:

```
podman ps -a --filter name=ansible-lightspeed
```

No containers with the name `ansible-lightspeed`should be listed.

2. Access the Ansible Automation Platform web interface and confirm that the chat icon is no longer displayed in the top navigation bar.

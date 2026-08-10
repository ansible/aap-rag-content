+++
title = "Re-enable the automation intelligent assistant - Red Hat Ansible Automation Platform 2.7"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/extend-reenable_the_automation_intelligent_assistant"
template = "docs/aem-title.html"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/extend-disable_or_remove_the_automation_intelligent_assistant/", "Disable or remove the automation intelligent assistant"]]
category = "Extend"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/extend-reenable_the_automation_intelligent_assistant/aem-page/extend-reenable_the_automation_intelligent_assistant.html"
last_crumb = "Re-enable the automation intelligent assistant"
modified = "2026-07-30T17:12:56.473Z"
multi_page_path = ""
name = "Re-enable the automation intelligent assistant"
oversized = "false"
page_slug = "extend-reenable_the_automation_intelligent_assistant"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/extend-reenable_the_automation_intelligent_assistant"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/extend-reenable_the_automation_intelligent_assistant/toc/toc.json"
type = "aem-page"
+++

# Re-enable the automation intelligent assistant

After you resolve the issue that caused you to disable the automation intelligent assistant, you can re-enable it.

For an operator-based deployment:

- Set `disabled` to `false` in the Ansible Automation Platform custom resource YAML, and click **Save**. The operator recreates the AnsibleLightspeed custom resource and the Lightspeed pods restart automatically.

For containerized installations:

- Restore the Lightspeed chatbot variables in the inventory file, re-enable and start the systemd services, and re-run the installer:

```
sudo systemctl enable ansible-lightspeed.service
ansible-lightspeed-chatbot.service
sudo systemctl start ansible-lightspeed.service
ansible-lightspeed-chatbot.service ansible-playbook -i inventory ansible.containerized_installer.install
```

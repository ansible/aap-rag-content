+++
title = "Add a safe plugin variable to Event-Driven Ansible controller - Red Hat Ansible Automation Platform 2.7"
template = "docs/aem-title.html"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-proc_add_eda_safe_plugin_var"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-con_aap_containerized_installation_intro/", "Install containerized Ansible Automation Platform"]]
category = "Install"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/install-proc_add_eda_safe_plugin_var/aem-page/install-proc_add_eda_safe_plugin_var.html"
last_crumb = "Add a safe plugin variable to Event-Driven Ansible controller"
modified = "2026-06-05T07:48:10.594Z"
multi_page_path = ""
name = "Add a safe plugin variable to Event-Driven Ansible controller"
oversized = "false"
page_slug = "install-proc_add_eda_safe_plugin_var"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/install-proc_add_eda_safe_plugin_var"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/install-proc_add_eda_safe_plugin_var/toc/toc.json"
type = "aem-page"
+++

# Add a safe plugin variable to Event-Driven Ansible controller

When using the `redhat.insights_eda` plugin for rulebook activations, add a safe plugin variable to a platform directory to ensure a secure connection and correct port mapping displays.

## Procedure

1.  Create a directory for the safe plugin variable:
  

```
mkdir -p ./group_vars/automationeda
```

2.  Create a file within that directory for your new setting (for example, `touch ./group_vars/automationeda/custom.yml`)
3.  Add the variable `eda_safe_plugins` with a list of plugins to enable. For example:
  

```
eda_safe_plugins: ['ansible.eda.webhook', 'ansible.eda.alertmanager']
```

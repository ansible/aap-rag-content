+++
title = "Add a safe plugin variable to Event-Driven Ansible controller - Red Hat Ansible Automation Platform 2.6"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.6/install-proc_add_eda_safe_plugin_var"
template = "docs/aem-title.html"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6", "2.6"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6/install-assembly_platform_install_overview/", "Install RPM-based Ansible Automation Platform"]]
category = "Install"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/install-proc_add_eda_safe_plugin_var/aem-page/install-proc_add_eda_safe_plugin_var.html"
last_crumb = "Add a safe plugin variable to Event-Driven Ansible controller"
modified = "2026-05-21T14:12:12.122Z"
multi_page_path = ""
name = "Add a safe plugin variable to Event-Driven Ansible controller"
oversized = "false"
page_slug = "install-proc_add_eda_safe_plugin_var"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.6"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/install-proc_add_eda_safe_plugin_var"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/install-proc_add_eda_safe_plugin_var/toc/toc.json"
type = "aem-page"
+++

# Add a safe plugin variable to Event-Driven Ansible controller

When using the `redhat.insights_eda` plugin for rulebook activations, add a safe plugin variable to a platform directory to ensure a secure connection and correct port mapping displays.

## Procedure

1.  Create a directory for the safe plugin variable: `mkdir -p ./group_vars/automationedacontroller`
2.  Create a file within that directory for your new setting (for example, `touch ./group_vars/automationedacontroller/custom.yml`)
3.  Add the variable `automationedacontroller_additional_settings` to extend the default `settings.yaml` template for Event-Driven Ansible controller and add the `SAFE_PLUGINS` field with a list of plugins to enable. For example:
  

```
automationedacontroller_additional_settings:
   SAFE_PLUGINS:
     - ansible.eda.webhook
     - ansible.eda.alertmanager
```
  Note:
      You can also extend the `automationedacontroller_additional_settings` variable beyond `SAFE_PLUGINS` in the Django configuration file `/etc/ansible-automation-platform/eda/settings.yaml`.

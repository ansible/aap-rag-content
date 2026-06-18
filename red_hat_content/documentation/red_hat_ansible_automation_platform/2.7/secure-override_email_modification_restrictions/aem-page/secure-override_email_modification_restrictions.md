+++
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/secure-override_email_modification_restrictions"
title = "Override email modification restrictions - Red Hat Ansible Automation Platform 2.7"
template = "docs/aem-title.html"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/secure-assembly_gw_configure_authentication/", "Configure central authentication for Ansible Automation Platform"]]
category = "Secure"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/secure-override_email_modification_restrictions/aem-page/secure-override_email_modification_restrictions.html"
last_crumb = "Override email modification restrictions"
modified = "2026-06-05T07:48:10.594Z"
multi_page_path = ""
name = "Override email modification restrictions"
oversized = "false"
page_slug = "secure-override_email_modification_restrictions"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/secure-override_email_modification_restrictions"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/secure-override_email_modification_restrictions/toc/toc.json"
type = "aem-page"
+++

# Override email modification restrictions

If your organization requires non-admin users to modify their own email addresses, you can enable the `ALLOW_USER_EMAIL_SELF_EDIT` setting for each Ansible Automation Platform component.

## About this task

Important:

Enabling `ALLOW_USER_EMAIL_SELF_EDIT` re-introduces the risk of account pre-hijacking through email address manipulation. Only enable this setting if your organization has compensating controls in place.

This setting is deprecated and will be removed in a future version of Ansible Automation Platform.

Each component manages its own settings independently. Apply the setting to each component based on your deployment topology.

## Procedure

 Configure the setting for your deployment type:

- **RPM deployments**: Create or edit the override file for the relevant component, then restart its service:
  * automation controller: /etc/tower/conf.d/custom.py
  * platform gateway: /etc/ansible-automation-platform/gateway/settings.py
  * automation hub: /etc/pulp/settings.py
  * Event-Driven Ansible: /etc/ansible-automation-platform/eda/settings.yaml

- **Containerized deployments**: Add the setting through the `extra_settings` variable for each component in your installer inventory or group variables:
  * `gateway_extra_settings` — platform gateway
  * `controller_extra_settings` — automation controller
  * `eda_extra_settings` — Event-Driven Ansible
  * `hub_extra_settings` — automation hub

     Use the following format:



```
controller_extra_settings:
  - setting: ALLOW_USER_EMAIL_SELF_EDIT
    value: true
```

- **OpenShift (Operator) deployments**: Add the setting under `spec.extra_settings` on the `AnsibleAutomationPlatform` custom resource:

```
spec:
  extra_settings:
    - setting: ALLOW_USER_EMAIL_SELF_EDIT
      value: "true"
```
     The operator writes these settings into a ConfigMap and mounts it as a settings file inside the pod. The platform applies changes automatically after you update the custom resource.

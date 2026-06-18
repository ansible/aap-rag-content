+++
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/secure-ref_controller_credential_insights"
template = "docs/aem-title.html"
title = "Red Hat Lightspeed credential type - Red Hat Ansible Automation Platform 2.7"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/secure-assembly_controller_credentials/", "Configure credentials to authenticate remote systems and services"]]
category = "Secure"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/secure-ref_controller_credential_insights/aem-page/secure-ref_controller_credential_insights.html"
last_crumb = "Red Hat Lightspeed credential type"
modified = "2026-06-05T07:48:10.594Z"
multi_page_path = ""
name = "Red Hat Lightspeed credential type"
oversized = "false"
page_slug = "secure-ref_controller_credential_insights"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/secure-ref_controller_credential_insights"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/secure-ref_controller_credential_insights/toc/toc.json"
type = "aem-page"
+++

# Red Hat Lightspeed credential type

Select this credential type to enable synchronization of cloud inventory with Red Hat Lightspeed.

Red Hat Lightspeed credentials are the Red Hat Lightspeed **Username** and **Password**, which are the user’s Red Hat Customer Portal Account username and password.

The `extra_vars` and `env` injectors for Red Hat Lightspeed are as follows:

```
ManagedCredentialType(
    namespace='insights',
....
....
....

injectors={
        'extra_vars': {
            "scm_username": "{{username}}",
            "scm_password": "{{password}}",
        },
        'env': {
            'INSIGHTS_USER': '{{username}}',
            'INSIGHTS_PASSWORD': '{{password}}',
        },
```

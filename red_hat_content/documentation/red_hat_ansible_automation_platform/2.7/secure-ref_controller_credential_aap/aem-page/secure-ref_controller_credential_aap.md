+++
title = "Red Hat Ansible Automation Platform credential type - Red Hat Ansible Automation Platform 2.7"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/secure-ref_controller_credential_aap"
template = "docs/aem-title.html"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/secure-assembly_controller_credentials/", "Configure credentials to authenticate remote systems and services"]]
category = "Secure"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/secure-ref_controller_credential_aap/aem-page/secure-ref_controller_credential_aap.html"
last_crumb = "Red Hat Ansible Automation Platform credential type"
modified = "2026-06-05T07:48:10.594Z"
multi_page_path = ""
name = "Red Hat Ansible Automation Platform credential type"
oversized = "false"
page_slug = "secure-ref_controller_credential_aap"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/secure-ref_controller_credential_aap"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/secure-ref_controller_credential_aap/toc/toc.json"
type = "aem-page"
+++

# Red Hat Ansible Automation Platform credential type

Select this credential to access another automation controller instance.

Important:

In Ansible Automation Platform 2.7, the Ansible Automation Platform credential type must use the platform gateway URL. Direct component URLs are no longer supported.

Ansible Automation Platform credentials require the following inputs:

- **Red Hat Ansible Automation Platform**: The base URL or IP address of the other instance to connect to.
- **Username**: The username to use to connect to it.
- **Password**: The password to use to connect to it.
- **Oauth Token**: If username and password are not used, provide an OAuth token to use to authenticate.


The `env` injectors for Ansible Automation Platform are as follows:

```
ManagedCredentialType(  
      namespace='controller',

  ....
  ....
  ....  
  
  injectors={  
          'env': {
              'TOWER_HOST': '{{host}}',
              'TOWER_USERNAME': '{{username}}',
              'TOWER_PASSWORD': '{{password}}',  
              'TOWER_VERIFY_SSL': '{{verify_ssl}}',
              'TOWER_OAUTH_TOKEN': '{{oauth_token}}',  
              'CONTROLLER_HOST': '{{host}}',  
              'CONTROLLER_USERNAME': '{{username}}',
              'CONTROLLER_PASSWORD': '{{password}}',  
              'CONTROLLER_VERIFY_SSL': '{{verify_ssl}}',  
              'CONTROLLER_OAUTH_TOKEN': '{{oauth_token}}',  
          }
```

## Access automation controller credentials in an Ansible Playbook

You can get the host, username, and password parameters from a job runtime environment:

```
vars:
  controller:
    host: '{{ lookup("env", "CONTROLLER_HOST") }}'
    username: '{{ lookup("env", "CONTROLLER_USERNAME") }}'
    password: '{{ lookup("env", "CONTROLLER_PASSWORD") }}'
```

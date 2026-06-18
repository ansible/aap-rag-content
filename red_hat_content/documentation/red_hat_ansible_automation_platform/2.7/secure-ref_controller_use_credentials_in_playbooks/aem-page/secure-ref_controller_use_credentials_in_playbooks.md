+++
title = "Use automation controller credentials in a playbook - Red Hat Ansible Automation Platform 2.7"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/secure-ref_controller_use_credentials_in_playbooks"
template = "docs/aem-title.html"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/secure-assembly_controller_credentials/", "Configure credentials to authenticate remote systems and services"]]
category = "Secure"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/secure-ref_controller_use_credentials_in_playbooks/aem-page/secure-ref_controller_use_credentials_in_playbooks.html"
last_crumb = "Use automation controller credentials in a playbook"
modified = "2026-06-05T07:48:10.594Z"
multi_page_path = ""
name = "Use automation controller credentials in a playbook"
oversized = "false"
page_slug = "secure-ref_controller_use_credentials_in_playbooks"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/secure-ref_controller_use_credentials_in_playbooks"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/secure-ref_controller_use_credentials_in_playbooks/toc/toc.json"
type = "aem-page"
+++

# Use automation controller credentials in a playbook

You can access automation controller credentials in an Ansible Playbook by using environment variables. You can get credential parameters from a job runtime environment:

Note:

In Ansible Automation Platform 2.7, the `CONTROLLER_HOST` environment variable contains the platform gateway URL, not the direct automation controller URL. This ensures all API access goes through platform gateway.

The following playbook is an example of how to use automation controller credentials in your playbook.

```
- hosts: all

  vars:
    machine:
      username: '{{ ansible_user }}'
      password: '{{ ansible_password }}'
    controller:
      host: '{{ lookup("env", "CONTROLLER_HOST") }}'
      username: '{{ lookup("env", "CONTROLLER_USERNAME") }}'
      password: '{{ lookup("env", "CONTROLLER_PASSWORD") }}'
    network:
      username: '{{ lookup("env", "ANSIBLE_NET_USERNAME") }}'
      password: '{{ lookup("env", "ANSIBLE_NET_PASSWORD") }}'
    aws:
      access_key: '{{ lookup("env", "AWS_ACCESS_KEY_ID") }}'
      secret_key: '{{ lookup("env", "AWS_SECRET_ACCESS_KEY") }}'
      security_token: '{{ lookup("env", "AWS_SECURITY_TOKEN") }}'
    vmware:
      host: '{{ lookup("env", "VMWARE_HOST") }}'
      username: '{{ lookup("env", "VMWARE_USER") }}'
      password: '{{ lookup("env", "VMWARE_PASSWORD") }}'
    gce:
      email: '{{ lookup("env", "GCE_EMAIL") }}'
      project: '{{ lookup("env", "GCE_PROJECT") }}'
    azure:
      client_id: '{{ lookup("env", "AZURE_CLIENT_ID") }}'
      secret: '{{ lookup("env", "AZURE_SECRET") }}'
      tenant: '{{ lookup("env", "AZURE_TENANT") }}'
      subscription_id: '{{ lookup("env", "AZURE_SUBSCRIPTION_ID") }}'

  tasks:
    - debug:
        var: machine

    - debug:
        var: controller

    - debug:
        var: network

    - debug:
        var: aws

    - debug:
        var: vmware

    - debug:
        var: gce

    - shell: 'cat {{ gce.pem_file_path }}'
      delegate_to: localhost

    - debug:
        var: azure
```

## Use 'delegate_to' and any lookup variable

```
- command: somecommand
  environment:
    USERNAME: '{{ lookup("env", "USERNAME") }}'
    PASSWORD: '{{ lookup("env", "PASSWORD") }}'
  delegate_to: somehost
```

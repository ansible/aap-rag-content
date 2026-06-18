+++
template = "docs/aem-title.html"
title = "Automate nodes that comply with security profiles - Red Hat Ansible Automation Platform 2.6"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.6/secure-con_more_compliance_profile_considerations"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6", "2.6"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6/secure-assembly_hardening_aap/", "Harden the platform security posture"]]
category = "Secure"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/secure-con_more_compliance_profile_considerations/aem-page/secure-con_more_compliance_profile_considerations.html"
last_crumb = "Automate nodes that comply with security profiles"
modified = "2026-05-21T14:12:12.122Z"
multi_page_path = ""
name = "Automate nodes that comply with security profiles"
oversized = "false"
page_slug = "secure-con_more_compliance_profile_considerations"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.6"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/secure-con_more_compliance_profile_considerations"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/secure-con_more_compliance_profile_considerations/toc/toc.json"
type = "aem-page"
+++

# Automate nodes that comply with security profiles

Edit specific security controls on your compliance-hardened RHEL nodes so Ansible Automation Platform can manage them properly. This helps ensure smooth automation in environments governed by strict profiles like CIS, PCI/DSS, or DISA STIG.

## Fapolicyd on managed RHEL nodes

Ansible jobs on RHEL nodes often fail if the `fapolicyd` service is enabled. This occurs because the service prevents the execution of Python code copied to the node during task processing.

To prevent this issue from occurring, use one of the following methods:

- Option 1: Set the fapolicyd service to permissive mode
- Option 2: Create custom fapolicyd rules

## Option 1: Set the fapolicyd service to permissive mode

The fapolicyd service can be set to "permissive" mode, meaning that it only logs fapolicyd rule violations, rather than enforcing them.

### About this task

To configure permissive mode for fapolicyd, use the following procedure:

### Procedure

1.  Edit the file `/etc/fapolicyd/fapolicyd.conf`, and set "permissive = 1".
2.  Restart the `fapolicy` service by running `systemctl restart fapolicyd.service`.
3.  In environments where this configuration might not meet a required compliance profile or local policy, discuss waiving the relevant security control with your security auditor.

## Option 2: Create custom fapolicyd rules

Where the `fapolicyd` service must enforce its rules, consider crafting a custom set of rules to permit Ansible Automation Platform to run its Python code.

### About this task

The following example procedure treats the "ansible" service account as a trusted entity and enables it to run content in the local Ansible temporary directory (by default, `$HOME/.ansible/tmp`).

### Procedure

1.  Create the file `/etc/fapolicy/rules.d/50-ansible.rules` with the following content:
       `allow perm=any uid=ansible trust=1 : dir=/home/ansible/.ansible/tmp/`

2.  Restart the fapolicyd service:
       `sudo systemctl restart fapolicyd.service`

    This example rule might require modification to work with any other `fapolicyd` rules that exist on the managed RHEL nodes, and must be thoroughly tested and approved by your security auditor before being put into production.

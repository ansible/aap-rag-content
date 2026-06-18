+++
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/secure-con_patch_automation_with_aap"
template = "docs/aem-title.html"
title = "Automate software patching - Red Hat Ansible Automation Platform 2.7"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/secure-assembly_aap_security_use_cases/", "Security automation use cases"]]
category = "Secure"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/secure-con_patch_automation_with_aap/aem-page/secure-con_patch_automation_with_aap.html"
last_crumb = "Automate software patching"
modified = "2026-06-05T07:48:10.594Z"
multi_page_path = ""
name = "Automate software patching"
oversized = "false"
page_slug = "secure-con_patch_automation_with_aap"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/secure-con_patch_automation_with_aap"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/secure-con_patch_automation_with_aap/toc/toc.json"
type = "aem-page"
+++

# Automate software patching

Software patching is a fundamental activity of security and IT operations teams everywhere. Keeping patches up to date is critical to remediating software vulnerabilities and meeting compliance requirements, but patching systems manually at scale can be time-consuming and error-prone.

Organizations should put thought into patch management strategies that meet their security, compliance, and business objectives, to prioritize the types of patches to apply (known exploits, critical or important vulnerabilities, optimizations, routine updates, new features, and so on) against the IT assets available across the enterprise. Once policies and priorities have been defined and a patching plan is established, the manual tasks involved in patch management can be automated using Red Hat Ansible Automation Platform to improve patch deployment speed and accuracy, reduce human error, and limit downtime.

## Benefits of patch automation

Patch automation reduces manual effort, accelerates patch deployment across all systems, and improves consistency by eliminating human errors in complex updates. In more detail it provides:

- Reduces error-prone manual effort.
- Decreases time to deploy patches at scale.
- Ensures consistency of patches across similar systems. Manual patching of similar systems can result in human error (forgetting one or more, patching using different versions) that impacts consistency.
- Enables orchestration of complex patching scenarios where an update might require taking a system snapshot before applying a patch, or might require additional configuration changes when the patch is applied.

## Patching examples

You can modify and thoroughly test the following playbooks that serve as patching examples, to fit the target environment before production use.

These examples use the `ansible.builtin.dnf` module for managing packages on RHEL and other operating systems that use the `dnf` package manager. Modules for patching other Linux operating systems, Microsoft Windows, and many network devices are also available.

## Keep everything up to date

For non-production systems like labs, you can automate weekly patching using a job template. This example playbook updates all RPMs to the latest versions on a regular cadence to keep your servers current.

```
- name: Install all available RPM updates
  hosts: target_hosts
  become: true

  tasks:
    - name: Install latest RPMs
      ansible.builtin.dnf:
        name: '*'
        state: latest
```

## Install security updates only

For organizations with a policy requiring that all RPMs including security errata be kept up to date, the following playbook might be used in a regularly scheduled job template.

```
- name: Install all security-related RPM updates
  hosts: target_hosts
  become: true

  tasks:
    - name: Install latest RPMs with security errata
      ansible.builtin.dnf:
        name: '*'
        security: true
        state: latest
```

## Specify package versions

For production systems, a well-established configuration management practice is to deploy only known, tested combinations of software to ensure that systems are configured correctly and perform as expected.

This includes deploying only known versions of operating system software and patches to ensure that system updates do not introduce problems with production applications.

 Note:

The following example playbook installs a specific version of the `httpd` RPM and its dependencies when the target host uses the RHEL 9 operating system. This playbook does not take action if the specified versions are already in place or if a different version of RHEL is installed.

```
- name: Install specific RPM versions
  hosts: target_hosts
  gather_facts: true
  become: true

  vars:
    httpd_packages_rhel9:
      - httpd-2.4.53-11.el9_2.5
      - httpd-core-2.4.53-11.el9_2.5
      - httpd-filesystem-2.4.53-11.el9_2.5
      - httpd-tools-2.4.53-11.el9_2.5
      - mod_http2-1.15.19-4.el9_2.4
      - mod_lua-2.4.53-11.el9_2.5

  tasks:
    - name: Install httpd and dependencies
      ansible.builtin.dnf:
        name: '{{ httpd_packages_rhel9 }}'
        state: present
        allow_downgrade: true
    when:
      - ansible_distribution == "RedHat"
      - ansible_distribution_major_version == "9"
```


 Note:

By setting `allow_downgrade: true`, if a newer version of any defined package is installed on the system, it is downgraded to the specified version instead.

## Complex patching scenarios

In Ansible Automation Platform, multiple automation jobs can be chained together into workflows, which can be used to coordinate multiple steps in a complex patching scenario.

The following example complex patching scenario demonstrates taking virtual machine snapshots, patching the virtual machines, and creating tickets when an error is encountered in the workflow.

1. Run a project sync to ensure the latest playbooks are available. In parallel, run an inventory sync to make sure the latest list of target hosts is available.
2. Take a snapshot of each target host.   1. If the snapshot task fails, submit a ticket with the relevant information.
3. Patch each of the target hosts.   1. If the patching task fails, restore the snapshot and submit a ticket with the relevant information.
4. Delete each snapshot where the patching task was successful.


The following workflow visualization shows how the components of the example complex patching scenario are executed:

 ![Workflow representation](/webassets/aem/red_hat_ansible_automation_platform/2.7/images/workflow.png)

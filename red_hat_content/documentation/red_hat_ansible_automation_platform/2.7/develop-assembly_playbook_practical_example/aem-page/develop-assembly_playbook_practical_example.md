+++
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/develop-assembly_playbook_practical_example"
template = "docs/aem-title.html"
title = "Example: automate software updates - Red Hat Ansible Automation Platform 2.7"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/get_started-assembly_intro_to_playbooks_1/", "Get started automating with playbooks"]]
category = "Develop"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/develop-assembly_playbook_practical_example/aem-page/develop-assembly_playbook_practical_example.html"
last_crumb = "Example: automate software updates"
modified = "2026-06-05T07:48:10.594Z"
multi_page_path = ""
name = "Example: automate software updates"
oversized = "false"
page_slug = "develop-assembly_playbook_practical_example"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/develop-assembly_playbook_practical_example"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/develop-assembly_playbook_practical_example/toc/toc.json"
type = "aem-page"
+++

# Example: automate software updates

Ansible can communicate with many different device classifications, from cloud-based REST APIs, to Linux and Windows systems, networking hardware, and much more. The following is a sample of two Ansible modules automatically updating two types of servers.

## Playbook execution

A playbook runs in order from top to bottom. Within each play, tasks also run in order from top to bottom. Playbooks with multiple 'plays' can orchestrate multi-machine deployments, running one play on your webservers, then another play on your database servers, and so on.

At a minimum, each play defines two things:

- the managed nodes to target, using a pattern
- at least one task to run


Note:

Use the fully-qualified collection name in your playbooks to ensure the correct module is selected, because multiple collections can contain modules with the same name (for example, `user`).

In this example, the first play targets the web servers; the second play targets the database servers.

```
---
- name: Update web servers
  hosts: webservers
  become: true

  tasks:
    - name: Ensure apache is at the latest version
      ansible.builtin.yum:
        name: httpd
        state: latest
    - name: Write the apache config file
      ansible.builtin.template:
        src: /srv/httpd.j2
        dest: /etc/httpd.conf
        mode: "0644"

- name: Update db servers
  hosts: databases
  become: true

  tasks:
    - name: Ensure postgresql is at the latest version
      ansible.builtin.yum:
        name: postgresql
        state: latest
    - name: Ensure that postgresql is started
      ansible.builtin.service:
        name: postgresql
        state: started
```
The playbook contains two plays:

- The first checks if the web server software is up to date and runs the update if necessary.
- The second checks if database server software is up to date and runs the update if necessary.


Your playbook can include more than just a hosts line and tasks.

For example, this example playbook sets a remote_user for each play. This is the user account for the SSH connection. You can add other playbook keywords at the playbook, play, or task level to influence how Ansible behaves. Playbook keywords can control the connection plugin, whether to use privilege escalation, how to handle errors, and more.

To support a variety of environments, Ansible enables you to set many of these parameters as command-line flags, in your Ansible configuration, or in your inventory. Learning the precedence rules for these sources of data can help you as you expand your Ansible ecosystem

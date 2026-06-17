+++
title = "Create automation content with playbooks - Red Hat Ansible Automation Platform 2.6"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.6/get_started-con_gs_create_automation_content"
template = "docs/aem-title.html"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6", "2.6"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6/get_started-assembly_gs_auto_dev/", "Get started as an automation developer"]]
category = "Get started"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/get_started-con_gs_create_automation_content/aem-page/get_started-con_gs_create_automation_content.html"
last_crumb = "Create automation content with playbooks"
modified = "2026-05-21T14:12:12.122Z"
multi_page_path = ""
name = "Create automation content with playbooks"
oversized = "false"
page_slug = "get_started-con_gs_create_automation_content"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.6"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/get_started-con_gs_create_automation_content"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/get_started-con_gs_create_automation_content/toc/toc.json"
type = "aem-page"
+++

# Create automation content with playbooks

Ansible playbooks are blueprints that tell Ansible Automation Platform what tasks to perform with which devices. Use a playbook to define automation tasks for the platform to run.

## Create a playbook

A playbook contains one or more plays. A basic play contains the following parameters:

- **Name**: a brief description of the overall function of the playbook, which assists in keeping it readable and organized for all users.
- **Hosts**: identifies the target or targets for Ansible to run against.
- **Become statements**: this optional statement can be set to `true` or `yes` to enable privilege escalation using a become plugin (such as `sudo`, `su`, `pfexec`, `doas`, `pbrun`, `dzdo`, `ksu`).
- **Tasks**: this is the list of actions that get executed against each host in the play.


Here is an example of a play in a playbook. You can see the name of the play, the host, and the list of tasks included in the play.

```
- name: Set Up a Project and Job Template
  hosts: host.name.ip
  become: true

  tasks:
    - name: Create a Project
      ansible.controller.project:
        name: Job Template Test Project
        state: present
        scm_type: git
        scm_url: https://github.com/ansible/ansible-tower-samples.git

    - name: Create a Job Template
      ansible.controller.job_template:
        name: my-job-1
        project: Job Template Test Project
        inventory: Demo Inventory
        playbook: hello_world.yml
        job_type: run
        state: present
```
For more detailed guidance on authoring playbooks, consult the following documentation:

- Developing automation content
- Creating playbooks and viewing playbook explanations in the Red Hat Ansible Lightspeed with IBM watsonx Code Assistant User Guide to learn how to generate a playbook with AI.
- Getting started with playbooks

+++
title = "Create a simple playbook to connect to managed hosts - Red Hat Ansible Automation Platform 2.7"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/develop-proc_creating_a_playbook"
template = "docs/aem-title.html"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/get_started-assembly_intro_to_playbooks_1/", "Get started automating with playbooks"]]
category = "Develop"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/develop-proc_creating_a_playbook/aem-page/develop-proc_creating_a_playbook.html"
last_crumb = "Create a simple playbook to connect to managed hosts"
modified = "2026-06-05T07:48:10.594Z"
multi_page_path = ""
name = "Create a simple playbook to connect to managed hosts"
oversized = "false"
page_slug = "develop-proc_creating_a_playbook"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/develop-proc_creating_a_playbook"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/develop-proc_creating_a_playbook/toc/toc.json"
type = "aem-page"
+++

# Create a simple playbook to connect to managed hosts

Learn how to create a playbook that pings your hosts and prints a “Hello world” message.

## Procedure

1.  Create a file named `playbook.yaml` in your `ansible_quickstart` directory, with the following content:
  

```
- name: My first play
  hosts: myhosts
  tasks:
   - name: Ping my hosts
     ansible.builtin.ping:

    - name: Print message
     ansible.builtin.debug:
      msg: Hello world
```

2.  Run your playbook, using the following command:
       `ansible-playbook -i inventory.ini playbook.yaml`

3.  Ansible returns the following output:
  

```
PLAY [My first play] ****************************************************************************

    TASK [Gathering Facts] **************************************************************************
ok: [192.0.2.50]
ok: [192.0.2.51]
ok: [192.0.2.52]

    TASK [Ping my hosts] ****************************************************************************
ok: [192.0.2.50]
ok: [192.0.2.51]
ok: [192.0.2.52]

    TASK [Print message] ****************************************************************************
ok: [192.0.2.50] => {
    "msg": "Hello world"
}
ok: [192.0.2.51] => {
    "msg": "Hello world"
}
ok: [192.0.2.52] => {
    "msg": "Hello world"
}

    PLAY RECAP **************************************************************************************
192.0.2.50: ok=3    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
192.0.2.51: ok=3    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
192.0.2.52: ok=3    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
```
    In this output you can see:

  - The names that you give the play and each task. Always use descriptive names that make it easy to verify and troubleshoot playbooks.
  - The Gather Facts task runs implicitly. By default Ansible gathers information about your inventory that it can use in the playbook.
  - The status of each task. Each task has a status of `ok` which means it ran successfully.
  - The play recap that summarizes results of all tasks in the playbook per host. In this example, there are three tasks so `ok=3` indicates that each task ran successfully.

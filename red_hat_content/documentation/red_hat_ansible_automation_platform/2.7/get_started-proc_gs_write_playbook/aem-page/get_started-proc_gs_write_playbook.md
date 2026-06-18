+++
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/get_started-proc_gs_write_playbook"
template = "docs/aem-title.html"
title = "Write a playbook - Red Hat Ansible Automation Platform 2.7"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/get_started-assembly_gs_auto_dev/", "Get started as an automation developer"]]
category = "Get started"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/get_started-proc_gs_write_playbook/aem-page/get_started-proc_gs_write_playbook.html"
last_crumb = "Write a playbook"
modified = "2026-06-05T07:48:10.594Z"
multi_page_path = ""
name = "Write a playbook"
oversized = "false"
page_slug = "get_started-proc_gs_write_playbook"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/get_started-proc_gs_write_playbook"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/get_started-proc_gs_write_playbook/toc/toc.json"
type = "aem-page"
+++

# Write a playbook

Create a playbook that pings your hosts and prints a "Hello world" message.

## About this task

Ansible uses the YAML syntax. YAML is a human-readable language that enables you to create playbooks without having to learn a complicated coding language.

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

2.  Run your playbook:
  

```
$ ansible-playbook -i inventory.ini playbook.yaml
```

## Results

Ansible returns the following output:

```
PLAY [My first play] ********************************************************

TASK [Gathering Facts] ******************************************************
ok: [192.0.2.50]
ok: [192.0.2.51]
ok: [192.0.2.52]

TASK [Ping my hosts] ********************************************************
ok: [192.0.2.50]
ok: [192.0.2.51]
ok: [192.0.2.52]

TASK [Print message] ********************************************************
ok: [192.0.2.50] => {
    "msg": "Hello world"
}
ok: [192.0.2.51] => {

    "msg": "Hello world"
}
ok: [192.0.2.52] => {
    "msg": "Hello world"
}

PLAY RECAP ******************************************************************
192.0.2.50: ok=3    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
192.0.2.51: ok=3    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
192.0.2.52: ok=3    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
```

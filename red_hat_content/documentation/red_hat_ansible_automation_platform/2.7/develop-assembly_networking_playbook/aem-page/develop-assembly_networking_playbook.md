+++
title = "Gather and display network device info with a playbook - Red Hat Ansible Automation Platform 2.7"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/develop-assembly_networking_playbook"
template = "docs/aem-title.html"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/get_started-assembly_intro_to_playbooks_1/", "Get started automating with playbooks"]]
category = "Develop"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/develop-assembly_networking_playbook/aem-page/develop-assembly_networking_playbook.html"
last_crumb = "Gather and display network device info with a playbook"
modified = "2026-06-05T07:48:10.594Z"
multi_page_path = ""
name = "Gather and display network device info with a playbook"
oversized = "false"
page_slug = "develop-assembly_networking_playbook"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/develop-assembly_networking_playbook"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/develop-assembly_networking_playbook/toc/toc.json"
type = "aem-page"
+++

# Gather and display network device info with a playbook

Learn how to create and run a simple Ansible Playbook that connects to a network device, gathers facts, and displays them.

To confirm your credentials, you can connect to a network device manually and retrieve its configuration. Replace the sample user and device name with your real credentials.

For example, for a VyOS router:

```
ssh my_vyos_user@vyos.example.net
show config
exit
```

## Run a network Ansible command

Instead of manually connecting and running a command on the network device, you can retrieve its configuration with a single Ansible command.

```
ansible all -i vyos.example.net, -c ansible.netcommon.network_cli -u \
my_vyos_user -k -m vyos.vyos.vyos_facts -e \
ansible_network_os=vyos.vyos.vyos
```
The flags in this command set seven values:

- the host group(s) to which the command should apply (in this case, `all`)
- the inventory (`-i`, the device or devices to target - without the trailing comma `-i` points to an inventory file)
- the connection method (`-c`, the method for connecting and executing ansible)
- the user (`-u`, the username for the SSH connection)
- the SSH connection method (-`k`, prompt for the password)
- the module (`-m`, the Ansible module to run, using the fully qualified collection name (FQCN))
- an extra variable ( `-e`, in this case, setting the network operating system value)


Note:

If you use `ssh-agent` with SSH keys, Ansible loads them automatically. You can omit the `-k` flag.

If you are running Ansible in a virtual environment, you must also add the variable `ansible_python_interpreter=/path/to/venv/bin/python`.

## Run a network Ansible Playbook

If you want to run a particular command every day, you can save it in a playbook and run it with `ansible-playbook` instead of ansible.

### Before you begin

Download `first_playbook.yml` from [here](https://docs.ansible.com/projects/ansible/latest/_downloads/588d4b6e9316c8eb903fbe2485b14d64/first_playbook.yml).

The playbook looks like this:

```
---

- name: Network Getting Started First Playbook
  connection: ansible.netcommon.network_cli
  gather_facts: false					        	①
  hosts: all
  tasks:

    - name: Get config for VyOS devices
      vyos.vyos.vyos_facts:
        gather_subset: all

    - name: Display the config
      debug:
        msg: "The hostname is {{ ansible_net_hostname }} and the OS is {{ ansible_net_version }}"
```

| Label               | Description                                                                                                                                                                                                            |
| ------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <br> `gather_facts` | <br>Ansible’s native fact gathering (`ansible.builtin.setup`) is disabled here because the playbook relies on the facts provided by a platform-specific module (`vyos.vyos.vyos_facts`) in this networking collection. |


The playbook sets three of the seven values from the command line above:

- the group (`hosts: all`)
- the connection method (`connection: ansible.netcommon.network_cli`) and
- the module (in each task).


With those values set in the playbook, you can omit them on the command line. The playbook also adds a second task to show the configuration output.

When facts are gathered from a system, either through a collection-specific fact module such as `vyos.vyos.vyos_facts` or `ansible.builtin.setup`, the gathered data is held in memory for use by future tasks instead of being written to the console.

When a module runs in a playbook, the output is held in memory for use by future tasks instead of written to the console. With most other modules you must explicitly register a variable to store and reuse the output of a module or task.

The following debug task lets you see the results in your shell.

### About this task

The playbook can store many of the parameters you provided with flags at the command line, leaving less to type at the command line. You need two files for this, a playbook and an inventory file.

### Procedure

1.  Run the playbook with the following command.  `ansible-playbook -i vyos.example.net, -u ansible -k -e ansible_network_os=vyos.vyos.vyos first_playbook.yml`

    The playbook contains one play with two tasks, and generates output similar to the following:

```
$ ansible-playbook -i vyos.example.net, -u ansible -k -e ansible_network_os=vyos.vyos.vyos first_playbook.yml

    PLAY [Network Getting Started First Playbook]
***************************************************************************************************************************

    TASK [Get config for VyOS devices]
***************************************************************************************************************************
ok: [vyos.example.net]

    TASK [Display the config]
***************************************************************************************************************************
ok: [vyos.example.net] => {
    "msg": "The hostname is vyos and the OS is VyOS 1.1.8"
}
```

2.  Now that you can retrieve the device configuration, you can try updating it with Ansible.
3.  Download `first_playbook_ext.yml` from [here](https://docs.ansible.com/projects/ansible/latest/_downloads/47cc11a5d29fe635cb56cb6e1cd74e0f/first_playbook_ext.yml), which is an extended version of the first playbook:
      The playbook looks like this:

```
---

    - name: Network Getting Started First Playbook Extended
  connection: ansible.netcommon.network_cli
  gather_facts: false
  hosts: all
  tasks:

    - name: Get config for VyOS devices
      vyos.vyos.vyos_facts:
        gather_subset: all

    - name: Display the config
      debug:
        msg: "The hostname is {{ ansible_net_hostname }} and the OS is {{ ansible_net_version }}"

    - name: Update the hostname
      vyos.vyos.vyos_config:
        backup: yes
        lines:
          - set system host-name vyos-changed

    - name: Get changed config for VyOS devices
      vyos.vyos.vyos_facts:
        gather_subset: all

    - name: Display the changed config
      debug:
        msg: "The new hostname is {{ ansible_net_hostname }} and the OS is {{ ansible_net_version }}"
```

4.  The extended first playbook has five tasks in a single play.
5.  Run the playbook with the following command.

```
$ ansible-playbook -i vyos.example.net, -u ansible -k -e ansible_network_os=vyos.vyos.vyos first_playbook_ext.yml
```

6.  The output shows you the change Ansible made to the configuration:
  

```
$ ansible-playbook -i vyos.example.net, -u ansible -k -e ansible_network_os=vyos.vyos.vyos first_playbook_ext.yml

    PLAY [Network Getting Started First Playbook Extended]
************************************************************************************************************************************

    TASK [Get config for VyOS devices]
**********************************************************************************************************************************
ok: [vyos.example.net]

    TASK [Display the config]
*************************************************************************************************************************************
ok: [vyos.example.net] => {
    "msg": "The hostname is vyos and the OS is VyOS 1.1.8"
}

    TASK [Update the hostname]
*************************************************************************************************************************************
changed: [vyos.example.net]

    TASK [Get changed config for VyOS devices]
*************************************************************************************************************************************
ok: [vyos.example.net]

    TASK [Display the changed config]
*************************************************************************************************************************************
ok: [vyos.example.net] => {
    "msg": "The new hostname is vyos-changed and the OS is VyOS 1.1.8"
}

    PLAY RECAP
************************************************************************************************************************************
vyos.example.net           : ok=5    changed=1    unreachable=0    failed=0
```

## Gather facts from network devices

The `gather_facts` keyword supports gathering network device facts in standardized key/value pairs. You can feed these network facts into further tasks to manage the network device.

You can also use the `gather_network_resources` parameter with the network `*_facts` modules (such as `arista.eos.eos_facts`) to return a subset of the device configuration, as the following example shows:

```
- hosts: arista
  gather_facts: True
  gather_subset: interfaces
  module_defaults:
    arista.eos.eos_facts:
      gather_network_resources: interfaces
```
The playbook returns the following interface facts:

```
"network_resources": {
      "interfaces": [
          {
              "description": "test-interface",
              "enabled": true,
              "mtu": "512",
              "name": "Ethernet1"
          },
          {
              "enabled": true,
              "mtu": "3000",
              "name": "Ethernet2"
          },
          {
              "enabled": true,
              "name": "Ethernet3"
          },
          {
              "enabled": true,
              "name": "Ethernet4"
          },
          {
              "enabled": true,
              "name": "Ethernet5"
          },
          {
              "enabled": true,
              "name": "Ethernet6"
          },
      ]
  }
```


Note:

`gather_network_resources` renders configuration data as facts for all supported resources (`` interfaces/bgp/ospf/etc` ``), whereas `gather_subset` is primarily used to fetch operational data.

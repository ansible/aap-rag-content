# 2. Use a playbook to establish a connection to a managed node
## 2.2. Running a network Ansible Playbook




If you want to run a particular command every day, you can save it in a playbook and run it with `ansible-playbook` instead of ansible.

The playbook can store many of the parameters you provided with flags at the command line, leaving less to type at the command line. You need two files for this, a playbook and an inventory file.

**Prerequisites**

Download `first_playbook.yml` from [here](https://docs.ansible.com/ansible/latest/_downloads/588d4b6e9316c8eb903fbe2485b14d64/first_playbook.yml) .


The playbook looks like this:

```
---

- name: Network Getting Started First Playbook
connection: ansible.netcommon.network_cli
gather_facts: false<span id="CO1-1"><!--Empty--></span><span class="callout">1</span>hosts: all
tasks:

- name: Get config for VyOS devices
vyos.vyos.vyos_facts:
gather_subset: all

- name: Display the config
debug:
msg: "The hostname is {{ ansible_net_hostname }} and the OS is {{ ansible_net_version }}"
```

| Label | Description |
| --- | --- |
|  `gather_facts` | Ansible’s native fact gathering ( `ansible.builtin.setup` ) is disabled here because the playbook relies on the facts provided by a platform-specific module ( `vyos.vyos.vyos_facts` ) in this networking collection. |


The playbook sets three of the seven values from the command line above:

- the group ( `    hosts: all` )
- the connection method ( `    connection: ansible.netcommon.network_cli` ) and
- the module (in each task).


With those values set in the playbook, you can omit them on the command line. The playbook also adds a second task to show the configuration output.

When facts are gathered from a system, either through a collection-specific fact module such as `vyos.vyos.vyos_facts` or `ansible.builtin.setup` , the gathered data is held in memory for use by future tasks instead of being written to the console.

When a module runs in a playbook, the output is held in memory for use by future tasks instead of written to the console. With most other modules you must explicitly register a variable to store and reuse the output of a module or task.

The following debug task lets you see the results in your shell.

**Procedure**

1. Run the playbook with the following command.

`    ansible-playbook -i vyos.example.net, -u ansible -k -e ansible_network_os=vyos.vyos.vyos first_playbook.yml`

The playbook contains one play with two tasks, and generates output similar to the following:


```
$ ansible-playbook -i vyos.example.net, -u ansible -k -e ansible_network_os=vyos.vyos.vyos first_playbook.yml        PLAY [Network Getting Started First Playbook]    ***************************************************************************************************************************        TASK [Get config for VyOS devices]    ***************************************************************************************************************************    ok: [vyos.example.net]        TASK [Display the config]    ***************************************************************************************************************************    ok: [vyos.example.net] =&gt; {        "msg": "The hostname is vyos and the OS is VyOS 1.1.8"    }
```


1. Now that you can retrieve the device configuration, you can try updating it with Ansible.
1. Download `    first_playbook_ext.yml` from [here](https://docs.ansible.com/ansible/latest/_downloads/47cc11a5d29fe635cb56cb6e1cd74e0f/first_playbook_ext.yml) , which is an extended version of the first playbook:

The playbook looks like this:


```
---        - name: Network Getting Started First Playbook Extended      connection: ansible.netcommon.network_cli      gather_facts: false      hosts: all      tasks:            - name: Get config for VyOS devices          vyos.vyos.vyos_facts:            gather_subset: all            - name: Display the config          debug:            msg: "The hostname is {{ ansible_net_hostname }} and the OS is {{ ansible_net_version }}"            - name: Update the hostname          vyos.vyos.vyos_config:            backup: yes            lines:              - set system host-name vyos-changed            - name: Get changed config for VyOS devices          vyos.vyos.vyos_facts:            gather_subset: all            - name: Display the changed config          debug:            msg: "The new hostname is {{ ansible_net_hostname }} and the OS is {{ ansible_net_version }}"
```


1. The extended first playbook has five tasks in a single play.
1. Run the playbook with the following command.


```
$ ansible-playbook -i vyos.example.net, -u ansible -k -e ansible_network_os=vyos.vyos.vyos first_playbook_ext.yml
```


1. The output shows you the change Ansible made to the configuration:


```
$ ansible-playbook -i vyos.example.net, -u ansible -k -e ansible_network_os=vyos.vyos.vyos first_playbook_ext.yml        PLAY [Network Getting Started First Playbook Extended]    ************************************************************************************************************************************        TASK [Get config for VyOS devices]    **********************************************************************************************************************************    ok: [vyos.example.net]        TASK [Display the config]    *************************************************************************************************************************************    ok: [vyos.example.net] =&gt; {        "msg": "The hostname is vyos and the OS is VyOS 1.1.8"    }        TASK [Update the hostname]    *************************************************************************************************************************************    changed: [vyos.example.net]        TASK [Get changed config for VyOS devices]    *************************************************************************************************************************************    ok: [vyos.example.net]        TASK [Display the changed config]    *************************************************************************************************************************************    ok: [vyos.example.net] =&gt; {        "msg": "The new hostname is vyos-changed and the OS is VyOS 1.1.8"    }        PLAY RECAP    ************************************************************************************************************************************    vyos.example.net           : ok=5    changed=1    unreachable=0    failed=0
```





# 1. Introduction
## 1.4. Building an inventory




Inventories organize managed nodes in centralized files that provide Ansible with system information and network locations. Using an inventory file, Ansible can manage a large number of hosts with a single command.

**Prerequisites**

- To complete the following steps, you need the IP address or fully qualified domain name (FQDN) of at least one host system. For demonstration purposes, the host could be running locally in a container or a virtual machine.
- You must also ensure that your public SSH key is added to the `    authorized_keys` file on each host. Use the following procedure to build an inventory.


**Procedure**

1. Create a file named `    inventory.ini` in the `    ansible_quickstart` directory that you created.
1. Add a new `    [myhosts]` group to the inventory.ini file and specify the IP address or fully qualified domain name (FQDN) of each host system.


```
[myhosts]    192.0.2.50    192.0.2.51    192.0.2.52
```


1. Verify your inventory, using:

`    ansible-inventory -i inventory.ini --list`


1. Ping the `    myhosts` group in your inventory, using:

'ansible myhosts -m ping -i inventory.ini`

Pass the `    -u` option with the Ansible command if the username is different on the control node and the managed node(s).


```
192.0.2.50 | SUCCESS =&gt; {        "ansible_facts": {            "discovered_interpreter_python": "/usr/bin/python3"        },        "changed": false,        "ping": "pong"    }    192.0.2.51 | SUCCESS =&gt; {        "ansible_facts": {            "discovered_interpreter_python": "/usr/bin/python3"        },        "changed": false,        "ping": "pong"    }    192.0.2.52 | SUCCESS =&gt; {        "ansible_facts": {            "discovered_interpreter_python": "/usr/bin/python3"        },        "changed": false,        "ping": "pong"    }
```

You have successfully built an inventory.





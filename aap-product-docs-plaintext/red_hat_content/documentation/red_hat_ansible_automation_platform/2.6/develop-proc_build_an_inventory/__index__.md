# Define which hosts to manage in an inventory file

Inventories organize managed nodes in centralized files that provide Ansible with system information and network locations. Using an inventory file, Ansible can manage a large number of hosts with a single command.

## Before you begin

- To complete the following steps, you need the IP address or fully qualified domain name (FQDN) of at least one host system. For demonstration purposes, the host could be running locally in a container or a virtual machine.
- You must also ensure that your public SSH key is added to the `authorized_keys` file on each host. Use the following procedure to build an inventory.

## Procedure

1.  Create a file named `inventory.ini` in the `ansible_quickstart` directory that you created.
2.  Add a new `[myhosts]` group to the inventory.ini file and specify the IP address or fully qualified domain name (FQDN) of each host system.

```
[myhosts]
192.0.2.50
192.0.2.51
192.0.2.52
```

3.  Verify your inventory, using:
`ansible-inventory -i inventory.ini --list`

4.  Ping the `myhosts` group in your inventory, using:
'ansible myhosts -m ping -i inventory.ini`

Pass the `-u` option with the Ansible command if the username is different on the control node and the managed node(s).

```
192.0.2.50 | SUCCESS => {
"ansible_facts": {
"discovered_interpreter_python": "/usr/bin/python3"
},
"changed": false,
"ping": "pong"
}
192.0.2.51 | SUCCESS => {
"ansible_facts": {
"discovered_interpreter_python": "/usr/bin/python3"
},
"changed": false,
"ping": "pong"
}
192.0.2.52 | SUCCESS => {
"ansible_facts": {
"discovered_interpreter_python": "/usr/bin/python3"
},
"changed": false,
"ping": "pong"
}
```
You have successfully built an inventory.

## Inventories in INI or YAML format

You can create inventories by using either INI files or in YAML. In most cases, such as the preceding example, INI files are straightforward and easy to read for a small number of managed nodes. Creating an inventory in YAML format becomes a sensible option as the number of managed nodes increases.

The following is the same as `inventory.ini` that declares unique names for managed nodes and uses the `ansible_host` field:

```
myhosts:
hosts:
my_host_01:
ansible_host: 192.0.2.50
my_host_02:
ansible_host: 192.0.2.51
my_host_03:
ansible_host: 192.0.2.52
```

## Tips for building inventories

When building inventories for Ansible automation, consider the following best practices to ensure efficient and effective management of your hosts.

- Ensure that group names are meaningful and unique.
- Group names are also case sensitive.
- Do not use spaces, hyphens, or preceding numbers (use `floor_19`, not `19th_floor`) in group names.
- Group hosts in your inventory logically according to their What, Where, and When:
* What: Group hosts according to the topology, for example: db, web, leaf, spine.
* Where: Group hosts by geographic location, for example: data center, region, floor, building.
* When: Group hosts by stage, for example: development, test, staging, production.

## Use metagroups

Organize your inventory by using metagroups to group multiple groups together.

Create a metagroup that organizes multiple groups in your inventory with the following syntax:

```
metagroupname:
children:
```
The following inventory illustrates a basic structure for a data center. This example inventory has a network metagroup that includes all network devices and a data center metagroup that includes the network group and all webservers.

```
leafs:
hosts:
leaf01:
ansible_host: 192.0.2.100
leaf02:
ansible_host: 192.0.2.110

spines:
hosts:
spine01:
ansible_host: 192.0.2.120
spine02:
ansible_host: 192.0.2.130

network:
children:
leafs:
spines:

webservers:
hosts:
webserver01:
ansible_host: 192.0.2.140
webserver02:
ansible_host: 192.0.2.150

datacenter:
children:
network:
webservers:
```

## Create inventory file variables to set values for managed nodes

Variables set values for managed nodes, such as the IP address, FQDN, operating system, and SSH user, so you do not need to pass them when running Ansible commands.

Variables can apply to specific hosts.

```
webservers:
hosts:
webserver01:
ansible_host: 192.0.2.140
http_port: 80
webserver02:
ansible_host: 192.0.2.150
http_port: 443
```
Variables can also apply to all hosts in a group.

```
webservers:
hosts:
webserver01:
ansible_host: 192.0.2.140
http_port: 80
webserver02:
ansible_host: 192.0.2.150
http_port: 443
vars:
ansible_user: my_server_user
```
For more information about inventories and Ansible inventory variables, see [About the Installer Inventory file](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/planning_your_installation/about_the_installer_inventory_file) and [Inventory file variables](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/rpm_installation/appendix-inventory-files-vars).

# Determine where automation runs with instance groups
## Define instance groups in the inventory file

Define custom instance groups in the inventory file to organize nodes in your automation mesh. By correctly assigning nodes to the `automationcontroller` or `execution_nodes` groups, you ensure the installer validates the mesh topology and prevents configuration errors.

Use the following criteria when defining nodes:

- Nodes in the `automationcontroller` group can define `node_type` hostvar to be `hybrid` (default) or `control`.
- Nodes in the `execution_nodes group` can define `node_type` hostvar to be `execution` (default) or `hop`.


You can define custom groups in the inventory file by naming groups with `instance_group_*` where `*` becomes the name of the group in the API. You can also create custom instance groups in the API after the install has finished.

The current behavior expects a member of an `instance_group_*` to be part of `automationcontroller` or `execution_nodes` group.

### Define instance groups

```
[automationcontroller]
126-addr.tatu.home ansible_host=192.168.111.126  node_type=control

[automationcontroller:vars]
peers=execution_nodes

[execution_nodes]

[instance_group_test]
110-addr.tatu.home ansible_host=192.168.111.110 receptor_listener_port=8928
```

After you run the installation program, the following error is displayed:

```
TASK [ansible.automation_platform_installer.check_config_static : Validate mesh topology] ***
fatal: [126-addr.tatu.home -> localhost]: FAILED! => {"msg": "The host '110-addr.tatu.home' is not present in either [automationcontroller] or [execution_nodes]"}
```
To fix this, move the box `110-addr.tatu.home` to an `execution_node` group, as follows:

```
[automationcontroller]
126-addr.tatu.home ansible_host=192.168.111.126  node_type=control

[automationcontroller:vars]
peers=execution_nodes

[execution_nodes]
110-addr.tatu.home ansible_host=192.168.111.110 receptor_listener_port=8928

[instance_group_test]
110-addr.tatu.home
```
This results in:

```
TASK [ansible.automation_platform_installer.check_config_static : Validate mesh topology] ***
ok: [126-addr.tatu.home -> localhost] => {"changed": false, "mesh": {"110-addr.tatu.home": {"node_type": "execution", "peers": [], "receptor_control_filename": "receptor.sock", "receptor_control_service_name": "control", "receptor_listener": true, "receptor_listener_port": 8928, "receptor_listener_protocol": "tcp", "receptor_log_level": "info"}, "126-addr.tatu.home": {"node_type": "control", "peers": ["110-addr.tatu.home"], "receptor_control_filename": "receptor.sock", "receptor_control_service_name": "control", "receptor_listener": false, "receptor_listener_port": 27199, "receptor_listener_protocol": "tcp", "receptor_log_level": "info"}}}
```
After upgrading from automation controller 4.0 or earlier, the legacy `instance_group_` member likely has the awx code installed. This places that node in the `automationcontroller` group.

# 4. Deprovisioning individual nodes or groups
## 4.1. Deprovisioning individual nodes using the installer




You can deprovision nodes from your automation mesh using the Ansible Automation Platform installer. Edit the `inventory` file to mark the nodes to deprovision, then run the installer. Running the installer also removes all configuration files and logs attached to the node.

Note
You can deprovision any of your inventory’s hosts except for the first host specified in the `[automationcontroller]` group.



**Procedure**

- Append `    <span class="strong strong"><strong><span class="Role ARG Spec Role ARG Spec">node_state=deprovision</span></strong></span>` to nodes in the installer file you want to deprovision.

The following example inventory file deprovisions two nodes from an automation mesh configuration.





<span id="idm140468920797184"></span>
**Example 4.1. Deprovision nodes**

```
[automationcontroller]
126-addr.tatu.home ansible_host=192.168.111.126  node_type=control
121-addr.tatu.home ansible_host=192.168.111.121  node_type=hybrid  routable_hostname=121-addr.tatu.home
115-addr.tatu.home ansible_host=192.168.111.115  node_type=hybrid node_state=deprovision

[automationcontroller:vars]
peers=connected_nodes

[execution_nodes]
110-addr.tatu.home ansible_host=192.168.111.110 receptor_listener_port=8928
108-addr.tatu.home ansible_host=192.168.111.108 receptor_listener_port=29182 node_state=deprovision
100-addr.tatu.home ansible_host=192.168.111.100 peers=110-addr.tatu.home node_type=hop
```





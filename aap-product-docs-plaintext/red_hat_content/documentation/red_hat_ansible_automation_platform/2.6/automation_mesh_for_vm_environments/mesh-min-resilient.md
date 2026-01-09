# 3. Automation mesh design patterns
## 3.2. Minimum resilient configuration




This example inventory file deploys a control plane consisting of two control nodes, and two execution nodes. All nodes in the control plane are automatically peered to one another. All nodes in the control plane are peered with all nodes in the `execution_nodes` group. This configuration is resilient because the execution nodes are reachable from all control nodes.

The capacity algorithm determines which control node is chosen when a job is launched. Refer to [Automation controller capacity determination and job impact](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/using_automation_execution/index#controller-capacity-determination) in Configuring automation execution for more information.

The following inventory file defines this configuration.

```
[automationcontroller]
aap_c_1.example.com
aap_c_2.example.com

[automationcontroller:vars]
node_type=control
peers=execution_nodes

[execution_nodes]
aap_e_1.example.com
aap_e_2.example.com
```

The `[automationcontroller]` stanza defines the control nodes. All nodes in the control plane are peered to one another. If you add a new node to the `automationcontroller` group, it will automatically peer with the original nodes.

The `[automationcontroller:vars]` stanza sets the node type to `control` for all nodes in the control plane and defines how the nodes peer to the execution nodes:

- If you add a new node to the `    execution_nodes` group, the control plane nodes automatically peer to it.
- If you add a new node to the `    automationcontroller` group, the node type is set to `    control` .


The following image displays the topology of this mesh network.

![The topology map of the minimum resilient mesh configuration consists of an automation controller group and two execution nodes. The automation controller group consists of two control nodes: aap_c_1 and aap_c_2. The execution nodes are aap_e_1 and aap_e_2. The aap_c_1 node is peered to aap_c_2. Every control node is peered to every execution node.](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.6-Automation_mesh_for_VM_environments-en-US/images/b800add8dd490e70a25dad03aa337a9c/mesh-resilient-config.png)



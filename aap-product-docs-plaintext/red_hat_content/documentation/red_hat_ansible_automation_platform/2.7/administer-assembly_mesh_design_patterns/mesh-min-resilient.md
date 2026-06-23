# Design patterns for mesh
## Minimum resilient configuration

This inventory deploys a control plane with two control nodes and two execution nodes. All control nodes peer automatically. Because each control node connects to every node in the **execution_nodes** group, the configuration is resilient.

The capacity algorithm determines which control node is chosen when a job is launched. Refer to [Automation controller capacity determination and job impact](/documentation/en-us/red_hat_ansible_automation_platform/2.7/optimize-con_controller_capacity_determination#controller-capacity-determination "The automation controller capacity system determines how many jobs can run on an instance given the amount of resources available to the instance and the size of the jobs that are running (referred to as Impact). The algorithm used to determine this is based on the following two things:") in Configuring automation execution for more information.

The following inventory file defines this configuration.

```yaml
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

- If you add a new node to the `execution_nodes` group, the control plane nodes automatically peer to it.
- If you add a new node to the `automationcontroller` group, the node type is set to `control`.


The following image displays the topology of this mesh network.


![The topology map of the minimum resilient mesh configuration consists of an automation controller group and two execution nodes. The automation controller group consists of two control nodes: aap_c_1 and aap_c_2. The execution nodes are aap_e_1 and aap_e_2. The aap_c_1 node is peered to aap_c_2. Every control node is peered to every execution node.](/webassets/aem/red_hat_ansible_automation_platform/2.7/images/mesh-resilient-config.png)


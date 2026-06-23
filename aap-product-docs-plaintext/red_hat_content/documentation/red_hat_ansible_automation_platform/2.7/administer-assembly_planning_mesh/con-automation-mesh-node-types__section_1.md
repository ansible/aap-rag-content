# Scale automation across your infrastructure with automation mesh
## Control and execution planes
### Peers

Peer relationships are essential for defining the node-to-node connections that form the automation mesh. The method for defining peers depends on your specific deployment model:

For VM environment mesh deployments
You can define peers within the `[automationcontroller]` and `[execution_nodes]` groups or using the `[automationcontroller:vars]` or `[execution_nodes:vars]` groups

**For managed cloud or operator environment mesh deployments**
Peers are defined through the UI for individual instances.


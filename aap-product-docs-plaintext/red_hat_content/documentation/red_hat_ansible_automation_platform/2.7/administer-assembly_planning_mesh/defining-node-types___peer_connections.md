# Scale automation across your infrastructure with automation mesh
## Define automation mesh node types
### Peer connections

Important:

For a container-based installation of Ansible Automation Platform, use the `receptor_peers=` variable instead of `peers=`.

The value of `receptor_peers` must be a comma-separated list of hostnames. Do not use inventory group names. For more information, see [Adding execution nodes](/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-ref_adding_execution_nodes "Containerized Ansible Automation Platform can deploy remote execution nodes.").

Create node-to-node connections using the `peers=` host variable. The following example connects `control-plane-1.example.com` to `execution-node-1.example.com` and `execution-node-1.example.com` to `execution-node-2.example.com`:

```
[automationcontroller]
control-plane-1.example.com peers=execution-node-1.example.com

[automationcontroller:vars]
node_type=control

[execution_nodes]
execution-node-1.example.com peers=execution-node-2.example.com
execution-node-2.example.com
```
See the example automation mesh topologies in this section for more examples of how to implement mesh nodes.

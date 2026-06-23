# Scale automation across your infrastructure with automation mesh
## Define automation mesh node types

The examples in this section demonstrate how to set the node type for the hosts in your inventory file.

Important:

For a container-based installation of Ansible Automation Platform, replace `node_type` with `receptor_type`.

You can set the `node_type` for single nodes in the control plane or execution plane inventory groups. To define the node type for an entire group of nodes, set the `node_type` in the `vars` stanza for the group.

- The permitted values for `node_type` in the control plane `[automationcontroller]` group are `hybrid` (default) and `control`.
- The permitted values for `node_type` in the `[execution_nodes]` group are `execution` (default) and `hop`.


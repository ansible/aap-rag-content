# Scale automation across your infrastructure with automation mesh

Learn how to plan an automation mesh deployment in your Ansible Automation Platform environment.

The subsequent sections:

- Explain the concepts that comprise automation mesh
- Provide examples on how you can design automation mesh topologies
- Include simple to complex topology examples that illustrate the various ways you can deploy automation mesh
- Contain information to help plan an automation mesh deployment in your operator-based Red Hat Ansible Automation Platform environment
- Covers the setting up of automation mesh on operator-based deployments, such as OpenShift Container Platform and Ansible Automation Platform on Amazon Web Services (AWS) and Microsoft Azure managed applications.

## About automation mesh

Automation mesh is an overlay network intended to ease the distribution of work across a large and dispersed collection of workers through nodes that establish peer-to-peer connections with each other using existing networks.

Red Hat Ansible Automation Platform 2 replaces Ansible Tower and isolated nodes with Ansible Automation Platform and automation hub. Ansible Automation Platform provides the control plane for automation through its UI, RESTful API, RBAC, workflows and CI/CD integration, while automation mesh can be used for setting up, discovering, changing or modifying the nodes that form the control and execution layers.

Automation mesh is useful for:

- traversing difficult network topologies
- bringing execution capabilities (the machine running `ansible-playbook`) closer to your target hosts


The nodes (control, hop, and execution instances) are interconnected through a receptor mesh, forming a virtual mesh.

Automation mesh uses TLS encryption for communication, so traffic that traverses external networks (the internet or other) is encrypted in transit.

Automation mesh introduces:

- Dynamic cluster capacity that scales independently, enabling you to create, register, group, ungroup and deregister nodes with minimal downtime.
- Control and execution plane separation that enables you to scale playbook execution capacity independently from control plane capacity.
- Deployment choices that are resilient to latency, reconfigurable without outage, and that dynamically re-reroute to choose a different path when outages occur.
- Connectivity that includes bi-directional, multi-hopped mesh communication possibilities which are *Federal Information Processing Standards* (FIPS) compliant.

## Control and execution planes

Automation mesh makes use of unique node types to create both the **control** and **execution** plane. Learn more about the control and execution plane and their node types before designing your automation mesh topology.

### Control plane

The control plane contains the persistent services that manage and scale your automation environment. The specific set up of the control plane depends on your deployment model:

For VM environment mesh deployments
The **control plane** consists of hybrid and control nodes. Instances in the control plane run persistent automation controller services such as the the web server and task dispatcher, in addition to project updates, and management jobs.

Hybrid nodes
This is the default node type for control plane nodes, responsible for automation controller runtime functions like project updates, management jobs and `ansible-runner` task operations. Hybrid nodes are also used for automation execution.

Control nodes
Control nodes run project and inventory updates and system jobs, but not regular jobs. Execution capabilities are disabled on these nodes.

**For managed cloud or operator environment mesh deployments**
Instances in the control plane run persistent Ansible Automation Platform services such as the web server and task dispatcher, in addition to project updates, and management jobs. However, in the operator-based model, there are no hybrid or control nodes. There are container groups, which make up containers running on the Kubernetes cluster. That comprises the control plane. That control plane is local to the kubernetes cluster in which Red Hat Ansible Automation Platform is deployed.

### Execution plane

The **execution plane** consists of execution nodes that execute automation on behalf of the control plane and have no control functions. Hop nodes serve to communicate. Nodes in the **execution plane** only run user-space jobs, and may be geographically separated, with high latency, from the control plane.

Execution notes
Execution nodes run jobs under `ansible-runner` with `podman` isolation. This node type is similar to isolated nodes. This is the default node type for execution plane nodes.

Hop nodes
Similar to a jump host, hop nodes route traffic to other execution nodes. Hop nodes cannot execute automation.

### Peers

Peer relationships are essential for defining the node-to-node connections that form the automation mesh. The method for defining peers depends on your specific deployment model:

For VM environment mesh deployments
You can define peers within the `[automationcontroller]` and `[execution_nodes]` groups or using the `[automationcontroller:vars]` or `[execution_nodes:vars]` groups

**For managed cloud or operator environment mesh deployments**
Peers are defined through the UI for individual instances.

## Define automation mesh node types

The examples in this section demonstrate how to set the node type for the hosts in your inventory file.

Important:

For a container-based installation of Ansible Automation Platform, replace `node_type` with `receptor_type`.

You can set the `node_type` for single nodes in the control plane or execution plane inventory groups. To define the node type for an entire group of nodes, set the `node_type` in the `vars` stanza for the group.

- The permitted values for `node_type` in the control plane `[automationcontroller]` group are `hybrid` (default) and `control`.
- The permitted values for `node_type` in the `[execution_nodes]` group are `execution` (default) and `hop`.

### Hybrid nodes

The following inventory consists of a single hybrid node in the control plane:

```
[automationcontroller]
control-plane-1.example.com
```

### Control nodes

The following inventory consists of a single control node in the control plane:

```
[automationcontroller]
control-plane-1.example.com node_type=control
```
If you set `node_type` to `control` in the `vars` stanza for the control plane nodes, then all of the nodes in control plane are control nodes.

```
[automationcontroller]
control-plane-1.example.com

[automationcontroller:vars]
node_type=control
```

### Execution nodes

The following stanza defines a single execution node in the execution plane:

```
[execution_nodes]
execution-plane-1.example.com
```

### Hop nodes

The following stanza defines a single hop node and an execution node in the execution plane. The `node_type` variable is set for every individual node.

```
[execution_nodes]
execution-plane-1.example.com node_type=hop
execution-plane-2.example.com
```
If you want to set the `node_type` at the group level, you must create separate groups for the execution nodes and the hop nodes.

```
[execution_nodes]
execution-plane-1.example.com
execution-plane-2.example.com

[execution_group]
execution-plane-2.example.com

[execution_group:vars]
node_type=execution

[hop_group]
execution-plane-1.example.com

[hop_group:vars]
node_type=hop
```

### Peer connections

Important:

For a container-based installation of Ansible Automation Platform, use the `receptor_peers=` variable instead of `peers=`.

The value of `receptor_peers` must be a comma-separated list of hostnames. Do not use inventory group names. For more information, see [Adding execution nodes](/documentation/en-us/red_hat_ansible_automation_platform/2.6/install-ref_adding_execution_nodes "Containerized Ansible Automation Platform can deploy remote execution nodes.").

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

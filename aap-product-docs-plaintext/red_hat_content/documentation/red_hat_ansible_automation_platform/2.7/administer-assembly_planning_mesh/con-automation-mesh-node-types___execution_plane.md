# Scale automation across your infrastructure with automation mesh
## Control and execution planes
### Execution plane

The **execution plane** consists of execution nodes that execute automation on behalf of the control plane and have no control functions. Hop nodes serve to communicate. Nodes in the **execution plane** only run user-space jobs, and may be geographically separated, with high latency, from the control plane.

Execution notes
Execution nodes run jobs under `ansible-runner` with `podman` isolation. This node type is similar to isolated nodes. This is the default node type for execution plane nodes.

Hop nodes
Similar to a jump host, hop nodes route traffic to other execution nodes. Hop nodes cannot execute automation.


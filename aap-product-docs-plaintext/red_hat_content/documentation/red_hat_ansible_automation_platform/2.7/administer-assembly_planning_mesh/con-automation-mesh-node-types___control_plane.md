# Scale automation across your infrastructure with automation mesh
## Control and execution planes
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


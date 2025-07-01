# 1. Planning for automation mesh in your VM-based Red Hat Ansible Automation Platform environment
## 1.2. Control and execution planes
### 1.2.1. Control plane




The **control plane** consists of hybrid and control nodes. Instances in the control plane run persistent automation controller services such as the the web server and task dispatcher, in addition to project updates, and management jobs.

-  **Hybrid nodes** - this is the default node type for control plane nodes, responsible for automation controller runtime functions like project updates, management jobs and `    ansible-runner` task operations. Hybrid nodes are also used for automation execution.
-  **Control nodes** - control nodes run project and inventory updates and system jobs, but not regular jobs. Execution capabilities are disabled on these nodes.



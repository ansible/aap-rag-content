# 1. Key functionality and concepts
## 1.5. Automation mesh




Automation mesh is an overlay network intended to ease the distribution of automation across a collection of execution nodes using existing connectivity. Execution nodes are where [Ansible Playbooks](https://www.redhat.com/en/topics/automation/what-is-an-ansible-playbook) are actually executed. A node runs an automation execution environment which, in turn, runs the Ansible Playbook. Automation mesh creates peer-to-peer connections between these execution nodes, increasing the resiliency of your automation workloads to network latency and connection disruptions. This also permits more flexible architectures and provides rapid, independent scaling of control and execution capacity.


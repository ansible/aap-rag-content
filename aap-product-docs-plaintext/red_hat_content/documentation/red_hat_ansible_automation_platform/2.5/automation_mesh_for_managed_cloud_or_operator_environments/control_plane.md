# 1. Planning for automation mesh in your operator-based Red Hat Ansible Automation Platform environment
## 1.2. Control and execution planes
### 1.2.1. Control plane




Instances in the control plane run persistent Ansible Automation Platform services such as the web server and task dispatcher, in addition to project updates, and management jobs. However, in the operator-based model, there are no hybrid or control nodes. There are container groups, which make up containers running on the Kubernetes cluster. That comprises the control plane. That control plane is local to the kubernetes cluster in which Red Hat Ansible Automation Platform is deployed.


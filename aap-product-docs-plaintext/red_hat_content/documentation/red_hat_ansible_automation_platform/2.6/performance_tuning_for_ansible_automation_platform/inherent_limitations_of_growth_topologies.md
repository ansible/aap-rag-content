# 2. Scaling the tested deployment models
## 2.4. Motivations for migrating to an enterprise topology
### 2.4.1. Inherent limitations of growth topologies




Growth topologies include single points of failure, such as a single platform gateway , and other critical components, such as the control plane, execution plane, and web services. These components often share resources on the same node, resulting in resource contention under increasing load. As workloads grow, specific services, such as job processing or API responsiveness, can become bottlenecks due to colocation or single node capacity limits. Consequently, growth topologies generally do not offer robust, high-availability capabilities. For VM-based installation and containerized deployments of Ansible Automation Platform, you can marginally increase possible workloads by vertically scaling the virtual machines or physical hosts within the growth deployment. However, vertical scaling capabilities within a growth topology are limited.


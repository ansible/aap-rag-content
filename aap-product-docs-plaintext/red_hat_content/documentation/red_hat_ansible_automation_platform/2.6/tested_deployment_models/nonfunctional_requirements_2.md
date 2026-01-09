# 3. Operator topologies
## 3.2. Operator enterprise topology
### 3.2.4. Nonfunctional requirements




Ansible Automation Platform’s performance characteristics and capacity depend on its resource allocation and configuration. With OpenShift, each Ansible Automation Platform component deploys as a pod. You can specify resource requests and limits for each pod.

Use the Ansible Automation Platform custom resource to configure resource allocation for OpenShift installations. Each configurable item has default settings. These settings are the exact configuration used in this reference deployment architecture. This configuration assumes deployment and management by an Enterprise IT organization for production purposes.

By default, each component’s deployments use minimum resource requests but no resource limits. OpenShift only schedules pods with available resource requests. However, pods can consume unlimited RAM or CPU as long as the OpenShift worker node is not under node pressure.

In the Operator enterprise topology, Ansible Automation Platform runs on a Red Hat OpenShift on AWS (ROSA) Hosted Control Plane (HCP) cluster. The cluster has 2 t3.xlarge worker nodes spread across 2 AWS availability zones within a single region. This is not a shared environment so Ansible Automation Platform pods have full access to all compute resources of the ROSA HCP cluster.

The capacity calculation for automation controller task pods comes from the underlying HCP worker node running the pod. It does not have access to the CPU or memory resources of the entire node. This capacity calculation influences how many concurrent jobs automation controller can run.

OpenShift manages storage distinctly from VMs. This impacts how automation hub stores its artifacts. In the Operator enterprise topology, automation hub uses S3 storage. automation hub requires `ReadWriteMany` type storage, which is not a default storage type in OpenShift.

This topology specifies externally provided Redis, PostgreSQL, and object storage for automation hub. This provides additional scalability and reliability features for the Ansible Automation Platform deployment. These features include specialized backup, restore, and replication services, as well as scalable storage.


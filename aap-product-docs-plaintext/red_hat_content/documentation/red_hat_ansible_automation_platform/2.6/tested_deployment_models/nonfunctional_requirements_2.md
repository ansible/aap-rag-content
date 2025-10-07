# 3. Operator topologies
## 3.2. Operator enterprise topology
### 3.2.4. Nonfunctional requirements




Ansible Automation Platform’s performance characteristics and capacity are impacted by its resource allocation and configuration. With OpenShift, each Ansible Automation Platform component is deployed as a pod. You can specify resource requests and limits for each pod.

Use the Ansible Automation Platform custom resource to configure resource allocation for OpenShift installations. Each configurable item has default settings. These settings are the exact configuration used within the context of this reference deployment architecture and presumes that the environment is being deployed and managed by an Enterprise IT organization for production purposes.

By default, each component’s deployments are set for minimum resource requests but no resource limits. OpenShift only schedules the pods with available resource requests, but the pods are allowed to consume unlimited RAM or CPU provided that the OpenShift worker node itself is not under node pressure.

In the Operator enterprise topology, Ansible Automation Platform is deployed on a Red Hat OpenShift on AWS (ROSA) Hosted Control Plane (HCP) cluster with 2 t3.xlarge worker nodes spread across 2 AZs within a single AWS Region. This is not a shared environment, so Ansible Automation Platform pods have full access to all of the compute resources of the ROSA HCP cluster. In this scenario, the capacity calculation for the automation controller task pods is derived from the underlying HCP worker node that runs the pod. It does not have access to the CPU or memory resources of the entire node. This capacity calculation influences how many concurrent jobs automation controller can run.

OpenShift manages storage distinctly from VMs. This impacts how automation hub stores its artifacts. In the Operator enterprise topology, we use S3 storage because automation hub requires a `ReadWriteMany` type storage, which is not a default storage type in OpenShift. Externally provided Redis, PostgreSQL, and object storage for automation hub are specified. This provides the Ansible Automation Platform deployment with additional scalability and reliability features, including specialized backup, restore, and replication services and scalable storage.


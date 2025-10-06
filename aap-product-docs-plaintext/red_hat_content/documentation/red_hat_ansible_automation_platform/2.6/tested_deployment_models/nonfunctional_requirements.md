# 3. Operator topologies
## 3.1. Operator growth topology
### 3.1.4. Nonfunctional requirements




Ansible Automation Platform’s performance characteristics and capacity are impacted by its resource allocation and configuration. With OpenShift, each Ansible Automation Platform component is deployed as a pod. You can specify resource requests and limits for each pod.

Use the Ansible Automation Platform Custom Resource (CR) to configure resource allocation for OpenShift installations. Each configurable item has default settings. These settings are the minimum requirements for an installation, but might not meet your production workload needs.

By default, each component’s deployments are set for minimum resource requests but no resource limits. OpenShift only schedules the pods with available resource requests, but the pods are allowed to consume unlimited RAM or CPU provided that the OpenShift worker node itself is not under node pressure.

In the Operator growth topology, Ansible Automation Platform is deployed on a Single Node OpenShift (SNO) with 32 GB RAM, 16 CPUs, 128 GB Local disk, and 3000 IOPS. This is not a shared environment, so Ansible Automation Platform pods have full access to all of the compute resources of the OpenShift SNO. In this scenario, the capacity calculation for the automation controller task pods is derived from the underlying OpenShift Container Platform node that runs the pod. It does not have access to the entire node. This capacity calculation influences how many concurrent jobs automation controller can run.

OpenShift manages storage distinctly from VMs. This impacts how automation hub stores its artifacts. In the Operator growth topology, we use S3 storage because automation hub requires a `ReadWriteMany` type storage, which is not a default storage type in OpenShift.


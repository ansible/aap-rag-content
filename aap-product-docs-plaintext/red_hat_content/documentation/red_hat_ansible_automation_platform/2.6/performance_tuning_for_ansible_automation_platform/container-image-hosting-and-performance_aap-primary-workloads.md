# 1. Types of workloads
## 1.6. Container image hosting and performance




Private automation hub has the capability to host container images for automation execution environments and decision environments. Event-Driven Ansible or automation controller can pull these container images when running activations or jobs. The frequency of job starts and the pull policy configured for the automation execution environments and decision environments in Event-Driven Ansible or automation controller determine how often they pull these containers.

The performance of pushing and pulling container images from automation hub depends on the disk performance of the underlying storage. This is because Pulp content workers store and fetch the layers of the container image from disk. The size of layers can impact the memory used by the pulp workers, because they serve entire layers in a single operation. The pull policy on jobs and activations, the frequency of job or activation starts, and the node or Container Group’s existing image status determine the frequency of container image pulls.


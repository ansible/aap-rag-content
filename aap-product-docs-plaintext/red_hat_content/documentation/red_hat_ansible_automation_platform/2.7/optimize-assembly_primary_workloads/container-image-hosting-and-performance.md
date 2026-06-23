# Understand primary workloads for automation controller
## Pull hosted container images from private automation hub

Private automation hub hosts container images for automation execution and decision environments. Event-Driven Ansible and automation controller pull these images to run activations or jobs. The pull frequency for these containers is determined by the following:

- The frequency of job starts
- The pull policy configured for the automation execution environments and decision environments


The performance of pushing and pulling container images from automation hub depends on the disk performance of the underlying storage. This is because Pulp content workers store and fetch the layers of the container image from disk.

The size of layers can impact the memory used by the Pulp content workers. This is because they serve entire layers in a single operation.

The frequency of container image pulls is determined by the following factors:

- The pull policy on jobs and activations
- The frequency of job or activation starts
- The node or Container Group’s existing image status


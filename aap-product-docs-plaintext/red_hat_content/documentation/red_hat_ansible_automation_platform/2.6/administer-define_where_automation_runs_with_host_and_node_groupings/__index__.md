# Define where automation runs with host and node groupings

Managing hosts and controlling where automation jobs run ensures efficient resource utilization and proper workload distribution across your infrastructure. Define which systems to manage and organize execution capacity to align with your operational requirements.

Defining where automation runs helps you to:

- **Target the right systems**: Organize hosts into inventories to define which systems to manage and ensure automation runs against the correct infrastructure components.
- **Control where jobs run**: Group instances into instance groups and assign them to resources to control where jobs run and manage capacity.
- **Optimize resource allocation**: Balance automation workloads across available capacity by configuring how instance groups distribute jobs.

## How Ansible Automation Platform supports host and node groupings

Ansible Automation Platform uses two grouping mechanisms:

- **Hosts and inventories** define which systems you want to manage. A host is a system managed by Ansible Automation Platform. It can be a physical server, a virtual machine, a cloud-based server, or another device. Group hosts in inventories and use patterns to select which hosts or groups to target when running automation.
- **Instance groups** organize instances together to control where automation jobs run. Assign instance groups to organizations, inventories, or job templates. When you launch a job, the platform checks for instance groups associated with the job template, then the inventory, then the organization in that order. The platform then runs the job on the instance group with available capacity.

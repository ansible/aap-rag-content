# Define where automation runs with host and node groupings
## How Ansible Automation Platform supports host and node groupings

Ansible Automation Platform uses two grouping mechanisms:

- **Hosts and inventories** define which systems you want to manage. A host is a system managed by Ansible Automation Platform. It can be a physical server, a virtual machine, a cloud-based server, or another device. Group hosts in inventories and use patterns to select which hosts or groups to target when running automation.
- **Instance groups** organize instances together to control where automation jobs run. Assign instance groups to organizations, inventories, or job templates. When you launch a job, the platform checks for instance groups associated with the job template, then the inventory, then the organization in that order. The platform then runs the job on the instance group with available capacity.

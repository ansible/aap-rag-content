# System requirements

Use this information when planning your Red Hat Ansible Automation Platform installations and designing automation mesh topologies that fit your use case.

## Prerequisites

- Obtain root access either through the `sudo` command, or through privilege escalation.   * De-escalate privileges from root to users such as: AWX, PostgreSQL, Event-Driven Ansible, or Pulp.
- Configured an NTP client on all nodes.

## Red Hat Ansible Automation Platform system requirements

Your system must meet the following minimum system requirements to install and run Red Hat Ansible Automation Platform.

A resilient deployment requires 10 virtual machines with a minimum of 16 gigabytes (GB) of RAM and 4 virtual CPUs (vCPU). See [Choose a deployment method and topology](/documentation/en-us/red_hat_ansible_automation_platform/2.6/plan-assembly_overview_tested_deployment_models "Red Hat tests Ansible Automation Platform with a defined set of topologies to give you opinionated deployment options. Deploy all components of Ansible Automation Platform so that all features and capabilities are available for use without the need to take further action.") for more information on topology options.

*Table 1. Base system*

| Type                 | Description                                                                                                                            | Notes                                                                                                                                                                                                                                                                                                                                                                                                                     |
| -------------------- | -------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <br>Subscription     | <br>Valid Red Hat Ansible Automation Platform subscription                                                                             |                                                                                                                                                                                                                                                                                                                                                                                                                           |
| <br>Operating system | Red Hat Enterprise Linux 9.6 or later minor versions of Red Hat Enterprise Linux 9                                                     | <br>Red Hat Ansible Automation Platform are also supported on OpenShift, see [Installing on OpenShift Container Platform](/documentation/en-us/red_hat_ansible_automation_platform/2.6/install-assembly_operator_install_operator "As a system administrator, you can use Ansible Automation Platform Operator to deploy new Ansible Automation Platform instances in your OpenShift environment.") for more information. |
| <br>CPU architecture | <br>x86\_64, AArch64, s390x (IBM Z), ppc64le (IBM Power)                                                                               |                                                                                                                                                                                                                                                                                                                                                                                                                           |
| <br>Ansible-core     | <br>Ansible-core version 2.16 or later                                                                                                 | <br>Ansible Automation Platform uses the system-wide ansible-core package to install the platform, but uses ansible-core 2.16 for both its control plane and built-in execution environments.                                                                                                                                                                                                                             |
| <br>Browser          | <br>A currently supported version of Mozilla Firefox or Google Chrome.                                                                 |                                                                                                                                                                                                                                                                                                                                                                                                                           |
| <br>Database         | For Ansible Automation Platform managed databases: PostgreSQL 15.For customer provided (external) databases: PostgreSQL 15, 16, or 17. | External (customer supported) databases require International Components for Unicode (ICU) support.External databases using PostgreSQL 16 or 17 must rely on external backup and restore processes. Backup and restore functionality is dependent on utilities provided with PostgreSQL 15.                                                                                                                               |
| <br>IP version       | <br>IPv4, IPv6 (single-stack and dual-stack)                                                                                           |                                                                                                                                                                                                                                                                                                                                                                                                                           |

*Table 2. Virtual machine requirements*

| Component                           | RAM      | vCPU  | Disk IOPS | Storage                                                            |
| ----------------------------------- | -------- | ----- | --------- | ------------------------------------------------------------------ |
| <br>Platform gateway                | <br>16GB | <br>4 | <br>3000  | <br>60GB minimum                                                   |
| <br>Control nodes                   | <br>16GB | <br>4 | <br>3000  | <br>80GB minimum with at least 20GB available under `/var/lib/awx` |
| <br>Execution nodes                 | <br>16GB | <br>4 | <br>3000  | <br>60GB minimum                                                   |
| <br>Hop nodes                       | <br>16GB | <br>4 | <br>3000  | <br>60GB minimum                                                   |
| <br>Automation hub                  | <br>16GB | <br>4 | <br>3000  | <br>60GB minimum with at least 40GB allocated to `/var/lib/pulp`   |
| <br>Database                        | <br>16GB | <br>4 | <br>3000  | <br>100GB minimum allocated to `/var/lib/pgsql`                    |
| <br>Event-Driven Ansible controller | <br>16GB | <br>4 | <br>3000  | <br>60GB minimum                                                   |


Note:

These are minimum requirements and can be increased for larger workloads in increments of 2x (for example 16GB becomes 32GB and 4 vCPU becomes 8vCPU). See [Horizontally scale tested deployment models to improve performance](/documentation/en-us/red_hat_ansible_automation_platform/2.6/optimize-con_horizontal_scaling_for_performance "Horizontal scaling involves increasing the number of replicas (pods or virtual machines) for a given service. Similar to vertical scaling, this approach is useful for high resource utilization or workload scaling.") for more information.

### Repository requirements

Enable the following repositories only when installing Red Hat Ansible Automation Platform:

- RHEL BaseOS
- RHEL AppStream


Note:

If you enable repositories besides those mentioned above, the Red Hat Ansible Automation Platform installation could fail unexpectedly.

The following are necessary for you to work with project updates and collections:

- Ensure that the [Network ports and protocols table](/documentation/en-us/red_hat_ansible_automation_platform/2.6/plan-assembly_network_ports_protocols#network-ports-protocols_table "The following table indicates the destination port and the direction of network traffic:") are available for successful connection and download of collections from automation hub or Ansible Galaxy server.

### Additional notes for Red Hat Ansible Automation Platform requirements

- The Ansible Automation Platform database backups are staged on each node at `/var/backups/automation-platform` through the variable `backup_dir`. You might need to mount a new volume to `/var/backups` or change the staging location with the variable `backup_dir` to prevent issues with disk space before running the `./setup.sh -b` script.
- If performing a bundled Ansible Automation Platform installation, the installation setup.sh script attempts to install ansible-core (and its dependencies) from the bundle for you.
- If you have installed Ansible-core manually, the Ansible Automation Platform installation setup.sh script detects that Ansible has been installed and does not attempt to reinstall it.


Note:

You must use Ansible-core, which is installed by using DNF. Ansible-core version 2.16 is required for versions 2.6 and later.

## Platform gateway system requirements

Platform gateway is the service that handles authentication and authorization for Ansible Automation Platform. It provides a single entry into the platform and serves the platform’s user interface.

## Automation controller system requirements

Automation controller is a distributed system, where different software components can be co-located or deployed across many compute nodes.

The installation program provides four node types as abstractions to help you design the topology appropriate for your use case: control, hybrid, execution, and hop nodes.

Use the following recommendations for node sizing:

*Table 3. Recommended Resource Sizing for Automation controller Node Types*

| Node Type               | RAM (Minimum) | vCPU (Minimum) | Disk IOPS (Minimum) | Storage and Notes                                                                                                                                                                                                                          |
| ----------------------- | ------------- | -------------- | ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| <br> **Execution Node** | <br>16 GB     | <br>4 vCPU     | <br>3000            | <br>Runs automation. Increase RAM/CPU to increase capacity for concurrent job **forks**. Performance depends heavily on the number of jobs run simultaneously.                                                                             |
| <br> **Control Node**   | <br>16 GB     | <br>4 vCPU     | <br>3000            | <br>Processes events and runs cluster jobs (e.g., project updates). \* **Storage:** 80GB minimum, with at least 20GB available under `/var/lib/awx`. \* **Storage Requirement:** Volume must be rated for a minimum baseline of 3000 IOPS. |
| <br> **Hybrid Node**    | <br>16 GB     | <br>4 vCPU     | <br>3000            | <br>A combination of Control and Execution node functions. Storage requirements generally match the Control Node.                                                                                                                          |
| <br> **Hop Node**       | <br>16 GB     | <br>4 vCPU     | <br>3000            | <br>Routes traffic within the automation mesh (e.g., bastion host). RAM can affect throughput, but CPU activity is typically low. Network latency is a more important factor than RAM or CPU.                                              |


- Actual RAM requirements vary based on how many hosts automation controller manages simultaneously (which is controlled by the `forks` parameter in the job template or the system `ansible.cfg` file). To avoid possible resource conflicts, Ansible recommends 1 GB of memory per 10 forks and 2 GB reservation for automation controller. See[How job capacity is determined and impacts job runs](/documentation/en-us/red_hat_ansible_automation_platform/2.6/optimize-con_controller_capacity_determination#controller-capacity-determination "The automation controller capacity system determines how many jobs can run on an instance given the amount of resources available to the instance and the size of the jobs that are running (referred to as Impact). The algorithm used to determine this is based on the following two things:"). If `forks` is set to 400, 42 GB of memory is recommended.
- A larger number of hosts can be addressed, but if the fork number is less than the total host count, more passes across the hosts are required. You can avoid these RAM limitations by using any of the following approaches:
* Use rolling updates.
* Use the provisioning callback system built into automation controller, where each system requesting configuration enters a queue and is processed as quickly as possible.
* In cases where automation controller is producing or deploying images such as AMIs.

## Automation hub system requirements

With Automation hub you can discover and use new certified automation content from Red Hat Ansible and Certified Partners.

On Ansible automation hub, you can discover and manage Ansible Collections, which are supported automation content developed by Red Hat and its partners for use cases such as cloud automation, network automation, and security automation.

Note:

Private automation hub

If you install private automation hub from an internal address with a certificate that only encompasses the external address, this can result in an installation that cannot be used as container registry without certificate issues.

To avoid this, use the `automationhub_main_url` inventory variable with a value such as https://pah.example.com linking to the private automation hub node in the installation inventory file.

This adds the external address to `/etc/pulp/settings.py`. This implies that you only want to use the external address.

For information about inventory file variables, see [Inventory file variables](/documentation/en-us/red_hat_ansible_automation_platform/2.6/install-assembly_appendix_inventory_file_vars#appendix-inventory-files-vars "The following tables contain information about the variables used in Ansible Automation Platform’s installation inventory files.").

### High availability automation hub requirements

Before deploying a high availability (HA) automation hub, ensure that you have a shared storage file system installed in your environment and that you have configured your network storage system, if applicable.

#### Required shared storage

Shared storage is required when installing more than one Automation hub with a `file` storage backend. The supported shared storage type for RPM-based installations is Network File System (NFS).

Before you run the Red Hat Ansible Automation Platform installer, verify that you installed the `/var/lib/pulp` directory across your cluster as part of the shared storage file system installation. The Red Hat Ansible Automation Platform installer returns an error if `/var/lib/pulp` is not detected in one of your nodes, causing your high availability automation hub setup to fail.

If you receive an error stating `/var/lib/pulp` is not detected in one of your nodes, ensure `/var/lib/pulp` is properly mounted in all servers and re-run the installation program.

#### Install firewalld for HA hub deployment

If you intend to install a HA automation hub using a network storage on the automation hub nodes itself, you must first install and use `firewalld` to open the necessary ports as required by your shared storage system before running the Ansible Automation Platform installer.

Install and configure `firewalld` by executing the following commands:

1. Install the `firewalld` daemon:

```
$ dnf install firewalld
```

2. Add your network storage under <service> using the following command:

```
$ firewall-cmd --permanent --add-service=<service>
```
Note:
For a list of supported services, use the `$ firewall-cmd --get-services` command

3. Reload to apply the configuration:

```
$ firewall-cmd --reload
```

## Event-Driven Ansible system requirements

The Event-Driven Ansible controller is a single-node system capable of handling a variable number of long-running processes (such as rulebook activations) on-demand, depending on the number of CPU cores.

Use the following minimum requirements for Event-Driven Ansible controller:

| Requirement         | Required                                                                                                                                                                                                                                                                       |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| <br> **RAM**        | <br>16 GB                                                                                                                                                                                                                                                                      |
| <br> **CPUs**       | <br>4                                                                                                                                                                                                                                                                          |
| <br> **Local disk** | Hard drive must be 40 GB minimum with at least 20 GB available under /var.Storage volume must be rated for a minimum baseline of 3000 IOPS.If the cluster has many large projects or decision environment images, consider doubling the GB in /var to avoid disk space errors. |


Important:

When you activate an Event-Driven Ansible rulebook under standard conditions, it uses about 250 MB of memory. However, the actual memory consumption can vary significantly based on the complexity of your rules and the volume and size of the events processed. In scenarios where a large number of events are anticipated or the rulebook complexity is high, conduct a preliminary assessment of resource usage in a staging environment. This ensures that your maximum number of activations is based on the capacity of your resources.

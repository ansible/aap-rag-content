# What is Ansible Automation Platform

Learn about what you can accomplish with Ansible Automation Platform.

With Ansible Automation Platform, you can create, manage, and scale automation for your organization across users, teams, and regions. Ansible Automation Platform also provides a unified, intuitive user interface (UI) that enables you to interact with each part of the platform so that you can orchestrate a range of automated tasks.

## Use cases

Ansible Automation Platform provides a powerful and flexible way for users to automate a wide range of IT tasks. Below are some common use cases illustrating what a typical user can achieve with the platform.

## Infrastructure provisioning

Users can automation the entire lifecycle of infrastructure deployment, from bare metal to cloud resources.

| Automation goal              | Description                                                                                                                            |
| ---------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| Cloud provisioning           | Launch and configure virtual machines, storage, and networking across public and private clouds (such as AWS, Azure, GCP, and VMware.) |
| Virtualization management    | Automate the creation, cloning, and decommissioning of virtual machines on platforms like VMware vSphere or Red Hat Virtualization.    |
| Network device configuration | Configure routers, switches, load balancers, and firewalls consistently across the network.                                            |

## Configuration management

Configuration management is a core use case, ensuring systems are configured and maintained across the environment.

Ansible automation platform can manage the following:

- Operating system configuration: Enforce standardized configurations (for example, security settings, user accounts, services) on Linux and Windows servers.
- Application deployment: Manage the deployment and configuration of applications, middleware, and their dependencies (like web servers or databases).
- Configuration drift correction: Automatically detect and remediate unauthorized changes to a system's configuration, bringing it back into compliance.

## Application deployment and continuous delivery

Ansible streamlines the process of moving code from development to production environments. Here are some examples how:

- Orchestration of multi-tier applications: Define and execute complex deployment workflows for applications that span multiple servers and services.
- Zero-downtime deployment: Implement strategies like rolling updates or blue/green deployments to ensure application availability during updates.
- Integration with CI/CD tools: Connect with tools like Jenkins or GitLab to trigger automated deployment pipelines.

## Security and compliance automation

Leverage Ansible to enforce security policies and automate compliance checks.

| Area                        | Example tasks                                                                                                    |
| --------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| Patch management            | Automation the scanning, staging, and deployment of security patches across all servers on a regular schedule.   |
| Security policy enforcement | Ensure firewalls are configured correctly, required security agents are running, and SSH settings are compliant. |
| Auditing and reporting      | Collect system configuration data for regular compliacne audits and generate reports.                            |

## Network automation

Ansible can manage and automate configuration tasks across diverse networking hardware.

For example:

- Automated troubleshooting: Run diagnostics, capture logs, and reset network interfaces automatically in response to alerts.
- OS upgrades: Standardize and automate the upgrade process for network operating systems (such as Cisco IOS or Juniper Junos OS).
- Firewall policy management: Automate the addition or removal of firewall rules based on approved changes.

## Enterprise IT automation and orchestration

Enterprise automation and orchestration involves automating complex, end-to-end business processes that can span multiple domains or teams. Users can create a centralized self-service portal for these tasks. - Self-service IT: Provide end users or teams with a simple interface to request and provision resources without direct access to the underlying structure.
- Service desk integration: Automate tasks triggered by help desk tickets, such as password resets or log collection, thereby reducing the need for manual intervention from a human agent.
- Disaster recovery automation: Automate the failover and failback procedures for applications and infrastructure at a secondary site.

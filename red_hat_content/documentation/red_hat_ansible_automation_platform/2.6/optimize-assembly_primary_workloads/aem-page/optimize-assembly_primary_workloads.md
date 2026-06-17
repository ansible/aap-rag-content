+++
template = "docs/aem-title.html"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.6/optimize-assembly_primary_workloads"
title = "Understand primary workloads for automation controller - Red Hat Ansible Automation Platform 2.6"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6", "2.6"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6/optimize-assembly_controller_improving_performance/", "Tune automation controller to improve performance"]]
category = "Optimize"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/optimize-assembly_primary_workloads/aem-page/optimize-assembly_primary_workloads.html"
last_crumb = "Understand primary workloads for automation controller"
modified = "2026-05-21T14:12:12.122Z"
multi_page_path = ""
name = "Understand primary workloads for automation controller"
oversized = "false"
page_slug = "optimize-assembly_primary_workloads"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.6"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/optimize-assembly_primary_workloads"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/optimize-assembly_primary_workloads/toc/toc.json"
type = "aem-page"
+++

# Understand primary workloads for automation controller

The primary workloads for automation controller include the following:

- Managing automation content through automation controller projects
- Initiating automation by executing jobs

## Automation controller project synchronization

Users define the source of automation content within the automation controller projects, such as Ansible Playbooks. The primary workload for these projects is synchronization. Project update jobs in the API manage synchronization. These jobs are also known as source control updates in the UI.

These project update jobs run only on the control plane and in task pods within the OpenShift Container Platform. Their role is to update the automation controller with the latest automation content. This content comes from its defined source, such as a Git repository.

Updating projects is not performance-sensitive, provided that they store only playbooks and Ansible-related text files. However, issues might arise when projects become excessively large.

Do not store large volumes of binary data within a project. If jobs require access to additional data, they should retrieve it from object storage or file storage. This retrieval must be done within the playbook’s scope.

## Jobs and automation workloads

Jobs are the primary workload for automation controller and run on the execution plane. They include the following job types:

- Standard jobs
- Workflow, sliced, and bulk jobs
- System jobs


### Standard jobs

Standard jobs involve the execution of an Ansible Playbook from a Project against a set of hosts from an Inventory. Jobs are initiated by a control node, which then streams, processes, and stores job results.

A performance sensitive part of this is the processing of the playbook output. The output is captured and serialized into job events by the automation controller. A single Ansible task running against a host typically produces multiple job events, for example:

- Task start
- Host-specific details
- Task completion


Event volume varies significantly with the playbook’s configured verbosity level. For example, a simple debug task that prints `Hello World` on one host might produce 6 job events at verbosity 1, increasing to 34 job events at verbosity 3.

The dispatcher and the callback receiver collaborate to process, transmit, and store job events. These actions contribute to the platform’s storage and processing usage. Job events are processed on the control plane and stored in the database. The dispatcher processes job events, and the callback receiver stores them.

### Workflow, sliced and bulk jobs

To enable complex automation and orchestration, use the following job types to extend standard jobs:

- Sliced jobs: Split jobs to run against slices of the inventory in parallel
- Bulk jobs: Launch multiple jobs in a single request
- Workflow jobs: Coordinate multiple job templates


These job types coordinate the launch and management of multiple underlying standard jobs. They impact job scheduling, which occurs in the control plane, but otherwise do not have significant impact on their services.

### System jobs

System jobs involve internal maintenance tasks, such as clean up of old job event data. The execution frequency of system jobs is managed by schedules. System jobs run on the control plane, because they run management commands that interact with the database. These workloads involve key platform activities.

Reducing the frequency of system jobs or increasing the number of days of data to retain can degrade database performance. It is generally recommended to retain as few days of data as possible. Use external logging features for long-term audit data storage. Storing more data in the database can make queries that scan large tables more costly.

## Tune Event-Driven Ansible activations

Activations are used by Event-Driven Ansible to run instances of `ansible-rulebook`. These activations can either connect to external event sources or listen to an event stream for incoming payloads.

Activation and output management uses the following:

- Event-Driven Ansible hybrid nodes
- Platform gateway for event stream handling
- The WebSocket server in each API node or pod
- The database for audit event storage


Activations process discrete payloads called events. The activation’s resource usage is affected by the event arrival rate and the complexity of the rulebook’s rules.

When events match rules, they trigger actions, which launch jobs in automation controller. Event auditing stores audit events in the database and is enabled by default.

Each event is sent from the activation to the WebSocket server to be serialized and written to the database. This process stresses the server and can cause performance issues. Selecting **Skip audit events** in the UI for a given activation eliminates this workload.

When **Skip audit events** is selected, rules are still fired. However, the fire count in the API and UI is updated at a periodic interval (default 300 seconds) rather than immediately.

## Minimize the impact of collection syncing

Private automation hub can synchronize collections from remote `ansible-galaxy` repositories, such as `galaxy.ansible.com` or automation hub on `console.redhat.com`.

Pulp content workers and the database synchronize the repositories. The automation controller can download these collections during project updates, or use them to build automation execution environments. Collections are also available for any other client by using the `ansible-galaxy` CLI to download and use.

The performance of collection synchronization is impacted by the following:

- The number of collections listed in the `requirements.yml`
- The number of versions synced
- The number of versions retained


Synchronization uses memory in direct proportion to the number of collections and versions synchronized. Using a targeted `requirements.yml` with specific versions can limit this impact.

Hosting collections uses storage space. Manage the storage space that collections use by specifying the retained number of versions on the repository.

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

## Reference workloads for growth topologies

The following table provides reference data for typical workloads, performance metrics, and capacity planning for the tested Ansible Automation Platform growth topologies.

*Table 1. Reference workloads for growth topologies*

| Component / Feature                                                                                                                                                                     | Metric                                                                                                                                          |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| <br>REST API                                                                                                                                                                            | <br>8 requests per second (RPS)                                                                                                                 |
| <br>REST API 50 percentile latency at 8 RPS                                                                                                                                             | <br>500 milliseconds                                                                                                                            |
| <br>REST API 99 percentile latency at 8 RPS                                                                                                                                             | <br>1.5 seconds                                                                                                                                 |
| <br>Hosts in automation controller inventory                                                                                                                                            | <br>1,000 hosts                                                                                                                                 |
| <br>Job start rate in automation controller (max burst rate with standard launch)                                                                                                       | <br>20 jobs started per second                                                                                                                  |
| <br>Concurrent jobs in automation controller                                                                                                                                            | <br>10 concurrent jobs with default forks (5 forks is default) + 100 with forks=1                                                               |
| <br>Callback receiver event processing rate                                                                                                                                             | <br>10,000 job events per second at peak                                                                                                        |
| <br>Job History with 30 days retention                                                                                                                                                  | <br>2kb event; 500 events per playbook run; 500 jobs a day + Less than 60Gb (as specified as minimum required disk on Database node)            |
| <br>(Certified) Sync time                                                                                                                                                               | <br>Less than 30 minutes                                                                                                                        |
| <br>(Validated) Sync time                                                                                                                                                               | <br>Less than 5 minutes                                                                                                                         |
| <br>Activation processing events with skip audit events enabled (6 activation) with events incoming via Event Stream and execution strategy set to sequential (default) in the rulebook | <br>1 actionable event/minute with minimal payload with job template action on local automation controller where each job completes in 1 minute |

## Reference workloads for enterprise topologies

The following table provides reference data for typical workloads, performance metrics, and capacity planning for the tested Ansible Automation Platform enterprise topologies.

*Table 2. Reference workloads for enterprise topologies*

| Component / Feature                                                                                                                                                           | Metric                                                                                                                                          |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| <br>REST API                                                                                                                                                                  | <br>16 requests per second (RPS)                                                                                                                |
| <br>REST API 50 percentile latency at 16 RPS                                                                                                                                  | <br>500 milliseconds                                                                                                                            |
| <br>REST API 99 percentile latency at 16 RPS                                                                                                                                  | <br>1.5 seconds                                                                                                                                 |
| <br>Hosts in automation controller inventory                                                                                                                                  | <br>10,000 hosts                                                                                                                                |
| <br>Job start rate in automation controller                                                                                                                                   | <br>80 jobs started per second                                                                                                                  |
| <br>Concurrent jobs in automation controller                                                                                                                                  | <br>40 with default forks (5 forks is default) + 400 with forks=1                                                                               |
| <br>Callback receiver event rate                                                                                                                                              | <br>40,000 events per second at peak                                                                                                            |
| <br>Job History with 7 days retention                                                                                                                                         | <br>2kb event; 500 events per playbook run; 2000 jobs a day + Less than 60Gb (as specified as minimum required disk on Database node)           |
| <br>(Certified) Sync time                                                                                                                                                     | <br>Less than 30 minutes                                                                                                                        |
| <br>(Validated) Sync time                                                                                                                                                     | <br>Less than 5 minutes                                                                                                                         |
| <br>Processing events with skip audit events enabled (6 activations) with events incoming via Event Stream and execution strategy set to sequential (default) in the rulebook | <br>3 actionable event/minute with minimal payload with job template action on local automation controller where each job completes in 1 minute |

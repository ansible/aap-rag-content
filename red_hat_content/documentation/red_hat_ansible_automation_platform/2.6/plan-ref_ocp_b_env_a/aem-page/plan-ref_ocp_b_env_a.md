+++
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.6/plan-ref_ocp_b_env_a"
template = "docs/aem-title.html"
title = "Operator enterprise topology - Red Hat Ansible Automation Platform 2.6"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6", "2.6"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6/plan-assembly_overview_tested_deployment_models/", "Choose a deployment method and topology"]]
category = "Plan"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/plan-ref_ocp_b_env_a/aem-page/plan-ref_ocp_b_env_a.html"
last_crumb = "Operator enterprise topology"
modified = "2026-05-21T14:12:12.122Z"
multi_page_path = ""
name = "Operator enterprise topology"
oversized = "false"
page_slug = "plan-ref_ocp_b_env_a"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.6"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/plan-ref_ocp_b_env_a"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/plan-ref_ocp_b_env_a/toc/toc.json"
type = "aem-page"
+++

# Operator enterprise topology

The Operator-based enterprise topology provides redundancy and higher compute for large volumes of automation on Red Hat OpenShift Container Platform.

The Ansible Automation Platform Service on AWS is an example of an OpenShift Operator based enterprise topology.

Included are the tested infrastructure topology, system requirements, network port configurations, and an example custom resource file for installation.

 Important:

You can only install a single instance of the Ansible Automation Platform Operator into a single namespace. Installing multiple instances in the same namespace can lead to improper operation for both Operator instances.

## Infrastructure topology

The Red Hat tested infrastructure topology for this deployment model:

*Figure 1. Infrastructure topology diagram*

![Operator enterprise topology diagram](/webassets/aem/red_hat_ansible_automation_platform/2.6/images/ocp-b-env-a.png)

 Important:

While Redis and PostgreSQL can be installed as part of the operator-based installation process, the topology diagram represents a Red Hat supported topology where both Redis and PostgreSQL are external to Ansible Automation Platform.

This infrastructure topology describes an OpenShift Cluster with 3 primary nodes and 2 worker nodes.

Red Hat tests each OpenShift Worker node with these requirements:

*Table 1. OpenShift Worker node requirements*

| Requirement | Minimum requirement |
| ----------- | ------------------- |
| RAM         | 16 GB               |
| CPUs        | 4                   |
| Local disk  | 128 GB              |
| Disk IOPS   | 3000                |

*Table 2. Infrastructure topology components*

| Count   | Component                                                          |
| ------- | ------------------------------------------------------------------ |
| <br>1   | <br>Automation controller web pod                                  |
| <br>1   | <br>Automation controller task pod                                 |
| <br>1   | <br>Automation hub web pod                                         |
| <br>1   | <br>Automation hub API pod                                         |
| <br>2   | <br>Automation hub content pod                                     |
| <br>2   | <br>Automation hub worker pod                                      |
| <br>1   | <br>Automation hub Redis pod                                       |
| <br>1   | <br>Event-Driven Ansible API pod                                   |
| <br>2   | <br>Event-Driven Ansible activation worker pod                     |
| <br>2   | <br>Event-Driven Ansible default worker pod                        |
| <br>2   | <br>Event-Driven Ansible event stream pod                          |
| <br>1   | <br>Event-Driven Ansible scheduler pod                             |
| <br>1   | <br>Platform gateway pod                                           |
| <br>2   | <br>Mesh ingress pod                                               |
| <br>N/A | <br>Externally managed database service                            |
| <br>N/A | <br>Externally managed Redis                                       |
| <br>N/A | <br>Externally managed object storage service (for automation hub) |

## Tested system configurations

Red Hat has tested these configurations to install and run Red Hat Ansible Automation Platform:

*Table 3. Tested system configurations*

| Type                           | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| ------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <br>Subscription               | <br>Valid Red Hat Ansible Automation Platform subscription                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| <br>Red Hat OpenShift          | Red Hat OpenShift on AWS Hosted Control Planes 4.15.16     2 worker nodes in different availability zones (AZs) at t3.xlarge                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| <br>Ansible-core               | <br>Ansible-core version 2.16 or later                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| <br>Browser                    | <br>A currently supported version of Mozilla Firefox or Google Chrome.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| <br>AWS RDS PostgreSQL service | engine: "postgres"engine\_version: 15"parameter\_group\_name: "default.postgres15"allocated\_storage: 20max\_allocated\_storage: 1000storage\_type: "gp2"storage\_encrypted: trueinstance\_class: "db.t4g.small"multi\_az: truebackup\_retention\_period: 5database: must have International Components for Unicode (ICU) support       Note:   <br>Minimum external database requirements<br>The external database must meet these minimum requirements:<br>4 vCPUs16 GB RAMmax\_connections: 1024 (minimum). You might need more connections when scaling replicas.200 GB storage on a volume capable of at least 3000 IOPS.<br>Database storage consumption depends on your workload, including job frequency, playbook task count, output verbosity, and the number of managed hosts per job. Start with a 200 GB baseline and monitor actual usage after deployment. Configure automated cleanup jobs to prevent unbounded database growth.<br>These requirements ensure adequate database performance for the enterprise topology workload profile. |
| <br>AWS Memcached Service      | engine: "redis"engine\_version: "6.2"auto\_minor\_version\_upgrade: "false"node\_type: "cache.t3.micro"parameter\_group\_name: "default.redis6.x.cluster.on"transit\_encryption\_enabled: "true"num\_node\_groups: 2replicas\_per\_node\_group: 1automatic\_failover\_enabled: true                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| <br>s3 storage                 | <br>HTTPS only accessible through AWS Role assigned to automation hub SA at runtime by using AWS Pod Identity                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| <br>IP version                 | <br>IPv4, IPv6 (single-stack and dual-stack)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |


 Note:

**Minimum external database requirements**

The external database must meet these minimum requirements:

- 4 vCPUs
- 16 GB RAM
- `max_connections`: 1024 (minimum). You might need more connections when scaling replicas.
- 200 GB storage on a volume capable of at least 3000 IOPS.

Database storage consumption depends on your workload, including job frequency, playbook task count, output verbosity, and the number of managed hosts per job. Start with a 200 GB baseline and monitor actual usage after deployment. Configure automated cleanup jobs to prevent unbounded database growth. These requirements ensure adequate database performance for the enterprise topology workload profile.

## Example custom resource file

For example CR files, see the [ocp-b.env-a](https://github.com/ansible/test-topologies/blob/aap-2.5/ocp-b.env-a/README.md) directory in the `test-topologies` GitHub repository.

## Nonfunctional requirements

Ansible Automation Platform’s performance characteristics and capacity depend on its resource allocation and configuration. With OpenShift, each Ansible Automation Platform component deploys as a pod. You can specify resource requests and limits for each pod.

Use the Ansible Automation Platform custom resource to configure resource allocation for OpenShift installations. Each configurable item has default settings. These settings are the exact configuration used in this reference deployment architecture. This configuration assumes deployment and management by an Enterprise IT organization for production purposes.

By default, each component’s deployments use minimum resource requests but no resource limits. OpenShift only schedules pods with available resource requests. However, pods can consume unlimited RAM or CPU as long as the OpenShift worker node is not under node pressure.

In the Operator enterprise topology, Ansible Automation Platform runs on a Red Hat OpenShift on AWS (ROSA) Hosted Control Plane (HCP) cluster. The cluster has 2 t3.xlarge worker nodes spread across 2 AWS availability zones within a single region. This is not a shared environment so Ansible Automation Platform pods have full access to all compute resources of the ROSA HCP cluster.

The capacity calculation for automation controller task pods comes from the underlying HCP worker node running the pod. It does not have access to the CPU or memory resources of the entire node. This capacity calculation influences how many concurrent jobs automation controller can run.

OpenShift manages storage distinctly from VMs. This impacts how automation hub stores its artifacts. In the Operator enterprise topology, automation hub uses S3 storage. automation hub requires `ReadWriteMany` type storage, which is not a default storage type in OpenShift.

This topology specifies externally provided Redis, PostgreSQL, and object storage for automation hub. This provides additional scalability and reliability features for the Ansible Automation Platform deployment. These features include specialized backup, restore, and replication services, as well as scalable storage.

## Network ports

Red Hat Ansible Automation Platform uses several ports to communicate with its services. These ports must be open and available for Red Hat Ansible Automation Platform to work. Ensure that these ports are available and are not blocked by a firewall.

*Table 4. Network ports and protocols*

| Port number | Protocol       | Service            | Source                                   | Destination                              |
| ----------- | -------------- | ------------------ | ---------------------------------------- | ---------------------------------------- |
| <br>80/443  | <br>HTTP/HTTPS | <br>Object storage | <br>OpenShift Container Platform cluster | <br>External object storage service      |
| <br>80/443  | <br>HTTP/HTTPS | <br>Receptor       | <br>Execution node                       | <br>OpenShift Container Platform ingress |
| <br>80/443  | <br>HTTP/HTTPS | <br>Receptor       | <br>Hop node                             | <br>OpenShift Container Platform ingress |
| <br>5432    | <br>TCP        | <br>PostgreSQL     | <br>OpenShift Container Platform cluster | <br>External database service            |
| <br>6379    | <br>TCP        | <br>Redis          | <br>OpenShift Container Platform cluster | <br>External Redis service               |
| <br>27199   | <br>TCP        | <br>Receptor       | <br>OpenShift Container Platform cluster | <br>Execution node                       |
| <br>27199   | <br>TCP        | <br>Receptor       | <br>OpenShift Container Platform cluster | <br>Hop node                             |

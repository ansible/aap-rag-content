+++
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.6/plan-con_redis_cache_and_queueing_system"
template = "docs/aem-title.html"
title = "Overview of the Redis cache and queueing system - Red Hat Ansible Automation Platform 2.6"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6", "2.6"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6/plan-con_redis_cache_and_queueing_system/", "Overview of the Redis cache and queueing system"]]
category = "Plan"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/plan-con_redis_cache_and_queueing_system/aem-page/plan-con_redis_cache_and_queueing_system.html"
last_crumb = "Overview of the Redis cache and queueing system"
modified = "2026-05-21T14:12:12.122Z"
multi_page_path = ""
name = "Overview of the Redis cache and queueing system"
oversized = "false"
page_slug = "plan-con_redis_cache_and_queueing_system"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.6"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/plan-con_redis_cache_and_queueing_system"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/plan-con_redis_cache_and_queueing_system/toc/toc.json"
type = "aem-page"
+++

# Overview of the Redis cache and queueing system

Redis (Remote Dictionary Server) provides centralized caching and queueing for Ansible Automation Platform 2.6 components. This in-memory system stores event queues, session data, and tokens to deliver improved performance, reliability, and data security.

Redis is an open source, in-memory, NoSQL key/value store used primarily as an application cache and lightweight message broker, which stores event queues, session data, and tokens to deliver improved performance, reliability, and data security.

Platform gateway and Event-Driven Ansible use Centralized Redis. Automation controller and automation hub have their own instances of Redis.

This cache and queue system stores data in memory, rather than on a disk or solid-state drive (SSD), which helps deliver speed, reliability, and performance. Secure communication with the cache and queue system through Transport Layer Security (TLS) encryption and authentication protects your data.

| Component                                      |
| ---------------------------------------------- |
| Data types cached                              |
| Platform gateway                               |
| Settings, Session Information, JSON Web Tokens |
| Event-Driven Ansible server                    |
| Event queues                                   |


Note:

The data in Redis from the platform gateway and Event-Driven Ansible are partitioned. Neither service can access the other service's data.

## Centralized Redis

Redis provides fast, in-memory caching and session management for Ansible Automation Platform components, improving performance and enabling scaling.

Ansible Automation Platform offers a centralized Redis instance in both standalone and clustered topologies.

## Clustered Redis

Clustered Redis delivers high availability and scalability for Ansible Automation Platform by distributing data across many nodes with automatic failover capabilities. Use clustered Redis when you need enterprise-grade resilience, data scalability, and protection against node failures in production environments.

Clustered Redis, shared between the platform gateway and Event-Driven Ansible, is the default configuration when installing Ansible Automation Platform in containerized and Operator-based deployments.

Note:

A Redis high availability (HA) compatible deployment require 6 VMs. In RPM deployments, Redis can be colocated on each Ansible Automation Platform component VM except for automation controller, execution nodes, or the PostgreSQL database. In containerized deployments, Redis can be colocated on any Ansible Automation Platform component VMs of your choice except for execution nodes or the PostgreSQL database.

A cluster has three primary nodes and each primary node has a replica node.

If a primary instance becomes unavailable due to failures, the other primary nodes will initiate a failover state to promote a replica node to a primary node.

The benefits of deploying clustered Redis over standalone Redis include the following:

- Data is automatically split across many nodes.
- Data can be dynamically adjusted.
- Automatic failover of the primary nodes initiates during system failures.


**Disclaimer**: Links contained in this information to external website(s) are provided for convenience only. Red Hat has not reviewed the links and is not responsible for the content or its availability. The inclusion of any link to an external website does not imply endorsement by Red Hat of the website or their entities, products or services. You agree that Red Hat is not responsible or liable for any loss or expenses that may result due to your use of (or reliance on) the external site or content.

## Standalone Redis

Standalone Redis offers a straightforward deployment option for Ansible Automation Platform environments where high availability is not critical.

Standalone Redis consists of a simple architecture that is easy to deploy and configure.

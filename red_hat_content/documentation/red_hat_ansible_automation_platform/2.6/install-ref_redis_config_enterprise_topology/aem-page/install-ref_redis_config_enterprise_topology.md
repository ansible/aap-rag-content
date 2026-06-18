+++
title = "Configure Redis - Red Hat Ansible Automation Platform 2.6"
template = "docs/aem-title.html"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.6/install-ref_redis_config_enterprise_topology"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6", "2.6"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6/install-assembly_platform_install_overview/", "Install RPM-based Ansible Automation Platform"]]
category = "Install"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/install-ref_redis_config_enterprise_topology/aem-page/install-ref_redis_config_enterprise_topology.html"
last_crumb = "Configure Redis"
modified = "2026-05-21T14:12:12.122Z"
multi_page_path = ""
name = "Configure Redis"
oversized = "false"
page_slug = "install-ref_redis_config_enterprise_topology"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.6"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/install-ref_redis_config_enterprise_topology"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/install-ref_redis_config_enterprise_topology/toc/toc.json"
type = "aem-page"
+++

# Configure Redis

Ansible Automation Platform offers a centralized Redis instance in both `standalone` and `clustered` topologies.

In RPM deployments, the Redis mode is set to `cluster` by default. You can change this setting in the inventory file `[all:vars]` section as in the following example:

```
[all:vars]
admin_password='<password>'
pg_host='data.example.com'
pg_port='5432'
pg_database='awx'
pg_username='awx'
pg_password='<password>'
pg_sslmode='prefer'  # set to 'verify-full' for client-side enforced SSL

registry_url='registry.redhat.io'
registry_username='<registry username>'
registry_password='<registry password>'

redis_mode=cluster
```
For more information about Redis, see [Caching and queueing system](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/planning_your_installation/ha-redis_planning) in *Planning your installation*.

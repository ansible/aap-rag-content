+++
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-redis_variables"
template = "docs/aem-title.html"
title = "Redis variables - Red Hat Ansible Automation Platform 2.7"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-assembly_appendix_inventory_file_vars/", "Inventory file variables"]]
category = "Install"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/install-redis_variables/aem-page/install-redis_variables.html"
last_crumb = "Redis variables"
modified = "2026-06-05T07:48:10.594Z"
multi_page_path = ""
name = "Redis variables"
oversized = "false"
page_slug = "install-redis_variables"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/install-redis_variables"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/install-redis_variables/toc/toc.json"
type = "aem-page"
+++

# Redis variables

Reference information for the inventory file variables used to configure Redis.

| Variable name                       | Description                                                                                                                                                                                                                                                                 | Required or optional | Default                                         |
| ----------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------- | ----------------------------------------------- |
| <br>`redis_cluster_ip`              | <br>The IPv4 address used by the Redis cluster to identify each host in the cluster. When defining hosts in the `[redis]` group, use this variable to identify the IPv4 address if the default is not what you want. Redis clusters cannot use hostnames or IPv6 addresses. | <br>Optional         | <br>Discovered IPv4 address from Ansible facts. |
| <br>`redis_firewall_zone`           | <br>The firewall zone where Redis related firewall rules are applied. This controls which networks can access Redis based on the zone's trust level.                                                                                                                        | <br>Optional         | <br>`public`                                    |
| <br>`redis_mode`                    | <br>The Redis mode to use for your Ansible Automation Platform installation. Valid options include: `standalone` and `cluster`.                                                                                                                                             | <br>Optional         | <br>`cluster`                                   |
| <br>`redis_tls_cert`                | <br>Path to the Redis server TLS certificate.                                                                                                                                                                                                                               | <br>Optional         |                                                 |
| <br>`redis_tls_key`                 | <br>Path to the Redis server TLS certificate key.                                                                                                                                                                                                                           | <br>Optional         |                                                 |
| <br>`redis_tls_remote`              | <br>Denote whether the Redis provided certificate files are local to the installation program (`false`) or on the remote component server (`true`).                                                                                                                         | <br>Optional         | <br>`false`                                     |
| <br>`redis_use_archive_compression` | <br>Controls whether archive compression is enabled or disabled for Redis. You can control this functionality globally by using `use_archive_compression`.                                                                                                                  | <br>Optional         | <br>`true`                                      |

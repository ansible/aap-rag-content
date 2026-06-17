+++
title = "Redis variables - Red Hat Ansible Automation Platform 2.6"
template = "docs/aem-title.html"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.6/install-ref_redis_inventory_variables"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6", "2.6"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6/install-assembly_appendix_inventory_file_vars/", "Inventory file variables"]]
category = "Install"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/install-ref_redis_inventory_variables/aem-page/install-ref_redis_inventory_variables.html"
last_crumb = "Redis variables"
modified = "2026-05-21T14:12:12.122Z"
multi_page_path = ""
name = "Redis variables"
oversized = "false"
page_slug = "install-ref_redis_inventory_variables"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.6"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/install-ref_redis_inventory_variables"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/install-ref_redis_inventory_variables/toc/toc.json"
type = "aem-page"
+++

# Redis variables

Reference information for the inventory file variables used to configure Redis.

| RPM variable name              | Container variable name              | Description                                                                                                                                                                                                                                                                                        | Required or optional | Default                                                                                                                                                               |
| ------------------------------ | ------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <br> `redis_cluster_ip`        | <br> `redis_cluster_ip`              | <br>The IPv4 address used by the Redis cluster to identify each host in the cluster. When defining hosts in the `[redis]` group, use this variable to identify the IPv4 address if the default is not what you want. Specific to container: Redis clusters cannot use hostnames or IPv6 addresses. | <br>Optional         | <br>RPM = Discovered IPv4 address from Ansible facts. If IPv4 address is not available, IPv6 address is used. Container = Discovered IPv4 address from Ansible facts. |
| <br> `redis_disable_mtls`      |                                      | <br>Controls whether mTLS is enabled or disabled for Redis. Set this variable to `true` to disable mTLS.                                                                                                                                                                                           | <br>Optional         | <br> `false`                                                                                                                                                          |
| <br> `redis_firewalld_zone`    | <br> `redis_firewall_zone`           | <br>The firewall zone where Redis related firewall rules are applied. This controls which networks can access Redis based on the zone’s trust level.                                                                                                                                               | <br>Optional         | <br>RPM = no default set. Container = `public`.                                                                                                                       |
| <br> `redis_hostname`          |                                      | <br>Hostname used by the Redis cluster when identifying and routing the host. By default `routable_hostname` is used.                                                                                                                                                                              | <br>Optional         | <br>The value defined in `routable_hostname`                                                                                                                          |
| <br> `redis_mode`              | <br> `redis_mode`                    | <br>The Redis mode to use for your Ansible Automation Platform installation. Valid options include: `standalone` and `cluster`.                                                                                                                                                                    | <br>Optional         | <br> `cluster`                                                                                                                                                        |
| <br> `redis_server_regen_cert` |                                      | <br>Denotes whether or not to regenerate the Ansible Automation Platform managed TLS key pair for Redis.                                                                                                                                                                                           | <br>Optional         | <br> `false`                                                                                                                                                          |
| <br> `redis_tls_cert`          | <br> `redis_tls_cert`                | <br>Path to the Redis server TLS certificate.                                                                                                                                                                                                                                                      | <br>Optional         |                                                                                                                                                                       |
| <br> `redis_tls_files_remote`  | <br> `redis_tls_remote`              | <br>Denote whether the Redis provided certificate files are local to the installation program (`false`) or on the remote component server (`true`).                                                                                                                                                | <br>Optional         | <br> `false`                                                                                                                                                          |
| <br> `redis_tls_key`           | <br> `redis_tls_key`                 | <br>Path to the Redis server TLS certificate key.                                                                                                                                                                                                                                                  | <br>Optional         |                                                                                                                                                                       |
|                                | <br> `redis_use_archive_compression` | <br>Controls whether archive compression is enabled or disabled for Redis. You can control this functionality globally by using `use_archive_compression`.                                                                                                                                         | <br>Optional         | <br> `true`                                                                                                                                                           |

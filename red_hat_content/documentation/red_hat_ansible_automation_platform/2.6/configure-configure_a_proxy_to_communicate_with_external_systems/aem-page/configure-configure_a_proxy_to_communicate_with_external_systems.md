+++
template = "docs/aem-title.html"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.6/configure-configure_a_proxy_to_communicate_with_external_systems"
title = "Configure a proxy to communicate with external systems - Red Hat Ansible Automation Platform 2.6"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6", "2.6"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6/configure-configure_a_proxy_to_communicate_with_external_systems/", "Configure a proxy to communicate with external systems"]]
category = "Configure"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/configure-configure_a_proxy_to_communicate_with_external_systems/aem-page/configure-configure_a_proxy_to_communicate_with_external_systems.html"
last_crumb = "Configure a proxy to communicate with external systems"
modified = "2026-05-21T14:12:12.122Z"
multi_page_path = ""
name = "Configure a proxy to communicate with external systems"
oversized = "false"
page_slug = "configure-configure_a_proxy_to_communicate_with_external_systems"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.6"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/configure-configure_a_proxy_to_communicate_with_external_systems"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/configure-configure_a_proxy_to_communicate_with_external_systems/toc/toc.json"
type = "aem-page"
+++

# Configure a proxy to communicate with external systems

Understand how proxies help you to control and route network traffic from Ansible Automation Platform to outside systems.

Proxies help you to meet your organization's network access and security requirements. You can use them in a number of ways, including:

- When your automation deployment is in a restricted network, use a proxy to download collections from automation hub, pull container images, access external APIs, and reach cloud services.
- When syncing content from automation hub or private automation hub, you can use a proxy to download collections, validate sugnatures, and sync remote repositories.
- You can also use a proxy for execution nodes that need to pull images from a container registry and access external package repositories.
- Outbound APIs from Ansible Automation Platform to other applications or cloud resources may also need to pass through a proxy.

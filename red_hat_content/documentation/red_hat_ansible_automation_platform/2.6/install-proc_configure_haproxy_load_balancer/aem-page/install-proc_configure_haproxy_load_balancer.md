+++
title = "Configure a HAProxy load balancer - Red Hat Ansible Automation Platform 2.6"
template = "docs/aem-title.html"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.6/install-proc_configure_haproxy_load_balancer"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6", "2.6"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6/install-con_aap_containerized_installation_intro/", "Install containerized Ansible Automation Platform"]]
category = "Install"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/install-proc_configure_haproxy_load_balancer/aem-page/install-proc_configure_haproxy_load_balancer.html"
last_crumb = "Configure a HAProxy load balancer"
modified = "2026-05-21T14:12:12.122Z"
multi_page_path = ""
name = "Configure a HAProxy load balancer"
oversized = "false"
page_slug = "install-proc_configure_haproxy_load_balancer"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.6"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/install-proc_configure_haproxy_load_balancer"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/install-proc_configure_haproxy_load_balancer/toc/toc.json"
type = "aem-page"
+++

# Configure a HAProxy load balancer

Configure a HAProxy load balancer in front of platform gateway with a custom CA cert.

## Procedure

 Set the following inventory file variables under the `[all:vars]` group:

```
custom_ca_cert=<path_to_cert_crt>
gateway_main_url=<https://load_balancer_url>
```


Important:

- Ensure your load balancer is configured to use HTTP/1.1 when communicating with platform gateway. HTTP/2 is not supported.
- HAProxy SSL passthrough mode is not supported with platform gateway.

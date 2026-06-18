+++
template = "docs/aem-title.html"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/configure-ref_automation_mesh_proxy"
title = "Configure proxy settings for automation mesh - Red Hat Ansible Automation Platform 2.7"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/configure-configure_a_proxy_to_communicate_with_external_systems/", "Configure a proxy to communicate with external systems"]]
category = "Configure"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/configure-ref_automation_mesh_proxy/aem-page/configure-ref_automation_mesh_proxy.html"
last_crumb = "Configure proxy settings for automation mesh"
modified = "2026-06-05T07:48:10.594Z"
multi_page_path = ""
name = "Configure proxy settings for automation mesh"
oversized = "false"
page_slug = "configure-ref_automation_mesh_proxy"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/configure-ref_automation_mesh_proxy"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/configure-ref_automation_mesh_proxy/toc/toc.json"
type = "aem-page"
+++

# Configure proxy settings for automation mesh

You can route outbound communication from the receptor on an automation mesh node through a proxy server. If your proxy does not strip out TLS certificates then an installation of Ansible Automation Platform automatically supports the use of a proxy server.

Every node on the mesh must have a Certifying Authority that the installation program creates on your behalf.

The default install location for the Certifying Authority is:

 `/etc/receptor/tls/ca/mesh-CA.crt`

The certificates and keys created on your behalf use the nodeID for their names:

For the certificate: `/etc/receptor/tls/NODEID.crt`

For the key: `/etc/receptor/tls/NODEID.key`

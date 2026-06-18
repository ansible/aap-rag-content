+++
template = "docs/aem-title.html"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-ref_adding_execution_nodes"
title = "Add execution nodes - Red Hat Ansible Automation Platform 2.7"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-con_aap_containerized_installation_intro/", "Install containerized Ansible Automation Platform"]]
category = "Install"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/install-ref_adding_execution_nodes/aem-page/install-ref_adding_execution_nodes.html"
last_crumb = "Add execution nodes"
modified = "2026-06-05T07:48:10.594Z"
multi_page_path = ""
name = "Add execution nodes"
oversized = "false"
page_slug = "install-ref_adding_execution_nodes"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/install-ref_adding_execution_nodes"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/install-ref_adding_execution_nodes/toc/toc.json"
type = "aem-page"
+++

# Add execution nodes

Containerized Ansible Automation Platform can deploy remote execution nodes.

You can define remote execution nodes in the `[execution_nodes]` group of your inventory file:

```
[execution_nodes]
<fqdn_of_your_execution_host>
```
By default, an execution node uses the following settings that you can update as needed:

```
receptor_port=27199
receptor_protocol=tcp
receptor_type=execution
```


- `receptor_port` - The port number that receptor listens on for incoming connections from other receptor nodes.
- `receptor_type` - The role of the node. Valid options include `execution` or `hop`.
- `receptor_protocol` - The protocol used for communication. Valid options include `tcp` or `udp`.


By default, execution nodes automatically peer with all automation controller nodes. To configure an execution node to peer with specific automation controller nodes instead, use the `receptor_peers` variable.

Note:

The value of `receptor_peers` must be a comma-separated list of host names. Do not use inventory group names.

 **Example:**

```
[execution_nodes]
# Uses default peering (peers with all controller nodes)
exec1.example.com
# Only peers with specific controller nodes
exec2.example.com receptor_peers='["controller1.example.com","controller2.example.com"]'
# Hop node that peers with specific execution nodes
hop1.example.com receptor_type=hop receptor_peers='["exec1.example.com","exec2.example.com"]'
```

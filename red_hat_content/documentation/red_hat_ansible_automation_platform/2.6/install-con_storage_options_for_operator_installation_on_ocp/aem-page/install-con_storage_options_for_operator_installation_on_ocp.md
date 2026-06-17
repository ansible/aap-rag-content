+++
template = "docs/aem-title.html"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.6/install-con_storage_options_for_operator_installation_on_ocp"
title = "Storage options for automation hub - Red Hat Ansible Automation Platform 2.6"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6", "2.6"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6/install-assembly_operator_install_operator/", "Install on OpenShift Container Platform"]]
category = "Install"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/install-con_storage_options_for_operator_installation_on_ocp/aem-page/install-con_storage_options_for_operator_installation_on_ocp.html"
last_crumb = "Storage options for automation hub"
modified = "2026-05-21T14:12:12.122Z"
multi_page_path = ""
name = "Storage options for automation hub"
oversized = "false"
page_slug = "install-con_storage_options_for_operator_installation_on_ocp"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.6"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/install-con_storage_options_for_operator_installation_on_ocp"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/install-con_storage_options_for_operator_installation_on_ocp/toc/toc.json"
type = "aem-page"
+++

# Storage options for automation hub

Automation hub requires `ReadWriteMany` file-based storage, Azure Blob storage, or Amazon S3 storage for operation so that multiple pods can access shared content, such as collections.

The process for configuring object storage on the `AutomationHub` CR is similar for Amazon S3 and Azure Blob Storage.

If you are using file-based storage and your installation scenario includes automation hub, ensure that the storage option for Ansible Automation Platform Operator is set to `ReadWriteMany`. `ReadWriteMany` is the default storage option.

In addition, OpenShift Data Foundation provides a `ReadWriteMany` or S3 implementation. Also, you can set up NFS storage configuration to support `ReadWriteMany`. This, however, introduces the NFS server as a potential, single point of failure.

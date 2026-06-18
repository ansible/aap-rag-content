+++
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-proc_provision_ocp_storage_with_readwritemany"
template = "docs/aem-title.html"
title = "Provision OpenShift Container Platform storage with ReadWriteMany access mode - Red Hat Ansible Automation Platform 2.7"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-assembly_operator_install_operator/", "Install on OpenShift Container Platform"]]
category = "Install"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/install-proc_provision_ocp_storage_with_readwritemany/aem-page/install-proc_provision_ocp_storage_with_readwritemany.html"
last_crumb = "Provision OpenShift Container Platform storage with ReadWriteMany access mode"
modified = "2026-06-05T07:48:10.594Z"
multi_page_path = ""
name = "Provision OpenShift Container Platform storage with ReadWriteMany access mode"
oversized = "false"
page_slug = "install-proc_provision_ocp_storage_with_readwritemany"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/install-proc_provision_ocp_storage_with_readwritemany"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/install-proc_provision_ocp_storage_with_readwritemany/toc/toc.json"
type = "aem-page"
+++

# Provision OpenShift Container Platform storage with `ReadWriteMany` access mode

To ensure successful installation of Ansible Automation Platform Operator, you must provision your storage type for automation hub initially to `ReadWriteMany` access mode.

## About this task

## Procedure

1.  Go to Storage> (and then)PersistentVolume.
2.  Click Create PersistentVolume.
3.  In the first step, update the `accessModes` from the default `ReadWriteOnce` to `ReadWriteMany`.   1.  See [Provisioning](https://docs.redhat.com/en/documentation/openshift_container_platform/4.10/html-single/storage/index#persistent-storage-nfs-provisioning_persistent-storage-nfs) to update the access mode. for a detailed overview.
4.  Complete the additional steps in this section to create the persistent volume claim (PVC).

+++
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.6/administer-assembly_automation_mesh_operator_aap"
template = "docs/aem-title.html"
title = "Scale with automation mesh in an operator environment - Red Hat Ansible Automation Platform 2.6"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6", "2.6"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6/administer-assembly_automation_mesh_operator_aap/", "Scale with automation mesh in an operator environment"]]
category = "Administer"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/administer-assembly_automation_mesh_operator_aap/aem-page/administer-assembly_automation_mesh_operator_aap.html"
last_crumb = "Scale with automation mesh in an operator environment"
modified = "2026-05-21T14:12:12.122Z"
multi_page_path = ""
name = "Scale with automation mesh in an operator environment"
oversized = "false"
page_slug = "administer-assembly_automation_mesh_operator_aap"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.6"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/administer-assembly_automation_mesh_operator_aap"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/administer-assembly_automation_mesh_operator_aap/toc/toc.json"
type = "aem-page"
+++

# Scale with automation mesh in an operator environment

Scaling your automation mesh is available on OpenShift deployments of Red Hat Ansible Automation Platform and is possible through adding or removing nodes from your cluster dynamically, using the **Instances** resource of the Ansible Automation Platform UI, without running the installation script.

Instances serve as nodes in your mesh topology. Automation mesh enables you to extend the footprint of your automation. The location where you launch a job can be different from the location where the ansible-playbook runs.

To manage instances from the Ansible Automation Platform UI, you must have System Administrator or System Auditor permissions.

In general, the more processor cores (CPU) and memory (RAM) a node has, the more jobs that can be scheduled to run on that node at once.

## Prerequisites

The automation mesh is dependent on hop and execution nodes running on *Red Hat Enterprise Linux* (RHEL). Your Red Hat Ansible Automation Platform subscription grants you ten Red Hat Enterprise Linux licenses that can be used for running components of Ansible Automation Platform.

For more information about Red Hat Enterprise Linux subscriptions, see **Registering the system and managing subscriptions** in the Red Hat Enterprise Linux documentation.

The following steps prepare the RHEL instances for deployment of the automation mesh.

1. You require a Red Hat Enterprise Linux operating system. Each node in the mesh requires a static IP address, or a resolvable DNS hostname that Ansible Automation Platform can access.
2. Ensure that you have the minimum requirements for the RHEL virtual machine before proceeding. For more information, see the **System requirements**.
3. Deploy the RHEL instances within the remote networks where communication is required. For information about creating virtual machines, see **Creating Virtual Machines** in the *Red Hat Enterprise Linux* documentation. Remember to scale the capacity of your virtual machines sufficiently so that your proposed tasks can run on them.   - RHEL ISOs can be obtained from access.redhat.com.
  - RHEL cloud images can be built using Image Builder from console.redhat.com.

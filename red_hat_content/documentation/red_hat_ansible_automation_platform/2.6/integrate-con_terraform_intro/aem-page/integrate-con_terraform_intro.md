+++
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.6/integrate-con_terraform_intro"
template = "docs/aem-title.html"
title = "About the Terraform integration - Red Hat Ansible Automation Platform 2.6"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6", "2.6"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6/integrate-assembly_terraform_introduction/", "Integrate with IBM HashiCorp Terraform"]]
category = "Integrate"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/integrate-con_terraform_intro/aem-page/integrate-con_terraform_intro.html"
last_crumb = "About the Terraform integration"
modified = "2026-05-21T14:12:12.122Z"
multi_page_path = ""
name = "About the Terraform integration"
oversized = "false"
page_slug = "integrate-con_terraform_intro"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.6"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/integrate-con_terraform_intro"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/integrate-con_terraform_intro/toc/toc.json"
type = "aem-page"
+++

# About the Terraform integration

Many organizations find themselves using both Ansible Automation Platform and Terraform Enterprise or HCP Terraform, recognizing that these can work in harmony to create an improved experience for developers and operations teams.

While Terraform Enterprise and HCP Terraform excel at Infrastructure as Code (IaC) for provisioning and de-provisioning cloud resources, Ansible Automation Platform is a versatile, all-purpose automation solution ideal for configuration management, application deployment, and orchestrating complex IT workflows across diverse domains.

This integration directly addresses common challenges such as managing disparate automation tools, ensuring consistent configuration across hybrid cloud environments and accelerating deployment cycles. By bringing together Terraform’s declarative approach to infrastructure provisioning with Ansible Automation Platform’s procedural approach to configuration and orchestration, users can achieve:

- **Optimized costs:** Reduce cloud waste, minimize manual processes, and combat tool sprawl. This integration can lead to a significant reduction in infrastructure costs and a high return on investment.
- **Reduced risk:** Lower the risk of breaches, enforce policies, and significantly decrease unplanned downtime. The ability to review Terraform plan output before applying it in a workflow, with approval steps, enhances security and compliance.
- **Faster time to value:** Boost developer productivity and deploy new compute resources more rapidly, leading to a faster time to market. This is achieved through unified lifecycle management and automation for Day 0 (provisioning), Day 1 (configuration), and Day 2 (ongoing management) operations.


By enabling direct calls between Ansible Automation Platform and Terraform Enterprise or HCP Terraform, organizations can unlock time to value by creating combined workflows, reduce risk through enhanced product integrations, and enhance Infrastructure-as-Code with Ansible Automation Platform content and practices. This allows for unified lifecycle management, enabling tasks from initial provisioning and configuration to ongoing health checks, incident response, patching, and infrastructure optimization.

## Integration options for Terraform

Depending on your existing setup, you can integrate these products from Ansible Automation Platform or from Terraform. Migration paths are provided for community users and for migrating from the `cloud.terraform` collection to `hashicorp.terraform`.

### Ansible-initiated workflow

Ansible automation hub collections allow Ansible Automation Platform users to leverage the Terraform Enterprise or HCP Terraform provisioning capabilities.

 **hashicorp.terraform collection**

This collection provides API integration between Ansible Automation Platform and Terraform Enterprise or HCP Terraform. This solution works natively with Ansible Automation Platform and reduces setup complexity because it doesn’t require a binary installation and it includes a default execution environment.

 **cloud.terraform collection**

This collection provides CLI integration between Ansible Automation Platform and Terraform Enterprise or HCP Terraform. To use this collection, you must install a binary and create an execution environment.

Although this collection is supported, we recommend using the `hashicorp.terraform` collection instead to take advantage of its API capabilities.

### Migration workflows

Community edition users can migrate to Terraform Enterprise or HCP Terraform, and then integrate the Ansible Automation Platform capabilities using the `cloud.terraform` (CLI) collection. However, we recommend using the `hashicorp.terraform` (API) collection instead.

If you are already using the `cloud.terraform` collection, you can migrate to `hashicorp.terraform`.

### Terraform-initiated workflow

For existing Terraform Enterprise or HCP Terraform users, Terraform can directly call Ansible Automation Platform at the end of provisioning for a more seamless and secure workflow. This enables Terraform Enterprise or HCP Terraform users to enhance their immutable infrastructure automation with Ansible Automation Platform Day 2 automation capabilities and manage infrastructure updates and lifecycle events.

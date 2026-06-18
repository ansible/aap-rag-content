+++
template = "docs/aem-title.html"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.6/integrate-assembly_terraform_hashicorp_authenticating"
title = "Use hashicorp.terraform - Red Hat Ansible Automation Platform 2.6"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6", "2.6"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6/integrate-assembly_terraform_introduction/", "Integrate with IBM HashiCorp Terraform"]]
category = "Integrate"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/integrate-assembly_terraform_hashicorp_authenticating/aem-page/integrate-assembly_terraform_hashicorp_authenticating.html"
last_crumb = "Use hashicorp.terraform"
modified = "2026-05-21T14:12:12.122Z"
multi_page_path = ""
name = "Use hashicorp.terraform"
oversized = "false"
page_slug = "integrate-assembly_terraform_hashicorp_authenticating"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.6"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/integrate-assembly_terraform_hashicorp_authenticating"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/integrate-assembly_terraform_hashicorp_authenticating/toc/toc.json"
type = "aem-page"
+++

# Use hashicorp.terraform

After installing or migrating to `hashicorp.terraform`, users must create credentials to use with job templates in Ansible Automation Platform.

## Create a credential for hashicorp.terraform

Users must create a credential to use with job templates in Ansible Automation Platform.

### Before you begin

- You must have a Terraform API token.

### Procedure

1.  Log in to Ansible Automation Platform.
2.  From the navigation panel, select **Automation Execution> (and then)Infrastructure> (and then)Credentials**, and then select Create credential.
3.  From the **Credential type** list, select the **HCP Terraform** credential type.
4.  In the **Token** field, enter the Terraform API token.
5.  (Optional) Edit the **Description** field and select the TF organization from the **Organization** list.
6.  Click Save credential. You are ready to use the credential in a job template.

## Ansible-initiated workflows and patterns

After you set up authentication with Ansible Automation Platform, there are many possible Ansible-initiated workflows and patterns that you can apply.

Some workflows to consider include:

- **Performing traditional infrastructure set up.** You first configure Ansible Automation Platform to do a task that Terraform cannot manage. Then perform `terraform apply`. For example, configure Ansible Automation Platform to set up the state backend for an initial run. Or use Ansible Automation Platform to set up initial cloud credentials or users to interact with a cloud provider’s API.
- **Modifying infrastructure with Terraform.** In this case, turn off Ansible monitoring for the infrastructure that you are modifying. Then perform `terraform apply` with your changes. Finally, turn monitoring back on.
- **Automating `terraform apply` based on an event.** For example, you might want to trigger an event when a ServiceNow ticket is opened or a service catalog order is placed. Set up a webhook with in the Ansible Automation Platform UI so that Terraform is able to receive the event.

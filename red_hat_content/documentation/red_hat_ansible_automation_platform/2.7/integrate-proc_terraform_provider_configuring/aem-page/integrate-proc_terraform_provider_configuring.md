+++
title = "Configure the provider - Red Hat Ansible Automation Platform 2.7"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/integrate-proc_terraform_provider_configuring"
template = "docs/aem-title.html"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/integrate-assembly_terraform_introduction/", "Integrate with IBM HashiCorp Terraform"]]
category = "Integrate"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/integrate-proc_terraform_provider_configuring/aem-page/integrate-proc_terraform_provider_configuring.html"
last_crumb = "Configure the provider"
modified = "2026-06-05T07:48:10.594Z"
multi_page_path = ""
name = "Configure the provider"
oversized = "false"
page_slug = "integrate-proc_terraform_provider_configuring"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/integrate-proc_terraform_provider_configuring"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/integrate-proc_terraform_provider_configuring/toc/toc.json"
type = "aem-page"
+++

# Configure the provider

You must configure the provider to allow Terraform to reference and manage a subset of Ansible Automation Platform resources.

## Before you begin

- You have installed and configured Terraform Enterprise or HCP Terraform.
- You have installed the latest release version of `terraform-provider-aap` from the Terraform registry. Note:
      The default latest version on the Terraform registry might be a pre-release version (such as 1.2.3-beta). Select a supported release version, which uses a 1.2.3 format without dashes.

- You have created a username and password or an API token for Ansible Automation Platform. Environment variables are also supported. Note:
      Token authentication is recommended because users can manage tokens for specific integrations (such as Terraform), limit token access, and have full control over token lifecycle.

## About this task

The provider configuration belongs in the root module of a Terraform configuration. Child modules receive their provider configurations from the root module.

## Procedure

1.  Create a Terraform configuration (`.tf`) file. Include a `provider` block. The name given in the block header is the local name of the provider to configure. This provider should already be included in a `required_providers` block.  **Example**

```
# This example creates an inventory named `My new inventory`
# and adds a host `tf_host` and a group `tf_group` to it,
# and then launches a job based on the "Demo Job Template"
# in the "Default" organization using the inventory created.
#
terraform {
  required_providers {
    aap = {
      source = "ansible/aap"
    }
  }
}

    provider "aap" {
  host     = "https://AAP_HOST"
  token = "my-aap-token" # Do not record credentials directly in the Terraform configuration. Provide your token using the AAP_TOKEN environment variable.
}

    resource "aap_inventory" "my_inventory" {
  name         = "My new inventory"
  description  = "A new inventory for testing"
  organization = 1
  variables = jsonencode(
    {
      "foo" : "bar"
    }
  )
}

    resource "aap_group" "my_group" {
  inventory_id = aap_inventory.my_inventory.id
  name         = "tf_group"
  variables = jsonencode(
    {
      "foo" : "bar"
    }
  )
}

    resource "aap_host" "my_host" {
  inventory_id = aap_inventory.my_inventory.id
  name         = "tf_host"
  variables = jsonencode(
    {
      "foo" : "bar"
    }
  )
  groups = [aap_group.my_group.id]
}

    data "aap_job_template" "demo_job_template" {
  name              = "Demo Job Template"
  organization_name = "Default"
}

    # In order for passing the inventory id to the job template execution, the Inventory on the job template needs to be set to "prompt on launch"
resource "aap_job" "my_job" {
  inventory_id    = aap_inventory.my_inventory.id
  job_template_id = aap_job_template.demo_job_template.id

    # This resource creation needs to wait for the host and group to be created in the inventory
  depends_on = [
    aap_host.my_host,
    aap_group.my_group
  ]
}
```

2.  Add the configuration arguments, as shown in the previous example. You must configure the host and credentials. A full list of supported schema is available on the Terraform registry for your `aap` provider release version.   - **`host`:** (String) AAP server URL. Can also be configured using the `AAP_HOST` environment variable.
  - **`insecure_skip_verify`:** (Boolean) If `true`, configures the provider to skip TLS certificate verification. Can also be configured by setting the `AAP_INSECURE_SKIP_VERIFY` environment variable.
  - **`password`:** (String, Case Sensitive) Password to use for basic authentication. Ignored if the token is set. Note that hardcoded credentials are not recommended for security reasons. It is a best practice to use the `AAP_PASSWORD` environment variable instead.
  - **`timeout`:** (Number) Timeout specifies a time limit for requests made to the AAP server. Defaults to 5 if not provided. A timeout of zero means no timeout. Can also be configured by setting the `AAP_TIMEOUT` environment variable.
  - **`token`:** (String, Case Sensitive): Token to use for token authentication. Note that hardcoded credentials are not recommended for security reasons. It is a best practice to use the `AAP_TOKEN` environment variable instead.
  - **`username`:** (String) Username to use for basic authentication. Ignored if the token is set. Can also be configured by setting the `AAP_USERNAME` environment variable.

3.  (Optional) You can use expressions in the values of these configuration arguments, but can only reference values that are known before the configuration is applied.
4.  (Optional) You can also use an `alias` meta-argument that is defined by Terraform and is available for all provider blocks. `alias` lets you use the same provider with different configurations for different resources.

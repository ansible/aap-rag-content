+++
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/integrate-proc_terraform_provider_using_tf_actions_direct_job"
template = "docs/aem-title.html"
title = "Use TF Actions as a direct job - Red Hat Ansible Automation Platform 2.7"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/integrate-assembly_terraform_introduction/", "Integrate with IBM HashiCorp Terraform"]]
category = "Integrate"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/integrate-proc_terraform_provider_using_tf_actions_direct_job/aem-page/integrate-proc_terraform_provider_using_tf_actions_direct_job.html"
last_crumb = "Use TF Actions as a direct job"
modified = "2026-06-05T07:48:10.594Z"
multi_page_path = ""
name = "Use TF Actions as a direct job"
oversized = "false"
page_slug = "integrate-proc_terraform_provider_using_tf_actions_direct_job"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/integrate-proc_terraform_provider_using_tf_actions_direct_job"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/integrate-proc_terraform_provider_using_tf_actions_direct_job/toc/toc.json"
type = "aem-page"
+++

# Use TF Actions as a direct job

When you use TF Actions to launch jobs directly with Ansible Automation Platform, the process is streamlined and sequential.

## Before you begin

- You have configured the AAP Terraform provider to authenticate with Ansible Automation Platform.
- You have configured the AWS Terraform provider to authenticate with Amazon Web Services. Note:
      The example below uses Amazon Web Services (AWS) and requires an AWS account that might incur charges. You can adapt the pattern to use a different cloud provider.

- You have job templates configured with:
  * Inventory set to **prompt on launch**.
  * A machine credential (private key) matching a public key available in a local file.

## About this task

The benefit of this approach is a clean, predictable state: the Ansible job launches during the Terraform apply cycle, and Terraform receives a clear, binary status. Note that each change launches a separate job with identical configuration.

This method can be useful when you want to execute Ansible automation against newly provisioned servers. For example, last mile provisioning or applying a routine security patching job on a new host.

## Procedure

1.  Define the `aap_job_launch` action in your `*.tf` file.
2.  Add a lifecycle job block to define which action will be invoked during the proper lifecycle event trigger.  **Example**

```
terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 6.0"
    }

    aap = {
      source  = "ansible/aap"
      version = "~> 1.4.0"
    }
  }
}

    provider "aap" {
  # Configure authentication as needed.
}

    provider "aws" {
  region = "us-west-1"
  # Configure authentication as needed.
}

    variable "public_key_path" {
  type        = string
  description = "Local path to a public key file to inject into the VM. Your AAP Job Template must have the matching private key configured as a machine credential."
}

    resource "aws_key_pair" "key_pair" {
  key_name   = "aap-terraform-actions-demo-key"
  public_key = file(var.public_key_path)
}

    data "aws_ami" "rhel_ami" {
  most_recent = true

    filter {
    name   = "name"
    values = ["RHEL-9*"]
  }

    filter {
    name   = "virtualization-type"
    values = ["hvm"]
  }

    owners = ["309956199498"] # Red Hat
}

    resource "aws_instance" "instance" {
  ami                         = data.aws_ami.rhel_ami.id
  instance_type               = "t2.micro"
  associate_public_ip_address = true
  key_name                    = aws_key_pair.key_pair.key_name
}

    # Look up Organization ID

    data "aap_organization" "organization" {
  name = "Default"
}

    # Create an inventory

    resource "aap_inventory" "inventory" {
  name         = "Actions Demo Inventory"
  organization = data.aap_organization.organization.id
}

    data "aap_job_template" "job_template" {
  name              = "Demo Job Template"
  organization_name = data.aap_organization.organization.name
}

    #
# Direct job launch action example
#

    resource "aap_host" "host" {
  inventory_id = aap_inventory.inventory.id
  name         = resource.aws_instance.instance.public_ip
  # Setting a value of 10 for SSH retries because terraform will mark the
  # instance 'created' before it is ready to accept connections from Ansible.
  variables = jsonencode(
    {
      "ansible_ssh_retries" : 10
    }
  )
  # Configure a job launch after the host is created in inventory
  lifecycle {
    action_trigger {
      events  = [after_create]
      actions = [action.aap_job_launch.job_launch]
    }
  }
}

    action "aap_job_launch" "job_launch" {
  config {
    inventory_id        = aap_inventory.inventory.id
    job_template_id     = data.aap_job_template.job_template.id
    wait_for_completion = true
  }
}
```

3.  (Required) Change the job template name and the inventory name in this example to your corresponding variables.
4.  (Optional) You can set `owners` to the Red Hat RHEL image ID so that the latest image is used each time the job runs.
5.  (Optional) Set additional parameters as needed. For example, you can set `wait_for_completion` to `true`, then Terraform will wait until this job is created and reaches any final state before continuing. You can also set `wait_for_completion_timeout_seconds` to control the timeout limit.
6.  Update and commit the Terraform code.
7.  Execute the Terraform plan and apply it.

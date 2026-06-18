+++
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/integrate-assembly_terraform_provider_using_tf_actions_eda"
title = "Use TF Actions with Event-Driven Ansible - Red Hat Ansible Automation Platform 2.7"
template = "docs/aem-title.html"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/integrate-assembly_terraform_introduction/", "Integrate with IBM HashiCorp Terraform"]]
category = "Integrate"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/integrate-assembly_terraform_provider_using_tf_actions_eda/aem-page/integrate-assembly_terraform_provider_using_tf_actions_eda.html"
last_crumb = "Use TF Actions with Event-Driven Ansible"
modified = "2026-06-05T07:48:10.594Z"
multi_page_path = ""
name = "Use TF Actions with Event-Driven Ansible"
oversized = "false"
page_slug = "integrate-assembly_terraform_provider_using_tf_actions_eda"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/integrate-assembly_terraform_provider_using_tf_actions_eda"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/integrate-assembly_terraform_provider_using_tf_actions_eda/toc/toc.json"
type = "aem-page"
+++

# Use TF Actions with Event-Driven Ansible

Event-Driven Ansible is an automation feature that allows Ansible Automation Platform to react to real-time events, instead of being triggered on a schedule or by a manual request.

## Configure an event stream for TF actions

To use TF Actions with Event-Driven Ansible, you must first configure the event stream in Ansible Automation Platform. TF actions will post events to this stream.

### Before you begin

- You have configured the AAP Terraform provider to authenticate with Ansible Automation Platform.
- You have configured the AWS Terraform provider to authenticate with Amazon Web Services. Note:
  The example below uses Amazon Web Services (AWS) and requires an AWS account that might incur charges. You can adapt the pattern to use a different cloud provider.

- You have an Ansible Automation Platform inventory named **EDA Actions Demo Inventory** in the **Default** organization.
- You have job templates configured with:
  * Inventory set to **EDA Actions Demo Inventory**.
  * A machine credential (private key) matching a public key available in a local file.

### Procedure

1.  Log in to the Ansible Automation Platform user interface.
2.  Navigate to **Automation Decisions> (and then)Event Streams**.
3.  Click Create event stream.
4.  On the **Create event stream** page, edit the fields:

  - **Name:** A descriptive, unique name for your event stream (such as `Terraform provider_Events`).
  - **Organization:** Select the organization this event stream will belong to (usually `Default` or your specific organization).
  - **Event stream type:** Select the type that matches how you want to receive events. **Basic Event Stream** (username/password) is supported with this integration.
  - **Credential:** Select a credential that you have pre-created for authentication with this event stream.
  - **Headers:** (Optional) Enter comma-separated HTTP header keys that you want to include in the event payload that gets forwarded to the rulebook. Leave this empty to include all headers.
  - **Forward events to rulebook activation:** This option is typically enabled by default. Disabling it is useful for testing and diagnosing your connection and incoming data without inadvertently triggering any automation.

5.  Click Create event stream. Then navigate to **Automation Decisions> (and then)Event Streams** to verify the event stream was created and see the number of events received so far. You can also click on the specific stream to see its detailed configuration, including the organization, event stream type, associated credential, and event forwarding settings.

6.  Set up a rule book activation. Make sure to:
  1.  Add the event stream to the rulebook.
  2.  (Recommended) Select the **Rulebook activation enabled?** option to automatically start the activation after creation.
  3.  Activate the rulebook.
7.  Select **Automation Decisions> (and then)Rulebook Activations** to verify that the rulebook is active and check its status.

## Configure TF Actions

To connect the event stream to Terraform actions, you configure the main TF file (`*.tf`) in Terraform.

### Procedure

1.  Add a lifecycle block to call the Event-Driven Ansible event stream to your `*.tf` file. The `after_create` action will trigger the `action.aap_eda_eventstream_post.create`.  **Example**

    The following example shows a `lifecycle` block added to the provisioning of an AWS EC2 server. After the new server is provisioned, the action runs.

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

    variable "event_stream_username" {
  type = string
}

    variable "event_stream_password" {
  type = string
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

    # Look up an inventory

    data "aap_inventory" "inventory" {
  name              = "EDA Actions Demo Inventory"
  organization_name = "Default"
}

    #
# EDA Event launch action example
#

    resource "aap_host" "host" {
  inventory_id = data.aap_inventory.inventory.id
  name         = resource.aws_instance.instance.public_ip
  # Configure an EDA eventstream POST after the host is created in inventory
  lifecycle {
    action_trigger {
      events  = [after_create]
      actions = [action.aap_eda_eventstream_post.event_post]
    }
  }
}

    data "aap_eda_eventstream" "eventstream" {
  name = "TF Actions Event Stream"
}

    action "aap_eda_eventstream_post" "event_post" {
  config {
    limit             = "all"
    template_type     = "job"
    job_template_name = "Demo Job Template"
    organization_name = "Default"
    event_stream_config = {
      username = var.event_stream_username
      password = var.event_stream_password
      url      = data.aap_eda_eventstream.eventstream.url
    }
  }
}
```

2.  (Required) Configure the following parameters:

  - **`event_stream_config`:** (Attributes) Details for the Event-Driven Ansible event stream. You must include:
    * **`username`:** (String) Username to use when performing the POST to the event stream URL
    * **`password`:** (String) Password to use when performing the POST to the event stream URL
    * **`url`:** (String) URL to receive the event POST
  - **`limit`:** (String) Ansible Automation Platform limit for job execution
  - **`organization_name`:** (String) Organization name
  - **`template_type`:** (String) Template type: either `job` or `workflow_job`

3.  (Optional) You can set `owners` to the Red Hat RHEL image ID so that the latest image is used each time the job runs.
4.  (Optional) Set additional parameters as needed.
5.  Configure an action integration with event payload specifications and target rulebook mapping.  **Example:**

```
- name: Dispatch TF Workflow Job Template Action
      condition: event.payload.template_type == "workflow"
      throttle:
        once_after: 1 minute
        group_by_attributes:
          - event.payload.workflow_template_name
          - event.payload.limit
          - event.payload.organization_name
      actions:
        - debug:
            msg: "Executing Workflow Template {{ event.payload.workflow_template_name }}"
        - run_workflow_template:
            name: "{{ event.payload.workflow_template_name }}"
            organization: "{{ event.payload.organization_name }}"
        - debug:
            msg: "Executed Workflow Job Template {{ event.payload.workflow_template_name }}"
```

## Create and apply the plan

After you configure your Terraform plan to include Event-Driven Ansible events, you create and apply the plan to trigger the events.

### Procedure

1.  Run `terraform init` to initialize your working directory.
2.  Use `terraform plan` to commit to create the plan. The following example also saves the plan to a file named `tfplan.out`, but you can specify any name for the plan. Saving the plan is a best practice for automation because the saved plan is strictly enforced.

```
terraform plan -out=tfplan.out
```

3.  Review the plan output.
4.  Apply the saved plan.

```
terraform apply tfplan.out
```
    This creates and sends an event to the specified event stream. As each resource is created, TF actions are invoked and the corresponding Ansible Automation Platform playbooks are executed sequentially.

### Results

1. Verify that the runs are updated in the Terraform user interface. Drill down on a resource to see that the action was invoked and a post event was executed.
2. From the Ansible Automation Platform user interface, verify that the event is successfully received by (EDAName} and triggers the appropriate rulebook activation:
  1. Check the **Event Streams** dashboard to see the TF Actions events were received.
  2. Check the **Jobs** dashboard to see the jobs running sequentially and with a **Success** status.
  3. Check the **Inventory** dashboard to see the updates. For example, if you created new servers, check the **Hosts** tab for the Terraform provisioned inventory.

## Example rulebook

The following rulebook example shows how to use TF actions and Event-Driven Ansible to listen for events on a webhook.

```
- name: Listen for events on a webhook
  hosts: all

  ## Define our source for events

  sources:
    - ansible.eda.webhook:
        host: 0.0.0.0
        port: 5000
      filters:
        - ansible.eda.insert_hosts_to_meta:
            host_path: payload.limit

  ## Define the conditions we are looking for

  rules:
    - name: Dispatch TF Job Template Action
      condition: event.payload.template_type == "job"
      throttle:
        once_after: 1 minute
        group_by_attributes:
          - event.payload.job_template_name
          - event.payload.limit
          - event.payload.organization_name
      actions:
        - debug:
            msg: "Executing Job Template {{ event.payload.job_template_name }}"
        - run_job_template:
            name: "{{ event.payload.job_template_name }}"
            organization: "{{ event.payload.organization_name }}"
        - debug:
            msg: "Executed Job Template {{ event.payload.job_template_name }}"
    - name: Dispatch TF Workflow Job Template Action
      condition: event.payload.template_type == "workflow"
      throttle:
        once_after: 1 minute
        group_by_attributes:
          - event.payload.workflow_template_name
          - event.payload.limit
          - event.payload.organization_name
      actions:
        - debug:
            msg: "Executing Workflow Template {{ event.payload.workflow_template_name }}"
        - run_workflow_template:
            name: "{{ event.payload.workflow_template_name }}"
            organization: "{{ event.payload.organization_name }}"
        - debug:
            msg: "Executed Workflow Job Template {{ event.payload.workflow_template_name }}"
```

+++
title = "Migrate from cloud.terraform to hashicorp.terraform - Red Hat Ansible Automation Platform 2.6"
template = "docs/aem-title.html"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.6/integrate-assembly_terraform_migrating_from_cloud_terraform"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6", "2.6"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6/integrate-assembly_terraform_introduction/", "Integrate with IBM HashiCorp Terraform"]]
category = "Integrate"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/integrate-assembly_terraform_migrating_from_cloud_terraform/aem-page/integrate-assembly_terraform_migrating_from_cloud_terraform.html"
last_crumb = "Migrate from cloud.terraform to hashicorp.terraform"
modified = "2026-05-21T14:12:12.122Z"
multi_page_path = ""
name = "Migrate from cloud.terraform to hashicorp.terraform"
oversized = "false"
page_slug = "integrate-assembly_terraform_migrating_from_cloud_terraform"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.6"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/integrate-assembly_terraform_migrating_from_cloud_terraform"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/integrate-assembly_terraform_migrating_from_cloud_terraform/toc/toc.json"
type = "aem-page"
+++

# Migrate from `cloud.terraform` to `hashicorp.terraform`

If you are using the existing `cloud.terraform` (CLI-based) collection, you can migrate your existing playbooks to the `hashicorp.terraform` (API-based) collection. The main modules for `hashicorp.terraform` that you must configure are `hashicorp.terraform.configuration_version` and `hashicorp.terraform.run`.

## Configure the `hashicorp.terraform.configuration_version` module

To migrate to the `hashicorp.terraform` collection, you must configure the `hashicorp.terraform.configuration_version` module. This module manages configuration versions in Terraform Enterprise or HCP Terraform.

### Before you begin

- Install the Ansible Automation Platform certified `hashicorp.terraform` collection.
- Verify that a valid organization and workspace are correctly set up in Terraform Enterprise or HCP Terraform.

### Procedure

1.  Replicate your automation tasks from the `cloud.terraform` modules.  **Example**

```
- name: Create configuration version with auto_queue_runs to false
  hashicorp.terraform.configuration_version:
   workspace_id: ws-1234
   configuration_files_path: "/usr/home/tf"
   auto_queue_runs: false
   tf_validate_certs: true
   poll_interval: 3
   poll_timeout: 15
   state: present
```

2.  Configure the following required parameters:

  - **`workspace_id` or `workspace` + `organization`:** The workspace ID or the workspace name and organization where the configuration version will be created and the file will be uploaded (for `state: present`).
  - **`configuration_files_path`:** The path where the required Terraform Enterprise or HCP Terraform files will be uploaded to create a configuration version (for `state: present`). The module accepts two file types for `configuration_files_path`:
    * **Directory:** Any folder containing Terraform Enterprise or HCP Terraform files. The module auto-creates the .tar.gz file from all contents recursively.
    * **.tar.gz Archive:** Pre-compressed gzip tarball. The module validates TAR format and gzip compression.
  - **`configuration_version_id`:** The configuration version ID that will be archived (`state: archived`). This action deletes the associated uploaded .tar.gz file. Note the following:
    * Only uploaded versions that were created using the API or CLI, have no active runs, and are not the current version for any workspace can be archived.
    * When the `configuration_version_id` is unspecified, Terraform Enterprise or HCP Terraform selects the latest approved `configuration_version_id` in the workspace.
  - **auto_queue_runs:** Determines if Terraform Enterprise or HCP Terraform automatically starts a run after the configuration upload (`true` by default) or requires manual initiation (`false`).

3.  Set additional optional parameters as needed.

## Configure the `hashicorp.terraform.run` module

The `hashicorp.terraform.run` module lets you manage Terraform Enterprise or HCP Terraform runs using create, apply, cancel, and discard operations. You can trigger plans or apply operations on specified workspaces with customizable settings.

### Before you begin

- Ensure that a valid Terraform API token is properly configured to authenticate with your Terraform Enterprise or HCP Terraform environment.
- Verify that a valid organization and workspace are correctly set up in Terraform Enterprise or HCP Terraform.

### Procedure

1.  Create a run module.  **Example**

```
- name: Create a destroy run with auto_apply
  hashicorp.terraform.run:
  workspace_id: ws-1234
  run_message: "destroy vpc"
  state: "present"
  tf_token: <your token>
  is_destroy: true
  auto_apply: true
  target_addrs:
    - "aws_vpc.vpc1"
    - "aws_vpc.vpc2"
  poll: true
  poll_interval: 10
  poll_timeout: 30
```

2.  Configure the following required parameters:

  - **`workspace_id` or `workspace` + `organization`:** The workspace ID or the workspace name and organization where the configuration version will be created and the file will be uploaded (for `state: present`).
  - **`run_id`:** The unique identifier of the run to apply, cancel, or discard operations.
  - **`tf_token`:** The Terraform API authentication token. If this value is not set, the `TF_TOKEN` environment variable is used.

3.  (Optional) Configure the built-in polling options that determine the wait period for Terraform Enterprise or HCP Terraform operations to complete:

  - **`poll: true`:** (Default) Checks the run status every `poll_interval` seconds (default: 5s) until completion or `poll_timeout` (default: 25s) is reached, returning the final status.
  - **`poll: false`:** Returns immediately after initiating the run without waiting.

4.  Set additional optional parameters as needed.

## Examples for `hashicorp.terraform` modules

These before and after examples help users understand how the modules can be configured in a real world environment.

### Plan Only

-  **Before (`cloud.terraform.terraform`):**

```
- name: Create a plan file using check mode
  cloud.terraform.terraform:
   force_init: true
   project_path: "/usr/home/tf"
   plan_file: "/usr/home/tf/terraform.tfplan"
   state: present
   check_mode: true
   check_destroy: true
   variables:
     environment: prod
```


-  **After (`hashicorp.terraform.*`):**
  * The `configuration_version` module:

```
- name: Create configuration version with auto_queue_runs to false
  hashicorp.terraform.configuration_version:
   workspace_id: ws-1234
   configuration_files_path: "usr/home/tf_files"
   auto_queue_runs: false
   tf_validate_certs: true
   poll_interval: 5
   poll_timeout: 10
   state: present
```

  * The `plan_only` run with the run module:

```
- name: Create a plan only run with variables
  hashicorp.terraform.run:
   workspace_id: ws-1234
   run_message: "plan-only vpc creation"
   poll: false
   state: "present"
   tf_token: "{{ tfc_token }}"
   plan_only: true
   variables:
    - key: "env"
      value: "production"
```

### Plan and apply

-  **Before (`cloud.terraform.terraform`):**
  1. Generate the plan:

```
- name: Plan and Apply Workflow - Step 1 - Generate Plan
  cloud.terraform.terraform:
   force_init: true
   project_path: "/usr/home/tf"
   plan_file: "/usr/home/tf/workflow.tfplan"
   state: present
   check_mode: true
   variables:
     environment: prod
```

  2. Apply the plan:

```
- name: Plan and Apply Workflow - Step 2 - Apply Plan
  cloud.terraform.terraform:
   project_path:  "/usr/home/tf"
   plan_file: "/usr/home/tf/workflow.tfplan"
   state: present
```

-  **After (`hashicorp.terraform.run`):**
  1. The `configuration_version` module:

```
- name: Create configuration version with auto_queue_runs to false
  hashicorp.terraform.configuration_version:
   workspace_id: ws-1234
   configuration_files_path: "usr/home/tf_files"
   auto_queue_runs: false
   tf_validate_certs: true
   poll_interval: 5
   poll_timeout: 10
   state: present
```

  2. The run module with two options for plan and apply workflow:
- **Option 1:** Uses the `auto_apply` parameter to handle both the plan and apply workflows:

```
- name: Create a run with auto_apply
  hashicorp.terraform.run:
   workspace_id: ws-1234
   run_message: "destroy vpc"
   state: "present"
   tf_token: "{{ tfc_token }}"
   auto_apply: true
   poll: true
   poll_interval: 10
   poll_timeout: 30
```

- **Option 2:** Uses two sub-steps to create a `save_plan` run and then apply it:
  1. Create the plan:

```
- name: Create a save plan run
  hashicorp.terraform.run:
   workspace_id: ws-1234
   run_message: "save plan vpc creation"
   state: "present"
   tf_token: "{{ tfc_token }}"
   poll: true
   poll_interval: 10
   poll_timeout: 30
   save_plan: true
```

  2. Apply the plan. You get the `run_id` from the output of the run module task:

```
- name: Apply the save plan run
  hashicorp.terraform.run:
   run_id: run-1234
   state: "applied"
   tf_token: "{{ tfc_token }}"
   poll: true
   poll_interval: 10
   poll_timeout: 30
```

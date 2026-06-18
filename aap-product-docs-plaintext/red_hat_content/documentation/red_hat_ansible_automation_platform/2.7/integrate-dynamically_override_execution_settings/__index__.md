# Dynamically override execution settings

As an administrator using Terraform provider, you can configure optional Prompt on Launch parameters in Ansible job and workflow templates to dynamically override default execution settings at runtime.placeholder.

This means that you can use one Ansible template with different Terraform `*.tf` files to deploy many environments. Terraform provides the values when the Ansible job or workflow runs.The Ansible playbooks and templates stored in Ansible Automation Platform remain reusable and independent of the specific Terraform configuration that provisioned them.

You must take the following steps to use Prompt on Launch:

- **Ansible UI:** Select the **Prompt on Launch** checkbox for any of the supported fields in the Ansible job or workflow template.
- **Terraform:** Set the values for the corresponding fields in the `*.tf` file that will launch jobs from that template. If the corresponding value is not set in the `*.tf` file, then the run fails and Ansible Automation Platform sends an error message.
The supported Prompt on Launch settings include:

- **Inventory:** Allows Terraform to specify the inventory that will be used by the Ansible job template.
- **Extra variables:** To use extra variables to pass data or trigger actionable workflows, provide either a JSON or YAML string.
- **Job tag:** Tags to include in the workflow job run.
- **Labels:** Labels can be used to describe a job template, such as dev or test. You can use labels to group and filter job templates and completed jobs in the display.
- **Limit:** The Prompt on Launch option restricts a job template to run against only a specific host or group of hosts within an inventory. Note:
When running as part of a workflow, the workflow job template limit is used instead.

- **Skip tag:** Tags to ignore in the workflow job run.

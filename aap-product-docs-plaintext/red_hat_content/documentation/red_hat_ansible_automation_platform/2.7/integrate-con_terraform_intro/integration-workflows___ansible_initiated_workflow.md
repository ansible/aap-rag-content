# About the Terraform integration
## Integration options for Terraform
### Ansible-initiated workflow

Ansible automation hub collections allow Ansible Automation Platform users to leverage the Terraform Enterprise or HCP Terraform provisioning capabilities.

**hashicorp.terraform collection**

This collection provides API integration between Ansible Automation Platform and Terraform Enterprise or HCP Terraform. This solution works natively with Ansible Automation Platform and reduces setup complexity because it doesn’t require a binary installation and it includes a default execution environment.

**cloud.terraform collection**

This collection provides CLI integration between Ansible Automation Platform and Terraform Enterprise or HCP Terraform. To use this collection, you must install a binary and create an execution environment.

Although this collection is supported, we recommend using the `hashicorp.terraform` collection instead to take advantage of its API capabilities.


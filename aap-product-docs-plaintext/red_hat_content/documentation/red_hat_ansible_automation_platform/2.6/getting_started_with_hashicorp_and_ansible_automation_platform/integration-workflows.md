# 1. Terraform integration
## 1.1. About the Terraform integration
### 1.1.2. Integration workflows




Depending on your existing setup, you can integrate these products from Ansible Automation Platform or from Terraform. Migration paths are provided for community users and for migrating from the `cloud.terraform` collection to `hashicorp.terraform` .

#### 1.1.2.1. Ansible-initiated workflow




Ansible automation hub collections allow Ansible Automation Platform users to leverage the Terraform Enterprise or HCP Terraform provisioning capabilities.

**hashicorp.terraform collection**

This collection provides API integration between Ansible Automation Platform and Terraform Enterprise or HCP Terraform. This solution works natively with Ansible Automation Platform and reduces setup complexity because it doesn’t require a binary installation and it includes a default execution environment.

**cloud.terraform collection**

This collection provides CLI integration between Ansible Automation Platform and Terraform Enterprise or HCP Terraform. To use this collection, you must install a binary and create an execution environment.

Although this collection is supported, we recommend using the `hashicorp.terraform` collection instead to take advantage of its API capabilities.

#### 1.1.2.2. Migration workflows




Community edition users can migrate to Terraform Enterprise or HCP Terraform, and then integrate the Ansible Automation Platform capabilities using the `cloud.terraform` (CLI) collection. However, we recommend using the `hashicorp.terraform` (API) collection instead.

If you are already using the `cloud.terraform` collection, you can migrate to `hashicorp.terraform` .

#### 1.1.2.3. Terraform-initiated workflow




For existing Terraform Enterprise or HCP Terraform users, Terraform can directly call Ansible Automation Platform at the end of provisioning for a more seamless and secure workflow. This enables Terraform Enterprise or HCP Terraform users to enhance their immutable infrastructure automation with Ansible Automation Platform Day 2 automation capabilities and manage infrastructure updates and lifecycle events.


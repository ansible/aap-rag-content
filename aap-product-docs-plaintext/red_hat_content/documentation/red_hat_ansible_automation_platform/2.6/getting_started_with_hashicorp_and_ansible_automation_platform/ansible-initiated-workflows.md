# 1. Terraform integration
## 1.2. Integrating from Ansible Automation Platform
### 1.2.3. Ansible-initiated workflows




After you set up authentication with Ansible Automation Platform, there are many possible Ansible-initiated workflows and many patterns that you can apply.

Some workflows to consider include:

-  **Performing traditional infrastructure set up.** You first configure Ansible Automation Platform to do a task that Terraform cannot manage. Then perform `    terraform apply` . For example, configure Ansible Automation Platform to set up the state backend for an initial run. Or use Ansible Automation Platform to set up initial cloud credentials or users to interact with a cloud provider’s API.
-  **Modifying infrastructure with Terraform.** In this case, turn off Ansible monitoring for the infrastructure that you are modifying. Then perform `    terraform apply` with your changes. Finally, turn monitoring back on.
-  **Automating `    terraform apply` based on an event.** For example, you might want to trigger an event when a ServiceNow ticket is opened or a service catalog order is placed. Set up a webhook with in the Ansible Automation Platform UI so that Terraform is able to receive the event.



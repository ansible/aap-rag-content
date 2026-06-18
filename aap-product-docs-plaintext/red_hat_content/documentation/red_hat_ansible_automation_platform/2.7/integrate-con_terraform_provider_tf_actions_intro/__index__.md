# About Terraform Actions and Ansible Automation Platform

The Terraform (TF) Actions adds an imperative `action` block to the HCL language, letting you execute steps after infrastructure is provisioned without leaving the declarative Terraform workflow. This keeps the entire infrastructure and configuration process visible in your Terraform configuration.

TF Actions can be used to trigger Ansible automation for configuration management, such as sending an event and payload to Ansible Automation Platform to configure newly provisioned virtual machines.

There are two actions implemented with the Terraform provider for Ansible Automation Platform:

- **Launch a job directly:** Runs the job as a direct, immediate execution request to Ansible Automation Platform. You must explicitly define which specific Ansible Automation Platform job template the TF Action should call.
- **Use Event-Driven Ansible:** Sends an event to Ansible Automation Platform, which then uses rulebooks to intelligently decide which playbook to run based on the event’s payload. This allows for more dynamic, scalable and reactive automation.

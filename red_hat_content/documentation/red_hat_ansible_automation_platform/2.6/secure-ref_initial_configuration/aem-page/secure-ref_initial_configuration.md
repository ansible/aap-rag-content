+++
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.6/secure-ref_initial_configuration"
title = "Recommended security practices for access controls - Red Hat Ansible Automation Platform 2.6"
template = "docs/aem-title.html"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6", "2.6"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6/secure-assembly_hardening_aap/", "Harden the platform security posture"]]
category = "Secure"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/secure-ref_initial_configuration/aem-page/secure-ref_initial_configuration.html"
last_crumb = "Recommended security practices for access controls"
modified = "2026-05-21T14:12:12.122Z"
multi_page_path = ""
name = "Recommended security practices for access controls"
oversized = "false"
page_slug = "secure-ref_initial_configuration"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.6"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/secure-ref_initial_configuration"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/secure-ref_initial_configuration/toc/toc.json"
type = "aem-page"
+++

# Recommended security practices for access controls

Granting access to certain parts of the system exposes security vulnerabilities. Apply the following practices to help secure access:

- Minimize access to system administrative accounts. There is a difference between the user interface (web interface) and access to the operating system that the automation controller is running on. A system administrator or super user can access, edit, and disrupt any system application. Anyone with root access to automation controller has the potential ability to decrypt those credentials, and so minimizing access to system administrative accounts is crucial for maintaining a secure system.
- Minimize local system access. Automation controller should not require local user access except for administrative purposes. Non-administrator users should not have access to the automation controller system.
- Enforce separation of duties. Different components of automation might need to access a system at different levels. Use different keys or credentials for each component so that the effect of any one key or credential vulnerability is minimized.
- Restrict automation controller to the minimum set of users possible for low-level automation controller configuration and disaster recovery only. In an automation controller context, any automation controller ‘system administrator’ or ‘superuser’ account can edit, change, and update any inventory or automation definition in automation controller.

## Use a configuration as code paradigm

Red Hat collections provide automation content to manage Red Hat Ansible Automation Platform infrastructure and configuration as code (CaC). This enables platform automation through CaC. Review the security implications of this approach.

The following Ansible content collections are available for managing Ansible Automation Platform components using an infrastructure as code methodology, all of which are found on the [Ansible Automation Hub](https://console.redhat.com/ansible/automation-hub):

*Table 1. Ansible content collections*

| Validated Collection           | Collection Purpose                                                                                                                                                                                                                                                                                                                                                                                                  |
| ------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <br> `infra.aap_utilities`     | <br>Ansible content for automating day 1 and day 2 operations of Ansible Automation Platform, including installation, backup and restore, certificate management, and more.                                                                                                                                                                                                                                         |
| <br> `infra.aap_configuration` | <br>A collection of roles to manage the creation of Ansible Automation Platform components, including users and groups (RBAC), projects, job templates and workflows, credentials, and more. This collection includes functionality from the older `infra.controller_configuration`, `infra.ah_configuration` and `infra.eda_configuration` and should be used in their place with Ansible Automation Platform 2.6. |
| <br> `infra.ee_utilities`      | <br>A collection of roles for creating and managing execution environment images, or migrating from the older Tower virtualenvs to execution environments.                                                                                                                                                                                                                                                          |


Many organizations use CI/CD platforms to configure pipelines or other methods to manage this type of infrastructure. However, using Ansible Automation Platform natively, a webhook can be configured to link a Git-based repository natively. In this way, Ansible can respond to Git events to trigger Job Templates directly. This removes the need for external CI components from this overall process and thus reduces the attack surface.

These practices enable version control of all infrastructure and configuration. Apply Git best practices to ensure proper code quality inspection before being synchronized into Ansible Automation Platform. Relevant Git best practices include the following:

- Creating pull requests.
- Ensuring that inspection tools are in place.
- Ensuring that no plain text secrets are committed.
- Ensuring that pre-commit hooks and any other policies are followed.


CaC also encourages using external vault systems which removes the need to store any sensitive data in the repository, or deal with having to individually vault files as needed. This is particularly important when storing Ansible Automation Platform configuration in a source code repository, as automation controller credentials and Event-Driven Ansible credentials must be provided to the collection variables in plain text which should not be committed to a source repository. For more information on using external vault systems, see [External credential vault considerations](/documentation/en-us/red_hat_ansible_automation_platform/2.6/secure-con_credential_management_planning#con-external-credential-vault "Secrets management is an essential component of maintaining a secure automation platform. We recommend the following secrets management practice:").

## Configure centralized logging

Configure centralized logging to collect all Ansible Automation Platform logs in a single location. Consolidating this data makes it easier to troubleshoot issues, detect tampering, and helps ensure the overall security and stability of your environment.

There are several additional benefits including:

- The data is sent in JSON format over a HTTP connection using minimal service-specific tweaks engineered in a custom handler or through an imported library. The types of data that are most useful to the controller are job fact data, job events/job runs, activity stream data, and log messages.
- Deeper insights into the automation process by analyzing logs from different parts of the infrastructure, including playbook execution details, task outcomes, and system events.
- Identifying performance bottlenecks and optimizing the Ansible playbooks by analyzing execution times and resource usage from the logs.
- Centralized logging helps meet compliance mandates by providing a single source of truth for auditing purposes.
- Third Party integration with a centralized log management platform like Splunk, Logstash, ElasticSearch, or Loggly to collect and analyze logs.


The logging aggregator service works with the following monitoring and data analysis systems:

- Splunk
- Loggly
- Sumologic
- Elastic stack (formerly ELK stack)

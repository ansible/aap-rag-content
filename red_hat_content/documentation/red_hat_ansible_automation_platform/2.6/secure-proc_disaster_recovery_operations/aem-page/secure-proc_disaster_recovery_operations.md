+++
title = "Disaster recovery and operational continuity - Red Hat Ansible Automation Platform 2.6"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.6/secure-proc_disaster_recovery_operations"
template = "docs/aem-title.html"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6", "2.6"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6/secure-assembly_hardening_aap/", "Harden the platform security posture"]]
category = "Secure"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/secure-proc_disaster_recovery_operations/aem-page/secure-proc_disaster_recovery_operations.html"
last_crumb = "Disaster recovery and operational continuity"
modified = "2026-05-21T14:12:12.122Z"
multi_page_path = ""
name = "Disaster recovery and operational continuity"
oversized = "false"
page_slug = "secure-proc_disaster_recovery_operations"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.6"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/secure-proc_disaster_recovery_operations"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/secure-proc_disaster_recovery_operations/toc/toc.json"
type = "aem-page"
+++

# Disaster recovery and operational continuity

Regularly back up Red Hat Ansible Automation Platform to ensure effective disaster recovery.

## About this task

An important aspect of backups is that they contain a copy of the database as well as the secret key used to decrypt credentials stored in the database, so the backup files should be stored in a secure encrypted location. This means that access to endpoint credentials are protected properly. Access to backups should be limited only to Ansible Automation Platform administrators who have root shell access to automation controller and the dedicated installation host.

The two main reasons an Ansible Automation Platform administrator needs to back up their Ansible Automation Platform environment are:

- To save a copy of the data from your Ansible Automation Platform environment, so you can restore it if needed.
- To use the backup to restore the environment into a different set of servers if you’re creating a new Ansible Automation Platform cluster or preparing for an upgrade.


In all cases, the recommended and safest process is to always use the same versions of PostgreSQL and Ansible Automation Platform to back up and restore the environment.

Using some redundancy on the system is highly recommended. If the secrets system is down, the automation controller cannot fetch the information and can fail in a way that would be recoverable once the service is restored. If you believe the SECRET_KEY automation controller generated for you has been compromised and has to be regenerated, you can run a tool from the installation program that behaves much like the automation controller backup and restore tool.

To generate a new secret key, perform the following steps:

## Procedure

1.  Backup your Ansible Automation Platform database before you do anything else! See the [Back up and restore](/documentation/en-us/red_hat_ansible_automation_platform/2.6/assembly_ag_controller_backup_and_restore "You can backup and restore your system by using the Ansible Automation Platform setup playbook.") section of the Configuring automation execution guide,
2.  Using the inventory from your install (same inventory with which you run backups/restores), run `setup.sh -k`.

## Results

A backup copy of the previous key is saved in `/etc/tower/`.

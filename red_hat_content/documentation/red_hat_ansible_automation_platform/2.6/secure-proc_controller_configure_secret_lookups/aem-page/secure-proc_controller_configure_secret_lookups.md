+++
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.6/secure-proc_controller_configure_secret_lookups"
template = "docs/aem-title.html"
title = "Configuring and linking secret lookups - Red Hat Ansible Automation Platform 2.6"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6", "2.6"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6/secure-assembly_gw_managing_access/", "Manage access with role-based access control"]]
category = "Secure"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/secure-proc_controller_configure_secret_lookups/aem-page/secure-proc_controller_configure_secret_lookups.html"
last_crumb = "Configuring and linking secret lookups"
modified = "2026-05-21T14:12:12.122Z"
multi_page_path = ""
name = "Configuring and linking secret lookups"
oversized = "false"
page_slug = "secure-proc_controller_configure_secret_lookups"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.6"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/secure-proc_controller_configure_secret_lookups"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/secure-proc_controller_configure_secret_lookups/toc/toc.json"
type = "aem-page"
+++

# Configuring and linking secret lookups

automation controller can be configured to retrieve secrets from third-party secret management systems, such as HashiCorp Vault, AWS Secrets Manager, CyberArk Conjur, and others.

## About this task

Learn how to configure automation controller to retrieve secrets from third-party systems by linking credential fields to external credentials that contain the necessary information to authenticate and retrieve secrets from these systems.

When pulling a secret from a third-party system, you are linking credential fields to external systems. To link a credential field to a value stored in an external system, select the external credential corresponding to that system and provide `metadata` to look up the required value. The metadata input fields are part of the external credential type definition of the source credential.

Automation controller provides a credential plugin interface for developers, integrators, system administrators, and power-users with the ability to add new external credential types to extend it to support other secret management systems.

Use the following procedure to use automation controller to configure and use each of the supported third-party secret management systems.

## Procedure

1.  Create an external credential for authenticating with the secret management system. At minimum, give a name for the external credential and select one of the following for the **Credential type** field:

  -  [AWS Secrets Manager Lookup](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/configuring_automation_execution/assembly-controller-secret-management#ref-aws-secrets-manager-lookup)

  -  [Centrify Vault Credential Provider Lookup](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/configuring_automation_execution/assembly-controller-secret-management#ref-centrify-vault-lookup)

  -  [CyberArk Central Credential Provider (CCP) Lookup](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/configuring_automation_execution/assembly-controller-secret-management#ref-cyberark-ccp-lookup)

  -  [CyberArk Conjur Secrets Manager Lookup](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/configuring_automation_execution/assembly-controller-secret-management#ref-cyberark-conjur-lookup)

  -  [HashiCorp Vault Secret Lookup](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/configuring_automation_execution/assembly-controller-secret-management#ref-hashicorp-vault-lookup)

  -  [HashiCorp Vault Signed SSH](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/configuring_automation_execution/assembly-controller-secret-management#ref-hashicorp-signed-ssh)

  -  [Microsoft Azure Key Vault](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/configuring_automation_execution/assembly-controller-secret-management#ref-azure-key-vault-lookup)

  -  [Thycotic DevOps Secrets Vault](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/configuring_automation_execution/assembly-controller-secret-management#ref-thycotic-devops-vault)

  -  [Thycotic Secret Server](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/configuring_automation_execution/assembly-controller-secret-management#ref-thycotic-secret-server)

  -  [Configuring a GitHub App Installation Access Token Lookup](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/configuring_automation_execution/assembly-controller-secret-management#controller-github-app-token)         In this example, the *Demo Credential* is the target credential.

2.  For any of the fields that follow the **Type Details** area that you want to link to the external credential, click the key ![Link](/webassets/aem/red_hat_ansible_automation_platform/2.6/images/leftkey.png) icon in the input field to link one or more input fields to the external credential along with metadata for locating the secret in the external system.
3.  Select the input source to use to retrieve your secret information.
4.  Select the credential you want to link to, and click Next. This takes you to the **Metadata** tab of the input source. This example shows the Metadata prompt for HashiVault Secret Lookup. Metadata is specific to the input source you select. For more information, see the [Metadata for credential input sources](/documentation/en-us/red_hat_ansible_automation_platform/2.6/secure-ref_controller_metadata_credential_input#ref-controller-metadata-credential-input "Learn how to apply the information required for the Metadata tab of the input source.") table.

5.  Click Test to verify connection to the secret management system. If the lookup is unsuccessful, an error message displays.
6.  Click OK. You return to the **Details** screen of your target credential.
7.  Repeat these steps, starting with Step 3 to complete the remaining input fields for the target credential. By linking the information in this manner, automation controller retrieves sensitive information, such as username, password, keys, certificates, and tokens from the third-party management systems and populates the remaining fields of the target credential form with that data.
8.  If necessary, supply any information manually for those fields that do not use linking as a way of retrieving sensitive information. For more information about each of the fields, see the appropriate [Credential types](/documentation/en-us/red_hat_ansible_automation_platform/2.6/secure-ref_controller_credential_types "Ansible Automation Platform supports a number of credential types.").
9.  Click Save.

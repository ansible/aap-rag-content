+++
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.6/upgrade-ref_upgrade_2_5_to_2_6"
template = "docs/aem-title.html"
title = "Upgrade from 2.5 to 2.6 - Red Hat Ansible Automation Platform 2.6"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6", "2.6"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6/upgrade-assembly_upgrade_data_movement/", "Identity and access management migration during upgrade"]]
category = "Upgrade"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/upgrade-ref_upgrade_2_5_to_2_6/aem-page/upgrade-ref_upgrade_2_5_to_2_6.html"
last_crumb = "Upgrade from 2.5 to 2.6"
modified = "2026-05-21T14:12:12.122Z"
multi_page_path = ""
name = "Upgrade from 2.5 to 2.6"
oversized = "false"
page_slug = "upgrade-ref_upgrade_2_5_to_2_6"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.6"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/upgrade-ref_upgrade_2_5_to_2_6"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/upgrade-ref_upgrade_2_5_to_2_6/toc/toc.json"
type = "aem-page"
+++

# Upgrade from 2.5 to 2.6

When upgrading from Ansible Automation Platform 2.5 to 2.6, existing authenticators and their mappings in platform gateway continue to function as they are, with no changes being imported.

This is because the core authentication service in 2.5 is already platform gateway, so a migration of this data is not needed.

## Automation controller

Customers upgrading from 2.5 to 2.6 must also begin moving away from using nested teams in automation controller APIs, as future releases will disable direct access to service APIs.

After the upgrade, user data is synchronized between automation controller and the platform-wide authentication gateway.

Automation controller users, teams, roles, and organizations should become platform entities upon upgrade without the need to run additional "merge" processes. Customers that first upgraded from 2.4 to 2.5 will have teams that existed in 2.4 merged into platform gateway when they upgrade from 2.5 to 2.6.

Roles should apply the permission model for non-admin access to execution, content, and event services.

## Automation hub

Understand identity changes for automation hub users when upgrading from 2.5 to 2.6. Review automatically merged teams, manually reassign permissions for removed admins, and reconfigure SSO to restore user access.

The following apply:

- A private automation hub admin (Automation Content Administrator) in 2.5 will be removed in the upgraded version and for this user the permissions must be reassigned manually as part of the data movement process.


Important:

If teams with the same name exist in both automation hub and within the platform-wide authentication gateway, users from automation hub will be automatically added to corresponding teams within the platform-wide authentication gateway, and new teams will be created if they do not exist. This approach aims to retain team memberships, but requires careful review of permissions post-upgrade.

- If you rely on automation hub *Single Sign-On* (SSO) to access the automation hub user interface (UI), automation hub SSO logins will no longer function after the upgrade. However, API tokens will remain active. Therefore, automated processes or systems that use API tokens for authentication will continue to operate without interruption. If your workflows predominantly rely on API access, the impact might be minimal. However, if users primarily access the UI through SSO, they will need to take action post-upgrade.
- To restore UI access for users who previously relied on automation hub SSO, you need to reconfigure SSO within Ansible Automation Platform to be able to login. For further information, see [Configuring Ansible Automation Platform Central Authentication Generic OIDC Settings and Red Hat SSO/KEYCLOAK for Red Hat SSO and Ansible Automation Platform](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.4/html-single/installing_and_configuring_central_authentication_for_the_ansible_automation_platform/index#configuring-central-auth-generic-oidc-settings).
- Automation controller admins will become platform admins and can administer automation hub.
- If you upgraded from 2.4 to 2.6 with both automation controller and private automation hub, then a dialog is displayed in the product post upgrade that informs you that there are steps to take to reconfigure private automation hub. This dialog can either display information in-product, or link to a product doc or Knowledge Base article. In either case, you will be guided to take action from within the product and not be expected to find that information unprompted.
- If you upgraded from 2.4 to 2.6 from an automation controller-only environment, then the addition of private automation hub and Event-Driven Ansible services involves adding the necessary roles to a normal user account to grant access to those services.

## Event-Driven Ansible

When upgrading Event-Driven Ansible from version 2.5 to 2.6, users must reset their password to log in unless they use SSO. Administrators must manually reassign permissions for the former Automation Decisions Administrator role

The following apply:

- An Event-Driven Ansible administrator (Automation Decisions Administrator) in 2.5 will be removed in the upgraded version and for this user the permissions must be reassigned manually as part of the movement process.
- For Event-Driven Ansible, you must reset your password to log in to Ansible Automation Platform. You can still use your Event-Driven Ansible username but will require new passwords.
- If an Event-Driven Ansible user with SSO exists, then they will not have to reset password and should have their permissions moved over as part of the SSO migration.

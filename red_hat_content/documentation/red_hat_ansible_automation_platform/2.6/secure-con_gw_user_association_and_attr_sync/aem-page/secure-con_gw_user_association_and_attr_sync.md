+++
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.6/secure-con_gw_user_association_and_attr_sync"
title = "User and external authentication mapping - Red Hat Ansible Automation Platform 2.6"
template = "docs/aem-title.html"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6", "2.6"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6/secure-assembly_gw_configure_authentication/", "Configure central authentication for Ansible Automation Platform"]]
category = "Secure"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/secure-con_gw_user_association_and_attr_sync/aem-page/secure-con_gw_user_association_and_attr_sync.html"
last_crumb = "User and external authentication mapping"
modified = "2026-05-21T14:12:12.122Z"
multi_page_path = ""
name = "User and external authentication mapping"
oversized = "false"
page_slug = "secure-con_gw_user_association_and_attr_sync"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.6"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/secure-con_gw_user_association_and_attr_sync"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/secure-con_gw_user_association_and_attr_sync/toc/toc.json"
type = "aem-page"
+++

# User and external authentication mapping

Ansible Automation Platform manages user accounts and synchronizes attributes by centralizing user identification around a matching email address. You can sign in with existing accounts from different sources while maintaining a consistent user profile and access permissions.

Warning:

The platform accepts email claims from identity providers without verifying email ownership. Before you configure an external authenticator, verify that your identity provider enforces email verification and restricts self-service email changes.

When you log in to the platform for the first time with an authenticator, such as Local, GitHub, SAML, or LDAP, the platform evaluates the username and email address. If a single email match exists, the platform links the external identity to that existing account.

- Subsequent logins with the same authenticator and external Unique Identifier (UID) directly sign the user into their linked account.
- If a user's external UID changes, the system re-triggers the email-based linking logic. If the new UID's email matches the existing account, the new authenticator is linked. If the email does not match or is not provided, a new user account might be created.
- If a user's external email changes, the platform does not automatically update the email address in the existing account, but the user can still sign in and a new account with the new email is created for the user.


If a user has a hashed account, such as `bob-hash`, due to a username collision from a previous version, that association is honored for that authenticator. However, for new authentications from other identity providers, the platform maps to the user's primary account, such as `bob`, provided a single matching email exists. This consolidates user identities and prevents the creation of new hashed accounts. If users should have been previously merged, you can delete the user-<hash> account from Ansible Automation Platform and on a subsequent login, the users are merged based on emails as described above.

Important:

- **Authenticators without email**: If an authenticator such as RADIUS or TACACS+ does not return an email address, a new account is created on first sign-in. To ensure consistent future access, manually add an email to the account after creation.
- **Multiple users with the same email**: If an email from an authenticator matches multiple existing platform accounts, the sign-in process fails.
- **LDAP usernames**: The platform treats LDAP usernames as case-insensitive. It converts the username to lowercase and stores it in the database.
- `associated_authenticators` field: The `associated_authenticators` field in the API supports multiple UIDs per user.

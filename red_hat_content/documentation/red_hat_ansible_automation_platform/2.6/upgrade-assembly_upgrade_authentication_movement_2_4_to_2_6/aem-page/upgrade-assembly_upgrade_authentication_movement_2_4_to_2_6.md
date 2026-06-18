+++
template = "docs/aem-title.html"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.6/upgrade-assembly_upgrade_authentication_movement_2_4_to_2_6"
title = "Authentication provider migration behavior - Red Hat Ansible Automation Platform 2.6"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6", "2.6"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6/upgrade-assembly_upgrade_authentication_movement_2_4_to_2_6/", "Authentication provider migration behavior"]]
category = "Upgrade"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/upgrade-assembly_upgrade_authentication_movement_2_4_to_2_6/aem-page/upgrade-assembly_upgrade_authentication_movement_2_4_to_2_6.html"
last_crumb = "Authentication provider migration behavior"
modified = "2026-05-21T14:12:12.122Z"
multi_page_path = ""
name = "Authentication provider migration behavior"
oversized = "false"
page_slug = "upgrade-assembly_upgrade_authentication_movement_2_4_to_2_6"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.6"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/upgrade-assembly_upgrade_authentication_movement_2_4_to_2_6"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/upgrade-assembly_upgrade_authentication_movement_2_4_to_2_6/toc/toc.json"
type = "aem-page"
+++

# Authentication provider migration behavior

During an upgrade from a version of Ansible Automation Platform that predates the platform gateway, only complete authentication provider configurations are migrated to the platform gateway.

A configuration is considered complete when it meets the following criteria:

- **LDAP**: You must specify a server URL.
- **GitHub and Microsoft Azure AD**: You must specify both a key and a secret.
- **OIDC**: You must define a key, a secret, and an OIDC endpoint.
- **RADIUS** and **TACACS+**: You must specify the host.


Before proceeding with the upgrade, ensure that you complete the following steps:

- **Create a local administrator account** and verify that you can log in to the environment using local authentication. You can also use the default administrator account from the inventory file.
- **Enable the local authenticator** in the target environment to ensure a fallback login method is available.
- **Perform a full backup** of your existing environment. Important:
      This is a critical step for data recovery in case any issues occur during the migration process.

**Post upgrade**

- **Update the callback URLs** in your *Identity Provider* (IdP) configurations after the migration. This is necessary for OAuth and SSO providers to function correctly with the platform gateway architecture.
- **Reestablish custom certificates for LDAPS** if your LDAP authentication uses custom certificates in the system's truststore. This configuration is not automatically migrated and you must manually reestablish it.


The migration of existing authentication configurations from automation controller to the platform gateway is automated. The following tables show how settings and mappings from the automation controller schema are transformed to fit the platform gateway API schema.

## Authentication type: OIDC

Review the general settings and mappings for OpenID Connect (OIDC) authentication. Compare how configurations transform from automation controller 2.4 to the platform gateway 2.6.

 **General settings**

| Automation controller 2.4                                                                                                                                                      | Platform gateway 2.6                                                                                                                               |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| ``` SOCIAL_AUTH_OIDC_KEY: "client-id" SOCIAL_AUTH_OIDC_SECRET: “client-secret" SOCIAL_AUTH_OIDC_OIDC_ENDPOINT: "https://idp.example.com" SOCIAL_AUTH_OIDC_VERIFY_SSL: true ``` | ``` "configuration": {   "OIDC_ENDPOINT": "https://idp.example.com",   "KEY": "client-id",   "SECRET": "client-secret",   "VERIFY_SSL": true } ``` |


 **Mappings**

| Automation controller 2.4                                                                                   | Platform gateway 2.6                                                                                                                                                                                                                                                                                   |
| ----------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| ``` AUTH_LDAP_ORGANIZATION_MAP:  "LDAP Organization":      users: true ```                                  | ```   "name": "Default - Users (users)",   "map_type": "organization",   "order": 1,   "authenticator": -1,   "triggers": {     "users": true   },   "organization": "Default",   "team": null,   "role": "Organization Member",   "revoke": true } ```                                                |
| ``` SOCIAL_AUTH_SAML_USER_FLAGS_BY_ATTR:  is_superuser_attr: "is_superuser"  is_superuser_value: "true" ``` | ``` {   "name": "is_superuser - role",   "authenticator": -1,   "revoke": true,   "map_type": "is_superuser",   "team": null,   "organization": null,   "triggers": {     "attributes": {       "is_superuser": {         "has_or": [           "true"         ]       }     }   },   "order": 2 } ``` |

## Authentication type: LDAP

Review the general settings and mappings for LDAP authentication. Compare how configurations transform from automation controller 2.4 to the platform gateway 2.6.

 **General settings**

| Automation controller 2.4                                                                                                                                                                                                                                                                                                                                                 | Platform gateway 2.6                                                                                                                                                                                                                                                                                                                                                             |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ``` AUTH_LDAP_SERVER_URI: "ldap://ldap.example.com:389" AUTH_LDAP_BIND_DN: "cn=admin,dc=example,dc=org" AUTH_LDAP_BIND_PASSWORD: "password" AUTH_LDAP_START_TLS: false AUTH_LDAP_USER_SEARCH: [   "ou=users,dc=example,dc=org",   "SCOPE_SUBTREE", "(cn=%(user)s)" ] AUTH_LDAP_USER_ATTR_MAP: {   "first_name": "givenName",   "last_name": "sn",   "email": "mail" } ``` | ``` "configuration": {   "SERVER_URI": "ldap://ldap.example.com:389",   "BIND_DN": "cn=admin,dc=example,dc=org",   "BIND_PASSWORD": "password",   "START_TLS": false,   "USER_SEARCH": [     "ou=users,dc=example,dc=org",     "SCOPE_SUBTREE",    "(cn=%(user)s)"   ],   "USER_ATTR_MAP": {     "first_name": "givenName",     "last_name": "sn",     "email": "mail"   } } ``` |


 **Mappings**

| Automation controller 2.4                                                                                                                      | Platform gateway 2.6                                                                                                                                                                                                                                                                                                                                                                                       |
| ---------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ``` AUTH_LDAP_ORGANIZATION_MAP:  "LDAP Organization":      users: true      admins:      - "cn=awx_org_admins,ou=groups,dc=example,dc=org" ``` | ``` {   "name": "LDAP Organization - Admins cn=awx_org_admins,ou=groups,dc=example,dc=org",   "map_type": "organization",   "order": 1,   "authenticator": -1,   "triggers": {     "groups": {       "has_or": [         "cn=awx_org_admins,ou=groups,dc=example,dc=org"       ]     }   },   "organization": "LDAP Organization",   "team": null,   "role": "Organization Admin",   "revoke": false } ``` |
| ``` AUTH_LDAP_USER_FLAGS_BY_GROUP:   is_superuser:     - 'cn=awx_admins,ou=groups,dc=example,dc=org' ```                                       | ``` {   "name": "is_superuser - role",   "authenticator": -1,   "revoke": true,   "map_type": "is_superuser",   "team": null,   "organization": null,   "triggers": {     "groups": {    "has_or": [         "cn=awx_admins,ou=groups,dc=example,dc=org"       ]     }   },   "order": 2 } ```                                                                                                             |

## Authentication type: SAML

Understand how Security Assertion Markup Language (SAML) provides secure, token-based authentication for your upgraded system. Implement SAML to ensure seamless single sign-on (SSO) and centralized identity management.

Important:

Automation controller in Ansible Automation Platform 2.4 allowed customers to enter an encrypted private key in SAML configuration without raising an error. If request signing was not enabled in the authenticator and the SAML IdP, then the Ansible Automation Platform administrator would not know that encrypted keys were not supported. Encrypted keys not supported in Ansible Automation Platform 2.6 authenticators. The platform alerts users that encrypted keys are not supported. However, when upgrading from Ansible Automation Platform 2.4 to 2.6, customers must replace encrypted private keys with unencrypted private keys in their SAML authenticators to prevent migration errors for the authenticator to platform gateway. If you skip this step, the authenticator is not migrated as part of the upgrade. The SAML authenticator must then be recreated manually by a local administrator to re-enable authentication. This might delay SSO users from logging back into the platform after the upgrade.

 **General settings**

| Automation controller 2.4                                                                                                                                                                                                                                                                                                                                                                                                   | Platform gateway 2.6                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ``` SOCIAL_AUTH_SAML_ENABLED_IDPS:   Keycloak: null   entity_id: 'https://idp.example.com/auth/realms/awx'   url: 'https://idp.example.com/auth/realms/awx/protocol/saml'   x509cert: MIICert...   attr_username: username   attr_email: email SOCIAL_AUTH_SAML_SP_ENTITY_ID: 'https://controller.example.com:8043' SOCIAL_AUTH_SAML_SP_PUBLIC_CERT: MIICertPublic... SOCIAL_AUTH_SAML_SP_PRIVATE_KEY: MIIKeyPrivate... ``` | ``` "configuration": {   "IDP_URL": "https://idp.example.com/auth/realms/awx/protocol/saml",   "IDP_X509_CERT": "-----BEGIN CERTIFICATE-----\nMIICert...\n-----END CERTIFICATE-----",   "IDP_ENTITY_ID": "https://idp.example.com/auth/realms/awx",   "IDP_ATTR_EMAIL": "email",   "IDP_ATTR_USERNAME": "username",   "SP_ENTITY_ID": "https://controller.example.com:8043",   "SP_PUBLIC_CERT": "MIICertPublic...",   "SP_PRIVATE_KEY": "MIIKeyPrivate..." } ``` |


 **Mappings**

| Automation controller 2.4                                                                                   | Platform gateway 2.6                                                                                                                                                                                                                                                                                   |
| ----------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| ``` SOCIAL_AUTH_SAML_ORGANIZATION_MAP:  "Default":     users: true ```                                      | ``` {   "name": "Default - Users (users)",   "map_type": "organization",   "order": 1,   "authenticator": -1,   "triggers": {     "users": true   },   "organization": "Default",   "team": null,   "role": "Organization Member",   "revoke": true } ```                                              |
| ``` SOCIAL_AUTH_SAML_USER_FLAGS_BY_ATTR:  is_superuser_attr: "is_superuser"  is_superuser_value: "true" ``` | ``` {   "name": "is_superuser - role",   "authenticator": -1,   "revoke": true,   "map_type": "is_superuser",   "team": null,   "organization": null,   "triggers": {     "attributes": {       "is_superuser": {         "has_or": [           "true"         ]       }     }   },   "order": 2 } ``` |

## Authentication type: Github

Review the general settings and mappings for Github authentication. Compare how configurations transform from automation controller 2.4 to the platform gateway 2.6.

 **General settings**

| Automation controller 2.4                                                                                                                    | Platform gateway 2.6                                                                                                                                  |
| -------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| ``` SOCIAL_AUTH_GITHUB_KEY: client-id SOCIAL_AUTH_GITHUB_SECRET: client-secret SOCIAL_AUTH_GITHUB_SCOPE:   - 'user:email'   - 'read:org' ``` | ``` {   "configuration": {     "KEY": "client-id",     "SECRET": "client-secret",     "SCOPE": [       "user:email",       "read:org"     ]   } } ``` |


 **Mappings**

| Automation controller 2.4                                                                                    | Platform gateway 2.6                                                                                                                                                                                                                                                                                        |
| ------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ``` SOCIAL_AUTH_GITHUB_ORGANIZATION_MAP:  "MyOrg":      users: true      admins:      - "admin-team" ```     | ``` {   "name": "MyOrg - Admins admin-team",   "map_type": "organization",   "order": 1,   "authenticator": -1,   "triggers": {     "users": {       "has_or": [         "admin-team"       ]     }   },   "organization": "MyOrg",   "team": null,   "role": "Organization Admin",   "revoke": false } ``` |
| ``` SOCIAL_AUTH_GITHUB_TEAM_MAP:  "Developers":      organization: "MyOrg"      users:      - "dev-team" ``` | ``` {   "name": "MyOrg - Developers dev-team",   "map_type": "team",   "order": 2,   "authenticator": -1,   "triggers": {     "users": {       "has_or": [         "dev-team"       ]     }   },   "organization": "MyOrg",   "team": "Developers",   "role": "Team Member",   "revoke": false } ```        |

## Authentication type: Azure AD

Review the general settings and mappings for Azure AD authentication. Compare how configurations transform from automation controller 2.4 to the platform gateway 2.6.

 **General settings**

| Automation controller 2.4                                                                                   | Platform gateway 2.6                                                                                            |
| ----------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- |
| ``` SOCIAL_AUTH_AZUREAD_OAUTH2_KEY: "application-id" SOCIAL_AUTH_AZUREAD_OAUTH2_SECRET: "client-secret" ``` | ``` "configuration": {   "KEY": "application-id",   "SECRET": "client-secret",   "GROUPS_CLAIM": "groups" } ``` |


 **Mappings**

| Automation controller 2.4                                                                                                                | Platform gateway 2.6                                                                                                                                                                                                                                                                                                                              |
| ---------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ``` SOCIAL_AUTH_AZUREAD_OAUTH2_ORGANIZATION_MAP:  "Azure Organization":      users: true ```                                             | ``` {   "name": "Azure Organization - Users (users)",   "map_type": "organization",   "order": 1,   "authenticator": -1,   "triggers": {     "users": true   },   "organization": "Azure Organization",   "team": null,   "role": "Organization Member",   "revoke": false } ```                                                                  |
| ``` SOCIAL_AUTH_AZUREAD_OAUTH2_TEAM_MAP:   "Admin Team":     organization: "Azure Organization"     users:     - "admin@company.com" ``` | ``` {   "name": "Azure Organization - Admin Team admin@company.com",   "map_type": "team",   "order": 2,   "authenticator": -1,   "triggers": {     "emails": {       "has_or": [         "admin@company.com"       ]     }   },   "organization": "Azure Organization",   "team": "Admin Team",   "role": "Team Member",   "revoke": false } ``` |

## Authentication type: RADIUS

Review the general settings and mappings for RADIUS authentication. Compare how configurations transform from automation controller 2.4 to the platform gateway 2.6.

 **General settings**

| Automation controller 2.4                                                                    | Platform gateway 2.6                                                                                       |
| -------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| ``` RADIUS_SERVER: "radius.example.com" RADIUS_PORT: 1812 RADIUS_SECRET: "shared-secret" ``` | ``` "configuration": {   "SERVER": "radius.example.com",   "PORT": 1812,   "SECRET": "shared-secret" } ``` |


 **Mappings**

RADIUS authentication does not support user mappings in either automation controller 2.4 or Platform gateway 2.6.

## Authentication type: TACACS+

Review the general settings and mappings for TACACS+ authentication. Compare how configurations transform from automation controller 2.4 to the platform gateway 2.6.

 **General settings**

| Automation controller 2.4                                                                                                                                                                       | Platform gateway 2.6                                                                                                                                                            |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ``` TACACSPLUS_HOST: "tacacs.example.com" TACACSPLUS_PORT: 49 TACACSPLUS_SECRET: "shared-secret" TACACSPLUS_SESSION_TIMEOUT: 5 TACACSPLUS_AUTH_PROTOCOL: "ascii" TACACSPLUS_REM_ADDR: false ``` | ``` "configuration": {   "HOST": "tacacs.example.com",   "PORT": 49,   "SECRET": "shared-secret",   "SESSION_TIMEOUT": 5,   "AUTH_PROTOCOL": "ascii",   "REM_ADDR": false } ``` |


 **Mappings**

TACACS+ authentication does not support user mappings in either automation controller 2.4 or Platform gateway 2.6.

## Authentication type: Google OAuth2

Review the general settings and mappings for Google OAuth2 authentication. Compare how configurations transform from automation controller 2.4 to the platform gateway 2.6.

 **General settings**

| Automation controller 2.4                                                                                                                                  | Platform gateway 2.6                                                                                                                                                        |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ``` SOCIAL_AUTH_GOOGLE_OAUTH2_KEY: "client-id" SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET: "client-secret" SOCIAL_AUTH_GOOGLE_OAUTH2_SCOPE: ["profile", "email"] ``` | ``` {   "configuration": {     "KEY": "client-id",     "SECRET": "client-secret",     "REDIRECT_STATE": true,     "SCOPE": [       "profile",       "email"     ]   } } ``` |


 **Mappings**

| Automation controller 2.4                                                                                  | Platform gateway 2.6                                                                                                                                                                                                                                             |
| ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ``` SOCIAL_AUTH_GOOGLE_OAUTH2_ORGANIZATION_MAP:  "Google Org":      users: true ```                        | ``` {   "name": "Google Org - Users (users)",   "map_type": "organization",   "order": 1,   "authenticator": -1,   "triggers": {     "users": true   },   "organization": "Google Org",   "team": null,   "role": "Organization Member",   "revoke": false } ``` |
| ``` SOCIAL_AUTH_GOOGLE_OAUTH2_TEAM_MAP:  "Engineers":      organization: "Google Org"      users: true ``` | ``` {   "name": "Google Org - Engineers (users)",   "map_type": "team",   "order": 2,   "authenticator": -1,   "triggers": {     "users": true   },   "organization": "Google Org",   "team": "Engineers",   "role": "Team Member",   "revoke": false } ```      |

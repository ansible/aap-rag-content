# 6. Authentication movement
## 6.8. Authentication type: Google OAuth2

Review the general settings and mappings for Google OAuth2 authentication. Compare how configurations transform from automation controller 2.4 to the platform gateway 2.6.

**General settings**

| Automation controller 2.4 | Platform gateway 2.6 |
| --- | --- |
| SOCIAL_AUTH_GOOGLE_OAUTH2_KEY: "client-id"     SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET: "client-secret"     SOCIAL_AUTH_GOOGLE_OAUTH2_SCOPE: ["profile", "email"] | {       "configuration": {         "KEY": "client-id",         "SECRET": "client-secret",         "REDIRECT_STATE": true,         "SCOPE": [           "profile",           "email"         ]       }     } |

**Mappings**

| Automation controller 2.4 | Platform gateway 2.6 |
| --- | --- |
| SOCIAL_AUTH_GOOGLE_OAUTH2_ORGANIZATION_MAP:      "Google Org":          users: true | {       "name": "Google Org - Users (users)",       "map_type": "organization",       "order": 1,       "authenticator": -1,       "triggers": {         "users": true       },       "organization": "Google Org",       "team": null,       "role": "Organization Member",       "revoke": false     } |
| SOCIAL_AUTH_GOOGLE_OAUTH2_TEAM_MAP:      "Engineers":          organization: "Google Org"          users: true | {       "name": "Google Org - Engineers (users)",       "map_type": "team",       "order": 2,       "authenticator": -1,       "triggers": {         "users": true       },       "organization": "Google Org",       "team": "Engineers",       "role": "Team Member",       "revoke": false     } |

## 6.9. The `MANAGE_ORGANIZATION_AUTH` setting

The automation controller setting previously called **Organization Admins Can Manage Users and Teams** in the UI (or `MANAGE_ORGANIZATION_AUTH` in the API) controls whether an organization administrator can create users and teams.

This setting now exists in both platform gateway and automation controller in Ansible Automation Platform 2.6. During an upgrade the value from automation controller is imported into the platform gateway server. If you decide to change the value of this setting ensure that you change it to the same values in both the platform gateway and automation controller.

Important

For environments with automation running directly against automation controller, maintain a consistent value for `MANAGE_ORGANIZATION_AUTH` across both automation controller and platform gateway to avoid unexpected behavior.

# Chapter 7. API changes in Ansible Automation Platform 2.6

Ansible Automation Platform 2.5 and 2.6 include changes to API endpoints with the addition of platform gateway. Versions 2.5 and 2.6 expose API access to individual services (automation controller, private automation hub, Event-Driven Ansible) to maintain compatibility with existing REST API integrations. This access will be removed in a future release.

These changes impact your organization if you have 2.4 API calls implemented directly with automation controller or private automation hub, or if you are integrating directly with automation controller or private automation hub hosts. You can use API endpoints exposed through the platform gateway for all Ansible Automation Platform services starting with Ansible Automation Platform 2.5. Moving integrations to API endpoints exposed through the platform gateway that your integrations are not disrupted when direct service API access is removed in a future Ansible Automation Platform release.

This section highlights the changed APIs between 2.4 and 2.5 or 2.6. For detailed API reference information, see the following sources:

- For platform gateway APIs, see the browsable API at `https://<gateway server name>/api/gateway/v1`.
- For automation controller APIs, see the browsable API at `https://<gateway server name>/api/controller/v2`.
- For automation hub APIs, see [Automation Hub API](https://developers.redhat.com/api-catalog/api/automation-hub) in *API Catalog and Documentation* to reference the 2.4 automation hub API.
- For Event-Driven Ansible, see the browsable API at `https://<gateway server name>/api/eda/v1`.

## 7.1. General changes

In Ansible Automation Platform 2.5 and later, API endpoints across components changed with the addition of platform gateway.

| Component | 2.4 and earlier endpoints start with… | 2.5 and later endpoints start with… | Notes |
| --- | --- | --- | --- |
| <br>  Automation controller | <br> `/api/v2/` | <br> `/api/controller/v2/` |  |
| <br>  Automation hub | <br> `/api/automation-hub` | <br> `/api/galaxy/v1` | <br>  This is the default path, but this path can be changed. For example: `https://<local_hub_URL>/api/` |
| <br>  Platform gateway | <br>  Not applicable | <br> `/api/gateway/v1/` |  |
| <br>  Event-Driven Ansible | <br>  Not applicable | <br> `/api/eda/v1/` |  |

## 7.2. Specific API changes

Specific API mappings for functionality that was centralized through the platform gateway are listed in the following table.

| Component | 2.4 and earlier endpoints start with… | 2.5 and 2.6 API endpoints | Action needed and notes |
| --- | --- | --- | --- |
| <br>  Automation controller | <br> `/api/v2/o` | <br> `/api/gateway/v1/tokens/` | <br>  Token authentication has moved to the platform gateway. <br>  The 2.4 API endpoint is deprecated; it still works in 2.6, but it will not work in a future release. |
| <br>  Automation controller | <br> `/api/v2/organizations` | <br> `/api/gateway/v1/organizations/` | <br>  Moved to the platform gateway. <br>  The 2.4 API endpoint is deprecated; it still works in 2.6, but it will not work in a future release. |
| <br>  Automation controller | <br> `/api/v2/teams` | <br> `/api/gateway/v1/teams/` | <br>  Moved to the platform gateway. <br>  The 2.4 API endpoint is deprecated; it still works in 2.6, but it will not work in a future release. |
| <br>  Automation controller | <br> `/api/v2/users` | <br> `/api/gateway/v1/users/` | <br>  Moved to the platform gateway. <br>  The 2.4 API endpoint is deprecated; it still works in 2.6, but it will not work in a future release. |
| <br>  Automation controller | <br> `/api/v2/roles` | <br> `/api/gateway/v1/role_definitions/` | <br>  Moved to the platform gateway. This is a list of roles. In Ansible Automation Platform 2.6, this is a list of roles which can apply to all services, and includes custom roles. <br>  The 2.4 API endpoint is only a listing. It still works in 2.6, but it will not work in a future release. |
| <br>  Automation controller | <br> `/api/v2/roles/{id}/teams/` `/api/gateway/v1/role_definitions/` | <br> `/api/gateway/v1/role_team_assignments/` `/api/gateway/v1/role_user_assignments/` | <br>  A POST request gives a user a role to a resource. This is how to give user permissions. <br>  The 2.4 API endpoint is only a listing. It still works in 2.6, but it will not work in a future release. |
| <br>  Automation controller | <br>  The following roles list:    <br> `/api/v2/teams/{id}/roles/` `/api/v2/users/{id}/roles/` | <br> `/api/gateway/v1/role_team_assignments/?team={id}` `/api/gateway/v1/role_user_assignments/?user={id}` | <br>  List user and team permissions, and give new permissions. <br>  The 2.4 API endpoint is only a listing. It still works in 2.6, but it will not work in a future release. |
| <br>  Automation controller | <br>  The following object roles list: <br> `/api/v2/{model_name}/{id}/object_roles/`<br>  Example: `/api/v2/credentials/42/` | <br> `/api/gateway/v1/role_user_assignments/?content_type__api_slug={model_api_slug}&object_id={id}`<br>  Example: `/api/gateway/v1/role_user_assignments/?content_type__api_slug=awx.credential&object_id=42` | <br>  List the roles that apply to a resource. |
| <br>  Automation controller | <br>  The following resource access list: <br> `/api/v2/{model_name}/{id}/access_list/`<br>  Example: `/api/v2/credentials/42/access_list/` | <br>  Replacement in 2.6: `/api/gateway/v1/role_user_access/{model_api_slug}/{id}/`<br>  Example: `/api/gateway/v1/role_user_access/awx.credential/42/` | <br>  List the users who have access to a resource. |
| <br>  Automation hub | <br> `/api/v3/login/keycloak` | <br> `/api/gateway/social/complete/<UID>/` | <br>  Moved to the platform gateway. |
| <br>  Automation hub | <br> `/api/v3/auth/token` | <br> `/api/gateway/v1/tokens/` | <br>  Token authentication used for pulling collections will migrate to the platform gateway tokens. |
| <br>  Event-Driven Ansible | <br>  N/A | <br> `/api/gateway/v1/organizations/` | <br>  No action needed, as upgrades from 2.4 are not supported. |
| <br>  Event-Driven Ansible | <br>  N/A | <br> `/api/gateway/v1/teams/` | <br>  No action needed, as upgrades from 2.4 are not supported. |
| <br>  Event-Driven Ansible | <br>  N/A | <br> `/api/gateway/v1/users/` | <br>  No action needed, as upgrades from 2.4 are not supported. |
| <br>  Event-Driven Ansible | <br>  N/A | <br> `/api/gateway/v1/role_definitions/` `/api/gateway/v1/role_team_assignments/` `/api/gateway/v1/role_user_assignments/` | <br>  New role capabilities included as part of the platform gateway API. |

# Legal Notice

Copyright © Red Hat.

Except as otherwise noted below, the text of and illustrations in this documentation are licensed by Red Hat under the Creative Commons Attribution–Share Alike 3.0 Unported license . If you distribute this document or an adaptation of it, you must provide the URL for the original version.

Red Hat, as the licensor of this document, waives the right to enforce, and agrees not to assert, Section 4d of CC-BY-SA to the fullest extent permitted by applicable law.

Red Hat, the Red Hat logo, JBoss, Hibernate, and RHCE are trademarks or registered trademarks of Red Hat, LLC. or its subsidiaries in the United States and other countries.

Linux® is the registered trademark of Linus Torvalds in the United States and other countries.

XFS is a trademark or registered trademark of Hewlett Packard Enterprise Development LP or its subsidiaries in the United States and other countries.

The OpenStack® Word Mark and OpenStack logo are trademarks or registered trademarks of the Linux Foundation, used under license.

All other trademarks are the property of their respective owners.

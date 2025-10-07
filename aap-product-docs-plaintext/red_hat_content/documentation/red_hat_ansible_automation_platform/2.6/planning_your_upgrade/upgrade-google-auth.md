# 6. Authentication movement
## 6.8. Authentication type: Google OAuth2




**General settings**

| Automation controller 2.4 | Platform gateway 2.6 |
| --- | --- |
| ```
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY: "client-id"
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET: "client-secret"
SOCIAL_AUTH_GOOGLE_OAUTH2_SCOPE: ["profile", "email"]
``` | ```
{
"configuration": {
"KEY": "client-id",
"SECRET": "client-secret",
"REDIRECT_STATE": true,
"SCOPE": [
"profile",
"email"
]
}
}
``` |


**Mappings**

| Automation controller 2.4 | Platform gateway 2.6 |
| --- | --- |
| ```
SOCIAL_AUTH_GOOGLE_OAUTH2_ORGANIZATION_MAP:
"Google Org":
users: true
``` | ```
{
"name": "Google Org - Users (users)",
"map_type": "organization",
"order": 1,
"authenticator": -1,
"triggers": {
"users": true
},
"organization": "Google Org",
"team": null,
"role": "Organization Member",
"revoke": false
}
``` |
| ```
SOCIAL_AUTH_GOOGLE_OAUTH2_TEAM_MAP:
"Engineers":
organization: "Google Org"
users: true
``` | ```
{
"name": "Google Org - Engineers (users)",
"map_type": "team",
"order": 2,
"authenticator": -1,
"triggers": {
"users": true
},
"organization": "Google Org",
"team": "Engineers",
"role": "Team Member",
"revoke": false
}
``` |


## 6.9. The `MANAGE_ORGANIZATION_AUTH` setting




The automation controller setting previously called **Organization Admins Can Manage Users and Teams** in the UI (or `MANAGE_ORGANIZATION_AUTH` in the API) controls whether an organization administrator can create users and teams. This setting now exists in both platform gateway and automation controller in Ansible Automation Platform 2.6. During an upgrade the value from automation controller is imported into the platform gateway server. If you decide to change the value of this setting ensure that you change it to the same values in both the platform gateway and automation controller.

Important
For environments with automation running directly against automation controller, maintain a consistent value for `MANAGE_ORGANIZATION_AUTH` across both automation controller and platform gateway to avoid unexpected behavior.



# Chapter 7. API changes in Ansible Automation Platform 2.6




Ansible Automation Platform 2.5 and 2.6 include changes to API endpoints with the addition of platform gateway. Versions 2.5 and 2.6 expose API access to individual services (automation controller, private automation hub, Event-Driven Ansible) to maintain compatibility with existing REST API integrations. This access will be removed in a future release.

These changes impact your organization if you have 2.4 API calls implemented directly with automation controller or private automation hub, or if you are integrating directly with automation controller or private automation hub hosts. You can use API endpoints exposed through the platform gateway for all Ansible Automation Platform services starting with Ansible Automation Platform 2.5. Moving integrations to API endpoints exposed through the platform gateway that your integrations are not disrupted when direct service API access is removed in a future Ansible Automation Platform release.

This section highlights the changed APIs between 2.4 and 2.5 or 2.6. For detailed API reference information, see the following sources:

- For platform gateway APIs, see the browsable API at `    https://&lt;gateway server name&gt;/api/gateway/v1` .
- For automation controller APIs, see the browsable API at `    https://&lt;gateway server name&gt;/api/controller/v2` .
- For automation hub APIs, see [Automation Hub API](https://developers.redhat.com/api-catalog/api/automation-hub) in _API Catalog and Documentation_ to reference the 2.4 automation hub API.
- For Event-Driven Ansible, see the browsable API at `    https://&lt;gateway server name&gt;/api/eda/v1` .


## 7.1. General changes




In Ansible Automation Platform 2.5 and later, API endpoints across components changed with the addition of platform gateway.

| Component | 2.4 and earlier endpoints start with… | 2.5 and later endpoints start with… | Notes |
| --- | --- | --- | --- |
| Automation controller |  `/api/v2/` |  `/api/controller/v2/` |  |
| Automation hub |  `/api/automation-hub` |  `/api/galaxy/v1` | This is the default path, but this path can be changed. For example: `https://&lt;local_hub_URL&gt;/api/` |
| Platform gateway | Not applicable |  `/api/gateway/v1/` |  |
| Event-Driven Ansible | Not applicable |  `/api/eda/v1/` |  |


## 7.2. Specific API changes




Specific API mappings for functionality that was centralized through the platform gateway are listed in the following table.

| Component | 2.4 and earlier endpoints start with… | 2.5 and 2.6 API endpoints | Action needed and notes |
| --- | --- | --- | --- |
| Automation controller |  `/api/v2/o` |  `/api/gateway/v1/tokens/` | Token authentication has moved to the platform gateway.

The 2.4 API endpoint is deprecated; it still works in 2.6, but it will not work in a future release. |
| Automation controller |  `/api/v2/organizations` |  `/api/gateway/v1/organizations/` | Moved to the platform gateway.

The 2.4 API endpoint is deprecated; it still works in 2.6, but it will not work in a future release. |
| Automation controller |  `/api/v2/teams` |  `/api/gateway/v1/teams/` | Moved to the platform gateway.

The 2.4 API endpoint is deprecated; it still works in 2.6, but it will not work in a future release. |
| Automation controller |  `/api/v2/users` |  `/api/gateway/v1/users/` | Moved to the platform gateway.

The 2.4 API endpoint is deprecated; it still works in 2.6, but it will not work in a future release. |
| Automation controller |  `/api/v2/roles` |  `/api/gateway/v1/role_definitions/` | Moved to the platform gateway. This is a list of roles. In Ansible Automation Platform 2.6, this is a list of roles which can apply to all services, and includes custom roles.

The 2.4 API endpoint is only a listing. It still works in 2.6, but it will not work in a future release. |
| Automation controller | -  `    /api/v2/roles/{id}/teams/`
-  `    /api/gateway/v1/role_definitions/` | -  `    /api/gateway/v1/role_team_assignments/`
-  `    /api/gateway/v1/role_user_assignments/` | A POST request gives a user a role to a resource. This is how to give user permissions.

The 2.4 API endpoint is only a listing. It still works in 2.6, but it will not work in a future release. |
| Automation controller | The following roles list:

-  `    /api/v2/teams/{id}/roles/`
-  `    /api/v2/users/{id}/roles/` | -  `    /api/gateway/v1/role_team_assignments/?team={id}`
-  `    /api/gateway/v1/role_user_assignments/?user={id}` | List user and team permissions, and give new permissions.

The 2.4 API endpoint is only a listing. It still works in 2.6, but it will not work in a future release. |
| Automation controller | The following object roles list:

`/api/v2/{model_name}/{id}/object_roles/`

Example: `/api/v2/credentials/42/` |  `/api/gateway/v1/role_user_assignments/?content_type__api_slug={model_api_slug}&amp;object_id={id}`

Example: `/api/gateway/v1/role_user_assignments/?content_type__api_slug=awx.credential&amp;object_id=42` | List the roles that apply to a resource. |
| Automation controller | The following resource access list:

`/api/v2/{model_name}/{id}/access_list/`

Example: `/api/v2/credentials/42/access_list/` | Replacement in 2.6: `/api/gateway/v1/role_user_access/{model_api_slug}/{id}/`

Example: `/api/gateway/v1/role_user_access/awx.credential/42/` | List the users who have access to a resource. |
| Automation hub |  `/api/v3/login/keycloak` |  `/api/gateway/social/complete/&lt;UID&gt;/` | Moved to the platform gateway. |
| Automation hub |  `/api/v3/auth/token` |  `/api/gateway/v1/tokens/` | Token authentication used for pulling collections will migrate to the platform gateway tokens. |
| Event-Driven Ansible | N/A |  `/api/gateway/v1/organizations/` | No action needed, as upgrades from 2.4 are not supported. |
| Event-Driven Ansible | N/A |  `/api/gateway/v1/teams/` | No action needed, as upgrades from 2.4 are not supported. |
| Event-Driven Ansible | N/A |  `/api/gateway/v1/users/` | No action needed, as upgrades from 2.4 are not supported. |
| Event-Driven Ansible | N/A | -  `    /api/gateway/v1/role_definitions/`
-  `    /api/gateway/v1/role_team_assignments/`
-  `    /api/gateway/v1/role_user_assignments/` | New role capabilities included as part of the platform gateway API. |



<span id="idm140440485526656"></span>
# Legal Notice

Copyright© 2025 Red Hat, Inc.
The text of and illustrations in this document are licensed by Red Hat under a Creative Commons Attribution–Share Alike 3.0 Unported license ("CC-BY-SA"). An explanation of CC-BY-SA is available at [http://creativecommons.org/licenses/by-sa/3.0/](http://creativecommons.org/licenses/by-sa/3.0/) . In accordance with CC-BY-SA, if you distribute this document or an adaptation of it, you must provide the URL for the original version.
Red Hat, as the licensor of this document, waives the right to enforce, and agrees not to assert, Section 4d of CC-BY-SA to the fullest extent permitted by applicable law.
Red Hat, Red Hat Enterprise Linux, the Shadowman logo, the Red Hat logo, JBoss, OpenShift, Fedora, the Infinity logo, and RHCE are trademarks of Red Hat, Inc., registered in the United States and other countries.
Linux® is the registered trademark of Linus Torvalds in the United States and other countries.
Java® is a registered trademark of Oracle and/or its affiliates.
XFS® is a trademark of Silicon Graphics International Corp. or its subsidiaries in the United States and/or other countries.
MySQL® is a registered trademark of MySQL AB in the United States, the European Union and other countries.
Node.js® is an official trademark of Joyent. Red Hat is not formally related to or endorsed by the official Joyent Node.js open source or commercial project.
TheOpenStack® Word Mark and OpenStack logo are either registered trademarks/service marks or trademarks/service marks of the OpenStack Foundation, in the United States and other countries and are used with the OpenStack Foundation's permission. We are not affiliated with, endorsed or sponsored by the OpenStack Foundation, or the OpenStack community.
All other trademarks are the property of their respective owners.






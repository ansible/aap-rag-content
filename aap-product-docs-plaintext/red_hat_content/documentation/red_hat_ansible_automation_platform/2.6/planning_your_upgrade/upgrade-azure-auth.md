# 6. Authentication movement
## 6.5. Authentication type: Azure AD




**General settings**

| Automation controller 2.4 | Platform gateway 2.6 |
| --- | --- |
| ```
SOCIAL_AUTH_AZUREAD_OAUTH2_KEY: "application-id"
SOCIAL_AUTH_AZUREAD_OAUTH2_SECRET: "client-secret"
``` | ```
"configuration": {
"KEY": "application-id",
"SECRET": "client-secret",
"GROUPS_CLAIM": "groups"
}
``` |


**Mappings**

| Automation controller 2.4 | Platform gateway 2.6 |
| --- | --- |
| ```
SOCIAL_AUTH_AZUREAD_OAUTH2_ORGANIZATION_MAP:
"Azure Organization":
users: true
``` | ```
{
"name": "Azure Organization - Users (users)",
"map_type": "organization",
"order": 1,
"authenticator": -1,
"triggers": {
"users": true
},
"organization": "Azure Organization",
"team": null,
"role": "Organization Member",
"revoke": false
}
``` |
| ```
SOCIAL_AUTH_AZUREAD_OAUTH2_TEAM_MAP:
"Admin Team":
organization: "Azure Organization"
users:
- "admin@company.com"
``` | ```
{
"name": "Azure Organization - Admin Team admin@company.com",
"map_type": "team",
"order": 2,
"authenticator": -1,
"triggers": {
"emails": {
"has_or": [
"admin@company.com"
]
}
},
"organization": "Azure Organization",
"team": "Admin Team",
"role": "Team Member",
"revoke": false
}
``` |



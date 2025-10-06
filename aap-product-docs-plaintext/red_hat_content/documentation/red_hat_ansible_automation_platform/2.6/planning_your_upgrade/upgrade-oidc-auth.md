# 6. Authentication movement
## 6.1. Authentication type: OIDC




**General settings**

| Automation controller 2.4 | Platform gateway 2.6 |
| --- | --- |
| ```
SOCIAL_AUTH_OIDC_KEY: "client-id"
SOCIAL_AUTH_OIDC_SECRET: “client-secret"
SOCIAL_AUTH_OIDC_OIDC_ENDPOINT: "https://idp.example.com"
SOCIAL_AUTH_OIDC_VERIFY_SSL: true
``` | ```
"configuration": {
"OIDC_ENDPOINT": "https://idp.example.com",
"KEY": "client-id",
"SECRET": "client-secret",
"VERIFY_SSL": true
}
``` |


**Mappings**

| Automation controller 2.4 | Platform gateway 2.6 |
| --- | --- |
| ```
AUTH_LDAP_ORGANIZATION_MAP:
"LDAP Organization":
users: true
``` | ```
"name": "Default - Users (users)",
"map_type": "organization",
"order": 1,
"authenticator": -1,
"triggers": {
"users": true
},
"organization": "Default",
"team": null,
"role": "Organization Member",
"revoke": true
}
``` |
| ```
SOCIAL_AUTH_SAML_USER_FLAGS_BY_ATTR:
is_superuser_attr: "is_superuser"
is_superuser_value: "true"
``` | ```
{
"name": "is_superuser - role",
"authenticator": -1,
"revoke": true,
"map_type": "is_superuser",
"team": null,
"organization": null,
"triggers": {
"attributes": {
"is_superuser": {
"has_or": [
"true"
]
}
}
},
"order": 2
}
``` |



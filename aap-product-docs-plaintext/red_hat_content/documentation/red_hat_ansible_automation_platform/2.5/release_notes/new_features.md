# 10. Patch releases
## 10.14. Ansible Automation Platform patch release February 13, 2025
### 10.14.1. New Features




#### 10.14.1.1. Ansible Automation Platform




- Keycloak now allows for the configuration of the claim key/name for the field containing a user’s group membership returned in the ID token and/or user info data. This can be configured by setting the `    GROUPS_CLAIM` configuration value on a per-authenticator plugin basis as was done for the OIDC plugin.(AAP-38720)



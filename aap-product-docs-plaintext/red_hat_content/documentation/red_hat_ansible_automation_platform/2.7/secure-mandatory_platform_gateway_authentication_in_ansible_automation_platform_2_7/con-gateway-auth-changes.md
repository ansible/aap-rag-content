# Mandatory platform gateway authentication in Ansible Automation Platform 2.7
## Authentication changes in platform gateway

In Ansible Automation Platform 2.7, all user authentication and API access is centralized through platform gateway. Third-party provider configuration must also be performed in platform gateway.

- **Centralized flow:** All user authentication flows through platform gateway.
- **API requests:** All API requests must use platform gateway URLs and gateway-issued tokens.
- **Third-party providers:** Configuration for LDAP, SAML, and OAuth, must be performed in platform gateway.
- **Disabled methods:** Basic and session authentication are no longer available at the component level.


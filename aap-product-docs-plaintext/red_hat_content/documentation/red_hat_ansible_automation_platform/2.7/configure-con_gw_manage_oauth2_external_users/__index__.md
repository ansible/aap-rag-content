# Security settings for OAuth2 tokens and external users

Configure your platform settings to enable OAuth2 token creation for external users. Allowing users authenticated via LDAP, SAML, or SSO to generate tokens prevents 403 Forbidden errors and helps ensure they maintain programmatic API access.

This default behavior is a deliberate security measure. Ansible Automation Platform prioritizes centralized control over token generation, which encourages administrators to select the appropriate method for enabling OAuth 2.0 user token generation for external authentication providers.

It is important to understand that an OAuth2 token is created within Ansible Automation Platform, and Ansible Automation Platform itself manages its lifecycle, including its expiration. This lifecycle is independent of the user’s session with their external Identity Provider (IdP). For example, if a user generates an Ansible Automation Platform token and their account is later disabled in the external IdP, the Ansible Automation Platform token remains valid until it expires or is manually revoked. Being aware of this interaction is crucial for a secure configuration, as it highlights the need for compensating controls if you enable token creation for external users.


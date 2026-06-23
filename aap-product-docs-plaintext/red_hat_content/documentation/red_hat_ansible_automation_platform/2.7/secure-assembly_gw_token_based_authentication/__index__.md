# Configure access to external applications with tokens

Token-based authentication permits authentication of third-party tools and services with the platform through integrated OAuth 2 token support. Ansible Automation Platform utilizes both OAuth Tokens and Personal Access Tokens (PATs).

In Ansible Automation Platform 2.7, you must create and manage all tokens through platform gateway. Component-level token creation has been removed.

OAuth Tokens
OAuth Tokens are tied to specific applications and allow applications to access data without disclosing user login information.

Personal Access Tokens
PATs are personal to a user and not tied to a specific application. They are created directly by a user for their own use through platform gateway.

The default expiration for access tokens has been updated from 1000 years to 1 year. This change ensures frequent token rotation for increased credential security.

Note:

Access tokens in controller 2.4 and previous versions of the platform gateway were valid for 1000 years. Any existing tokens created before the 2.5.20250604 patch release will retain a 1000 year expiration.

You can customize this setting to meet your specific requirements by modifying the expiration time in your `settings.py` file as follows:

```
OAUTH2_PROVIDER__ACCESS_TOKEN_EXPIRE_SECONDS = 31536000
```


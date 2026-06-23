# Integrate third-party secret management systems
## Centrify Vault Credential Provider Lookup

Centrify Vault Credential Provider Lookup enables automation controller to retrieve secrets from Centrify Vault when executing jobs. This integration uses the Centrify Vault API to look up secrets at job runtime.

You need the Centrify Vault web service running to store secrets for this integration to work. When you select **Centrify Vault Credential Provider Lookup** for **Credential Type**, give the following metadata to configure your lookup:

- **Centrify Tenant URL** (required): give the URL used for communicating with Centrify’s secret management system
- **Centrify API User** (required): give the username
- **Centrify API Password** (required): give the password
- **OAuth2 Application ID** : specify the identifier given associated with the OAuth2 client
- **OAuth2 Scope** : specify the scope of the OAuth2 client


# Integrate third-party secret management systems
## Microsoft Azure Key Vault

Use the Microsoft Azure Key Vault lookup to retrieve secrets from Microsoft Azure’s Key Management System (KMS) within your automation controller environment.

When you select **Microsoft Azure Key Vault** for **Credential Type**, give the following metadata to configure your lookup:

- **Vault URL (DNS Name)** (required): give the URL used for communicating with Microsoft Azure’s key management system
- **Client ID** (required): give the identifier as obtained by Microsoft Entra ID
- **Client Secret** (required): give the secret as obtained by Microsoft Entra ID
- **Tenant ID** (required): give the unique identifier associated with an Microsoft Entra ID instance within an Azure subscription
- **Cloud Environment**: select the applicable cloud environment to apply


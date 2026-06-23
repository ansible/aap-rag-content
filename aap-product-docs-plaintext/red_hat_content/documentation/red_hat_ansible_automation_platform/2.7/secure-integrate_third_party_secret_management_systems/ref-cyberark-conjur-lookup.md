# Integrate third-party secret management systems
## CyberArk Conjur Secrets Manager Lookup

Learn how to configure a CyberArk Conjur Secrets Manager Lookup credential in automation controller.

When you select **CyberArk Conjur Secrets Manager Lookup** for **Credential Type**, give the following metadata to configure your lookup:

- **Conjur URL** (required): give the URL used for communicating with CyberArk Conjur’s secret management system. This must include the URL scheme, such as http or https.
- **API Key** (required): give the key given by your Conjur admin
- **Account** (required): the organization’s account name
- **Username** (required): the authenticated user for this service
- **Public Key Certificate**: include the `BEGIN CERTIFICATE` and `END CERTIFICATE` lines when pasting the public key, if provided by CyberArk


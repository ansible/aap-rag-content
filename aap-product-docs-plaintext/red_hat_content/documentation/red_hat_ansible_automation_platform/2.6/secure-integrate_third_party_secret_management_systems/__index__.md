# Integrate third-party secret management systems

Integrating third-party secret management systems with Ansible Automation Platform lets you store credentials in your existing infrastructure instead of providing them directly to the platform.

Integrating third-party secret management helps you to:

- Use existing secret management infrastructure: Store automation credentials in your enterprise secret management system instead of providing them directly to the platform.
- Maintain centralized credential storage: Manage automation credentials alongside other organizational credentials in a single secret management system.
- Choose the system that fits your needs: Select from multiple supported secret management systems including CyberArk, HashiCorp Vault, Microsoft Azure, and others.

## How Ansible Automation Platform supports third-party secret management

Ansible Automation Platform integrates with external secret management systems. Map credential fields to values stored in your secret management system. The platform fetches these external secret values before running a playbook that needs them.

## AWS Secrets Manager lookup

This plugin enables Amazon Web Services to be used as a credential input source to pull secrets from the Amazon Web Services Secrets Manager. The AWS Secrets Manager provides similar service to Microsoft Azure Key Vault, and the AWS collection provides a lookup plugin for it.

When AWS Secrets Manager lookup is selected for **Credential type**, give the following metadata to configure your lookup:

- **AWS Access Key** (required): give the access key used for communicating with AWS key management system
- **AWS Secret Key** (required): give the secret as obtained by the AWS IAM console

## Centrify Vault Credential Provider Lookup

Centrify Vault Credential Provider Lookup enables automation controller to retrieve secrets from Centrify Vault when executing jobs. This integration uses the Centrify Vault API to look up secrets at job runtime.

You need the Centrify Vault web service running to store secrets for this integration to work. When you select **Centrify Vault Credential Provider Lookup** for **Credential Type**, give the following metadata to configure your lookup:

- **Centrify Tenant URL** (required): give the URL used for communicating with Centrify’s secret management system
- **Centrify API User** (required): give the username
- **Centrify API Password** (required): give the password
- **OAuth2 Application ID** : specify the identifier given associated with the OAuth2 client
- **OAuth2 Scope** : specify the scope of the OAuth2 client

## CyberArk Central Credential Provider (CCP) Lookup

You can use automation controller to look up credentials stored in CyberArk Central Credential Provider (CCP) and use them in your automation tasks. This integration allows you to securely retrieve secrets from CyberArk CCP during job execution.

The CyberArk Central Credential Provider web service must be running to store secrets for this integration to work. When you select **CyberArk Central Credential Provider Lookup** for **Credential Type**, give the following metadata to configure your lookup:

- **CyberArk CCP URL** (required): give the URL used for communicating with CyberArk CCP’s secret management system. It must include the URL scheme such as http or https.
- Optional: **Web Service ID**: specify the identifier for the web service. Leaving this blank defaults to AIMWebService.
- **Application ID** (required): specify the identifier given by CyberArk CCP services.
- **Client Key**: paste the client key if provided by CyberArk.
- **Client Certificate**: include the `BEGIN CERTIFICATE` and `END CERTIFICATE` lines when pasting the certificate, if provided by CyberArk.
- **Verify SSL Certificates**: this option is only available when the URL uses HTTPS. Check this option to verify that the server’s SSL/TLS certificate is valid and trusted. For environments that use internal or private CA’s, leave this option unchecked to disable verification.

## CyberArk Conjur Secrets Manager Lookup

Learn how to configure a CyberArk Conjur Secrets Manager Lookup credential in automation controller.

When you select **CyberArk Conjur Secrets Manager Lookup** for **Credential Type**, give the following metadata to configure your lookup:

- **Conjur URL** (required): give the URL used for communicating with CyberArk Conjur’s secret management system. This must include the URL scheme, such as http or https.
- **API Key** (required): give the key given by your Conjur admin
- **Account** (required): the organization’s account name
- **Username** (required): the authenticated user for this service
- **Public Key Certificate**: include the `BEGIN CERTIFICATE` and `END CERTIFICATE` lines when pasting the public key, if provided by CyberArk

## HashiCorp Vault Secret Lookup

The HashiCorp Vault secret lookup credential type allows you to retrieve secrets from a HashiCorp Vault server during playbook execution. This integration supports various authentication methods, including Token, AppRole, LDAP, Userpass, Kubernetes, and TLS Certificates.

When you select **HashiCorp Vault Secret Lookup** for **Credential Type**, give the following metadata to configure your lookup:

- **Server URL** (required): give the URL used for communicating with HashiCorp Vault’s secret management system.
- **Token**: specify the access token used to authenticate HashiCorp’s server.
- **CA Certificate**: specify the CA certificate used to verify HashiCorp’s server.
- **AppRole role_id**: specify the ID if using AppRole for authentication.
- **AppRole secret_id**: specify the corresponding secret ID for AppRole authentication.
- **Client Certificate**: specify a PEM-encoded client certificate when using the TLS authentication method, including any required intermediate certificates expected by Hashicorp Vault.
- **Client Certificate Key**: specify a PEM-encoded certificate private key when using the TLS authentication method.
- **TLS Authentication Role**: specify the role or certificate name in Hashicorp Vault that corresponds to your client certificate when using the TLS authentication method. If it is not provided, Hashicorp Vault attempts to match the certificate automatically.
- **Namespace name**: specify the Namespace name (Hashicorp Vault enterprise only).
- **Kubernetes role**: specify the role name when using Kubernetes authentication.
- **Username**: enter the username of the user to be used to authenticate this service.
- **Password**: enter the password associated with the user to be used to authenticate this service.
- **Path to Auth**: specify a path if other than the default path of `/approle`.
- **API Version** (required): select v1 for static lookups and v2 for versioned lookups.


LDAP authentication requires LDAP to be configured in HashiCorp’s Vault UI and a policy added to the user. Cubbyhole is the name of the default secret mount. If you have proper permissions, you can create other mounts and write key values to those.

To test the lookup, create another credential that uses Hashicorp Vault lookup.

## HashiCorp Vault Signed SSH

You can use HashiCorp Vault Signed SSH to securely manage SSH credentials for accessing managed nodes in automation controller.

When you select **HashiCorp Vault Signed SSH** for **Credential Type**, give the following metadata to configure your lookup:

- **Server URL** (required): give the URL used for communicating with HashiCorp Signed SSH’s secret management system.
- **Token**: specify the access token used to authenticate HashiCorp’s server.
- **CA Certificate**: specify the CA certificate used to verify HashiCorp’s server.
- **AppRole role_id**: specify the ID for AppRole authentication.
- **AppRole secret_id**: specify the corresponding secret ID for AppRole authentication.
- **Client Certificate**: specify a PEM-encoded client certificate when using the TLS authentication method, including any required intermediate certificates expected by Hashicorp Vault.
- **Client Certificate Key**: specify a PEM-encoded certificate private key when using the TLS authentication method.
- **TLS Authentication Role**: specify the role or certificate name in Hashicorp Vault that corresponds to your client certificate when using the TLS authentication method. If it is not provided, Hashicorp Vault attempts to match the certificate automatically.
- **Namespace name**: specify the Namespace name (Hashicorp Vault enterprise only).
- **Kubernetes role**: specify the role name when using Kubernetes authentication.
- **Username**: enter the username of the user to be used to authenticate this service.
- **Password**: enter the password associated with the user to be used to authenticate this service.
- **Path to Auth**: specify a path if other than the default path of `/approle`.

## Microsoft Azure Key Vault

Use the Microsoft Azure Key Vault lookup to retrieve secrets from Microsoft Azure’s Key Management System (KMS) within your automation controller environment.

When you select **Microsoft Azure Key Vault** for **Credential Type**, give the following metadata to configure your lookup:

- **Vault URL (DNS Name)** (required): give the URL used for communicating with Microsoft Azure’s key management system
- **Client ID** (required): give the identifier as obtained by Microsoft Entra ID
- **Client Secret** (required): give the secret as obtained by Microsoft Entra ID
- **Tenant ID** (required): give the unique identifier associated with an Microsoft Entra ID instance within an Azure subscription
- **Cloud Environment**: select the applicable cloud environment to apply

## Thycotic DevOps Secrets Vault

Thycotic DevOps Secrets Vault is a secrets management system that enables secure storage and retrieval of sensitive information such as passwords, API keys, and certificates.

When you select **Thycotic DevOps Secrets Vault** for **Credential Type**, give the following metadata to configure your lookup:

- **Tenant** (required): give the URL used for communicating with Thycotic’s secret management system
- **Top-level Domain (TLD)**: give the top-level domain designation, for example .com, .edu, or .org, associated with the secret vault you want to integrate
- **Client ID** (required): give the identifier as obtained by the Thycotic secret management system
- **Client Secret** (required): give the secret as obtained by the Thycotic secret management system

## Thycotic Secret Server

Thycotic Secret Server is a secrets management system that enables secure storage and retrieval of sensitive information such as passwords, API keys, and certificates.

Give the following metadata to configure your lookup When you select **Thycotic Secrets Server** as **Credential Type**:

- **Secret Server URL** (required): give the URL used for communicating with the Thycotic Secrets Server management system
- **Username** (required): specify the authenticated user for this service
- **Domain**: give the (application) user domain
- **Password** (required): give the password associated with the user

## Configuring a `GitHub App Installation Access Token Lookup`

Learn how to configure a `GitHub App Installation Access Token Lookup` credential in automation controller.

### About this task

With this plugin you can use a private GitHub App RSA key as a credential input source to pull access tokens from GitHub App installations. Platform gateway uses existing GitHub authorization from organizations' GitHub repositories.

For more information, see [Generating an installation access token for a GitHub App](https://docs.github.com/en/apps/creating-github-apps/authenticating-with-a-github-app/generating-an-installation-access-token-for-a-github-app).

### Procedure

1.  Create a lookup credential that stores your secrets. For more information, see [Create new credentials](/documentation/en-us/red_hat_ansible_automation_platform/2.6/secure-proc_controller_create_credential "Learn how to create new credentials in Automation controller.").
2.  Select **GitHub App Installation Access Token Lookup** for **Credential type**, and enter the following attributes to properly configure your lookup:

- **GitHub App ID**: Enter the App ID provided by your instance of GitHub, this is what is used to authenticate.
- **GitHub App Installation ID**: Enter the ID of the application into your target organization where the access token is scoped. You must set it up to have access to your target repository.
- **RSA Private Key**: Enter the generated private key that your GitHub instance generated. You can get it from the GitHub App maintainer within GitHub. For more information, see [Managing private keys for GitHub Apps](https://docs.github.com/en/apps/creating-github-apps/authenticating-with-a-github-app/managing-private-keys-for-github-apps).

3.  Click Create credential to confirm and save the credential. The following is an example of a configured **GitHub App Installation Access Token Lookup** credential:

![GitHub App token lookup credential](/webassets/aem/red_hat_ansible_automation_platform/2.6/images/credentials-create-github-app-lookup-credential.png)

4.  Create a target credential that searches for the lookup credential. To use your lookup in a private repository, select **Source Control** as your **Credential type**. Enter the following attributes to properly configure your target credential:

- **Username**: Enter the username `x-access-token`.

- **Password**: Click the ![Link](/webassets/aem/red_hat_ansible_automation_platform/2.6/images/leftkey.png) icon for managing external credentials in the input field. You are prompted to set the input source to use to retrieve your secret information. This is the lookup credential that you have already created. ![Target credential secret info](/webassets/aem/red_hat_ansible_automation_platform/2.6/images/credentials-github-app-target-secret-info.png)

5.  Enter an optional description for the metadata requested and click Finish.
6.  Click Create credential to confirm and save the credential.
7.  Verify both your lookup credential and your target credential are now available on the **Credentials** list view. To use the target credential in a project, create a project and enter the following information:

- **Name**: Enter the name for your project.

- **Organization**: Select the name of the organization from the drop-down menu..

- **Execution environment**: Optionally select an execution environment, if applicable.

- **Source control type**: If you are syncing with a private repository, select **Git** for your source control. The **Type Details** view opens for additional input. Enter the following information:

- **Source control URL**: Enter the URL of the private repository you want to access. The other related fields pertaining to **branch/tag/commit** and **refspec** are not relevant for use with a lookup credential.

- **Source control credential**: Select the target credential that you have already created. The following is an example of a configured target credential in a project:

![GitHub App project](/webassets/aem/red_hat_ansible_automation_platform/2.6/images/project-create-git-github-app.png)

8.  Click Create project and the project sync automatically starts. The project **Details** tab displays the progress of the job:
![Project sync GitHub App](/webassets/aem/red_hat_ansible_automation_platform/2.6/images/project-sync-github-app.png)

If your project sync fails, you might have to manually re-enter `<https://api.github.com>` in the **GitHub API endpoint URL** field from Step 2 and re-run your project sync.

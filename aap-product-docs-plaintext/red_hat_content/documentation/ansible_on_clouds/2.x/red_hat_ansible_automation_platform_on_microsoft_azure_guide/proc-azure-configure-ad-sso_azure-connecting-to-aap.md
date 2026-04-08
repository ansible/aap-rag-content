# 5. Connecting to Red Hat Ansible Automation Platform
## 5.4. Accessing Red Hat Ansible Automation Platform on Microsoft Azure
### 5.4.2. Microsoft Entra ID SSO configuration




Set up your Microsoft Entra ID SSO configuration.

**Procedure**

- For help with setting up and configuring your enterprise authentication, see the _Chapter 3. Configuring Microsoft Entra ID authentication_ section of the [Access management and authentication](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/access_management_and_authentication/index) guide.


#### 5.4.2.1. Creating a registered application in Microsoft Entra ID




To create a Microsoft Entra ID SSO configuration you must first register for Microsoft Entra ID.

**Procedure**

1. In a web browser, open the Azure portal.
1. Ensure that you are using the tenant where you deployed Ansible Automation Platform.
1. Type `    Microsoft Entra ID` in the search bar.
1. Select **Microsoft Entra ID** from the search results.
1. Under **Manage** in the menu options, click **App registrations** .
1. In the **App registrations** page, click **+ New registration** .
1. Configure the new registration as follows:


- In the **Name** field, enter the same name that you used for the deployed application.
- Select the default value for **Supported account types** .
- Select **Web** for **Redirect URI (optional)** .
- In the **Redirect URI (optional)** field, enter the _Microsoft Entra ID OAuth2 Callback URL_ value that you fetched from Ansible Automation Platform.

1. Click **Register** to create the registration.


**Verification**

When registration is complete, the registration page for the Ansible Automation Platform application is displayed.


#### 5.4.2.2. Generating secrets for communication




Create secrets so your applications can communicate with one another.

**Procedure**

1. In the **Ansible Automation Platform application registration page** on Azure, copy and save the value of _Application (client) ID_ .

You need this value for the _Microsoft Entra ID OAuth2 Key_ in the Ansible Automation Platform settings.


1. Under **Manage** , click **Certificates & secrets** .
1. Click **Client secrets** and then **New client secret** .
1. Provide a description for the new secret.


- It is not possible to automatically renew a certificate or identify when it is about to expire.
- It is useful to include the date in the description, for example: _Ansible Automation Platform Client Secret <Today’s Date in YYYY-MM-DD format>_ .

1. Provide an expiration date for the new secret.


1. The maximum lifetime for the certificate is 2 years. Unless you have specific security needs that prevent the creation of a long term certificate, select an expiration date of **24 months** .

1. Save the secret _Value_ to a location on your local machine. After you navigate away from this page the secret value is no longer retrievable.


#### 5.4.2.3. Creating a service principal for automating Azure resources




To enable the Ansible Automation Platform application to access and manage Azure resources, you must provide authorization credentials after deployment. The Microsoft Azure collection supports service principal authentication.

To create a service principal, you must have administrator privileges with tenancy-wide permissions on your Azure tenant. Your Ansible Automation Platform on Microsoft Azure deployment provisions in the same Subscription ID as the service principal created in this step.

**Procedure**

1. Navigate to the Azure portal
1. Click the [Cloud Shell](https://learn.microsoft.com/en-us/azure/cloud-shell/overview) icon to open a bash Cloud Shell in your browser.
1. Set the Azure CLI to use the subscription that you intend to use for automating Azure services. Run the following command from the shell:


```
az account set --subscription &lt;your_subscription_id&gt;
```


1. Run the following command using the Azure CLI to create a privileged service principal in Microsoft Entra ID:


```
az ad sp create-for-rbac --name ansible --role Contributor
```

The output displays the _appID_ and _tenant_ keys for the service principal:


```
{      "appId": "xxxxxxx-xxx-xxxx",      "displayName": "ansible",      "name": "xxxxxxx-xxx-xxxx",      "password": "xxxxxxx-xxx-xxxx",      "tenant": "xxxxxxx-xxx-xxxx"    }
```


1. Store the service principal details securely, as they are displayed only when you create the secret.


#### 5.4.2.4. Maintain your service principals




Service principal credentials have a limited lifetime that is set in your Microsoft Entra ID configuration.

Track the lifespan of the service principal if you intend to automate against Azure for an extended period of time. You can create a new one when needed.

To view records of updated or deleted service principles, run the following Azure CLI command:

```
az ad sp list -o table | grep ansible
```

This command does not display the secrets for your service principals. Delete the service principal and create a new one if the secret is lost.

When you create a new service principal to replace an expired or deleted one, you must update the credential that uses the service principal that you are replacing. If the credential is not updated, automations that use that credential will fail.


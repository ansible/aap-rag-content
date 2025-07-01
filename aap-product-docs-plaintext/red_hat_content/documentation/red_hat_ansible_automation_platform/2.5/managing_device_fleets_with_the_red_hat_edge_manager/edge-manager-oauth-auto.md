# 3. Installing the Red Hat Edge Manager on Ansible Automation Platform
## 3.2. Set up the OAuth application for Ansible Automation Platform
### 3.2.2. Setting up the OAuth application automatically




**Procedure**

1. Generate an OAuth token in Ansible Automation Platform:


1. From the navigation panel, selectAccess Management→Users.
1. Select a user with write permissions to the **Default** organization (admin user recommended).
1. Click the **Tokens** tab for that user.
1. ClickCreate tokenand enter the relevant details.

1. Add the token to **oAuthToken** in your configuration file, for example:


```
global:      baseDomain: &lt;your-edge-manager-ip-or-domain&gt;      auth:        type: aap        insecureSkipTlsVerify: true        aap:          apiUrl: https://your-aap-instance.example.com          externalApiUrl: https://your-aap-instance.example.com          oAuthApplicationClientId:  # Leave empty          oAuthToken: &lt;your-oauth-token&gt;
```




When you start the services, the OAuth application is created automatically, and the **oAuthApplicationClientId** is updated in the configuration file.


# 3. Installing the Red Hat Edge Manager on Ansible Automation Platform
## 3.2. Set up the OAuth application for Ansible Automation Platform
### 3.2.1. Setting up the OAuth application manually




**Procedure**

1. From the navigation panel on your Ansible Automation Platform instance, go toAccess Management→OAuth Applications.
1. ClickCreate OAuth application.
1. Enter the following details:


-  **Name** : Enter a name such as "Red Hat Edge Manager".
-  **URL** : The `        baseDomain` of your Ansible Automation Platform UI.
-  **Authorization grant type** : Select **Authorization code** .
-  **Client** : Select **Public** .
-  **Redirect URIs** :


- The redirect configured for your UI is your `            baseDomain` with a /callback route appended, such as `            <a class="link" href="https://your-edge-manager-ip-or-domain/callback">https://your-edge-manager-ip-or-domain/callback</a>` .
- To provide a redirect for console usage, configure a redirect URI, such as `            <a class="link" href="http://127.0.0.1/callback">http://127.0.0.1/callback</a>` .


1. Copy the **Client ID** and update **oAuthApplicationClientId** in your configuration file with this value when [Integrating with Ansible Automation Platform](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/managing_device_fleets_with_the_red_hat_edge_manager/assembly-edge-manager-install#edge-manager-integrate-aap) .


Note
URIs must be separated by spaces in the **Redirect URIs** field, not commas or other delimiters.



**Additional resources**

For more information, see [Configuring access to external applications with token-based authentication](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/access_management_and_authentication/gw-token-based-authentication) .



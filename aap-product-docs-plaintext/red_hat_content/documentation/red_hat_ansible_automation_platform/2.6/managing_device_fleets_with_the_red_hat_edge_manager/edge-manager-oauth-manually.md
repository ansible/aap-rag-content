# 3. Installing the Red Hat Edge Manager on Ansible Automation Platform
## 3.2. Set up the OAuth application for Ansible Automation Platform
### 3.2.2. Setting up the OAuth application manually




Manually set up an OAuth application within your Ansible Automation Platform instance. This is important for enabling token-based authentication and integrating external applications such as the Red Hat Edge Manager.

**Procedure**

1. From the navigation panel on your Ansible Automation Platform instance, go toAccess Management→OAuth Applications.
1. ClickCreate OAuth application.
1. Enter the following details:


-  **Name** : Enter a name such as "Red Hat Edge Manager". This is the name visible in the Ansible Automation Platform UI.
-  **URL** : The `        baseDomain` of your Red Hat Edge Manager UI with `        https://` .
-  **Organization** : Select **Default** .
-  **Authorization grant type** : Select **Authorization code** .
-  **Client** : Select **Public** .
-  **Redirect URIs** :


- The redirect configured for your UI is your `            baseDomain` with a /callback route appended, such as `            <a class="link" href="https://your-edge-manager-ip-or-domain:443/callback">https://your-edge-manager-ip-or-domain:443/callback</a>` . If you have more than one URI, enter them in this field separated by a space, not commas or other delimiters.
- To provide a redirect for CLI usage ( `            flightctl login` ), configure a redirect URI, such as `            <a class="link" href="http://127.0.0.1/callback">http://127.0.0.1/callback</a>` .


1. ClickCreate OAuth application. An **Application Links** section is now visible in the navigation panel.
1. Copy the **Client ID** as you need it to update the **oAuthApplicationClientId** in your `    service-config.yaml` file with this value.
1. Go to the [Integrating with Ansible Automation Platform](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/managing_device_fleets_with_the_red_hat_edge_manager/assembly-edge-manager-install#edge-manager-integrate-aap) section for the steps to edit your `    service-config.yaml` file and complete setting up the OAuth application manually.


**Additional resources**

-  [Configuring access to external applications with token-based authentication](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/access_management_and_authentication/gw-token-based-authentication)



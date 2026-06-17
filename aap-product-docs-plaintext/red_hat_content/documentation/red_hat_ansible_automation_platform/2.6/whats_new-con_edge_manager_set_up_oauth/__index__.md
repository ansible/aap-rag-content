# Set up the OAuth application for Ansible Automation Platform

You have two options for setting up the OAuth application in Ansible Automation Platform, either manually or automatically in the Ansible Automation Platform UI.

## Set up the OAuth application automatically

Automatic setup of an OAuth application by generating an OAuth token within Ansible Automation Platform and adding it to your configuration file. Upon service startup, the application is automatically created, and the client ID updated.

### About this task

### Procedure

1.  Generate an OAuth token in Ansible Automation Platform:
1.  From the navigation panel, select Access Management> (and then)Users.
2.  Select a user with write permissions to the **Default** organization (admin user recommended).
3.  Click the **Tokens** tab for that user.
4.  Click Create token and enter the relevant details.     1. **Scope**: Select **Write**.

2.  Go to the [Integrate with Ansible Automation Platform](/documentation/en-us/red_hat_ansible_automation_platform/2.6/whats_new-con_edge_manager_set_up_oauth#edge-manager-integrate-aap "Integrate the Red Hat Edge Manager with your Ansible Automation Platform instance by modifying the service-config.yaml file to include authentication type, API URLs, OAuth client ID, and an optional OAuth token, followed by restarting the services.") section for the steps to edit your `service-config.yaml` file and complete setting up the OAuth application automatically.

## Set up the OAuth application manually

Manually set up an OAuth application within your Ansible Automation Platform instance. This is important for enabling token-based authentication and integrating external applications such as the Red Hat Edge Manager.

### About this task

### Procedure

1.  From the navigation panel on your Ansible Automation Platform instance, go to Access Management> (and then)OAuth Applications.
2.  Click Create OAuth application.
3.  Enter the following details:

- **Name**: Enter a name such as "Red Hat Edge Manager". This is the name visible in the Ansible Automation Platform UI.
- **URL**: The `baseDomain` of your Red Hat Edge Manager UI with `https://`.
- **Organization**: Select **Default**.
- **Authorization grant type**: Select **Authorization code**.
- **Client**: Select **Public**.
- **Redirect URIs**:
* The redirect configured for your UI is your `baseDomain` with a /callback route appended, such as `<https://your-edge-manager-ip-or-domain:443/callback>`. If you have more than one URI, enter them in this field separated by a space, not commas or other delimiters.
* To provide a redirect for CLI usage (`flightctl login`), configure a redirect URI, such as `<http://127.0.0.1/callback>`.

4.  Click Create OAuth application. An **Application Links** section is now visible in the navigation panel.
5.  Copy the **Client ID** as you need it to update the **oAuthApplicationClientId** in your `service-config.yaml` file with this value.
6.  Go to the [Integrating with Ansible Automation Platform](/documentation/en-us/red_hat_ansible_automation_platform/2.6/whats_new-con_edge_manager_set_up_oauth#edge-manager-integrate-aap "Integrate the Red Hat Edge Manager with your Ansible Automation Platform instance by modifying the service-config.yaml file to include authentication type, API URLs, OAuth client ID, and an optional OAuth token, followed by restarting the services.") section for the steps to edit your `service-config.yaml` file and complete setting up the OAuth application manually.

## Integrate with Ansible Automation Platform

Integrate the Red Hat Edge Manager with your Ansible Automation Platform instance by modifying the `service-config.yaml` file to include authentication type, API URLs, OAuth client ID, and an optional OAuth token, followed by restarting the services.

### About this task

### Procedure

1.  Stop the flightctl services before editing your `service-config.yaml` file:


```
sudo systemctl stop flightctl.target
```

2.  Configure the integration settings by editing the configuration file:


```
sudo vi /etc/flightctl/service-config.yaml
```

3.  Update the configuration file to integrate with Ansible Automation Platform:


```yaml
global:
baseDomain: <your-edge-manager-ip-or-domain>
auth:
type: aap
insecureSkipTlsVerify: false
aap:
apiUrl: https://your-aap-instance.example.com
externalApiUrl: https://your-aap-instance.example.com
oAuthApplicationClientId: <client-id-from-oauth-app>
oAuthToken: <your-oauth-token>
```


baseDomain
The domain name or IP for the host. This is the only mandatory field.

type
Set this to `aap` to enable Ansible Automation Platform authentication.

insecureSkipTlsVerify
Set to `false`. Only set this to `true` to skip TLS certificate verification for the Ansible Automation Platform URLs. For production environments, consider configuring a CA certificate (see the Self-signed certificates section).

apiUrl
The internal facing API URL for the running Ansible Automation Platform instance that makes requests against.

externalApiUrl
The externally accessible URL of your running Ansible Automation Platform instance.

oAuthApplicationClientId
This is the Client ID of the OAuth application configured in Ansible Automation Platform for the Red Hat Edge Manager. This is not necessary if you are using the automatic method.

oAuthToken
This is an OAuth token with write permissions for the "Default" organization. This is only needed if you want the setup process to automatically create the OAuth application. This is not necessary if you are using the manual method.

4.  Start the services:


```
sudo systemctl start flightctl.target
```

## Self-signed certificates

The Red Hat Edge Manager services automatically generate and store self-signed certificates in the `/etc/flightctl/pki` directory. These include:

-  `/etc/flightctl/pki/ca.crt`
-  `/etc/flightctl/pki/ca.key`
-  `/etc/flightctl/pki/client-enrollment.crt`
-  `/etc/flightctl/pki/client-enrollment.key`
-  `/etc/flightctl/pki/server.crt`
-  `/etc/flightctl/pki/server.key`


You can use your own custom certificates by placing them in the following locations:

- Custom Server Certificate/Key Pair:
* `/etc/flightctl/pki/server.crt`
* `/etc/flightctl/pki/server.key`
- Custom CA Certificate for Ansible Automation Platform authentication:
* `/etc/flightctl/pki/auth/ca.crt`


Note:

Ensure that you adjust the `insecureSkipTlsVerify` setting in the `service-config.yaml` if you use a custom CA certificate for your Ansible Automation Platform instance.

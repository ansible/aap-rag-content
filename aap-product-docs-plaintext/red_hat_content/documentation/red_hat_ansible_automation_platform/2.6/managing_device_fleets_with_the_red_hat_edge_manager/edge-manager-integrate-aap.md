# 3. Installing the Red Hat Edge Manager on Ansible Automation Platform
## 3.2. Set up the OAuth application for Ansible Automation Platform
### 3.2.3. Integrating with Ansible Automation Platform

Integrate the Red Hat Edge Manager with your Ansible Automation Platform instance by modifying the `service-config.yaml` file to include authentication type, API URLs, OAuth client ID, and an optional OAuth token, followed by restarting the services.

**Procedure**

1. Stop the flightctl services before editing your `service-config.yaml` file:

sudo systemctl stop flightctl.target

2. Configure the integration settings by editing the configuration file:

sudo vi /etc/flightctl/service-config.yaml

3. Update the configuration file to integrate with Ansible Automation Platform:

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

4. Start the services:

sudo systemctl start flightctl.target


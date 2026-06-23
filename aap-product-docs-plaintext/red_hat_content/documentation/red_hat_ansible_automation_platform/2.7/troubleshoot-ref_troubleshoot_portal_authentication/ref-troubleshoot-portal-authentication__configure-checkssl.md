# Troubleshoot Ansible automation portal authentication
## Configure checkSSL for self-signed certificates

When Ansible Automation Platform uses a self-signed certificate or a certificate from an untrusted certificate authority, configure Ansible automation portal to skip TLS certificate verification for backend-to-Ansible Automation Platform communication. This setting affects only the portal backend and does not change browser behavior.

Important:

- Setting `checkSSL` to `false` disables TLS certificate verification between the portal backend and Ansible Automation Platform. Use this setting only in development, testing, or demo environments.
- For production environments, use a CA-signed certificate on Ansible Automation Platform or add the Ansible Automation Platform CA certificate to the portal trust store. See [Configure custom SSL certificates for the Ansible automation portal](/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-proc_self_service_configure_custom_ssl "If your Ansible Automation Platform instance uses custom or self-signed SSL certificates, configure the Ansible automation portal to trust those certificates to prevent authentication failures.").
- You must set `checkSSL` to `false` in **two separate locations** in the configuration. Missing either location causes different failures.

In your Helm chart `values.yaml` or `app-config.yaml`, locate and update both `checkSSL` settings:

```yaml
ansible:
rhaap:
baseUrl: https://*aap-host*
checkSSL: false    # Backend API calls to AAP (catalog sync, token exchange)
token: ${AAP_TOKEN}

auth:
providers:
rhaap:
production:
host: https://*aap-host*
checkSSL: false  # OAuth authentication calls to AAP
clientId: ${OAUTH_CLIENT_ID}
clientSecret: ${OAUTH_CLIENT_SECRET}
```
If you deployed with Helm, upgrade the release:

```terminal
$ helm upgrade *release-name* *chart* -f values.yaml -n *namespace*
```
If you edited the ConfigMap directly, restart the deployment:

```terminal
$ oc rollout restart deployment/*portal-deployment-name* -n *namespace*
```
Wait for the new pod to become ready:

```terminal
$ oc rollout status deployment/*portal-deployment-name* -n *namespace*
```
Verify the configuration took effect by checking the pod logs for successful Ansible Automation Platform connectivity:

```terminal
$ oc logs -n *namespace* deployment/*portal-deployment-name* -c backstage-backend | grep -i "rhaap\|AAP\|error"
```
Successful catalog sync logs look like:

```
[catalog] info  Fetching job templates from RH AAP.
[catalog] info  [backstage-rhaap-common]: Executing get request to https://*aap-host*/api/controller/v2/job_templates...
```
If you still see `fetch failed` errors, verify that the correct ConfigMap was updated and the pod restarted with the new configuration.

**Accept the Ansible Automation Platform certificate in your browser**

Setting `checkSSL` to `false` fixes backend communication but does not affect your browser. Before signing in to Ansible automation portal for the first time in a new browser session:

1. Open a new tab and navigate directly to your Ansible Automation Platform URL (for example, `https://*aap-host*/`).
2. Accept the browser certificate warning (click **Advanced**, then **Proceed**).
3. Return to Ansible automation portal and click **Sign In**.


Note:

For RHEL appliance deployments, the `check_ssl` cloud-init setting automatically mirrors to both configuration locations. If you edit `app-config.production.yaml` manually, you must update both locations.


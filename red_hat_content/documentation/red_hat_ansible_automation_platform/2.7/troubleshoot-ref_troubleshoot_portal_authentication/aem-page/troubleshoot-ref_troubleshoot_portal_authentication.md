+++
title = "Troubleshoot Ansible automation portal authentication - Red Hat Ansible Automation Platform 2.7"
template = "docs/aem-title.html"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/troubleshoot-ref_troubleshoot_portal_authentication"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/troubleshoot-ref_troubleshoot_portal_authentication/", "Troubleshoot Ansible automation portal authentication"]]
category = "Troubleshoot"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/troubleshoot-ref_troubleshoot_portal_authentication/aem-page/troubleshoot-ref_troubleshoot_portal_authentication.html"
last_crumb = "Troubleshoot Ansible automation portal authentication"
modified = "2026-06-05T07:48:10.594Z"
multi_page_path = ""
name = "Troubleshoot Ansible automation portal authentication"
oversized = "false"
page_slug = "troubleshoot-ref_troubleshoot_portal_authentication"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/troubleshoot-ref_troubleshoot_portal_authentication"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/troubleshoot-ref_troubleshoot_portal_authentication/toc/toc.json"
type = "aem-page"
+++

# Troubleshoot Ansible automation portal authentication

Identify and resolve common authentication and login issues when connecting Ansible automation portal to Ansible Automation Platform.

## Overview

Use the symptom table to identify your issue, then follow the resolution steps. If the table does not cover your issue, use the diagnostic procedure to check portal logs for additional information.

For issues specific to execution environment builder, see [Troubleshoot execution environment builder](/documentation/en-us/red_hat_ansible_automation_platform/2.7/troubleshoot-ref_troubleshoot_ee_builder "Identify and resolve common issues when configuring or using execution environment builder in Ansible automation portal."). For issues specific to the RHEL appliance deployment, see [Troubleshooting RHEL appliances](/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-ref_self_service_rhel_troubleshooting "Common issues and solutions for deploying and managing Ansible automation portal RHEL appliances.").

## Common authentication issues

| Symptom                                                                                                                         | Cause                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | Resolution                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| ------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Sign In** redirects to a browser certificate error page instead of the Ansible Automation Platform login form                 | Ansible Automation Platform uses a self-signed certificate or a certificate from an untrusted CA. The browser rejects the connection to the Ansible Automation Platform OAuth authorization endpoint (`/o/authorize/`).                                                                                                                                                                                                                                                                            | Before signing in to Ansible automation portal, open the Ansible Automation Platform URL directly in your browser (for example, `https://*aap-host*/`) and accept the certificate warning. After accepting, return to Ansible automation portal and click **Sign In** again. For production environments, use a CA-signed certificate on Ansible Automation Platform.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| **Sign In** completes at Ansible Automation Platform but returns to the portal with `Failed to send POST request: fetch failed` | The portal backend cannot reach the Ansible Automation Platform OAuth token endpoint (`/o/token/`) because `checkSSL` is set to `true` and Ansible Automation Platform uses a self-signed certificate. The Node.js backend rejects the untrusted certificate during the authorization code exchange.                                                                                                                                                                                               | Set `checkSSL` to `false` in **both** locations in the Helm chart values: under `ansible.rhaap.checkSSL` and under `auth.providers.rhaap.production.checkSSL`. Restart the portal deployment. See [Configure checkSSL for self-signed certificates](/documentation/en-us/red_hat_ansible_automation_platform/2.7/troubleshoot-ref_troubleshoot_portal_authentication#ref-troubleshoot-portal-authentication__configure-checkssl).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| **Sign In** completes at Ansible Automation Platform but returns to the portal with `Auth response is missing cookie nonce`     | The OAuth nonce cookie set during the authorization start was not sent back with the callback request. This can occur when the Ansible Automation Platform host is a bare IP address, when browser cookie policies block cross-site cookies, or when there is a protocol mismatch between the portal and Ansible Automation Platform URLs.                                                                                                                                                         | Verify that `app.baseUrl` and `backend.baseUrl` use the same protocol (`https://`). If Ansible Automation Platform is accessed by IP address, accept the certificate in your browser before starting the OAuth flow. Clear browser cookies for the portal domain and retry.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Catalog sync fails with `Failed to send fetch data: fetch failed` (users and teams not synced from Ansible Automation Platform) | The portal backend cannot reach the Ansible Automation Platform API because `ansible.rhaap.checkSSL` is `true` and Ansible Automation Platform uses a self-signed certificate. This is the same root cause as the OAuth token exchange failure.                                                                                                                                                                                                                                                    | Set `ansible.rhaap.checkSSL` to `false` in the Helm chart values or `app-config.yaml`. Restart the portal deployment. Catalog sync runs on a schedule and resumes automatically after the restart.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Portal shows `Authenticated but no permissions` or users see an empty interface after login                                     | Catalog synchronization has not completed, or the user does not exist in the portal catalog. The `allowNewAAPUserSignIn` resolver creates users automatically, but requires the catalog backend module to be functioning.                                                                                                                                                                                                                                                                          | Verify catalog sync is running without errors. Check that `catalog.providers.rhaap` is configured with the correct Ansible Automation Platform organization. Check logs for `AapEntityProvider` errors. If using the `usernameMatchingUser` resolver, verify the user exists in the portal catalog.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| OAuth login redirects to Ansible Automation Platform but Ansible Automation Platform returns `invalid redirect_uri`             | The redirect URI configured in the Ansible Automation Platform OAuth application does not match the portal callback URL. The redirect URI must be exactly `https://*portal-host*/api/auth/rhaap/handler/frame`.                                                                                                                                                                                                                                                                                    | In Ansible Automation Platform, navigate to **Administration** > **OAuth Applications**, edit the application, and set the redirect URI to `https://*portal-host*/api/auth/rhaap/handler/frame`. Verify there are no trailing slashes or protocol mismatches.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Portal pod logs show errors reaching Ansible Automation Platform but `curl -k` from the pod works                               | `checkSSL` is `true` in the portal configuration. The `-k` flag in `curl` skips certificate verification, but the portal Node.js backend respects the `checkSSL` setting.                                                                                                                                                                                                                                                                                                                          | Set `checkSSL` to `false` in both locations. See [Configure checkSSL for self-signed certificates](/documentation/en-us/red_hat_ansible_automation_platform/2.7/troubleshoot-ref_troubleshoot_portal_authentication#ref-troubleshoot-portal-authentication__configure-checkssl).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| The login page shows **Sign in with GitHub** instead of **Sign in with RHAAP**, or both options appear                          | The `app.baseUrl`, `backend.baseUrl`, and `backend.cors.origin` values in the configuration do not match the URL used to access Ansible automation portal. This commonly happens when accessing the portal by IP address or through port-forwarding (for example, `localhost:7007`) but the configuration uses the OpenShift Container Platform route URL, or vice versa. The CORS mismatch can cause the RHAAP provider to fail silently, falling back to a GitHub provider if one is configured. | Access Ansible automation portal using the OpenShift Container Platform route URL, not through port-forwarding to `localhost`.Verify that `app.baseUrl`, `backend.baseUrl`, and `backend.cors.origin` all match the URL you use to access the portal in your browser. Check the Helm chart values:   ```terminal $ helm get values *release-name* -n *namespace* | grep -E 'baseUrl|origin' ``` Verify that the `auth.providers` section does not contain an uncommented `github` provider. If a `github` provider is present and not required for execution environment builder SCM integration, remove it.Apply the corrected values:   ```terminal $ helm upgrade *release-name* *chart* -f values.yaml -n *namespace* ``` <br>For RHEL appliance deployments, see [Troubleshooting RHEL appliances](/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-ref_self_service_rhel_troubleshooting "Common issues and solutions for deploying and managing Ansible automation portal RHEL appliances."). |
| Portal deployed with `global._environment._development: true` in Helm values                                                    | The `_development` flag changes plugin image sources and catalog environment settings. It is intended for internal development and testing only. Production deployments must use `_development: false` and `_production: true` (the defaults).                                                                                                                                                                                                                                                     | In the Helm chart `values.yaml`, verify the environment settings:   ```yaml global:   _environment:     _development: false     _stage: false     _production: true ``` <br>Apply the corrected values with `helm upgrade` and wait for the pods to restart.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |

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

## Diagnose authentication failures

If the symptom table does not match your issue, use the following steps to gather diagnostic information.

1. Check portal backend logs for authentication errors:

```terminal
$ oc logs -n *namespace* deployment/*portal-deployment-name* -c backstage-backend | grep -i "auth\|rhaap\|error\|fetch\|token"
```

2. Check for certificate-related failures from inside the pod:

```terminal
$ oc exec -n *namespace* deployment/*portal-deployment-name* -c backstage-backend -- \
  curl -k -s -o /dev/null -w "HTTP_CODE: %{http_code}\nSSL_VERIFY: %{ssl_verify_result}\n" \
  https://*aap-host*/
```
  - `HTTP_CODE: 200` confirms Ansible Automation Platform is reachable.
  - `SSL_VERIFY: 0` means the certificate is trusted. `SSL_VERIFY: 20` means the issuer certificate is not in the trust store (self-signed CA).

3. Verify the Ansible Automation Platform OAuth application configuration:

```terminal
$ curl -k -s -u *admin-user*:*password* https://*aap-host*/api/gateway/v1/me/ | python3 -m json.tool
```
     A successful response confirms Ansible Automation Platform credentials are valid and the API is accessible.

For a complete list of common log messages and their meanings, see [View Ansible automation portal logs for execution environment builder](/documentation/en-us/red_hat_ansible_automation_platform/2.7/troubleshoot-proc_view_ee_builder_logs "View Ansible automation portal logs to diagnose authentication failures, sync errors, catalog registration issues, and SCM connectivity problems.").

+++
title = "Get started with OAuth Applications - Red Hat Ansible Automation Platform 2.7"
template = "docs/aem-title.html"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/secure-ref_controller_applications_getting_started"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/secure-assembly_gw_configure_authentication/", "Configure central authentication for Ansible Automation Platform"]]
category = "Secure"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/secure-ref_controller_applications_getting_started/aem-page/secure-ref_controller_applications_getting_started.html"
last_crumb = "Get started with OAuth Applications"
latest = "true"
modified = "2026-10-06T15:21:13.207Z"
multi_page_path = ""
name = "Get started with OAuth Applications"
oversized = "false"
page_slug = "secure-ref_controller_applications_getting_started"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/secure-ref_controller_applications_getting_started"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/secure-ref_controller_applications_getting_started/toc/toc.json"
type = "aem-page"
+++

# Get started with OAuth Applications

You can access the **OAuth Applications** page from the navigation panel by selecting Access Management> (and then)OAuth Applications. From there you can view, create, sort and search for applications currently managed by Ansible Automation Platform and automation controller.

If no applications exist, you can create one by clicking Create OAuth application.

## Application functions

Several OAuth 2 utilities are available for authorization, token refresh, and revoke.
You can specify the following grant types when creating an application:

Password
This grant type is ideal for users who have native access to the web application and must be used when the client is the resource owner.

Authorization code
This grant type should be used when access tokens must be issued directly to an external application or service.

Note:

You can only use the authorization code type to acquire an access token when using an application. When integrating an external web application with Ansible Automation Platform, that web application might need to create OAuth2 tokens on behalf of users in that other web application. Creating an application in the platform with the authorization code grant type is the preferred way to do this because:

- This allows an external application to obtain a token from Ansible Automation Platform for a user, using their credentials.
- Compartmentalized tokens issued for a particular application enables those tokens to be easily managed. For example, revoking *all* tokens associated with that application without having to revoke all tokens in the system.

## Refresh an access token after expiration

You can use a refresh token to request a new access token after the original token expires.

### About this task

The default expiration for OAuth2 access tokens is 31,536,000 seconds (1 year). You can configure this value in the `OAUTH2_PROVIDER` settings in `etc/ansible-automation-platform/gateway/settings.py`.

When an access token expires, use the original refresh token to request a new access token without re-authorizing.

### Procedure

1. Make a POST request to the `/o/token/` endpoint with your client credentials in the Authorization header:
  

```
curl -X POST \
  -H "Authorization: Basic <base64(client_id:client_secret)>" \
  -d "grant_type=refresh_token" \
  -d "refresh_token=<your_refresh_token>" \
  https://<platform_gateway>/o/token/
```

    Replace `<base64(client_id:client_secret)>` with the Base64-encoded string of your application client ID and client secret, separated by a colon.

    Replace `<your_refresh_token>` with the refresh token returned in the original token response.

    Replace `<platform_gateway>` with the hostname of your platform gateway.

2. Verify that the response includes a new `access_token` and `refresh_token`.
      The server revokes the previous refresh token after use.

### What to do next

Note:

Refresh tokens expire after approximately 30 days (2,628,000 seconds) by default. After the refresh token expires, you must complete a full re-authorization. You can configure this value with the `REFRESH_TOKEN_EXPIRE_SECONDS` setting in `OAUTH2_PROVIDER` in `/etc/ansible-automation-platform/gateway/settings.py`.

## Configure the OAuth access token lifetime on OpenShift Container Platform

On an operator-based installation, set the OAuth access token lifetime in the `AnsibleAutomationPlatform` custom resource so platform gateway applies it across reconciliations.

### Before you begin

- Cluster access to edit the `AnsibleAutomationPlatform` custom resource (CR).

### About this task

Set the OAuth access token lifetime in the `AnsibleAutomationPlatform` CR by using `spec.extra_settings`.

Important:

Do not edit the operator-managed platform gateway settings Secret directly. The operator regenerates that Secret from the CR, so manual edits are lost on the next reconciliation.

### Procedure

1. Edit your `AnsibleAutomationPlatform` CR and add the setting under `spec.extra_settings`:
  

```
apiVersion: aap.ansible.com/v1alpha1
kind: AnsibleAutomationPlatform
metadata:
  name: myaap
  namespace: ansible-automation-platform
spec:
  extra_settings:
    - setting: OAUTH2_PROVIDER['ACCESS_TOKEN_EXPIRE_SECONDS']
      value: '<seconds>'
```

    Replace `myaap` and `ansible-automation-platform` with the name and namespace of your `AnsibleAutomationPlatform` instance. Set `value` to the required lifetime in seconds, as a quoted string. For example, `'28800'` limits token validity to 8 hours.

2. Save the CR.
      The operator automatically applies this configuration to platform gateway on the next reconciliation. You do not need to redeploy manually

### What to do next

- Changing the lifetime affects only newly created tokens. Existing tokens keep their original expiration.
- Avoid extremely short lifetimes. A short lifetime can affect the operator service-account OAuth token if that token is recreated after the setting is applied.

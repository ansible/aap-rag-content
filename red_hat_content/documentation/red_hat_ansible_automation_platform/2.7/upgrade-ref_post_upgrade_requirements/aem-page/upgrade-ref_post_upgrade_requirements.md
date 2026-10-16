+++
title = "Post-upgrade requirements - Red Hat Ansible Automation Platform 2.7"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/upgrade-ref_post_upgrade_requirements"
template = "docs/aem-title.html"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/upgrade-ref_post_upgrade_requirements/", "Post-upgrade requirements"]]
category = "Upgrade"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/upgrade-ref_post_upgrade_requirements/aem-page/upgrade-ref_post_upgrade_requirements.html"
last_crumb = "Post-upgrade requirements"
latest = "true"
modified = "2026-10-06T15:21:13.207Z"
multi_page_path = ""
name = "Post-upgrade requirements"
oversized = "false"
page_slug = "upgrade-ref_post_upgrade_requirements"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/upgrade-ref_post_upgrade_requirements"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/upgrade-ref_post_upgrade_requirements/toc/toc.json"
type = "aem-page"
+++

# Post-upgrade requirements

After upgrading to Ansible Automation Platform 2.7, update tokens, scripts, and integrations to use platform gateway for all external authentication and API access.

After upgrading to Ansible Automation Platform 2.7, perform the following actions:

- **Regenerate tokens:** Regenerate all Personal Access Tokens through platform gateway.
- **Update CaC:** Update Configuration as Code files to use platform gateway URLs.
- **Update scripts:** Update scripts and integrations to point to platform gateway.
- **Update container registry:** Re-authenticate to the container registry.
- **Update collection connection parameters:** Update playbooks that use `ansible.controller`, `ansible.hub`, or `ansible.eda` collections to point to the platform gateway hostname instead of direct component hostnames. For example, change `controller_host` from `controller.example.com` to `gateway.example.com`. Token parameters such as `controller_oauthtoken` must use tokens created through platform gateway.

## Validating gateway authentication after the 2.7 upgrade

After upgrading to Red Hat Ansible Automation Platform 2.7, validate that all platform components and integrations are functioning correctly with gateway-based authentication.

### About this task

**Validation checklist**

Confirm the following results to ensure the upgrade was successful:

- Users can log in to the platform gateway UI.
- Direct access to component APIs (controller, hub, or EDA) returns an HTTP 401 Unauthorized response.
- Job templates launch successfully through the platform gateway API.
- Collections download from automation hub through the gateway.
- Container registry authentication works using `podman login` or `docker login`.
- Event-Driven Ansible rulebook activations are in a Running state.
- Configuration as Code (CaC) playbooks execute successfully.
- Third-party authentication providers, such as LDAP or SAML, function through the gateway.

### Procedure

Quick validation commands

1. Test platform gateway API access:
  

```
$ curl -H "Authorization: Bearer ${GATEWAY_TOKEN}" \
  https://gateway.example.com/api/gateway/v1/ping/
```

2. Verify direct access is blocked (should return 401):
  

```
$ curl -H "Authorization: Bearer ${OLD_TOKEN}" \
  https://controller.example.com/api/v2/ping/
```

### Results

In Ansible Automation Platform 2.7, authentication at the component level is disabled for external requests. An HTTP 401 Unauthorized response for direct component access is the correct behavior.

### What to do next

If validation steps fail, see the following resources:

- For authentication issues, see [Mandatory platform gateway authentication](/documentation/en-us/red_hat_ansible_automation_platform/2.7/secure-mandatory_platform_gateway_authentication_in_ansible_automation_platform_2_7#con-mandatory-gateway-auth "In Red Hat Ansible Automation Platform 2.7, platform gateway is the only supported method for external authentication to platform components. Direct API access to automation controller, automation hub, and Event-Driven Ansible has been removed.").
- For large uploads failing after upgrade, you may need to adjust gateway upload settings. For more information, see [Configure platform gateway route timeouts](/documentation/en-us/red_hat_ansible_automation_platform/2.7/secure-con_gateway_route_timeouts#con-gateway-route-timeouts "In Ansible Automation Platform 2.7, all API access to platform components goes through platform gateway. Gateway-level timeout settings control how long platform gateway waits for backend services to respond before closing a connection.").
- For operational issues, see the specific component documentation.

## Verify your authentication configuration after upgrade

After upgrading to Ansible Automation Platform 2.7, verify that your authentication providers are configured and functioning in platform gateway.

### About this task

In Ansible Automation Platform 2.7, all third-party authentication provider configuration has moved to platform gateway. Configuration in automation controller has been removed.

This applies to:

- LDAP
- SAML
- RADIUS
- TACACS+
- OAuth providers (GitHub, Google, Azure AD, Generic OIDC)

### Procedure

1. Log in to the platform gateway UI.
2. Navigate to Access Management> (and then)Authentication Methods.
3. Verify that all previously configured authentication providers are present and enabled.
4. Test user login for each configured authentication method.

## Personal Access Token removal in Ansible Automation Platform 2.7

In Ansible Automation Platform 2.7, component-level Personal Access Tokens (PATs) have been removed. Tokens created directly in automation controller, automation hub, or Event-Driven Ansible controller in Ansible Automation Platform 2.6 or earlier no longer work in Ansible Automation Platform 2.7.

All tokens must now be created and managed through platform gateway.

### Token migration timeline

- **Ansible Automation Platform 2.5:** Platform gateway introduced; component-level PATs deprecated.
- **Ansible Automation Platform 2.6:** PAT migration from components to platform gateway supported; component-level PATs still functional.
- **Ansible Automation Platform 2.7:** Component-level PATs removed; only platform gateway tokens supported.

Important:

The Automation Hub API token is intended only for authenticating with the `ansible-galaxy` CLI for collection operations (sync, install, publish). It is not supported for container registry operations such as `podman login` or `podman pull` of Execution Environment images. For execution environment image operations, use your username and password.

## Create new tokens after upgrade

Component-level tokens from automation controller, automation hub, or Event-Driven Ansible are not migrated to platform gateway during upgrade. After upgrading to Ansible Automation Platform 2.7, you must create new tokens through platform gateway.

### Procedure

1. Log in to the platform gateway UI.
2. Navigate to Access Management> (and then)Users> (and then)[your user]> (and then)Tokens.
3. Create new tokens as needed.
4. Update any scripts or integrations to use the new platform gateway tokens.

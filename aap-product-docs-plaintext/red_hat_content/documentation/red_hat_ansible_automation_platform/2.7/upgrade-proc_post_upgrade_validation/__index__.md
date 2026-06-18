# Validating gateway authentication after the 2.7 upgrade

After upgrading to Red Hat Ansible Automation Platform 2.7, validate that all platform components and integrations are functioning correctly with gateway-based authentication.

## About this task

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

## Procedure

Quick validation commands

1.  Test platform gateway API access:


```
$ curl -H "Authorization: Bearer ${GATEWAY_TOKEN}" \
https://gateway.example.com/api/gateway/v1/ping/
```

2.  Verify direct access is blocked (should return 401):


```
$ curl -H "Authorization: Bearer ${OLD_TOKEN}" \
https://controller.example.com/api/v2/ping/
```

## Results

In Ansible Automation Platform 2.7, authentication at the component level is disabled for external requests. An HTTP 401 Unauthorized response for direct component access is the correct behavior.

## What to do next

If validation steps fail, see the following resources:

- For authentication issues, see [Mandatory platform gateway authentication](/documentation/en-us/red_hat_ansible_automation_platform/2.7/secure-mandatory_platform_gateway_authentication_in_ansible_automation_platform_2_7#con-mandatory-gateway-auth "In Red Hat Ansible Automation Platform 2.7, platform gateway is the only supported method for external authentication to platform components. Direct API access to automation controller, automation hub, and Event-Driven Ansible has been removed.").
- For large uploads failing after upgrade, you may need to adjust gateway upload settings. For more information, see [Configure platform gateway route timeouts](/documentation/en-us/red_hat_ansible_automation_platform/2.7/secure-con_gateway_route_timeouts#con-gateway-route-timeouts "In Ansible Automation Platform 2.7, all API access to platform components goes through platform gateway. Gateway-level timeout settings control how long platform gateway waits for backend services to respond before closing a connection.").
- For operational issues, see the specific component documentation.

# Security settings for OAuth2 tokens and external users
## Implement security controls for external user OAuth2 tokens

After enabling OAuth2 token creation for external users, implement the following compensating controls to keep a strong security posture.

### Procedure

- **Limit token lifetime**: Configure a shorter duration for OAuth2 tokens to reduce the window of exposure. Adjust the OAuth2 access token expiration setting to limit token validity. A value of 28800 seconds (8 hours) is recommended, limiting token validity to a standard workday.

* For manual `settings.py` configuration, see [Configure access to external applications with tokens](/documentation/en-us/red_hat_ansible_automation_platform/2.7/secure-assembly_gw_token_based_authentication#gw-token-based-authentication "Token-based authentication permits authentication of third-party tools and services with the platform through integrated OAuth 2 token support. Ansible Automation Platform utilizes both OAuth Tokens and Personal Access Tokens (PATs).").
* For RPM or containerized installations, see the `gateway_extra_settings` example in [Platform gateway variables](/documentation/en-us/red_hat_ansible_automation_platform/2.7/../install/ref-gateway-variables.html "Reference information for the inventory file variables used to configure platform gateway.").
* For operator-based installations on OpenShift Container Platform, see [Configure the OAuth access token lifetime on OpenShift Container Platform](/documentation/en-us/red_hat_ansible_automation_platform/2.7/secure-ref_controller_applications_getting_started#proc-gw-configure-oauth-token-lifetime-operator "On an operator-based installation, set the OAuth access token lifetime in the AnsibleAutomationPlatform custom resource so platform gateway applies it across reconciliations.").

- **Enforce strict role-based access control (RBAC)**: Grant users only the minimum necessary permissions.   * Assign users who create tokens to **Teams** with highly restrictive roles. Avoid granting broad permissions that could lead to privilege escalation.

- **Establish a clear offboarding process**: Integrate token revocation into your organizational offboarding procedures. Your HR and IT offboarding processes must include a step for an Ansible Automation Platform administrator to revoke all active tokens for a departing user. Tokens can be manually revoked from the user’s profile under the **Tokens** tab.
- **Audit and monitor**: Regularly review token-related activities for legitimacy in the **Activity Stream**.

# 2. Configuring authentication in the Ansible Automation Platform
## 2.5. Configuring an authentication type
### 2.5.10. Configuring keycloak authentication




You can configure Ansible Automation Platform to integrate Keycloak to manage user authentication.

Note
When using this authenticator some specific setup in your Keycloak instance is required. Refer to the [Python Keycloak reference](https://python-social-auth.readthedocs.io/en/latest/backends/keycloak.html) for more details.



**Procedure**

1. From the navigation panel, selectAccess Management→Authentication Methods.
1. ClickCreate authentication.
1. Enter a **Name** for this authentication configuration.
1. Select **Keycloak** from the **Authentication type** list. The **Authentication details** section automatically updates to show the fields relevant to the selected authentication type.
1. Enter the location where the user’s token can be retrieved in the **Keycloak Access Token URL** field.
1. Optional: Enter the redirect location the user is taken to during the login flow in the **Keycloak Provider URL** field.
1. Enter the Client ID from your Keycloak installation in the **Keycloak OIDC Key** field.
1. Enter the RS256 public key provided by your Keycloak realm in the **Keycloak Public Key** field.
1. Enter the OIDC secret (Client Secret) from your Keycloak installation in the **Keycloak OIDC Secret** field.
1. Optional: Enter any **Additional Authenticator Fields** that this authenticator can take. These fields are not validated and are passed directly back to the authenticator.

Note
Values defined in this field override the dedicated fields provided in the UI. Any values not defined here are not provided to the authenticator.




1. To automatically create organizations, users, and teams upon successful login, select **Create objects** .
1. To enable this authentication method upon creation, select **Enabled** .
1. To remove a user for any groups they were previously added to when they authenticate from this source, select **Remove users** .
1. ClickCreate Authentication Method.


**Next steps**

To control which users are allowed into the Ansible Automation Platform server, and placed into Ansible Automation Platform organizations or teams based on their attributes (such as username and email address) or to what groups they belong, continue to [Mapping](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html-single/access_management_and_authentication/index#gw-mapping) .


**Troubleshooting**

If you receive an `jwt.exceptions.InvalidAudienceError: Audience doesn’t match` error, you must re-enable the audience by doing the following:


1. From the navigation for your Keycloak configuration, selectClient scopes→ _YOUR-CLIENT-ID-dedicated_ →Add mapper→Audience.
1. Pick a name for the mapper.
1. Select the **Client ID** corresponding to your client in `    Included Client Audience` .



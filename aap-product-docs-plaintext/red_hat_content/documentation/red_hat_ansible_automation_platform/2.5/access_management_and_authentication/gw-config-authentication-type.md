# 2. Configuring authentication in the Ansible Automation Platform
## 2.5. Configuring an authentication type




Ansible Automation Platform provides multiple authenticator plugins that you can configure to simplify the login experience for your organization. These are the authenticator plugins that are provided:

-  [Local](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/access_management_and_authentication/index#gw-local-authentication)
-  [LDAP](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/access_management_and_authentication/index#controller-set-up-LDAP)
-  [SAML](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/access_management_and_authentication/index#controller-set-up-SAML)
-  [TACACS+](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/access_management_and_authentication/index#controller-set-up-tacacs)
-  [Radius](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/access_management_and_authentication/index#controller-set-up-radius)
-  [Azure](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/access_management_and_authentication/index#controller-set-up-azure)
-  [Google OAuth](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/access_management_and_authentication/index#proc-controller-google-oauth2-settings)
-  [Generic OIDC](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/access_management_and_authentication/index#controller-set-up-generic-oidc)
-  [Keycloak](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/access_management_and_authentication/index#gw-keycloak-authentication)
-  [GitHub](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/access_management_and_authentication/index#proc-controller-github-settings)
-  [GitHub organization](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/access_management_and_authentication/index#proc-controller-github-organization-settings)
-  [GitHub team](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/access_management_and_authentication/index#proc-controller-github-team-settings)
-  [GitHub enterprise](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/access_management_and_authentication/index#proc-controller-github-enterprise-settings)
-  [GitHub enterprise organization](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/access_management_and_authentication/index#proc-controller-github-enterprise-org-settings)
-  [GitHub enterprise team](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/access_management_and_authentication/index#proc-controller-github-enterprise-team-settings)


Note
The **Controller admin** authentication method is for a specific installation and deployment scenario and should only be used if explicitly instructed to do so. This method provides no beneficial functionality for the normal operation of Ansible Automation Platform.




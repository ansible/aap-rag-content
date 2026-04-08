# 2. Hardening Ansible Automation Platform
## 2.1. Planning considerations
### 2.1.4. User authentication planning




When planning user authentication for Ansible Automation Platform, consider both infrastructure-level and application-level authentication requirements.

There are two types of user accounts to consider in an Ansible Automation Platform environment:

- Infrastructure accounts: user accounts on the RHEL servers that run the Ansible Automation Platform services.
- Application accounts: user accounts for the Ansible Automation Platform web UI and API.


#### 2.1.4.1. Infrastructure server account planning




For user accounts on the RHEL servers that run Ansible Automation Platform services, follow your organizational policies to determine if individual user accounts should be local or should use an external authentication source.

Only users who have a valid need to perform maintenance tasks on the Ansible Automation Platform components themselves should have access to the underlying RHEL servers, as the servers store configuration files that contain sensitive information, such as encryption keys and service passwords. Because these individuals must have privileged access to support Ansible Automation Platform services, minimizing access to the underlying RHEL servers is critical. Do not grant sudo access to the root account or local Ansible Automation Platform service accounts (awx, pulp, postgres) to untrusted users.

Note
Some local service accounts are created and managed by the RPM-based installation program. These particular accounts on the underlying RHEL hosts cannot come from an external authentication source.



#### 2.1.4.2. Ansible Automation Platform account planning




Ansible Automation Platform user accounts for accessing the user interface or API can either be local (stored in the Ansible Automation Platform database) or mapped to an external authentication source, such as a _Lightweight Directory Access Protocol_ (LDAP) server.

Where possible, map all primary user accounts to an external authentication source. Using external account sources eliminates a source of error when working with permissions in this context and minimizes the amount of time devoted to maintaining a full set of users exclusively within Ansible Automation Platform. This includes accounts assigned to individual persons and for non-person entities, such as service accounts used for external application integration. Reserve any local accounts, such as the default “admin” account, for emergency access or “break glass” scenarios where the external authentication mechanism isn’t available.

The following external authentication mechanisms are supported in Ansible Automation Platform 2.5:

- LDAP
- SAML
- TACACS+
- Radius
- Azure Active Directory
- Google OAuth
- Generic OIDC
- Keycloak
- GitHub
- GitHub Organization
- GitHub team
- GitHub enterprise
- GitHub enterprise organization
- GitHub enterprise team


Choose an authentication mechanism that adheres to your organization’s policies, and refer to [Access management and authentication](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/access_management_and_authentication) to understand the prerequisites for the relevant authentication mechanism. The authentication mechanism used must ensure that the authentication-related traffic between Ansible Automation Platform and the authentication back-end is encrypted when the traffic occurs on a public or insecure network (for example, LDAPS or LDAP over TLS, HTTPS for OAuth2 and SAML providers, and so on.).

In the Ansible Automation Platform UI, any account with “system administrator” privileges can edit, change, and update any inventory or automation resource. Restrict these account privileges to the minimum set of users necessary for Ansible Automation Platform administration and maintenance.


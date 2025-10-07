# Chapter 3. Configuring access to external applications with token-based authentication




Token-based authentication permits authentication of third-party tools and services with the platform through integrated OAuth 2 token support. Ansible Automation Platform utilizes both OAuth Tokens and Personal Access Tokens (PATs).

The default expiration for access tokens has been updated from 1000 years to 1 year. This change ensures frequent token rotation for increased credential security.

Note
Access tokens in controller 2.4 and previous versions of the platform gateway were valid for 1000 years. Any existing tokens created prior to the 2.5.20250604 patch release will retain a 1000 year expiration.



You can customize this setting to meet your specific requirements by modifying the expiration time in your `settings.py` file as follows:

```
OAUTH2_PROVIDER__ACCESS_TOKEN_EXPIRE_SECONDS = 31536000
```

For more information about the `settings.py` file and how it can be used to configure aspects of the platform, see [settings.py](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/operating_ansible_automation_platform/aap-advanced-config#settings-py_advanced-config) in Operating Ansible Automation Platform.

For more information about the OAuth2 specification, see [The OAuth 2.0 Authorization Framework](https://datatracker.ietf.org/doc/html/rfc6749) .

For more information about using the `manage` utility to create tokens, see [Token and session management](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/access_management_and_authentication/index#ref-controller-token-session-management) .


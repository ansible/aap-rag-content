# 10. Authenticating in the API
## 10.4. Single sign-on authentication




Single sign-on (SSO) authentication methods are different from other methods because the authentication of the user happens external to automation controller, such as Google SSO, Microsoft Azure SSO, SAML, or GitHub. For example, with GitHub SSO, GitHub is the single source of truth, which verifies your identity based on the username and password you gave automation controller.

You can configure SSO authentication by using automation controller inside a large organization with a central Identity Provider. Once you have configured an SSO method in automation controller, an option for that SSO is available on the login screen. If you click that option, it redirects you to the Identity Provider, in this case GitHub, where you present your credentials. If the Identity Provider verifies you successfully, automation controller makes a user linked to your GitHub user (if this is your first time logging in with this SSO method), and logs you in.

**Additional resources**

For the various types of supported SSO authentication methods, see [Configuring an authentication type](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/access_management_and_authentication/gw-configure-authentication#gw-config-authentication-type) .



<span id="idm140642558709712"></span>

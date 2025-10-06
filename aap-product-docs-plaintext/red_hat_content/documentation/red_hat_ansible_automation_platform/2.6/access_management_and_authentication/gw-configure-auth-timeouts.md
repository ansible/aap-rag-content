# 2. Configuring authentication in the Ansible Automation Platform
## 2.5. Configuring an authentication type
### 2.5.2. Configure authenticator timeouts




Ansible Automation Platform uses a system of layered timeouts for password-based authenticators such as LDAP, RADIUS, and TACACS+. To prevent authentication requests from failing, configure each timeout setting in relation to the others. The principle is that each upstream timeout should be slightly longer than the sum of its downstream timeouts.

The system processes authentication requests through a chain of services, each with its own timeout setting:

-  **Envoy timeout** : The total time a request can take before the initial entry point (Envoy) terminates the connection. This is the highest-level timeout.
-  **gRPC timeout** : A downstream timeout that bounds the time spent communicating with the internal authentication service.
-  **Authenticator timeout** : The lowest-level timeout, which defines how long an individual authenticator (LDAP, RADIUS, TACACS+) waits for a response from its third-party server.


#### 2.5.2.1. Setting timeout values




Red Hat recommends that you configure your timeout values based on the performance needs of your authentication servers. While the installation program provides a way to set timeouts for the Ansible Automation Platform components, a system administrator must still review and adjust the individual authenticator timeouts to align with their specific environment.

**Procedure**

- Configure authenticator timeouts: Adjust the timeout setting for each authenticator to a value that aligns with the expected response time of your external server.


- For LDAP, set the `        OPT_NETWORK_TIMEOUT` in seconds. For example, `        OPT_NETWORK_TIMEOUT` : 30 sets an LDAP timeout of 30 seconds. For more information, see [Configuring LDAP authentication](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/access_management_and_authentication/gw-configure-authentication#controller-set-up-LDAP) .
- For TACACS+ authentication, if you want to change the timeout you have to do it through the platform gateway API.
- For RADIUS authentication, the timeout is not changeable and is set to 5 seconds.




# Configuration notes for all authentication types
## Set timeout values

Adjust your individual authenticator timeout values to align with the specific performance needs of your authentication servers. Fine-tuning these settings helps ensure stable and reliable authentication for your Ansible Automation Platform environment.

### Procedure

Configure authenticator timeouts: Adjust the timeout setting for each authenticator to a value that aligns with the expected response time of your external server.

- For LDAP, set the `OPT_NETWORK_TIMEOUT` in seconds. For example, `OPT_NETWORK_TIMEOUT`: 30 sets an LDAP timeout of 30 seconds. For more information, see [Configuring LDAP authentication](/documentation/en-us/red_hat_ansible_automation_platform/2.7/secure-proc_controller_set_up_ldap#controller-set-up-LDAP "As a platform administrator, you can configure LDAP as the source for account authentication information for Ansible Automation Platform users.").
- For TACACS+ authentication, if you want to change the timeout you have to do it through the platform gateway API.
- For RADIUS authentication, the timeout is not changeable and is set to 5 seconds.

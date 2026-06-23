# Configure the Ansible plug-ins
## Configure Ansible Automation Platform details

Connect Red Hat Developer Hub to your automation controller by configuring the Ansible Automation Platform details. This configuration uses a Personal Access Token (PAT) to authenticate the plug-ins, which allows them to interact with your automation environment.

### About this task

Note:

The Ansible plug-ins continue to function regardless of the Ansible Automation Platform subscription status.

### Procedure

1.  Create a Personal Access Token (PAT) with "read and write” scope in automation controller, following the [Applications](/documentation/en-us/red_hat_ansible_automation_platform/2.7/secure-assembly_gw_token_based_authentication#gw-token-based-authentication "Token-based authentication permits authentication of third-party tools and services with the platform through integrated OAuth 2 token support. Ansible Automation Platform utilizes both OAuth Tokens and Personal Access Tokens (PATs).") section of *Access management and authentication*.
2.  Edit your custom Red Hat Developer Hub config map, for example `app-config-rhdh`.
3.  Add your Ansible Automation Platform details to `app-config-rhdh.yaml`.   1.  Set the `baseURL` key with your automation controller URL.
2.  Set the `token` key with the generated token value that you created in Step 1.
3.  Set the `checkSSL` key to `true` or `false`. If `checkSSL` is set to `true`, the Ansible plug-ins verify whether the SSL certificate is valid.

```
data:
app-config-rhdh.yaml: |
...
ansible:
...
rhaap:
baseUrl: '<https://MyControllerUrl>'
token: '<AAP Personal Access Token>'
checkSSL: true
```
Note:
You are responsible for protecting your Red Hat Developer Hub installation from external and unauthorized access. Manage the backend authentication key like any other secret. Meet strong password requirements, do not expose it in any configuration files, and only inject it into configuration files as an environment variable.


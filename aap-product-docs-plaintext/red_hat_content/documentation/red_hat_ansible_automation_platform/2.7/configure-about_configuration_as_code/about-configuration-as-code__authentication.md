# Configuration as Code with the ansible.platform collection
## Authentication methods

You can authenticate to Ansible Automation Platform by using one of the following module parameters:

- **Username and password**: Set the `aap_username` and `aap_password` module parameters.
- **OAuth2 token**: Set the `aap_token` module parameter with a token string or a token object returned by the `ansible.platform.token` module.


All authentication module parameters accept both `aap_` and `gateway_` prefixed names for backward compatibility.

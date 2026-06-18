# Configure the HashiCorp Vault server

You must perform a one-time configuration of the Vault server to enable OIDC authentication with Ansible Automation Platform. This configuration allows OIDC-enabled credential plugins to use JWT-based workload identity to request secure, short-lived tokens instead of relying on static passwords.

## Procedure

1.  Identify your OIDC discovery URL.
This is the base URL of your Ansible Automation Platform instance followed by `/o`
For example, `https://aap.example.com/o`

2.  Enable the JWT authentication method on your Vault server: `vault auth enable jwt`
3.  Configure the Vault JWT authentication backend to point to your Ansible Automation Platform discovery URL by running one of the following commands:
- If your Ansible Automation Platform server uses a certificate signed by a CA that your Vault server trusts, run the following command:


```
vault write auth/jwt/config
oidc_discovery_url=https://aap.example.com/o
```

- If your Ansible Automation Platform server uses a certificate signed by a custom CA that your Vault server doesn’t already trust, you must add the CA Certificate when performing discovery:


```
vault write auth/jwt/config
oidc_discovery_url=<https://aap.example.com/o> oidc_discovery_ca_pem=@aap-ca.pem
```

4.  Create a JWT role in your HashiCorp Vault server that binds your Ansible Automation Platform issued JWTs to vault policies. The role name specified here will be referenced later when configuring a credential. `bound_audiences` must match the URL of the Vault server. `policies` must reference a valid HashiCorp Vault policy.


```
vault write auth/jwt/role/aap-example-role \
role_type=jwt \
bound_audiences=”<https://vault.example.com:8200>” \
user_claim=sub \
policies=aap-example-policy
```

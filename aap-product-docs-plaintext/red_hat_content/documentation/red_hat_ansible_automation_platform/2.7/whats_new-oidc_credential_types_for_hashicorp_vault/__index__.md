# OIDC credential types for HashiCorp Vault

Ansible Automation Platform supports OIDC credential types for HashiCorp Vault that use short-lived JSON Web Tokens instead of static credentials, providing secure, automatic authentication without the need to store or rotate Vault secrets.

You can configure credentials using one of the following OIDC credential types:

-      **HashiCorp Vault Secret Lookup (OIDC):**Fetches arbitrary Key/Value (KV) secrets from HashiCorp Vault that are needed for Ansible automation, such as passwords, private keys, and API keys.

-      **HashiCorp Vault Signed SSH (OIDC):**HashiCorp Vault digitally signs a certificate that Ansible Automation Platform uses to authenticate to a remote host and run automation.

Instead of relying on long-lived credentials that must be stored, rotated, and protected, OIDC credential types use short-lived JSON Web Tokens (JWTs) that are issued per job and expire automatically. This reduces the risk of credential exposure and removes the operational burden of manual credential rotation.

## **JWT expiration and timeout behavior**

When issuing JWTs for OIDC credentials, Ansible Automation Platform uses the job's configured timeout to determine the token's expiration time, aligning it with the expected duration of the job. If the job has no configured timeout, a platform default of 5 minutes (plus 1 minute for clock skew) is used.

This time is intentionally short but generally sufficient because the JWT is only used by the control plane to access HashiCorp Vault and retrieve secrets before automation begins executing. This value is configurable and can be adjusted if jobs fail due to an expired JWT or if a shorter time is needed.

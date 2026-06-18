# OIDC authentication for HashiCorp Vault

Ansible Automation Platform supports zero trust access to HashiCorp Vault using OpenID Connect (OIDC)-based workload identity, eliminating the need to store Vault credentials in Ansible Automation Platform.

For each automation job configured with a Vault OIDC credential, Ansible Automation Platform issues a JSON Web Token (JWT) to authenticate the workload with HashiCorp Vault. Vault then validates this token via OIDC and applies your configured policies to either allow or deny access to the requested secrets.

JWTs are issued with an expiration time that matches the job timeout when available. When the timeout is not available, a configurable platform default is used.

To configure OIDC for your environment, follow this workflow:

1. Configure the HashiCorp Vault server to allow OIDC/JWT Authentication.
2. Configure credentials in Ansible Automation Platform to use either of these credential types: HashiCorp Vault Secret Lookup (OIDC) or HashiCorp Vault Signed SSH (OIDC).

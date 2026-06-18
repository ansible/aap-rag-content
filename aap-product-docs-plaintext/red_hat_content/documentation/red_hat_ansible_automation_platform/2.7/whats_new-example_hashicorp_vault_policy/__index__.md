# Example HashiCorp Vault Policy

HashiCorp Vault policies secure sensitive data by granting path-based access. When creating the JWT Role for Ansible Automation Platform JWT authentication, the role must reference a valid policy to maintain administrator security control.

## Static Vault Policies (Simple)

The script below shows a simple configuration (Vault policies and JWT Roles) that enables automation in two different AAP organizations (**Development, Production**) to access appropriate paths in Vault:

```
# Create a Vault policy 'aap-development-policy' allowing read access
# to dev secrets. Vault is default-deny so no explicit deny block is needed
vault policy write aap-development-policy - <<EOF
path "secret/data/development/*" {
capabilities = ["read"]
}
EOF

# Create a Vault policy 'aap-production-policy' allowing read access
# to prod secrets. Vault is default-deny so no explicit deny block is needed vault policy write aap-production-policy - <<EOF
path "secret/data/production/*" {
capabilities = ["read"]
}
EOF

# Create a JWT Role 'aap-development-role' using the 'aap-development-policy'
# Set a bound_claims mapping to limit this role only to jobs run in the
# 'Development' organization.
vault write auth/jwt/role/aap-development-role - <<EOF
{
"role_type": "jwt",
"bound_audiences": ["https://vault.example.com:8200"],
"user_claim": "sub",
"bound_claims": {
"aap_controller_organization_name": ["Development"]
},
"policies": ["aap-development-policy"]
}
EOF

# Create a JWT Role 'aap-production-role' using the 'aap-production-policy'
# Set a bound_claims mapping to limit this role only to jobs run in the
# 'Production' organization.

vault write auth/jwt/role/aap-production-role - <<EOF
{
"role_type": "jwt",
"bound_audiences": ["https://vault.example.com:8200"],
"user_claim": "sub",
"bound_claims": {
"aap_controller_organization_name": ["Production"]
},
"policies": ["aap-production-policy"]
}
EOF
```
When configuring Credentials, use the `aap-development-role` in the `Development` organization and the `aap-production-role` in the `Production` organization. The JWT Role configured in Vault enforces that Jobs can only use the role and access the policy-controlled secrets if their organization claim matches. Jobs in the `Development` organization will be able to access secrets under `secret/data/development/*` but not `secret/data/production/*`. Even if a credential is configured with the `aap-production-role`, the platform authoritatively populates the `aap_controller_organization_name` at launch time, and Vault will only allow the role to be used if the organization is `Production`.

Mapping JWT roles to simple Vault policies is a great way to integrate with existing Vault deployments. This simple approach provides secure, granular control, regardless of how the data is structured in Vault.

## Templated Vault Policies (Advanced)

For a more integrated approach, you can write templated Vault policies that depend on metadata extracted from JWT. By aligning Vault secret paths with the structured configuration in Ansible Automation Platform, policies can leverage authoritative details of the automation from AAP (including Organization, Job Template, User, Playbook, Launch Type, Instance Group, etc). This allows for much richer policies that enable scalability with security.

The example script below provides a more dynamic configuration (single, templated Vault policy and single JWT Role) that uses both the Organization Name and the Job Template Name from Ansible Automation Platform to determine the path to allow:

```
# Read the accessor for the JWT auth method, this will be needed to write
# template policies that reference JWT claims via this auth method
JWT_ACCESSOR=$(vault auth list --format json | jq -r '."jwt/".accessor')

# Write a policy that references org and job_template variables from JWT.
# JWT_ACCESSOR is an environment variable interpolated when the script runs,
# but {{identity...org}} is a Vault template variable that is interpolated when
# the policy is applied
vault policy write aap-template-policy - <<EOF
path "secret/data/aap/{{identity.entity.aliases.${JWT_ACCESSOR}.metadata.org}}/{{identity.entity.aliases.${JWT_ACCESSOR}.metadata.job_template}}/*" {
capabilities = ["read"]
}
EOF

# Write a single JWT Role 'aap-dynamic-role' using the 'aap-template-policy'
# Allows three named organizations via bound_claims and defines the mapping of
# specific JWT claims to metadata variables via claim_mappings
vault write auth/jwt/role/aap-dynamic-role - <<EOF
{
"role_type": "jwt",
"bound_audiences": ["https://vault.example.com:8200"],
"user_claim": "sub",
"bound_claims": {
"aap_controller_organization_name": "Development", "Production", "Staging"]
},
"claim_mappings": {
"aap_controller_organization_name": "org",
"aap_controller_job_template_name": "job_template"
},
"policies": ["aap-template-policy"]
}
EOF
```
When configuring credentials, use the `aap-dynamic-role` in all organizations. The `bound_claims` limits authentication to these allowed organizations. The `claim_mappings` define JWT claims to be available for policy templating (`org` and `job_template`).

For example, only a job executing in the `Production` organization from the `configure_firewall` job template can read Vault secrets beneath `aap/Production/configure_firewall/*`.

Whether using simple role/policy mapping or template policies, the claims issued by Ansible Automation Platform provide a rich catalog of workload identifiers that can be used to simply and securely limit access to specifically what’s required for automation.

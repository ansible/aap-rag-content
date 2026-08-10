+++
title = "Authenticate the Windows user - Red Hat Ansible Automation Platform 2.7"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/secure-authenticate_the_windows_user"
template = "docs/aem-title.html"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/secure-authenticate_the_windows_user/", "Authenticate the Windows user"]]
category = "Secure"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/secure-authenticate_the_windows_user/aem-page/secure-authenticate_the_windows_user.html"
last_crumb = "Authenticate the Windows user"
modified = "2026-07-30T17:12:56.473Z"
multi_page_path = ""
name = "Authenticate the Windows user"
oversized = "false"
page_slug = "secure-authenticate_the_windows_user"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/secure-authenticate_the_windows_user"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/secure-authenticate_the_windows_user/toc/toc.json"
type = "aem-page"
+++

# Authenticate the Windows user

You must decide whether the connecting automation user is a domain or a local user and an administrator user account or not.

There are four main questions:

1. Which user to use to connect.
2. If, or where, credential delegation is required.
3. Is using SSH acceptable given the support-related limitations?
4. When using WinRM, is a central certificate management already established and used in the organization?

**Domain or Local User**

Ensure reliable automation access by configuring appropriate local or domain users. Prevent connection failures by verifying domain user accessibility, and streamline cross-domain management by using a consistent user account.

**Administrator or Less Privileged User**

To establish initial connectivity and validate critical playbooks, configure your setup using an administrator account if permitted by your security policies. Since features like default NTLM access are strictly restricted to the true Administrator user, first verifying your automation with full privileges ensures reliable baseline functionality before you transition to a less privileged account.

## WinRM authentication methods

Evaluate and configure the optimal WinRM authentication method for your Ansible-managed Windows environments by comparing security trade-offs, credential delegation capabilities, and domain integration requirements.

**WinRM authentication methods**

| **Option**      | **Local accounts** | **Active directory accounts**                                       | **Credential delegation** | **HTTP encryption** |
| --------------- | ------------------ | ------------------------------------------------------------------- | ------------------------- | ------------------- |
| **Basic**       | Yes                | No                                                                  | No                        | No                  |
| **Certificate** | Yes                | No                                                                  | No                        | No                  |
| **Kerberos**    | No                 | Yes                                                                 | Yes                       | Yes                 |
| **NTLM**        | Yes                | Yes (NTLM with AD works but only for Administrator user by default) | No                        | Yes                 |
| **CredSSP**     | Yes                | Yes                                                                 | Yes                       | Yes                 |

Ensure that you have the required Python modules installed on the control node or execution environment for the authentication method in use, such as `pywinrm`, `pypsrp`, `pykerberos`, `requests-credssp`, and/or `requests-ntlm`. These are all included in recent supported execution environments.

If legacy WinRM transport or alternative authentication methods must be retained due to compliance constraints, consult this architectural decision matrix:

```
Authentication Selection Path]
   |
   +-> Domain Joined?
   |     |
   |     +--> Yes: Use Kerberos (High Security, Native Delegation)
   |     +--> No:  Workgroup Environment?
   |              |
   |              +--> Certificates (X.509) -> Secure Local Auth (No passwords over wire)
   |              +--> NTLM (Message Encryption) -> Fallback, FIPS-Incompatible
   |              +--> CredSSP -> Avoid unless multi-hop required without AD
```

**HTTPS and WinRM Certificates**

One way to manage certificates in AD domains is Active Directory Certificate Services (AD CS). It makes configuring WinRM with HTTPS and proper certificates feasible. However, if the customer is not using AD CS, if their DNS setup is not optimal, if they have many non-domain systems, or they do not want additional certificate management, then that might prevent using WinRM HTTPS with proper certificates.

**Basic-over-HTTP**

Basic authentication should be avoided in all environments. For non-domain joined systems, NTLM with message encryption is the preferred baseline. For production and domain-joined systems, Kerberos or PSRP with Kerberos authentication should be the standard to ensure secure credential delegation and mutual authentication.

**Basic-over-HTTPS and Self-Signed Certificate**

Basic-over-HTTPS using a self-signed certificate is an improvement over Basic-over-HTTP for non-production setups without the need for a fully thought-out authentication scheme with WinRM. While not acceptable for production, this can be considered for early testing as it allows for encrypted authentication and communications.

**Basic-over-HTTPS and Signed Certificates**

This requires a certificate management solution to be in place. In this case it might be better to use X.509 certificates, instead of username+password, for Ansible, but with certificate CA chain validation enabled after making the issuer certificate of the CA known to Ansible on the control node or execution environment.

`ansible_winrm_server_cert_validation: validate`

`ansible_winrm_ca_trust_path: /path/to/certificate/public/ca.pem`

**Certificate authentication (X.509)**

Certificate-based authentication maps X.509 certificates to local users, mimicking SSH key behaviors.

- **Architectural Trade-offs**: Keys cannot map to Active Directory domain accounts. Private keys used by Ansible must be unencrypted and stored securely on the control node as local files. If the underlying Windows local account password changes, an administrator must rebuild the cryptographic mapping manually.
- **Inventory Variable Syntax**

```
ansible_winrm_transport=certificate
ansible_winrm_cert_validation=validate
ansible_winrm_ca_trust_path=/path/to/ca_cert.pem
ansible_winrm_cert_key_pem=/path/to/client.key
ansible_winrm_cert_pem=/path/to/client.pem
```

**NTLM authentication**

By default NTLM only allows the Administrator user, not users in the Administrators group, to connect (at least in non-domain environments). Also note that NTLM is not compatible with FIPS so with FIPS Kerberos is likely the best option.

```
ansible_winrm_transport: ntlm
ansible_winrm_message_encryption: always
```

**CredSSP authentication**

CredSSP is a more modern authentication method with support for domain and local users, credential delegation, and authentication and session traffic encryption over HTTP. It uses NTLM or Kerberos for initial authentication underneath. However, a recent Microsoft post states that enabling CredSSP is a degraded security posture.

If CredSSP is needed, even considering the warning above, enable CredSSP authentication on the WinRM server side with the following command or with the WinRM role:

Powershell: (on the Windows host)

 `Set-Item -Path WSMan:\localhost\Service\Auth\CredSSP -Value $true`

Ansible inventory/host variables

```
ansible_winrm_transport: credssp
ansible_winrm_message_encryption: always
```

CredSSP might be considered in some special cases, especially when credential delegation is crucial, but in most cases it is not recommended. In FIPS mode NTLM is not possible to use for the initial CredSSP authentication.

- **Security Risk**: CredSSP enables remote credential delegation for multi-hop operations outside Active Directory. However, Microsoft identifies enabling CredSSP as a degraded security posture because cleartext-equivalent credentials pass to the target memory space. Use Kerberos delegation instead wherever possible.

**FIPS-Compliant Alternatives**

If Certificate authentication proves unsuitable for your FIPS-compliant environment, consider these more stable alternatives in order of preference:

- **Kerberos Authentication**: The standard for domain-joined systems; highly recommended over certificates.
- **SSH Connection**: Using OpenSSH for Windows avoids WinRM complexities entirely while maintaining high security.

**Authentication decision table**

Select the optimal WinRM authentication method to securely manage your Windows environment. Use this decision table to compare Kerberos, CredSSP, NTLM, Basic, and Certificate schemes based on domain support, credential delegation needs, and security levels

| Win RM Auth scheme | Supports local | Supports domain | Credential delegation | Security level     | Recommended use case                                                                |
| ------------------ | -------------- | --------------- | --------------------- | ------------------ | ----------------------------------------------------------------------------------- |
| **Kerberos**       | No             | Yes             | Yes                   | High               | Default for domain-joined environments. Required for secure "double-hop" scenarios. |
| **CredSSP**        | Yes            | Yes             | Yes                   | Medium (High risk) | When delegation is needed but Kerberos is not an option. Use with extreme caution.  |
| **NTLM**           | Yes            | Yes             | No                    | Medium             | Fallback for domain or workgroup environments where delegation is not required.     |
| **Basic**          | Yes            | No              | No                    | Low                | Insecure. For initial lab setup or testing over HTTPS only. Avoid in production.    |
| **Certificate**    | Yes            | No              | No                    | High               | Secure option for non-domain hosts, but requires complex certificate management.    |

## Protect Windows credentials in automated workflows

When executing automated workflows at runtime, retrieving secrets from a centralized vault safeguards sensitive credentials and enforces corporate compliance.

```
[Ansible Automation Platform]
      |
      +---(Runtime Lookup Request)---> [ CyberArk / HashiCorp Vault ]
      |                                       |
      |                                (Retrieves Secret)
      |                                       v
      +<--(Injects transient variable)--------+
      |
[Target Windows Host]
```

- **CyberArk and HashiCorp Vault**: Automation controller uses native credential lookups to fetch `ansible_password` values from centralized vaults at runtime. Credentials exist only as transient variables in memory during task execution.
- **Azure Key Vault**: For workloads hosted in public cloud infrastructure, use the azure.azcollection to pull administrative passwords dynamically from cloud key management stores.

## Validate Windows security baselines and verify readiness

Validate operational parameters and run remote privilege audits during Windows instance provisioning or migration to verify correct configuration and baseline security posture.

**Baseline configuration enforcement**

Ensure target nodes do not drift from their desired cryptographic state by applying a structured configuration role. The following example outlines properties managed by the `winrm_configuration` structural role:

```
# Compliance State Variables
winrm_configuration_enable: true
winrm_configuration_start_mode: auto
winrm_configuration_http_block: true # Enforce absolute port security isolation

winrm_configuration_service_config:
  AllowUnencrypted: false
  Auth:
    Basic: false
    Kerberos: true
    Negotiate: true
    Certificate: false
    CredSSP: false
    CbtHardeningLevel: Relaxed
  IPv4Filter: '*'
  IPv6Filter: '*'

winrm_configuration_firewall_profiles:
  - domain
  - private
```

**Validate production connectivity**

Run this playbook against newly provisioned or migrated nodes to confirm PSRP operational compliance, collect environment facts, and verify local security group privileges.

```
---
- name: Validate Enterprise Windows Infrastructure Connectivity
  hosts: windows
  become: false
  gather_facts: false

  vars:
    target_admin_group: Administrators

    # Standardized Enterprise PSRP Variable Set
    ansible_connection: psrp
    ansible_pipelining: true
    ansible_psrp_port: 5986
    ansible_psrp_protocol: https
    ansible_psrp_auth: kerberos
    ansible_psrp_kerberos_delegation: true
    ansible_psrp_cert_validation: validate
    ansible_psrp_ca_cert:
   /etc/pki/ca-trust/source/anchors/internal_corporate_ca.pem
    ansible_user: <Domain_User>
    ansible_password: <Password_or_Vault_Variable>

  tasks:
    - name: Verify Transport Connectivity
      ansible.windows.win_ping:

    - name: Extract Target Endpoint Infrastructure Facts
      ansible.windows.setup:

    - name: Audit Administrative Group Access Matrix
      ansible.windows.win_powershell:
        script: |
          $AnsibleResponse = @{
              HostName = $env:COMPUTERNAME
              AdministrativeMembers = @()
          }
          $Members = Get-LocalGroupMember -Group "{{ target_admin_group }}" -ErrorAction Stop
          foreach ($Member in $Members) {
              $AnsibleResponse.AdministrativeMembers += $Member.Name
          }
          $AnsibleResponse
      register: acl_audit_result

    - name: Output Security Posture Summary
      ansible.builtin.debug:
        var: acl_audit_result.output
```

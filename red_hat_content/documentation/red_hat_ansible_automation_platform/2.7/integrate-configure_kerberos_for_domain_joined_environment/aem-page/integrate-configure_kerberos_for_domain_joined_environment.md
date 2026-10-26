+++
template = "docs/aem-title.html"
title = "Configure Kerberos for domain-joined environment - Red Hat Ansible Automation Platform 2.7"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/integrate-configure_kerberos_for_domain_joined_environment"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/integrate-automate_microsoft_windows_with_ansible_automation_platform/", "Integrate with Microsoft Windows"]]
category = "Integrate"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/integrate-configure_kerberos_for_domain_joined_environment/aem-page/integrate-configure_kerberos_for_domain_joined_environment.html"
last_crumb = "Configure Kerberos for domain-joined environment"
latest = "true"
modified = "2026-10-06T15:21:13.207Z"
multi_page_path = ""
name = "Configure Kerberos for domain-joined environment"
oversized = "false"
page_slug = "integrate-configure_kerberos_for_domain_joined_environment"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/integrate-configure_kerberos_for_domain_joined_environment"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/integrate-configure_kerberos_for_domain_joined_environment/toc/toc.json"
type = "aem-page"
+++

# Configure Kerberos for domain-joined environment

Configure Kerberos authentication in Ansible Automation Platform using a custom credential type to securely authenticate domain-joined Windows targets, resolve double-hop dilemmas, and effectively troubleshoot handshake failures.

Kerberos provides encrypted, mutual authentication across domain-joined environments and solves the "double-hop" dilemma, allowing an automation runspace to connect to secondary remote shares or SQL assets.

**Setup**

Using Kerberos requires configuration on both the Ansible execution node and the Windows target. The execution node (or more accurately, the Ansible Automation Platform execution environment running on the execution node) must have the Kerberos client libraries, for example, krb5-workstation, installed and a correctly configured `/etc/krb5.conf`file that defines the Active Directory realm and the location of the *Key Distribution Center* (KDC).The one notable configuration task with Kerberos is to provide the required krb5 configuration file(s) for each domain. This is easier by creating a custom credential type which avoids the need to create and maintain custom execution environments or configure file mappings on execution nodes.

**Create a custom Kerberos credential type**

To avoid building custom execution environments or hardcoding static `/etc/krb5.conf` volumes across automation nodes, configure a Custom Credential Type within the automation controller interface.

**Input configuration**

```
fields:
  - id: username
    type: string
    label: Domain Username
  - id: password
    type: string
    label: Domain Password
    secret: true
  - id: default_realm
    type: string
    label: Active Directory Realm (UPPERCASE)
  - id: kdc
    type: string
    label: Key Distribution Center (KDC Host/IP)
    help_text: Optional. Populate only if environment lacks working KDC DNS SRV lookups.
required:
  - username
  - password
  - default_realm
```

**Injector configuration**

```
env:
  KRB5_CONFIG: '{{ tower.filename }}'
file:
  template: |-
    [libdefaults]
    default_realm = {{ default_realm | upper }}
    dns_canonicalize_hostname = fallback
    dns_lookup_kdc = {% if kdc %}false{% else %}true{% endif %}
    dns_lookup_realm = true
    forwardable = true
    rdns = false

    [realms]
    {{ default_realm | upper }} = {
        {% if kdc %}kdc = {{ kdc }}{% endif %}
    }

    [domain_realm]
    {{ default_realm | lower }} = {{ default_realm | upper }}
extra_vars:
  ansible_user: '{{ username }}'
  ansible_password: '{{ password }}
```

**Configure Kerberos environment variable forwarding**

When executing Kerberos lifecycle operations, ensure the engine forwards the generated configurations down to underlying sub-processes by enforcing expected tracking:

```
# Set encryption and authentication
ansible_psrp_auth: kerberos
ansible_psrp_message_encryption: always
# Forward Kerberos environment variables to the connection plugin:
ansible_psrp_env:
  - KRB5_CONFIG
  - KRB5_TRACE
```

To diagnose Kerberos handshake failures through the Ansible Automation Platform interface, capture verbose transaction traces by wrapping tasks in a block or rescue sequence that prints the file target assigned to `KRB5_TRACE`.

**Kerberos inventory variables**

When using Kerberos, the username must be in the `user@EXAMPLE.COM` format. The `ansible_winrm_kinit_env_vars` variable is used to pass the specified environment variables through pexpect to kinit and thus must be used with the custom credential type.

```
ansible_winrm_transport: kerberos
ansible_winrm_message_encryption: always
ansible_winrm_kerberos_delegation: false  # change to true where needed
ansible_winrm_kinit_env_vars:
  - KRB5_CONFIG
  - KRB5_TRACE
```

Since Kerberos with WinRM encrypts session traffic HTTPS is not required for encryption.

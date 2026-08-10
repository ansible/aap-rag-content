+++
title = "Connect securely to Windows hosts - Red Hat Ansible Automation Platform 2.7"
template = "docs/aem-title.html"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/configure-connect_securely_to_windows_hosts"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/configure-connect_securely_to_windows_hosts/", "Connect securely to Windows hosts"]]
category = "Configure"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/configure-connect_securely_to_windows_hosts/aem-page/configure-connect_securely_to_windows_hosts.html"
last_crumb = "Connect securely to Windows hosts"
modified = "2026-07-30T17:12:56.473Z"
multi_page_path = ""
name = "Connect securely to Windows hosts"
oversized = "false"
page_slug = "configure-connect_securely_to_windows_hosts"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/configure-connect_securely_to_windows_hosts"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/configure-connect_securely_to_windows_hosts/toc/toc.json"
type = "aem-page"
+++

# Connect securely to Windows hosts

Select a connection protocol and configure authentication for your environment.

Selecting a transport protocol directly impacts execution speed, security posture, and network footprint. Ansible Automation Platform supports three connectivity models for Windows.

**Architectural recommendations**

- **Adopt PSRP as the Enterprise Standard**: For general infrastructure configuration, patching, and compliance enforcement, PSRP offers optimal execution velocity, native Active Directory integration, and minimal CPU overhead.
- **Use OpenSSH for Specific Edge Cases**: Deploy OpenSSH only if corporate firewalls strictly limit cross-zone communication to Port 22, if proxy infrastructure requires SSH brokering, or if workloads demand frequent, ultra-large file transfers (e.g., database binaries or ISOs). This requires Windows Server 2022+ and ansible-core 2.18+.
- **Deprecate Legacy WinRM**: Update production inventories from ansible_connection: winrm to `ansible_connection: psrp`. This shift lowers CPU use on managed endpoints and shortens playbook execution windows.

**Protocol comparison**

| Feature                   | Legacy WinRM                                                  | PSRP (recommended)                                                  | OpenSSH for Windows                                                                        |
| ------------------------- | ------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------------------------------ |
| **Connection plugin**     | `winrm`                                                       | `psrp`                                                              | `ssh`                                                                                      |
| **Network port**          | <br>5985 (HTTP)<br>5986 (HTTPS)                               | <br>5985 (HTTP)<br>5986 (HTTPS)                                     | 22 (TCP                                                                                    |
| **Execution mechanism**   | Spawns a new`powershell.exe` process per task. Heavy CPU load | Uses persistent Runspace Pools. Executes tasks on internal threads. | Spawns a basic shell; invokes a new interpreter process per task.                          |
| **Task execution speed**  | Slow                                                          | Fastest (~20-25% faster than WinRM in typical workloads.)           | Moderate                                                                                   |
| **File transfer speed**   | Slow                                                          | Moderate                                                            | Fastest (Native SFTP/SCP                                                                   |
| **Active directory auth** | Excellent (Kerberos)                                          | Excellent (Kerberos)                                                | Excellent (Kerberos via GSSAPI)                                                            |
| **Double-hop delegation** | Supported (CredSSP / Kerberos)                                | Supported (CredSSP / Kerberos)                                      | GSSAPI / Kerberos Delegation or plaintext passwords; unsupported when using SSH Key-Pairs. |
| **Security profiles**     | Basic, NTLM, Kerberos, Certs                                  | Basic, NTLM, Kerberos, Certs                                        | SSH Key-pairs, Password, GSSAPI                                                            |
| **FIPS 140 compliance**   | Complex (Requires Kerberos/HTTPS)                             | Complex (Requires Kerberos/HTTPS)                                   | Native                                                                                     |

## PowerShell Remoting Protocol (PSRP)

Upgrade your production inventories from legacy WinRM to PSRP to eliminate performance bottlenecks. By switching to PSRP and enforcing certificate validation, you get faster, secure remote management using persistent runspaces over your existing network.

**Production PSRP inventory configuration**

```
[windows]
winserver.example.com ansible_host=192.168.1.10

[windows:vars]
ansible_user=AnsibleUser@EXAMPLE.COM
ansible_password={{ vault_win_password }}
ansible_connection=psrp
ansible_psrp_port=5986
ansible_psrp_auth=kerberos
ansible_psrp_kerberos_delegation=true
ansible_psrp_cert_validation=validate
ansible_psrp_ca_cert=/etc/pki/ca-trust/source/anchors/internal_corporate_ca.pem
```

**Security Best Practice**: Never use `ansible_psrp_cert_validation: ignore` in production HTTPS environments. Only bypass validation in isolated lab spaces or when executing over HTTP (Port 5985) with message-level encryption strictly enabled (`ansible_psrp_message_encryption: always`). When Kerberos authentication is combined with message encryption over HTTP, traffic is secured at the protocol layer, making transport-level TLS validation optional.

## OpenSSH for Windows

OpenSSH provides a consistent connection method across Linux and Windows environments.

**Administrative account access permissions**

Windows OpenSSH handles credential lookup based on user privileges.

- **Standard Users**: Lookups occur within the user profile path: `C:\Users\<UserName>\.ssh\authorized_keys`.
- **Administrative Users**: Lookups bypass user directories and check a global configuration file: `C:\ProgramData\ssh\administrators_authorized_key.`.

**Critical Security Warning**: The `administrators_authorized_keys` file must be restricted to explicit *Access Control Lists* (ACLs). Only the local `SYSTEM` and Administrators groups may possess permissions. If permissions are too broad, the OpenSSH service ignores the keys for security compliance.

**Set the Default Shell**

By default, OpenSSH on Windows may drop you into a Command Prompt (cmd.exe). Ansible requires a PowerShell environment. You must set the default shell on the Windows target using the following registry command (run as Admin):

```
New-ItemProperty `
     -Path "HKLM:\SOFTWARE\OpenSSH" `
     -Name "DefaultShell" `
     -Value "C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe" `
     -PropertyType String `
     -Force
```

**OpenSSH inventory configuration**

```
[windows_ssh]
winserver.example.com

[windows_ssh:vars]
ansible_connection=ssh
ansible_shell_type=cmd
ansible_user=Administrator
```

**SSH authentication methods**

| **Option**   | **local accounts** | **Active directory accounts** | **Credential delegation** |
| ------------ | ------------------ | ----------------------------- | ------------------------- |
| **Key**      | Yes                | Yes                           | No                        |
| **GSSAPI**   | No                 | Yes                           | Yes                       |
| **Password** | Yes                | Yes                           | Yes                       |

**Provision OpenSSH on target hosts**

Use the following PowerShell script to automate installation, enable the firewall rules, enforce the correct default shell, and harden administrative access permissions:

```
<#
.SYNOPSIS
    Production-Hardened OpenSSH Provisioning Script for Windows Targets.
    Compatible with Windows Server 2019, 2022, and 2025.
#>
$ErrorActionPreference = "Stop"

# ==============================================================================
# 1. Enforce Administrator Elevation Access Layer
# ==============================================================================
$identity = [Security.Principal.WindowsIdentity]::GetCurrent()
$principal = New-Object Security.Principal.WindowsPrincipal($identity)
if (-not $principal.IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)) {
    Write-Error "Execution Halted: This script must be executed within an Elevated Administrator context."
    Exit 1
}

# ==============================================================================
# 2. Unified Windows Capability Onboarding (Server 2019 - 2025)
# ==============================================================================
Write-Host "Evaluating Component-Based Servicing state for OpenSSH..." -ForegroundColor Cyan
$capability = Get-WindowsCapability -Online -Name "OpenSSH.Server*"

if ($capability.State -ne 'Installed') {
    Write-Host "Target missing capability. Provisioning via Active OS Deployment Engine..." -ForegroundColor Yellow
    Add-WindowsCapability -Online -Name $capability.Name
} else {
    Write-Host "OpenSSH Server capability confirmed active." -ForegroundColor Green
}

# ==============================================================================
# 3. Configure Daemon Service State Machine
# ==============================================================================
Write-Host "Configuring service operational thresholds..." -ForegroundColor Cyan
Set-Service -Name sshd -StartupType 'Automatic'
if ((Get-Service -Name sshd).Status -ne 'Running') {
    Start-Service sshd
}

# ==============================================================================
# 4. Assertive Firewall Enforcement
# ==============================================================================
Write-Host "Validating Security Edge Boundaries..." -ForegroundColor Cyan
$fwRule = Get-NetFirewallRule -Name "OpenSSH-Server-In-TCP" -ErrorAction SilentlyContinue

if (-not $fwRule) {
    Write-Host "Inbound Rule missing. Applying clean Port 22 Profile..." -ForegroundColor Yellow
    New-NetFirewallRule -Name 'OpenSSH-Server-In-TCP' -DisplayName 'OpenSSH Server (sshd)' -Enabled True `
        -Direction Inbound -Protocol TCP -LocalPort 22 -Action Allow
} elseif ($fwRule.Enabled -ne 'True') {
    Write-Host "Inbound Rule exists but is suppressed. Overriding to Enabled status..." -ForegroundColor Yellow
    Set-NetFirewallRule -Name 'OpenSSH-Server-In-TCP' -Enabled True
} else {
    Write-Host "Firewall verification passed." -ForegroundColor Green
}

# ==============================================================================
# 5. Native 64-Bit Registry Overrides (Bypassing WoW64 Translation)
# ==============================================================================
Write-Host "Locking default command interpretation environment..." -ForegroundColor Cyan
$shellPath = "C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe"

$hive = [Microsoft.Win32.RegistryHive]::LocalMachine
$view = [Microsoft.Win32.RegistryView]::Registry64
$baseKey = [Microsoft.Win32.RegistryKey]::OpenBaseKey($hive, $view)

$sshKey = $baseKey.CreateSubKey("SOFTWARE\OpenSSH")
$sshKey.SetValue("DefaultShell", $shellPath, [Microsoft.Win32.RegistryValueKind]::String)

$sshKey.Close()
$baseKey.Close()
Write-Host "Default shell environment set to native 64-bit PowerShell process architecture." -ForegroundColor Green

# ==============================================================================
# 6. Cryptographic ACL Normalization via Well-Known SIDs
# ==============================================================================
Write-Host "Hardening key storage access schemas..." -ForegroundColor Cyan
$adminKeyPath = "$env:ProgramData\ssh\administrators_authorized_keys"

if (-not (Test-Path $adminKeyPath)) {
    # Ensure parent directory is structured if service hasn't initialized disk footprints yet
    $null = New-Item -ItemType File -Path $adminKeyPath -Force
}

# Using Explicit SIDs (*S-1-5-32-544 = Builtin Administrators, *S-1-5-18 = Local System)
# This preserves execution integrity across global internationalized operating systems.
icacls.exe $adminKeyPath /inheritance:r /grant "*S-1-5-32-544:F" /grant "*S-1-5-18:F"

Write-Host "OpenSSH configuration normalized. Target node is fully prepped for Ansible orchestration." -ForegroundColor Green
```

An Ansible role for setting up and enabling sshd on Windows Server 2019+ using Features On Demand (FODs) is available at [Windows Ansible roles](https://github.com/myllynen/windows-ansible-roles)

## Legacy WinRM

When establishing remote communication on Windows Server 2016 or newer, configuring legacy WinRM listeners and firewall rules enables default, SOAP-based connectivity over HTTP/HTTPS.

**Advantages**

- Native to Windows (service enabled by default on Server 2016+).
- Deep integration with Active Directory authentication (Kerberos, NTLM).
- Supports CredSSP for "double-hop" authentication, for example, accessing a network share from the managed node.

**Disadvantages**

- **Performance**: Relies on XML/SOAP overhead. Each Ansible task spins up a new powershell.exe process, which is highly CPU-intensive and slow.
- **Configuration Complexity**: Setting up HTTPS listeners and managing WinRM certificates can be burdensome without existing PKI automation.

Ansible communicates with Windows hosts over the WinRM protocol using one of two connection plugins. While both use the same underlying protocol, they have different implementations and capabilities:

- **ansible.builtin.winrm**: The original WinRM connection plugin. While still fully functional, it is often superseded by PSRP for new deployments. It provides specific timeout controls, such as `ansible_winrm_operation_timeout_sec` and `ansible_winrm_read_timeout_sec`, which can be tuned for long-running tasks.
- **psrp (PowerShell Remoting Protocol)**: For new deployments on Ansible Automation Platform, the psrp connection plugin is the recommended choice over winrm. It offers better performance and handles heavy loads more effectively. Use `ansible_connection: psrp` in your inventory to enable this.

## Configure Kerberos for domain-joined environment

Configure Kerberos authentication in Ansible Automation Platform using a custom credential type to securely authenticate domain-joined Windows targets, resolve double-hop dilemmas, and effectively troubleshoot handshake failures.

Kerberos provides encrypted, mutual authentication across domain-joined environments and solves the "double-hop" dilemma, allowing an automation runspace to connect to secondary remote shares or SQL assets.

**Setup**

Using Kerberos requires configuration on both the Ansible control node and the Windows target. The control node (or more accurately, the Ansible Automation Platform execution environment) must have the Kerberos client libraries, for example, krb5-workstation, installed and a correctly configured `/etc/krb5.conf`file that defines the Active Directory realm and the location of the *Key Distribution Center* (KDC).The one notable configuration task with Kerberos is to provide the required krb5 configuration file(s) for each domain. This is easier by creating a custom credential type which avoids the need to create and maintain custom execution environments or configure file mappings on execution nodes.

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

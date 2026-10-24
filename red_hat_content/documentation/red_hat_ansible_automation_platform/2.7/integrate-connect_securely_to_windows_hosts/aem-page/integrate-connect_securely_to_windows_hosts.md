+++
template = "docs/aem-title.html"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/integrate-connect_securely_to_windows_hosts"
title = "Connect securely to Windows hosts - Red Hat Ansible Automation Platform 2.7"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/integrate-automate_microsoft_windows_with_ansible_automation_platform/", "Integrate with Microsoft Windows"]]
category = "Integrate"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/integrate-connect_securely_to_windows_hosts/aem-page/integrate-connect_securely_to_windows_hosts.html"
last_crumb = "Connect securely to Windows hosts"
latest = "true"
modified = "2026-10-06T15:21:13.207Z"
multi_page_path = ""
name = "Connect securely to Windows hosts"
oversized = "false"
page_slug = "integrate-connect_securely_to_windows_hosts"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/integrate-connect_securely_to_windows_hosts"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/integrate-connect_securely_to_windows_hosts/toc/toc.json"
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
| **Network port**          | 5985 (HTTP)<br>5986 (HTTPS)                                   | 5985 (HTTP)<br>5986 (HTTPS)                                         | 22 (TCP                                                                                    |
| **Execution mechanism**   | Spawns a new`powershell.exe` process per task. Heavy CPU load | Uses persistent Runspace Pools. Executes tasks on internal threads. | Spawns a basic shell; invokes a new interpreter process per task.                          |
| **Task execution speed**  | Slow                                                          | Fastest (~20-25% faster than WinRM in typical workloads.)           | Moderate                                                                                   |
| **File transfer speed**   | Slow                                                          | Moderate                                                            | Fastest (Native SFTP/SCP                                                                   |
| **Active directory auth** | Excellent (Kerberos)                                          | Excellent (Kerberos)                                                | Excellent (Kerberos via GSSAPI)                                                            |
| **Double-hop delegation** | Supported (CredSSP / Kerberos)                                | Supported (CredSSP / Kerberos)                                      | GSSAPI / Kerberos Delegation or plaintext passwords; unsupported when using SSH Key-Pairs. |
| **Security profiles**     | Basic, NTLM, Kerberos, Certs                                  | Basic, NTLM, Kerberos, Certs                                        | SSH Key-pairs, Password, GSSAPI                                                            |
| **FIPS 140 compliance**   | Complex (Requires Kerberos/HTTPS)                             | Complex (Requires Kerberos/HTTPS)                                   | Native                                                                                     |

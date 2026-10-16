+++
template = "docs/aem-title.html"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/integrate-legacy_winrm"
title = "Legacy WinRM - Red Hat Ansible Automation Platform 2.7"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/integrate-automate_microsoft_windows_with_ansible_automation_platform/", "Integrate with Microsoft Windows"]]
category = "Integrate"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/integrate-legacy_winrm/aem-page/integrate-legacy_winrm.html"
last_crumb = "Legacy WinRM"
latest = "true"
modified = "2026-10-06T15:21:13.207Z"
multi_page_path = ""
name = "Legacy WinRM"
oversized = "false"
page_slug = "integrate-legacy_winrm"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/integrate-legacy_winrm"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/integrate-legacy_winrm/toc/toc.json"
type = "aem-page"
+++

# Legacy WinRM

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

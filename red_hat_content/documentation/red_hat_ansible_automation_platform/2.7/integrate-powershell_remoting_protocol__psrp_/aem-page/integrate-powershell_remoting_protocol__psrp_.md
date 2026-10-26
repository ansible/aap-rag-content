+++
template = "docs/aem-title.html"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/integrate-powershell_remoting_protocol__psrp_"
title = "PowerShell Remoting Protocol (PSRP) - Red Hat Ansible Automation Platform 2.7"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/integrate-automate_microsoft_windows_with_ansible_automation_platform/", "Integrate with Microsoft Windows"]]
category = "Integrate"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/integrate-powershell_remoting_protocol__psrp_/aem-page/integrate-powershell_remoting_protocol__psrp_.html"
last_crumb = "PowerShell Remoting Protocol (PSRP)"
latest = "true"
modified = "2026-10-06T15:21:13.207Z"
multi_page_path = ""
name = "PowerShell Remoting Protocol (PSRP)"
oversized = "false"
page_slug = "integrate-powershell_remoting_protocol__psrp_"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/integrate-powershell_remoting_protocol__psrp_"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/integrate-powershell_remoting_protocol__psrp_/toc/toc.json"
type = "aem-page"
+++

# PowerShell Remoting Protocol (PSRP)

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

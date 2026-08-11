+++
title = "Troubleshoot Kerberos - Red Hat Ansible Automation Platform 2.7"
template = "docs/aem-title.html"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/troubleshoot-troubleshoot_kerberos"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/troubleshoot-troubleshoot_kerberos/", "Troubleshoot Kerberos"]]
category = "Troubleshoot"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/troubleshoot-troubleshoot_kerberos/aem-page/troubleshoot-troubleshoot_kerberos.html"
last_crumb = "Troubleshoot Kerberos"
modified = "2026-07-30T17:12:56.473Z"
multi_page_path = ""
name = "Troubleshoot Kerberos"
oversized = "false"
page_slug = "troubleshoot-troubleshoot_kerberos"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/troubleshoot-troubleshoot_kerberos"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/troubleshoot-troubleshoot_kerberos/toc/toc.json"
type = "aem-page"
+++

# Troubleshoot Kerberos

Diagnose Kerberos authentication failures using command-line tracing and Ansible Automation Platform environment variables, and configure the Negotiate protocol for resilient domain fallback.

**Troubleshooting Kerberos**

Common failures include "Server not found in Kerberos database" (`ansible_host` not set to FQDN) and "Cannot find KDC for realm" (`krb5.conf `or DNS issue).

**Command-line troubleshooting**

```
vi ./krb5.conf
export KRB5_CONFIG=./krb5.conf
export KRB5_TRACE=/dev/stdout
kinit user@DOMAIN.EXAMPLE.COM
klist
kdestroy
```

**Troubleshoot Kerberos within Ansible Automation Platform**

Define the `KRB5_TRACE` environment variable pointing to a file and then in block/rescue cat the file, or alternatively expose a path to the execution environment and set KRB5_TRACE to the exposed path. Also add KRB5_TRACE to the list of environment variables to pass through pexpect to kinit:

```
ansible_winrm_kinit_env_vars:
  - KRB5_CONFIG
  - KRB5_TRACE
```

**Negotiate**

Negotiate is a Microsoft "wrapper" protocol designed for flexibility. It attempts to authenticate using Kerberos first; if Kerberos is unavailable, that is, the target is not domain-joined or a SPN is missing, it automatically falls back to NTLM. This is the recommended default for most domain-joined environments as it provides a path to high-security authentication while maintaining connectivity during transition periods.

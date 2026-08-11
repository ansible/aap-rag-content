+++
template = "docs/aem-title.html"
title = "Establish a Windows compatible host and control node environment - Red Hat Ansible Automation Platform 2.7"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/plan-establish_a_windows_compatible_host_and_control_node_environment"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/plan-establish_a_windows_compatible_host_and_control_node_environment/", "Establish a Windows compatible host and control node environment"]]
category = "Plan"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/plan-establish_a_windows_compatible_host_and_control_node_environment/aem-page/plan-establish_a_windows_compatible_host_and_control_node_environment.html"
last_crumb = "Establish a Windows compatible host and control node environment"
modified = "2026-07-30T17:12:56.473Z"
multi_page_path = ""
name = "Establish a Windows compatible host and control node environment"
oversized = "false"
page_slug = "plan-establish_a_windows_compatible_host_and_control_node_environment"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/plan-establish_a_windows_compatible_host_and_control_node_environment"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/plan-establish_a_windows_compatible_host_and_control_node_environment/toc/toc.json"
type = "aem-page"
+++

# Establish a Windows compatible host and control node environment

Align infrastructure architecture and host configurations to ensure reliable Windows automation execution.

**Prerequisites**

To fully control and customize your Windows target systems, you must write and execute scripts natively. While Ansible handles the orchestration, you must have basic familiarity with the Microsoft Windows Operating System and PowerShell.

- **Write foundational scripts**: You must be able to write at least basic PowerShell scripts to further develop and tailor your automation platform for Microsoft Windows.
- **Use native control**: Unlike Bash or Python scripts used in Linux environments, PowerShell scripts are the Windows-native way of executing tasks, giving you almost complete administrative control over your target systems.

**Host OS compatibility**

Ansible Automation Platform manages Windows versions currently under Microsoft's extended support lifecycle (typically 10 years from the operating system release date).

- **WinRM and PSRP**: Supported seamlessly across Windows Server 2016, 2019, 2022, and 2025.
- **OpenSSH:** Requires OpenSSH version 7.9.0.0p1 or higher to prevent known command-line argument parsing bugs. This is native to Windows Server 2022 and 2025. Windows Server 2019 ships with version 7.7.2.1 and must be updated before use with Ansible. PowerShell 5.1 or PowerShell Core 7.x must be present.

**Control node architecture**

- **Production**: Production automation must execute within Linux-based Automation execution environments managed by Ansible Automation Platform. Ansible execution is not natively supported on Windows.
- **Development**: *Windows Subsystem for Linux* (WSL) is acceptable for local playbook development and testing but is not supported for enterprise production deployments.

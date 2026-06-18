+++
template = "docs/aem-title.html"
title = "Access Ansible Automation Platform through the UI - Red Hat Ansible Automation Platform 2.7"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-proc_operator_access_aap"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-assembly_operator_install_operator/", "Install on OpenShift Container Platform"]]
category = "Install"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/install-proc_operator_access_aap/aem-page/install-proc_operator_access_aap.html"
last_crumb = "Access Ansible Automation Platform through the UI"
modified = "2026-06-05T07:48:10.594Z"
multi_page_path = ""
name = "Access Ansible Automation Platform through the UI"
oversized = "false"
page_slug = "install-proc_operator_access_aap"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/install-proc_operator_access_aap"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/install-proc_operator_access_aap/toc/toc.json"
type = "aem-page"
+++

# Access Ansible Automation Platform through the UI

Use the **Ansible Automation Platform** instance as your default. This instance links the automation controller, automation hub, and Event-Driven Ansible deployments to a single interface.

## About this task

## Procedure

1.  Log in to Red Hat OpenShift Container Platform.
2.  Navigate to Networking> (and then)Routes
3.  Click the link under **Location** for **Ansible Automation Platform**.
4.  This redirects you to the Ansible Automation Platform login page. Enter "admin" as your username in the **Username** field.
5.  For the password you must:
  1.  Go to Workloads> (and then)Secrets.
  2.  Click <your instance name>-admin-password and copy the password.
  3.  Paste the password into the **Password** field.
6.  Click Login.
7.  Apply your subscription:
  1.  Click Subscription manifest or Username/password.
  2.  Upload your manifest or enter your username and password.
  3.  Select your subscription from the **Subscription** list.
  4.  Click Next. This redirects you to the **Analytics** page.
8.  Click Next.
9.  Select the **I agree to the terms of the license agreement** checkbox.
10.  Click Next.

## Results

You now have access to the platform gateway user interface.

If you cannot access the Ansible Automation Platform see [Frequently asked questions on platform gateway](/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-configure_your_ansible_automation_platform_deployment#operator-aap-troubleshooting "Manage your Ansible Automation Platform deployment and troubleshoot common issues with these frequently asked questions. Learn about resource management, logging, and error recovery for your components.") for help with troubleshooting and debugging.

+++
title = "Install and configure the Dev Containers extension - Red Hat Ansible Automation Platform 2.6"
template = "docs/aem-title.html"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.6/install-proc_devtools_ms_dev_containers_ext"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6", "2.6"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6/install-assembly_devtools_install/", "Install Ansible development tools"]]
category = "Install"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/install-proc_devtools_ms_dev_containers_ext/aem-page/install-proc_devtools_ms_dev_containers_ext.html"
last_crumb = "Install and configure the Dev Containers extension"
modified = "2026-05-21T14:12:12.122Z"
multi_page_path = ""
name = "Install and configure the Dev Containers extension"
oversized = "false"
page_slug = "install-proc_devtools_ms_dev_containers_ext"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.6"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/install-proc_devtools_ms_dev_containers_ext"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/install-proc_devtools_ms_dev_containers_ext/toc/toc.json"
type = "aem-page"
+++

# Install and configure the Dev Containers extension

If you are installing the containerized version of Ansible development tools, you must install the [Microsoft Dev Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) extension in VS Code.

## About this task

## Procedure

1.  Open VS Code.
2.  Click the **Extensions** (![Extensions](/webassets/aem/red_hat_ansible_automation_platform/2.6/images/vscode-extensions-icon.png)) icon in the Activity Bar, or click View> (and then)Extensions, to display the **Extensions** view.
3.  In the search field in the **Extensions** view, type `Dev Containers`.
4.  Select the Dev Containers extension from Microsoft and click Install. If you are using Podman or Podman Desktop as your containerization platform, you must modify the default settings in the `Dev Containers` extension.

5.  Replace docker with podman in the `Dev Containers` extension settings:
  1.  In VS Code, open the settings editor.
  2.  Search for `@ext:ms-vscode-remote.remote-containers`. Alternatively, click the **Extensions** icon in the activity bar and click the gear icon for the `Dev Containers` extension.

6.  Set `Dev > Containers:Docker Path` to `podman`.
7.  Set `Dev > Containers:Docker Compose Path` to `podman-compose`.

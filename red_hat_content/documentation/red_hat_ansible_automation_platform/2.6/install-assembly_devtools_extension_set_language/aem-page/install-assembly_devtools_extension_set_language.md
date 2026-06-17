+++
title = "Set the language for the VS Code extension - Red Hat Ansible Automation Platform 2.6"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.6/install-assembly_devtools_extension_set_language"
template = "docs/aem-title.html"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6", "2.6"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6/install-assembly_devtools_install/", "Install Ansible development tools"]]
category = "Install"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/install-assembly_devtools_extension_set_language/aem-page/install-assembly_devtools_extension_set_language.html"
last_crumb = "Set the language for the VS Code extension"
modified = "2026-05-21T14:12:12.122Z"
multi_page_path = ""
name = "Set the language for the VS Code extension"
oversized = "false"
page_slug = "install-assembly_devtools_extension_set_language"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.6"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/install-assembly_devtools_extension_set_language"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/install-assembly_devtools_extension_set_language/toc/toc.json"
type = "aem-page"
+++

# Set the language for the VS Code extension

The Ansible VS Code extension works only when the language associated with a file is set to Ansible. The extension provides features that help create Ansible playbooks, such as auto-completion, hover, and diagnostics.

The Ansible VS Code extension automatically associates the Ansible language with some files. The procedures below describe how to set the language for files that are not recognized as Ansible files.

## Associate the Ansible language to YAML files

The following procedure describes how to manually assign the Ansible language to a YAML file that is open in VS Code.

### About this task

### Procedure

1.  Open or create a YAML file in VS Code.
2.  Hover the cursor over the language identified in the status bar at the bottom of the VS Code window to open the **Select Language Mode** list.
3.  Select **Ansible** in the list. The language shown in the status bar at the bottom of the VS Code window for the file is changed to Ansible.

## Add the persistent file association for the Ansible language to `settings.json`

Instead of manually associating the Ansible language to YAML files, you can add file association for the Ansible language in your `settings.json` file.

### About this task

### Procedure

1.  Open the `settings.json` file:
  1.  Click View> (and then)Command Palette to open the command palette.
  2.  Enter `Workspace settings` in the search box and select **Open Workspace Settings (JSON)**.
2.  Add the following code to `settings.json`.

```
{
  ...

    "files.associations": {
    "*plays.yml": "ansible",
    "*init.yml": "yaml",
  }
}
```

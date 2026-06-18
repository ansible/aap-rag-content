+++
template = "docs/aem-title.html"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.6/install-assembly_inventory_file_importing_1"
title = "Import your inventory file from source control - Red Hat Ansible Automation Platform 2.6"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6", "2.6"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6/install-assembly_platform_install_overview/", "Install RPM-based Ansible Automation Platform"]]
category = "Install"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/install-assembly_inventory_file_importing_1/aem-page/install-assembly_inventory_file_importing_1.html"
last_crumb = "Import your inventory file from source control"
modified = "2026-05-21T14:12:12.122Z"
multi_page_path = ""
name = "Import your inventory file from source control"
oversized = "false"
page_slug = "install-assembly_inventory_file_importing_1"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.6"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/install-assembly_inventory_file_importing_1"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/install-assembly_inventory_file_importing_1/toc/toc.json"
type = "aem-page"
+++

# Import your inventory file from source control

With automation controller you can select an inventory file from source control, rather than creating one from scratch.

The files are non-editable, and as inventories are updated at the source, the inventories within the projects are also updated accordingly, including the `group_vars` and `host_vars` files or directory associated with them. SCM types can consume both inventory files and scripts. Both inventory files and custom inventory types use scripts.

Imported hosts have a description of *imported* by default. This can be overridden by setting the `_awx_description` variable on a given host. For example, if importing from a sourced `.ini` file, you can add the following host variables:

```
[main]
127.0.0.1 _awx_description="my host 1"
127.0.0.2 _awx_description="my host 2"
```
Similarly, group descriptions also default to *imported*, but can also be overridden by `_awx_description`.

## Inventory file fields for source control

You can use a source control management (SCM) system, such as Git, to manage your inventory files in automation controller. You can use an SCM system to version control your inventory files and manage them in a collaborative manner.

The source fields used are:

- `source_project`: the project to use.
- `source_path`: the relative path inside the project indicating a directory or a file. If left blank, "" is still a relative path indicating the root directory of the project.
- `source_vars`: if set on a "file" type inventory source then they are passed to the environment variables when running.


Additionally:

- An update of the project automatically triggers an inventory update where it is used.
- An update of the project is scheduled immediately after creation of the inventory source.
- Neither inventory nor project updates are blocked while a related job is running.
- In cases where you have a large project (around 10 GB), disk space on `/tmp` can be an issue.


You can specify a location manually in the automation controller UI from the **Add source** page of an inventory. Refer to [Adding a source](/documentation/en-us/red_hat_ansible_automation_platform/2.6/administer-proc_controller_add_source#proc-controller-add-source "Use the following procedure to add a source to an inventory. When you add a source to an inventory, the system creates a new group for that source.") for instructions on creating an inventory source.

When you update a project, refresh the listing to use the latest source control management (SCM) information. If no inventory sources use a project as an SCM inventory source, then the inventory listing might not be refreshed on update.

For inventories with SCM sources, the job **Details** page for inventory updates displays a status indicator for the project update and the name of the project.

The status indicator links to the project update job.

The project name links to the project.

You can perform an inventory update while a related job is running.

### Supported file syntax

Automation controller uses the `ansible-inventory` module from Ansible to process inventory files, and supports all valid inventory syntax that automation controller requires.

Important:

You do not need to write inventory scripts in Python. You can enter any executable file in the source field and must run `chmod +x` for that file and check it into Git.

The following is a working example of JSON output that automation controller can read for the import:

```
{
    "_meta": {
        "hostvars": {
            "host1": {
                "fly_rod": true
            }
        }
    },
    "all": {
        "children": [
            "groupA",
            "ungrouped"
        ]
    },
    "groupA": {
        "hosts": [
            "host1",
            "host10",
            "host11",
            "host12",
            "host13",
            "host14",
            "host15",
            "host16",
            "host17",
            "host18",
            "host19",
            "host2",
            "host20",
            "host21",
            "host22",
            "host23",
            "host24",
            "host25",
            "host3",
            "host4",
            "host5",
            "host6",
            "host7",
            "host8",
            "host9"
        ]
    }
}
```

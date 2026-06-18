+++
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.6/administer-proc_create_requirements_file"
template = "docs/aem-title.html"
title = "Create a requirements file - Red Hat Ansible Automation Platform 2.6"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6", "2.6"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6/administer-manage_your_organization_s_automation_content/", "Manage your organization's automation content"]]
category = "Administer"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/administer-proc_create_requirements_file/aem-page/administer-proc_create_requirements_file.html"
last_crumb = "Create a requirements file"
modified = "2026-05-21T14:12:12.122Z"
multi_page_path = ""
name = "Create a requirements file"
oversized = "false"
page_slug = "administer-proc_create_requirements_file"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.6"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/administer-proc_create_requirements_file"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/administer-proc_create_requirements_file/toc/toc.json"
type = "aem-page"
+++

# Create a requirements file

Use a requirements file to add collections to your automation hub.

## About this task

Requirements files are in YAML format and list the collections that you want to install in your automation hub. A standard `requirements.yml` file contains the following parameters:

- `name`: the name of the collection formatted as `<namespace>.<collection_name>`
- `version`: the collection version number

## Procedure

 Create your requirements file.

In YAML format, collection information in your requirements file should contain the following information:

```bash
collections:
  - name: namespace.collection_name
    version: 1.0.0
```

## Example

Be sure to specify the collection version number, otherwise you will sync all collection versions. Syncing all versions can require more space than expected.

## What to do next

To sync the collections in your requirements file, follow the steps in [Synchronizing content collections](/documentation/en-us/red_hat_ansible_automation_platform/2.6/administer-proc_create_synclist "You can sync certified and validated collections in Ansible automation hub from console.redhat.com.").

+++
title = "Configure the private automation hub community remote - Red Hat Ansible Automation Platform 2.6"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.6/administer-proc_set_community_remote"
template = "docs/aem-title.html"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6", "2.6"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6/administer-manage_your_organization_s_automation_content/", "Manage your organization's automation content"]]
category = "Administer"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/administer-proc_set_community_remote/aem-page/administer-proc_set_community_remote.html"
last_crumb = "Configure the private automation hub community remote"
modified = "2026-05-21T14:12:12.122Z"
multi_page_path = ""
name = "Configure the private automation hub community remote"
oversized = "false"
page_slug = "administer-proc_set_community_remote"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.6"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/administer-proc_set_community_remote"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/administer-proc_set_community_remote/toc/toc.json"
type = "aem-page"
+++

# Configure the private automation hub community remote

Configure the community remote so you can sync content from Ansible Galaxy.

## Before you begin

- You have a `requirements.yml` file that identifies those collections to synchronize from Ansible Galaxy as in the following example:     **Requirements.yml example**

```
collections:
  # Install a collection from Ansible Galaxy.
  - name: community.aws
    version: 5.2.0
    source: https://galaxy.ansible.com
```

## About this task

You can edit the **community** remote repository to synchronize chosen collections from Ansible Galaxy to your private automation hub. By default, your private automation hub community repository directs to `galaxy.ansible.com/api/`.

## Procedure

1.  Log in to Ansible Automation Platform.
2.  From the navigation panel, select Automation Content> (and then)Remotes.
3.  In the **Details** tab in the **Community** remote, click Edit remote.
4.  In the **YAML requirements** field, paste the contents of your `requirements.yml` file.
5.  Click Save remote.

## Results

You can now synchronize collections identified in your `requirements.yml` file from Ansible Galaxy to your private automation hub.

## What to do next

See [Synchronizing content collections](/documentation/en-us/red_hat_ansible_automation_platform/2.6/administer-proc_create_synclist "You can sync certified and validated collections in Ansible automation hub from console.redhat.com.")for syncing steps.

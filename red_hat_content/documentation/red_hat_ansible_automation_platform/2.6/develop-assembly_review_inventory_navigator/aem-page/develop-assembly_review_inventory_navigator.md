+++
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.6/develop-assembly_review_inventory_navigator"
title = "View groups and hosts in your inventory - Red Hat Ansible Automation Platform 2.6"
template = "docs/aem-title.html"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6", "2.6"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6/develop-assembly_intro_navigator/", "Emulate a platform environment locally with automation content navigator"]]
category = "Develop"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/develop-assembly_review_inventory_navigator/aem-page/develop-assembly_review_inventory_navigator.html"
last_crumb = "View groups and hosts in your inventory"
modified = "2026-05-21T14:12:12.122Z"
multi_page_path = ""
name = "View groups and hosts in your inventory"
oversized = "false"
page_slug = "develop-assembly_review_inventory_navigator"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.6"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/develop-assembly_review_inventory_navigator"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/develop-assembly_review_inventory_navigator/toc/toc.json"
type = "aem-page"
+++

# View groups and hosts in your inventory

As a content creator, you can review your Ansible inventory with automation content navigator and interactively delve into the groups and hosts.

## Review inventory from automation content navigator

You can review Ansible inventories with the automation content navigator text-based user interface in interactive mode and delve into groups and hosts for more details.

### Before you begin

- A valid inventory file or an inventory plugin.

### Procedure

1.  Start automation content navigator.

```
$ ansible-navigator
```
    Optional: type `ansible-navigator inventory -i simple_inventory.yml` from the command line to view the inventory.

2.  Review the inventory.

```
:inventory -i simple_inventory.yml

    TITLE            DESCRIPTION
0│Browse groups    Explore each inventory group and group members members
1│Browse hosts     Explore the inventory with a list of all hosts
```

3.  Type `0` to brows the groups.

```
  NAME               TAXONOMY                      TYPE
0│general            all                           group
1│nodes              all                           group
2│ungrouped          all                           group
```
    The `TAXONOMY` field details the hierarchy of groups the selected group or node belongs to.

4.  Type the number corresponding to the group you want to delve into.

```
  NAME              TAXONOMY                        TYPE
0│node-0            all▸nodes                       host
1│node-1            all▸nodes                       host
2│node-2            all▸nodes                       host
```

5.  Type the number corresponding to the host you want to delve into, or type `:<number>` for numbers greater than 9.

```
[node-1]
0│---
1│ansible_host: node-1.example.com
2│inventory_hostname: node-1
```

### Results

- Review the inventory output.

```
  TITLE            DESCRIPTION
0│Browse groups   Explore each inventory group and group members members
1│Browse hosts    Explore the inventory with a list of all hosts
```

+++
title = "Create dynamic groups with constructed inventories - Red Hat Ansible Automation Platform 2.7"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/administer-ref_controller_constructed_inventories"
template = "docs/aem-title.html"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/administer-assembly_controller_inventories/", "Define automation target hosts in your inventory files"]]
category = "Administer"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/administer-ref_controller_constructed_inventories/aem-page/administer-ref_controller_constructed_inventories.html"
last_crumb = "Create dynamic groups with constructed inventories"
modified = "2026-06-05T07:48:10.594Z"
multi_page_path = ""
name = "Create dynamic groups with constructed inventories"
oversized = "false"
page_slug = "administer-ref_controller_constructed_inventories"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/administer-ref_controller_constructed_inventories"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/administer-ref_controller_constructed_inventories/toc/toc.json"
type = "aem-page"
+++

# Create dynamic groups with constructed inventories

You can create a new inventory (called a constructed inventory) from a list of input inventories.

A constructed inventory has copies of hosts and groups in its input inventories, permitting jobs to target groups of servers across many inventories. Groups and hostvars can be added to the inventory content, and hosts can be filtered to limit the size of the constructed inventory.

The key factors of a constructed inventory are:

- The normal Ansible hostvars namespace is available
- They provide groups


Constructed inventories take `source_vars` and `limit` as inputs and transform its `input_inventories` into a new inventory, complete with groups. Groups (existing or constructed) can then be referenced in the `limit` field to reduce the number of hosts produced.

You can construct groups based on these host properties:

- RHEL major or minor versions
- Windows hosts
- Cloud based instances tagged in a certain region
- other


The examples described in later sections are organized by the structure of the input inventories.

## Debugging tips

When using constructed inventory scripts, you might need to debug your Jinja2 templates.

It is important to set the `strict` parameter to `true` so that you can debug problems with your templates. If the template fails to render, an error occurs in the associated inventory update for that constructed inventory.

When encountering errors, increase verbosity to get more details.

Giving a default, such as `| default("running")` is a generic use of Jinja2 templates in Ansible. Doing this avoids errors from the template when you set `strict: true`.

You can also set `strict: false`, and so enable the template to produce an error, which results in the host not getting included in that group. However, doing this makes it difficult to debug issues in the future if your templates continue to grow in complexity.

You might still have to debug the intended function of the templates if they are not producing the expected inventory content. For example, if a `groups` group has a complex filter (such as `shutdown_in_product_dev`) but does not contain any hosts in the resultant constructed inventory, then use the `compose` parameter to help debug.

 **Example**

```
source_vars:

plugin: constructed
strict: true
groups:
  shutdown_in_product_dev: state | default("running") == "shutdown" and account_alias == "product_dev"
compose:
  resolved_state: state | default("running")
  is_in_product_dev: account_alias == "product_dev"

limit: ``
```
Running with a blank `limit` returns all hosts. You can use this to inspect specific variables on specific hosts, giving insight into where problems in the `groups` lie.

## Nested groups

You can create nested groups in your inventory to organize hosts and apply variables at different levels.

A nested group consists of two groups where one is a child of the other. In the following example, the child group has another host inside of it, and the parent group has a variable defined.

Because of the way Ansible core operates, the variable of the parent group is available in the namespace as a playbook is running, and can be used for filtering.

The following example inventory file, `nested.yml` is in YAML format:

```
all:
  children:
    groupA:
      vars:
        filter_var: filter_val
      children:
        groupB:
          hosts:
            host1: {}
    ungrouped:
      hosts:
        host2: {}
```
Because `host1` is in `groupB`, it is also in `groupA`.

 **Filter on nested group names**

Use the following YAML format to filter on nested group names:

```
`source_vars`:

plugin: constructed

`limit`: `groupA`
```
 **Filter on nested group property**

Use the following YAML format to filter on a group variable, even if the host is indirectly a member of that group.

In the inventory content, note that `host2` is not expected to have the variable `filter_var` defined, because it is not in any of the groups. Because `strict: true` is used, use a default value so that hosts without that variable are defined. Using this, `host2`, returns `false` from the expression, instead of producing an error. `host1` inherits the variable from its groups, and is returned.

```
source_vars:

plugin: constructed
strict: true
groups:
  filter_var_is_filter_val: filter_var | default("") == "filter_val"

limit: filter_var_is_filter_val
```

## Ansible facts

You can create an inventory that uses Ansible facts to populate host variables.

To create an inventory with Ansible facts, you must run a playbook against the inventory that has the setting `gather_facts: true`. The facts differ system-to-system. The following examples are not intended to address all known scenarios.

## Filter on environment variables

You can filter hosts in an inventory by using the `ansible_env` variable in a constructed inventory plugin.

```
source_vars:

plugin: constructed
strict: true
groups:
  hosts_using_xterm: ansible_env.TERM == "xterm"

limit: hosts_using_xterm
```

## Filter hosts by processor type

You can create a constructed inventory that filters hosts by CPU type by using the `ansible_processor` fact.

The following example involves filtering hosts by processor type (Intel) using the YAML format:

```
source_vars:

plugin: constructed
strict: true
groups:
  intel_hosts: "GenuineIntel" in ansible_processor

limit: intel_hosts
```


Note:

Hosts in constructed inventories are not counted against your license allotment because they are referencing the original inventory host. Additionally, hosts that are disabled in the original inventories are not included in the constructed inventory.

An inventory update run using `ansible-inventory` creates the constructed inventory contents.

This is always configured to update-on-launch before a job, but you can still select a cache timeout value in case this takes too long.

When creating a constructed inventory, the API ensures that it always has one inventory source associated with it. All inventory updates have an associated inventory source, and the fields needed for constructed inventory (`source_vars` and `limit`) are fields already present on the inventory source model.

## Filtering on group name and variables

You can filter on a combination of groups and variables. For example, you can filter hosts that match a group variable value and also match a host variable value.

There are two approaches to executing this filter:

- Define two groups: one group to match the group variable and the other group to match the host variable value. Use the `limit` pattern to return the hosts that are in both groups. This is the recommended approach.
- Define one group. In the definition, include the condition that the group and host variables must match specific values. Use the `limit` pattern to return all the hosts in the new group.

### Example

The following inventory file defines four hosts and sets group and host variables. It defines a product group, a sustaining group, and it sets two hosts to a shutdown state.

The goal is to create a filter that returns only production hosts that are shutdown.

```
[account_1234]
host1
host2 state=shutdown

[account_4321]
host3
host4 state=shutdown

[account_1234:vars]
account_alias=product_dev

[account_4321:vars]
account_alias=sustaining
```
The goal here is to return only shutdown hosts that are present in the group with the `account_alias` variable equal to `product_dev`. There are two approaches to this, both shown in YAML format. The first one suggested is recommended.

1. **Construct 2 groups, limit to intersection**:     `source_vars`:



```
plugin: constructed
strict: true
groups:
  is_shutdown: state | default("running") == "shutdown"
  product_dev: account_alias == "product_dev"
```
     `limit`: `is_shutdown:&product_dev`

     This constructed inventory input creates a group for both categories and uses the `limit` (host pattern) to only return hosts that are in the intersection of those two groups.

     When a variable is or is not defined (depending on the host), you can give a default. For example, use `| default("running")` if you know what value it should have when it is not defined. This helps with debugging, as described in [Debugging tips](/documentation/en-us/red_hat_ansible_automation_platform/2.7/administer-ref_controller_constructed_inventories#ref-controller-inv-debugging-tips "When using constructed inventory scripts, you might need to debug your Jinja2 templates.").

2. **Construct 1 group, limit to group**:     `source_vars`:



```
plugin: constructed
strict: true
groups:
  shutdown_in_product_dev: state | default("running") == "shutdown" and account_alias == "product_dev"
```
     `limit`: `shutdown_in_product_dev`

     This input creates one group that only includes hosts that match both criteria. The limit is then just the group name by itself, returning **host2**. The same as the earlier approach.

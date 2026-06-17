+++
title = "Define a collection of hosts with Smart Inventories - Red Hat Ansible Automation Platform 2.6"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.6/administer-ref_controller_smart_inventories"
template = "docs/aem-title.html"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6", "2.6"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6/administer-assembly_controller_inventories/", "Define automation target hosts in your inventory files"]]
category = "Administer"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/administer-ref_controller_smart_inventories/aem-page/administer-ref_controller_smart_inventories.html"
last_crumb = "Define a collection of hosts with Smart Inventories"
modified = "2026-05-21T14:12:12.122Z"
multi_page_path = ""
name = "Define a collection of hosts with Smart Inventories"
oversized = "false"
page_slug = "administer-ref_controller_smart_inventories"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.6"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/administer-ref_controller_smart_inventories"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/administer-ref_controller_smart_inventories/toc/toc.json"
type = "aem-page"
+++

# Define a collection of hosts with Smart Inventories

Smart Inventories are collections of hosts defined by a stored search that can be viewed such as a standard inventory and can be easily used with job runs. Organization administrators have admin permission for inventories in their organization and can create Smart Inventories.

You can identify a Smart Inventory by the `KIND=smart` variable.

You can define a Smart Inventory by using the same method being used with Search. `InventorySource` is directly associated with an Inventory.

Note:

Smart inventories are deprecated and will be removed in a future release. Consider moving to constructed inventories for enhancements and replacement.

The `Inventory` model has the following new fields that are blank by default but are set accordingly for Smart Inventories:

- Set `kind` to `smart` for Smart Inventories.
- Set `host_filter` AND `kind` to `smart` for Smart Inventories.


The `host` model has a related endpoint, `smart_inventories` that identifies a set of all the Smart Inventories a host is associated with. The membership table updates every time a job runs against a smart inventory.

Note:

To update the memberships more often, you can change the `AWX_REBUILD_SMART_MEMBERSHIP` file-based setting to `True`. (The default is False). This updates memberships if the following events occur:

- A new host is added
- An existing host is modified (updated or deleted)
- A new Smart Inventory is added
- An existing Smart Inventory is modified (updated or deleted)

You can view inventories without being editable:

- Names of Host and Group created as a result of an inventory source synchronization.
- You cannot move or edit Group records.


You cannot create hosts from a Smart Inventory host endpoint (`/inventories/N/hosts/`) as with a normal inventory. The administrator of a Smart Inventory has permission to edit fields such as the name, description, variables, and the ability to delete. The administrator does not have the permission to change the `host_filter`, because that affects which hosts (that have a primary membership inside another inventory) are included in the smart inventory.

`host_filter` only applies to hosts inside of inventories inside the Smart Inventory’s organization.

To modify `host_filter`, you must be the organization administrator of the inventory’s organization. Organization administrators have implicit "admin" access to all inventories inside the organization, therefore, this does not convey any permissions they did not already possess.

Administrators of the Smart Inventory can grant other users (who are not also admins of your organization) permissions such as "use" and "adhoc" to the smart inventory. These permit the actions indicated by the role, as with other standard inventories. However, this does not grant any special permissions to hosts (which live in a different inventory). It does not permit direct read permission to hosts, or permit them to see additional hosts under `/#/hosts/`, although they can still view the hosts under the smart inventory host list.

In some situations, you can change the following:

- A new Host created manually on Inventory with Inventory sources.
- Groups created as a result of inventory source synchronizations.
- Variables on Host and Group are not changeable, even as the local System Administrator.


Hosts associated with the Smart Inventory are manifested at view time. If the results of a Smart Inventory contains more than one host with identical hostnames, only one of the matching hosts is included as part of the Smart Inventory, ordered by Host ID.

## Smart Host Filters

You can use a search filter to populate hosts for an inventory. This feature uses the fact searching feature.

Automation controller stores facts generated by an Ansible Playbook during a Job Template in the database whenever `use_fact_cache=True` is set per-Job Template. New facts are merged with existing facts and are per-host. These stored facts can be used to filter hosts with the `/api/v2/hosts` endpoint, using the `GET` query parameter `host_filter`.

For example:

```
/api/v2/hosts?host_filter=ansible_facts__ansible_processor_vcpus=8
```
The `host_filter` parameter permits:

- grouping with ()
- use of the boolean and operator:
  * `__` to reference related fields in relational fields
  * `__` is used on ansible_facts to separate keys in a JSON key path
  * `[] is used to denote a json array in the path specification
  * `""` can be used in the value when spaces are wanted in the value
- "classic" Django queries may be embedded in the `host_filter`


**Examples**:

```
/api/v2/hosts/?host_filter=name=localhost
/api/v2/hosts/?host_filter=ansible_facts__ansible_date_time__weekday_number="3"
/api/v2/hosts/?host_filter=ansible_facts__ansible_processor[]="GenuineIntel"
/api/v2/hosts/?host_filter=ansible_facts__ansible_lo__ipv6[]__scope="host"
/api/v2/hosts/?host_filter=ansible_facts__ansible_processor_vcpus=8
/api/v2/hosts/?host_filter=ansible_facts__ansible_env__PYTHONUNBUFFERED="true"
/api/v2/hosts/?host_filter=(name=localhost or name=database) and (groups__name=east or groups__name="west coast") and ansible_facts__an
```
You can search `host_filter` by **host name**, **group name**, and **Ansible facts**.

Group search has the following format:

```
groups.name:groupA
```
Fact search has the following format:

```
ansible_facts.ansible_fips:false
```
You can also perform Smart Search searches, which consist of a host name and host description.

```
host_filter=name=my_host
```


Note:

If a search term in `host_filter` is of string type, to make the value a number (for example, `2.66`) or a JSON keyword (for example, `null`, `true` or `false`) valid, add double quotations around the value to prevent the controller from parsing it as a non-string:

```
host_filter=ansible_facts__packages__dnsmasq[]__version="2.66"
```

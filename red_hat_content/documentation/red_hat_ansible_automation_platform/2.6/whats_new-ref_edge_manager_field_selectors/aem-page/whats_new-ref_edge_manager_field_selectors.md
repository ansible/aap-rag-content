+++
template = "docs/aem-title.html"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.6/whats_new-ref_edge_manager_field_selectors"
title = "Filter a list with field selectors - Red Hat Ansible Automation Platform 2.6"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6", "2.6"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6/whats_new-technology_preview/", "Technology Preview"]]
category = "What's new"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/whats_new-ref_edge_manager_field_selectors/aem-page/whats_new-ref_edge_manager_field_selectors.html"
last_crumb = "Filter a list with field selectors"
modified = "2026-05-21T14:12:12.122Z"
multi_page_path = ""
name = "Filter a list with field selectors"
oversized = "false"
page_slug = "whats_new-ref_edge_manager_field_selectors"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.6"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/whats_new-ref_edge_manager_field_selectors"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/whats_new-ref_edge_manager_field_selectors/toc/toc.json"
type = "aem-page"
+++

# Filter a list with field selectors

Field selectors filter a list of Red Hat Edge Manager resources based on specific resource field values. They follow the same syntax, principles, and operators as Kubernetes Field and Label selectors, with additional operators available for more advanced search use cases.

## Supported fields

Red Hat Edge Manager resources give a set of metadata fields that you can select.

Each resource supports the following metadata fields:

-  `metadata.name`
-  `metadata.owner`
-  `metadata.creationTimestamp`


Note:

To query labels, use Label Selectors for advanced and flexible label filtering.

For more information, see [Labels and label selectors](/documentation/en-us/red_hat_ansible_automation_platform/2.6/whats_new-assembly_edge_manager_manage_devices#edge-manager-labels "You can organize resources by assigning labels for location, hardware, or purpose. The Red Hat Edge Manager labels follow the same syntax, principles, and operators as Kubernetes labels and label selectors. Use these labels to select devices or apply operations to devices in the inventory.").

## List of additional supported fields

In addition to the metadata fields, each resource has its own unique set of fields that you can select, offering further flexibility in filtering and selection based on resource-specific attributes.

The following table lists the fields supported for filtering for each resource kind:

| Kind                                 | Fields                                                                                                                                               |
| ------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| <br> **Certificate Signing Request** | <br> `status.certificate`                                                                                                                            |
| <br> **Device**                      | <br> `status.summary.status`<br> `status.applicationsSummary.status`<br> `status.updated.status`<br> `status.lastSeen`<br> `status.lifecycle.status` |
| <br> **Enrollment Request**          | <br> `status.approval.approved`<br> `status.certificate`                                                                                             |
| <br> **Fleet**                       | <br> `spec.template.spec.os.image`                                                                                                                   |
| <br> **Repository**                  | <br> `spec.type`<br> `spec.url`                                                                                                                      |
| <br> **Resource Sync**               | <br> `spec.repository`                                                                                                                               |

## Fields discovery

Some Red Hat Edge Manager resources might expose additional supported fields. You can discover the supported fields by using `flightctl` with the `--field-selector` option. If you try to use an unsupported field, the error message lists the available supported fields.

See the following examples:

```bash
flightctl get device --field-selector='text'
```

```bash
Error: listing devices: 400, message: unknown or unsupported selector: unable to resolve selector name "text". Supported selectors are: [metadata.alias metadata.creationTimestamp metadata.name metadata.nameoralias metadata.owner status.applicationsSummary.status status.lastSeen status.summary.status status.updated.status]
```
The field `text` is not a valid field for filtering. The error message provides a list of supported fields that you can use with `--field-selector` for the `Device` resource.

You can then use one of the supported fields:

```bash
flightctl get devices --field-selector 'metadata.alias contains cluster'
```
The `metadata.alias` field is checked with the containment operator `contains` to see if it has the value `cluster`.

 **Examples**

 **Example 1: Excluding a specific device by name**

The following command filters out a specific device by its name:

```bash
flightctl get devices --field-selector 'metadata.name!=c3tkb18x9fw32fzx5l556n0p0dracwbl4uiojxu19g2'
```
 **Example 2: Filter by owner, labels, and creation timestamp**

This command retrieves devices owned by `Fleet/pos-fleet`, located in the `us` region, and created in 2024:

```bash
flightctl get devices --field-selector 'metadata.owner=Fleet/pos-fleet, metadata.creationTimestamp >= 2024-01-01T00:00:00Z, metadata.creationTimestamp < //2025-01-01T00:00:00Z' -l 'region=us'
```
 **Example 3: Filter by Owner, Labels, and Device Status**

This command retrieves devices owned by `Fleet/pos-fleet`, located in the `us` region, and with a `status.updated.status` of either `Unknown` or `OutOfDate`:

```bash
flightctl get devices --field-selector 'metadata.owner=Fleet/pos-fleet, status.updated.status in (Unknown, OutOfDate)' -l 'region=us'
```

## Supported operators

Learn the operators and corresponding symbols you can use to construct sophisticated field selectors when querying or filtering Red Hat Edge Manager resources. This enables precise and flexible control over resource selection.

| Operator                | Symbol             | Description                                               |
| ----------------------- | ------------------ | --------------------------------------------------------- |
| <br>Exists              | <br> `exists`      | <br>Checks if a field exists                              |
| <br>DoesNotExist        | <br> `!`           | <br>Checks if a field does not exist                      |
| <br>Equals              | <br> `=`           | <br>Checks if a field is equal to a value                 |
| <br>DoubleEquals        | <br> `==`          | <br>Another form of equality check                        |
| <br>NotEquals           | <br> `!=`          | <br>Checks if a field is not equal to a value             |
| <br>GreaterThan         | <br> `>`           | <br>Checks if a field is greater than a value             |
| <br>GreaterThanOrEquals | <br> `>=`          | <br>Checks if a field is greater than or equal to a value |
| <br>LessThan            | <br> `<`           | <br>Checks if a field is less than a value                |
| <br>LessThanOrEquals    | <br> `⇐`           | <br>Checks if a field is less than or equal to a value    |
| <br>In                  | <br> `in`          | <br>Checks if a field is within a list of values          |
| <br>NotIn               | <br> `notin`       | <br>Checks if a field is not in a list of values          |
| <br>Contains            | <br> `contains`    | <br>Checks if a field has a value                         |
| <br>NotContains         | <br> `notcontains` | <br>Checks if a field does not contain a value            |

### Operators usage by field type

Each field type supports a specific subset of operators:

| Field Type         | Supported Operators                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Value                                |
| ------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------ |
| <br> **String**    | <br>`Equals`: Matches if the field value is an exact match to the specified string.<br>`DoubleEquals`: Matches if the field value is an exact match to the specified string (alternative to `Equals`).<br>`NotEquals`: Matches if the field value is not an exact match to the specified string.<br>`In`: Matches if the field value matches at least one string in the list.<br>`NotIn`: Matches if the field value does not match any of the strings in the list.<br>`Contains`: Matches if the field value has the specified substring.<br>`NotContains`: Matches if the field value does not contain the specified substring.<br>`Exists`: Matches if the field is present.<br>`DoesNotExist`: Matches if the field is not present.                                                                                                                                                                                                                  | <br>Text string                      |
| <br> **Timestamp** | <br>`Equals`: Matches if the field value is an exact match to the specified timestamp.<br>`DoubleEquals`: Matches if the field value is an exact match to the specified timestamp (alternative to `Equals`).<br>`NotEquals`: Matches if the field value is not an exact match to the specified timestamp.<br>`GreaterThan`: Matches if the field value is after the specified timestamp.<br>`GreaterThanOrEquals`: Matches if the field value is after or equal to the specified timestamp.<br>`LessThan`: Matches if the field value is before the specified timestamp.<br>`LessThanOrEquals`: Matches if the field value is before or equal to the specified timestamp.<br>`In`: Matches if the field value matches at least one timestamp in the list.<br>`NotIn`: Matches if the field value does not match any of the timestamps in the list.<br>`Exists`: Matches if the field is present.<br>`DoesNotExist`: Matches if the field is not present. | <br>RFC 3339 format                  |
| <br> **Number**    | <br>`Equals`: Matches if the field value equals the specified number.<br>`DoubleEquals`: Matches if the field value equals the specified number (alternative to `Equals`).<br>`NotEquals`: Matches if the field value does not equal to the specified number.<br>`GreaterThan`: Matches if the field value is greater than the specified number.<br>`GreaterThanOrEquals`: Matches if the field value is greater than or equal to the specified number.<br>`LessThan`: Matches if the field value is less than the specified number.<br>`LessThanOrEquals`: Matches if the field value is less than or equal to the specified number.<br>`In`: Matches if the field value equals at least one number in the list.<br>`NotIn`: Matches if the field value does not equal any numbers in the list.<br>`Exists`:Matches if the field is present.<br>`DoesNotExist`: Matches if the field is not present.                                                    | <br>Number format                    |
| <br> **Boolean**   | <br>`Equals`: Matches if the value is `true` or `false`.<br>`DoubleEquals`: Matches if the value is `true` or `false` (alternative to `Equals`).<br>`NotEquals`: Matches if the value is the opposite of the specified value.<br>`In`: Matches if the value (`true` or `false`) is in the list.  Note:   <br>The list can only contain `true` or `false`, so this operator is limited in use.<br>`NotIn`: Matches if the value is not in the list.<br>`Exists`: Matches if the field is present.<br>`DoesNotExist`: Matches if the field is not present.                                                                                                                                                                                                                                                                                                                                                                                                 | <br>Boolean format (`true`, `false`) |
| <br> **Array**     | <br>`Contains`: Matches if the array has the specified value.<br>`NotContains`: Matches if the array does not contain the specified value. `In`: Matches if the array overlaps with the specified values.<br>`NotIn`: Matches if the array does not overlap with the specified values. `Exists`: Matches if the field is present.<br>`DoesNotExist`:Matches if the field is not present.  Note:   <br>Using `Array[Index]` treats the element as the type defined for the array elements. For example string, timestamp, number, or boolean.                                                                                                                                                                                                                                                                                                                                                                                                             | <br>Array element                    |

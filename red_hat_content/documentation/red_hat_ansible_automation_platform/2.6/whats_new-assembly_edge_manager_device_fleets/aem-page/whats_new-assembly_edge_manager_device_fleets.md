+++
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.6/whats_new-assembly_edge_manager_device_fleets"
title = "Manage a large number of devices with device fleets - Red Hat Ansible Automation Platform 2.6"
template = "docs/aem-title.html"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6", "2.6"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6/whats_new-technology_preview/", "Technology Preview"]]
category = "What's new"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/whats_new-assembly_edge_manager_device_fleets/aem-page/whats_new-assembly_edge_manager_device_fleets.html"
last_crumb = "Manage a large number of devices with device fleets"
modified = "2026-05-21T14:12:12.122Z"
multi_page_path = ""
name = "Manage a large number of devices with device fleets"
oversized = "false"
page_slug = "whats_new-assembly_edge_manager_device_fleets"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.6"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/whats_new-assembly_edge_manager_device_fleets"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/whats_new-assembly_edge_manager_device_fleets/toc/toc.json"
type = "aem-page"
+++

# Manage a large number of devices with device fleets

The Red Hat Edge Manager simplifies the management of a large number of devices and workloads through *device fleets*. A fleet is a resource that defines a group of devices governed by a common device template and management policies.

When you make a change to the device template, all devices in the fleet receive the changes when the Red Hat Edge Manager agent detects the new target specification.

Device monitoring in a fleet is also simplified because you can check the status summary of the whole fleet.

Fleet-level management offers the following advantages:

- Scales your operations because you perform operations only once for each fleet instead of once for each device.
- Minimizes the risk of configuration mistakes and configuration drift.
- Automatically applies the target configuration when you add devices to the fleet or replace devices in the fleet. The fleet specification consists of the following features:

Label selector
Determines which devices are part of the fleet.

Device template
Defines the configuration that the Red Hat Edge Manager enforces on devices in the fleet.

Policies
Governs how devices are managed, for example, how changes to the device template are rolled out to the devices.

You can have both individually managed and fleet-managed devices at the same time.

When you select a device into a fleet, the Red Hat Edge Manager creates the device specification for the new device based on the device template. If you update the device template for a fleet or a new device joins the fleet, the Red Hat Edge Manager enforces the new specification in the fleet.

If a device is not selected into any fleets, the device is considered user-managed or unmanaged. For user-managed devices, you must update the device specification either manually or through an external automation.

Important:

A device cannot be a member of more than one fleet at the same time.

## Device selection into a fleet

By default, devices are not assigned to a fleet. Instead, each fleet uses a selector that defines which labels a device must have to be added to the fleet.

To understand how to use labels in a fleet, see the following example.

The following list shows point-of-sales terminal devices and their labels:

| Device | Labels                                                         |
| ------ | -------------------------------------------------------------- |
| <br>A  | <br>`type: pos-terminal`, `region: east`, `stage: production`  |
| <br>B  | <br>`type: pos-terminal`, `region: east`, `stage: development` |
| <br>C  | <br>`type: pos-terminal`, `region: west`, `stage: production`  |
| <br>D  | <br>`type: pos-terminal`, `region: west`, `stage: development` |


If all point-of-sale terminals use the same configuration and are managed by the same operations team, you can define a single fleet called `pos-terminals` with the `type=pos-terminal` label selector. Then, the fleet contains devices A, B, C, and D.

However, you might want to create separate fleets for the different organizations for development or production. You can define a fleet for development with the `type=pos-terminal, stage=development` label selector, which selects devices C and D. Then, you can define another fleet for production with the `type=pos-terminal, stage=production` label selector. By using the correct label selectors, you can manage both fleets independently.

Important:

You must define selectors in a way that two fleets do not select the same device. For example, if one fleet selects `region=east`, and another fleet selects `stage=production`, both fleets try to select device A. If two fleets try to select the same device, the Red Hat Edge Manager keeps the device in the currently assigned fleet, if any, and sets the `OverlappingSelectors` condition on the affected fleets to `true`.

## Device templates

A device template of a fleet has a device specification that is applied to all devices in the fleet when the template is updated.

For example, you can specify in the device template of a fleet that all devices in the fleet must run the `quay.io/flightctl/rhel:9.5` operating system image.

The Red Hat Edge Manager service then rolls out the target specification to all devices in the fleet, and the Red Hat Edge Manager agents update each device.

You can change other specification items in the device template and the Red Hat Edge Manager applies the changes in the same way.

However, sometimes not all of the devices in the fleet need to have the exact same specification. The Red Hat Edge Manager allows templates to contain placeholders that are populated based on the device name or label values.

The syntax of the placeholders matches that of [Go templates](https://pkg.go.dev/text/template). However, you can only use simple text and actions.

The use of conditionals or loops in the placeholders is not supported.

You can reference anything from the metadata of a device, such as `{{ .metadata.labels.key }}` or `{{ .metadata.name }}`.

You can also use the following functions in your placeholders:

- The `upper` function changes the value to uppercase. For example, the function is `{{ upper .metadata.name }}`.
- The `lower` function changes the value to lowercase. For example, the function is `{{ lower .metadata.labels.key }}`.
- The `replace` function replaces all occurrences of a substring with another string. For example, the function is `{{ replace "old" "new" .metadata.labels.key }}`.
- The `getOrDefault` function returns a default value if accessing a missing label. For example, the function is `{{ getOrDefault .metadata.labels "key" "default" }}`. You can combine the functions in pipelines, for example, a combined function is `{{ getOrDefault .metadata.labels "key" "default" | upper | replace " " "-" }}`.


Note:

Ensure you are using proper Go template syntax. For example, `{{ .metadata.labels.target-revision }}` is not valid because of the hyphen. Instead, you must refer to the field as `{{ index .metadata.labels "target-revision" }}`.

You can use the placeholders in device templates in the following ways:

- You can label devices by deployment stage, for example, stage labels are `stage: testing` and `stage: production`. Then, you can use the label with the `stage` key as placeholder when referencing the operating system image to use, for example, use `quay.io/myorg/myimage:latest-{{ .metadata.labels.stage }}` or when referencing a configuration folder in a Git repository.
- You can label devices by deployment site, for example, deployment sites are `site: factory-berlin` and `site: factory-madrid`.
- Then, you can use the label with the `site` key as parameter when referencing the secret with network access credentials in Kubernetes. The following fields in device templates support placeholders:
    | Field                  | Placeholders supported in              |
    | ---------------------- | -------------------------------------- |
    | Operating System Image | repository name, image name, image tag |
    | Git Config Provider    | target revision, path                  |
    | HTTP Config Provider   | URL suffix, path                       |
    | Inline Config Provider | content, path                          |

## Add devices to a fleet on the web UI

Define the label selector for a device fleet by using the Red Hat Edge Manager web UI to automatically include devices that match your specified criteria. This streamlines fleet management by applying a common device template and ensuring consistent policies across all enrolled devices.

### About this task

### Procedure

1.  From the navigation panel, select Application Links> (and then)Edge Manager. This opens the external Edge Manager instance.
2.  From the navigation panel, select **Fleets**. Select the fleet that you want to add devices to.
3.  Click Actions and select **Edit fleet**.
4.  In the **General info** tab, click **Add label** under the **Device selector** option.
5.  Add the label to select devices for your fleet. Any devices with that label are added to the fleet.

## Add devices to a fleet on the CLI

Use the Red Hat Edge Manager CLI to define the label selectors for a fleet resource, automatically enrolling devices that match the specified criteria. This streamlines fleet management by enabling consistent configuration and policy enforcement across a defined group of devices.

### About this task

### Procedure

1.  Run the following command to verify that the label selector returns the devices that you want to add to the fleet:
  

```bash
flightctl get devices -l type=pos-terminal -l stage=development
```

2.  If running the command returns the expected list of devices, you can define a fleet that selects the devices by using the following YAML file:
  

```yaml
apiVersion: flightctl.io/v1alpha1
kind: Fleet
metadata:
  name: my_fleet
spec:
  selector:
    matchLabels:
      type: pos-terminal
      stage: development
[...]
```

3.  Apply the change by running the following command:
  

```bash
flightctl apply -f my_fleet.yaml
```

4.  Check for any overlaps with the selector of other fleets by running the following command:
  

```bash
flightctl get fleets/my_fleet -o json | jq -r '.status.conditions[] | select(.type=="OverlappingSelectors").status'
```
    See the following example output:

```bash
False
```

## Rollout device selection

When performing a rollout by using `flightctl`, you must manage which devices participate in the rollout and how much disruption is acceptable. The device selection process and the rollout disruption budget concept ensure controlled and predictable rollouts.

The process and configuration for selecting devices during a rollout includes targeting strategies, batch sequencing, and success criteria for controlled software deployment.

## Device targeting

A rollout applies only to devices that belong to a fleet. Each device can belong to only a single fleet. Since rollout definitions are done at the fleet level, the selection process determines which devices within a fleet that participate in a batch rollout based on label criteria.

After processing all batches, all fleet devices are rolled out.

- **Labels**: Devices with specific metadata labels can be targeted for rollouts.
- **Fleet membership**: Rollouts apply only to devices within the specified fleet.

## Device selection strategy

The Red Hat Edge Manager supports only the `BatchSequence` strategy for device selection. This strategy defines a stepwise rollout process where devices are added in batches based on specific criteria. Batches are executed sequentially.

After each batch completes, execution proceeds to the next batch only if the success rate of the previous batch meets or exceeds the configured success threshold.

The success rate is determined as:

```
# of successful rollouts in the batch / # of devices in the batch >= success threshold
```
In a batch sequence, the final batch is an implicit batch and it is not specified in the batch sequence. It selects all devices in a fleet that have not been selected by the explicit batches in the sequence.

## Limit in device selection

Each batch in the `BatchSequence` strategy might use an optional `limit` parameter to define how many devices should be included in the batch. You can specify the limit can in two ways:

- **Absolute number**: A fixed number of devices to be selected.
- **Percentage**: The percentage of the total matching device population to be selected.   * If you provide a `selector` with labels, the percentage is calculated based on the number of devices that match the label criteria within the fleet.
  * If you do not provide a `selector`, the percentage is applied to all devices in the fleet.

## Success threshold

The `successThreshold` defines the percentage of successfully updated devices required to continue the rollout. If the success rate falls below this threshold, the rollout might be paused to prevent further failures.

 **Example**

The following shows an example YAML configuration for a fleet specification:

```
apiVersion: v1alpha1
kind: Fleet
metadata:
  name: default
spec:
  selector:
    matchLabels:
      fleet: default
  rolloutPolicy:
    deviceSelection:
      strategy: 'BatchSequence'
      sequence:
        - selector:
            matchLabels:
              site: madrid
          limit: 1  # Absolute number
        - selector:
            matchLabels:
              site: madrid
          limit: 80%  # Percentage of devices matching the label criteria within the fleet
        - limit: 50%  # Percentage of all devices in the fleet
        - selector:
            matchLabels:
              site: paris
        - limit: 80%
        - limit: 100%
    successThreshold: 95%
```
In this example, there are 6 explicit batches and 1 implicit batch:

- The first batch selects 1 device having a label **site:madrid**.
- With the second batch 80% of all devices having the label **site:madrid** are either selected for rollout in the current batch or were previously selected for rollout.
- With the third batch 50% of all devices are either selected for rollout in the current batch or were previously selected for rollout.
- With the fourth batch all devices that were not previously selected and have the label **site:paris** are selected.
- With the fifth batch 80% of all devices are either selected for rollout in the current batch or were previously selected for rollout.
- With the sixth batch 100% of all devices are either selected for rollout in the current batch or were previously selected for rollout.
- The last implicit batch selects all devices that have not been selected in any previous batch (might be none).

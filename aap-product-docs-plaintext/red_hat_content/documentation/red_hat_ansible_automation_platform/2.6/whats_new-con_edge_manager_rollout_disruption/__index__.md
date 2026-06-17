# Define a rollout disruption budget

A rollout disruption budget defines the acceptable level of service impact during a rollout. This ensures that a deployment does not take down too many devices at once, maintaining overall system stability.

## Disruption budget parameters

Configure rollout disruption parameters, such as grouping criteria (`groupBy`) and availability limits (`minAvailable`, `maxUnavailable`), to control the maximum acceptable service impact during fleet updates and keep overall system stability.

- `groupBy`: Defines how devices are grouped when applying the disruption budget. The grouping is done by label keys.
- `minAvailable`: Specifies the minimum number of devices that must remain available during a rollout.
- `maxUnavailable`: Limits the number of devices that can be unavailable at the same time.


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
disruptionBudget:
groupBy: ['site', 'function']
minAvailable: 1
maxUnavailable: 10
```
In this example, the grouping is performed on 2 label keys: **site** and **function**. A group for disruption budget consists of all devices in a fleet having the same label values for the preceding label keys. For every such group the conditions defined in this specification are continuously enforced.

# Capture telemetry data for the Ansible self-service portal
## Disable telemetry data collection

You can disable and enable the telemetry data collection feature for Ansible automation portal by updating the Helm chart for your OpenShift Container Platform project.

### Procedure

1.  Log in to the OpenShift Container Platform console and open the project for Ansible automation portal in the **Developer** perspective.
2.  Navigate to **Helm**.
3.  Click the **More actions ⋮** icon for your Ansible automation portal Helm chart and select Upgrade.
4.  Select YAML view.
5.  Locate the `redhat-developer-hub.global.dynamic.plugins` section of the Helm chart.
6.  To disable telemetry data collection, add the following lines to the `redhat-developer-hub.global.dynamic.plugins` section.


```
redhat-developer-hub:
global:
# ...
dynamic:
plugins:
- disabled: true
package: >-
./dynamic-plugins/dist/backstage-community-plugin-analytics-provider-segment
```
To re-enable telemetry data collection, delete these lines.

7.  Click Upgrade to apply the changes to the Helm chart and restart the pod.

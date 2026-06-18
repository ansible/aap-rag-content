# Capture telemetry data for the Ansible self-service portal

The telemetry data collection feature helps in collecting and analyzing the telemetry data to improve your experience with Ansible automation portal. This feature is enabled by default.

## Telemetry data collected by Red Hat

Red Hat collects and analyses the following data:

- Events of page visits and clicks on links or buttons.
- System-related information, for example, locale, timezone, user agent including browser and OS details.
- Page-related information, for example, title, category, extension name, URL, path, referrer, and search parameters.
- Anonymized IP addresses, recorded as `0.0.0.0`.
- Anonymized username hashes, which are unique identifiers used solely to identify the number of unique users of the RHDH application.
- Feedback and sentiment submitted through the Ansible automation portal feedback form, including a 1-5 star rating and feedback text. Users must acknowledge that they share the feedback with Red Hat before submitting.


Note:

The feedback form is optional and disabled by default. You can enable for your users if you choose.

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

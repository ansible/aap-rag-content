# Configure Google Cloud for increased authentication performance

Increase the default port limit on your Google Cloud Platform (GCP) Cloud NAT gateway to prevent authentication and performance issues during high traffic. This helps ensure stable connectivity for Ansible Automation Platform deployments on OpenShift (version 4.17 and above).

The default setting for the Cloud NAT gateway’s **Minimum ports per VM instance** in OpenShift installations on GCP (version 4.17 and above) is 64. This low port limit can be quickly exhausted when platform gateway handles concurrent external network connections, such as Single Sign-On (SSO) requests. When the limit is reached, it prevents new outgoing connections, causing authentication failures or severe performance degradation.

## Increase the minimum ports

To address this limitation, manually increase the **Minimum ports per VM instance** setting for the Cloud NAT gateway associated with the worker nodes.

### About this task

Use the Google Cloud Console to apply this workaround.

### Procedure

1.  Go to the [Cloud NAT service](https://console.cloud.google.com/net-services/nat/).
2.  Locate and select the NAT gateway configured for your OpenShift cluster’s worker nodes.
3.  Increase the default value of 64 for the **Minimum ports per VM instance** setting to a higher value to accommodate your anticipated traffic volume. Increasing this limit ensures enough available ports for external communication, reducing the likelihood of performance issues during high-volume authentication and external communication tasks.

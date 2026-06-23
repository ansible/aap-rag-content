# Configure Google Cloud for increased authentication performance
## Increase the minimum ports

To address this limitation, manually increase the **Minimum ports per VM instance** setting for the Cloud NAT gateway associated with the worker nodes.

### About this task

Use the Google Cloud Console to apply this workaround.

### Procedure

1.  Go to the [Cloud NAT service](https://console.cloud.google.com/net-services/nat/).
2.  Locate and select the NAT gateway configured for your OpenShift cluster’s worker nodes.
3.  Increase the default value of 64 for the **Minimum ports per VM instance** setting to a higher value to accommodate your anticipated traffic volume. Increasing this limit ensures enough available ports for external communication, reducing the likelihood of performance issues during high-volume authentication and external communication tasks.

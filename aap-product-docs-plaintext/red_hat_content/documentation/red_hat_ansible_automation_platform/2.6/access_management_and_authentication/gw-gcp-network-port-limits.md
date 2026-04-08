# 2. Configuring authentication in the Ansible Automation Platform
## 2.8. Managing authentication in Ansible Automation Platform
### 2.8.6. Google Cloud Platform network configuration for increased authentication performance




In a Google Cloud Platform (GCP) environment, a high volume of traffic can lead to authentication and performance issues because of the low default port limit set on the GCP Cloud NAT gateway. While this configuration affects all GCP deployments, the highest risk for hitting this limit occurs when Ansible Automation Platform is deployed on OpenShift (version 4.17 and above).

The default setting for the Cloud NAT gateway’s **Minimum ports per VM instance** in OpenShift installations on GCP (version 4.17 and above) is 64. This low port limit can be quickly exhausted when platform gateway handles concurrent external network connections, such as Single Sign-On (SSO) requests. When the limit is reached, it prevents new outgoing connections, causing authentication failures or severe performance degradation.

#### 2.8.6.1. Increasing the minimum ports




To address this limitation, manually increase the **Minimum ports per VM instance** setting for the Cloud NAT gateway associated with the worker nodes.

Use the Google Cloud Console to apply this workaround.

**Procedure**

1. Go to the [Cloud NAT service](https://console.cloud.google.com/net-services/nat/) .
1. Locate and select the NAT gateway configured for your OpenShift cluster’s worker nodes.
1. Increase the default value of 64 for the **Minimum ports per VM instance** setting to a higher value to accommodate your anticipated traffic volume.

Increasing this limit ensures enough available ports for external communication, reducing the likelihood of performance issues during high-volume authentication and external communication tasks.





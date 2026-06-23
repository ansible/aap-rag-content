# Configure Google Cloud for increased authentication performance

Increase the default port limit on your Google Cloud Platform (GCP) Cloud NAT gateway to prevent authentication and performance issues during high traffic. This helps ensure stable connectivity for Ansible Automation Platform deployments on OpenShift (version 4.17 and above).

The default setting for the Cloud NAT gateway’s **Minimum ports per VM instance** in OpenShift installations on GCP (version 4.17 and above) is 64. This low port limit can be quickly exhausted when platform gateway handles concurrent external network connections, such as Single Sign-On (SSO) requests. When the limit is reached, it prevents new outgoing connections, causing authentication failures or severe performance degradation.


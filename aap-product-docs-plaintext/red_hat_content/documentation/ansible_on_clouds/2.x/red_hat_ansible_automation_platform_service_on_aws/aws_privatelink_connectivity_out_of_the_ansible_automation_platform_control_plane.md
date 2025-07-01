# 7. Red Hat Ansible Automation Platform Service on AWS Private Link Connectivity
## 7.2. How AWS PrivateLink works
### 7.2.2. AWS PrivateLink connectivity out of the Ansible Automation Platform control plane




To enable AWS PrivateLink connectivity from the control plane to your private resources, create one or more Endpoint Services in your VPC and work with Red Hat to create the consuming Endpoints. With this in place, the Ansible Automation Platform control plane can connect privately to your resources such as registries, repositories, and execution nodes. Traffic is stateful, so there is no need to open a private link in the reverse direction for responses to Transmission Control Protocol (TCP) requests that originate from the control plane VPC.


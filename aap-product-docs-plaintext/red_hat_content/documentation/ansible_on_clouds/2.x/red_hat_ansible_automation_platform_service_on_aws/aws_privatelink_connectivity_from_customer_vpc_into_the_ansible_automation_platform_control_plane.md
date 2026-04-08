# 7. Red Hat Ansible Automation Platform Service on AWS Private Link Connectivity
## 7.2. How AWS PrivateLink works
### 7.2.1. AWS PrivateLink connectivity from customer VPC into the Ansible Automation Platform control plane




For AWS PrivateLink connectivity into the control plane, an AWS Endpoint Service has automatically provisioned AWS PrivateLink connectivity into the control plane in your AWS environment. You must create an AWS Endpoint to connect to this service in your Virtual Private Cloud (VPC), and enable private DNS resolution of the endpoint service hostname. With this in place, any traffic originating from your VPC to the control plane API or mesh ingress connects to a private IP address and does not traverse the public internet. Traffic is stateful, so there is no need to open a private link in the reverse direction for responses to Transmission Control Protocol (TCP) requests that originate from the customer VPC


# 7. Red Hat Ansible Automation Platform Service on AWS Private Link Connectivity
## 7.2. How AWS PrivateLink works
### 7.2.2. AWS PrivateLink connectivity out of the Ansible Automation Platform control plane




You can configure Ansible Automation Platform to use external resources such as source code repositories, container registries, and execution nodes. By default, the control plane connects to these resources over the public internet. However, if your resources are not publicly available, you can leverage AWS PrivateLink to securely access your private resources without traversing the public internet.

AWS PrivateLink connectivity allows the Ansible Automation Platform control plane to connect privately to your resources including, registries, repositories, and execution nodes. Traffic is stateful, eliminating the need to open a private link in the reverse direction for responses to Transmission Control Protocol (TCP) requests that originate from the control plane VPC.

To enable AWS PrivateLink connectivity from the control plane to your private resources, create one or more Endpoint Services in your VPC. Then reach out to Red Hat support to create the consuming Endpoints.

Important
When creating the Endpoint Service in your VPC, you must enable the **Private DNS** option. This ensures that the Ansible Automation Platform control plane can resolve and connect to your service using the specified domain over AWS PrivateLink. Private DNS enables DNS queries from Ansible Automation Platform resolve to the private IP addresses of the interface endpoint, facilitating secure and direct communication over PrivateLink.



Note
This document does not cover all steps required for PrivateLink connectivity. To complete PrivateLink connectivity, you must work with Red Hat through the Customer Support portal.




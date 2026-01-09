# 7. Red Hat Ansible Automation Platform Service on AWS Private Link Connectivity
## 7.1. Key benefits of private link connectivity




To ensure maximum network isolation and security, AWS PrivateLink connectivity establishes a private connection for the Ansible Automation Platform Service on AWS, which is essential because:

- It enables the Ansible Automation Platform Service on AWS control plane to connect to project and execution environment repositories hosted on private networks that are inaccessible from the public internet.
- It keeps automation mesh data within a private network rather than traversing the public internet.


Note
Automation mesh uses industry standard TLS encryption regardless of how automation mesh nodes are connected. Consider this traffic secured in the same manner as all TLS traffic.




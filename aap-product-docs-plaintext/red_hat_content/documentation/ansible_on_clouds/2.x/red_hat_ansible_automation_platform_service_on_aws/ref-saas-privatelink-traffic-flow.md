# 7. Red Hat Ansible Automation Platform Service on AWS Private Link Connectivity
## 7.3. AWS PrivateLink traffic flow summary

The following table summarizes the primary AWS components, critical settings, and corresponding automation mesh connectivity model for each AWS PrivateLink direction.

| Traffic flow  | Connectivity model | Direction                                                       | Primary component required                                     | Critical setting                                                                                                       |
| ------------- | ------------------ | --------------------------------------------------------------- | -------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| <br>  Ingress | <br>  PULL         | <br>  Customer VPC to Ansible Automation Platform control plane | <br>  AWS VPC Endpoint (Interface)                             | <br>  Enable Private DNS resolution and restrict the security group attached to your VPC Endpoint to HTTPS (port 443). |
| <br>  Egress  | <br>  PUSH         | <br>  Ansible Automation Platform control plane to customer VPC | <br>  AWS VPC Endpoint Service and Network Load Balancer (NLB) | <br>  Enable Private DNS on the Endpoint Service and implement split-horizon DNS.                                      |

Note

**PULL** and **PUSH** refer to the automation mesh connectivity models described in [Red Hat Ansible Automation Platform Service on AWS PULL and PUSH models](https://docs.redhat.com/en/documentation/ansible_on_clouds/2.x/html/red_hat_ansible_automation_platform_service_on_aws/saas-pull-push). Ingress PrivateLink supports the PULL model (UI/API and mesh-ingress access from your VPC). Egress PrivateLink supports the PUSH model (control plane access to private resources in your VPC, such as execution nodes, Git, and private automation hub).


# 2. Prerequisites for Installing Red Hat Ansible Automation Platform on Microsoft Azure
## 2.5. Network
### 2.5.2. AKS CIDR Blocks

You can configure the AKS network CIDR blocks. Traffic that originates from the AKS cluster appears to come from the range configured in AKS, not from the VNet.

When you are planning your AKS CIDR block configuration, bear the following in mind:

- Ensure that these network ranges do not overlap with any existing network range in your enterprise network.

- Do not use the following reserved network ranges:

| AKS Reserved CIDR Blocks |
| --- |
| <br>  169.254.0.0/16 |
| <br>  172.30.0.0/16 |
| <br>  172.31.0.0/16 |
| <br>  192.0.2.0/24 |
| <br>  172.17.0.1/26 |

You can configure the AKS network CIDR blocks in the `Configure AKS networks` area of the `networking` tab. Do not accept the default values suggested in the Azure user interface. Instead, use the CIDR blocks that you have planned. The settings have the following requirements:

| <br>  Network | <br>  Description | <br>  Requirements |
| --- | --- | --- |
| <br>  Service CIDR | <br>  A CIDR notation IP range from which to assign service cluster IPs. <br>  It must not overlap with any Subnet IP ranges. | <br>  Requires a /24 block at minimum. A larger block is not necessary. <br>  This CIDR block must not intersect with the CIDR of the Pod CIDR block. <br>  This CIDR block also must not intersect with the CIDR of the VNet CIDR block. |
| <br>  DNS Service IP | <br>  An IP address assigned to the Kubernetes DNS service. <br>  It must be within the Kubernetes service address range specified in `serviceCidr`. | <br>  Must be an IP address in the Service CIDR other than the first IP in that range. <br>  Red Hat recommends using the first `.10` IP address within the Service CIDR block. |
| <br>  Pod CIDR | <br>  A CIDR notation IP range from which to assign pod IPs when kubenet is used. | <br>  Requires a /19 or larger block. <br>  This CIDR block must not intersect with the CIDR of the Service CIDR block. |


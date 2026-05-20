# 7. Red Hat Ansible Automation Platform Service on AWS Private Link Connectivity
## 7.3. Inbound traffic control (IP restrictions)

Two distinct layers of traffic control are available depending on your connectivity method.

| Method | Scope | Managed by | Action required |
| --- | --- | --- | --- |
| <br>  Public internet access | <br>  Restricts access to the Ansible Automation Platform UI and API over the public internet. | <br>  Red Hat SRE | <br>  Open a **Support Ticket** requesting "**Traffic Control CIDR Allowlisting**." <br>  You must provide the specific **IP CIDR blocks** (for example, `192.0.2.0/24`) to be allowed. |
| <br>  PrivateLink access | <br>  Restricts access coming through your PrivateLink VPC Endpoint. | <br>  Customer | <br>  Configure the **AWS Security Group** attached to your **VPC Endpoint** to allow inbound **HTTPS (443)** traffic only from specific internal subnets or VPN CIDRs. |


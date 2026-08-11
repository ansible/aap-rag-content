# 7. Red Hat Ansible Automation Platform Service on AWS Private Link Connectivity
## 7.4. Inbound traffic control (IP restrictions)

Two distinct layers of traffic control are available depending on your connectivity method.

| Method                       | Scope                                                                                          | Managed by        | Action required                                                                                                                                                                         |
| ---------------------------- | ---------------------------------------------------------------------------------------------- | ----------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <br>  Public internet access | <br>  Restricts access to the Ansible Automation Platform UI and API over the public internet. | <br>  Red Hat SRE | <br>  Open a **Support Ticket** requesting "**Traffic Control CIDR Allowlisting**." <br>  You must provide the specific **IP CIDR blocks** (for example, `192.0.2.0/24`) to be allowed. |
| <br>  PrivateLink access     | <br>  Restricts access coming through your PrivateLink VPC Endpoint.                           | <br>  Customer    | <br>  Configure the **AWS Security Group** attached to your **VPC Endpoint** to allow inbound **HTTPS (443)** traffic only from specific internal subnets or VPN CIDRs.                 |

Note

Public internet access and PrivateLink access are independent layers that can coexist. Enabling PrivateLink does not automatically disable public internet access to the Ansible Automation Platform UI and API.

If you require absolute network isolation, you must explicitly request that Red Hat SRE disable public internet access entirely, or restrict public access to specific CIDR blocks. Submit this request as a separate [Customer support](https://access.redhat.com/support/cases/?extIdCarryOver=true&sc_cid=RHCTG0250000454096#/case/new/get-support?caseCreate=true) case alongside your PrivateLink initialization ticket.


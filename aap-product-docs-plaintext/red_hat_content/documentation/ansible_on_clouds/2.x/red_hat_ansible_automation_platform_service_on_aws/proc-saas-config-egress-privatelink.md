# 7. Red Hat Ansible Automation Platform Service on AWS Private Link Connectivity
## 7.4. Enabling AWS PrivateLink connectivity
### 7.4.2. Configuring AWS PrivateLink connectivity from Red Hat managed control plane to customer VPCs




This configuration allows the Ansible Automation Platform control plane to connect to your private resources, such as internal Git or private automation hub.

**Procedure**

1. Create an Endpoint Service in your VPC:


1. Confirm your private resource is behind an AWS Network Load Balancer (NLB).
1. Create an Endpoint Service in your AWS VPC that points to that NLB.

Important
You must select the service type that supports Interface endpoints and enable the Private DNS option.





1. To initiate control plane egress, you must submit a **separate**  [Customer support](https://access.redhat.com/support/cases/?extIdCarryOver=true&sc_cid=RHCTG0250000454096#/case/new/get-support?caseCreate=true) case using the **Egress PrivateLink request template** .
1. Red Hat uses the information provided to create an Interface Endpoint on their side. When Red Hat creates this endpoint, they select the category "Endpoint services that use NLBs and GWLBs" to connect to your service.
1. Your Internal Network or IT Team must configure the Internal DNS.
1. To ensure users route through the secure PrivateLink connection, you must request a Split-Horizon DNS configuration.
1. Copy the **Egress PrivateLink request template** , fill in your specific VPC Endpoint Service Name, and submit it to Red Hat.


**Egress PrivateLink request template**

```
Subject:
Egress PrivateLink Configuration for &lt;Instance ID&gt;

Body:
We need to enable Egress PrivateLink connectivity to allow the AAP control plane to access our internal private resources (for example, private automation hub, Git and so on).

Configuration details:
Our AWS Account ID: &lt;Your 12-digit AWS Account ID&gt;
Our Endpoint Service Name: &lt;for example, com.amazonaws.vpce.us-east-1.vpce-svc-xxxxxxxx&gt;
Service Regions/AZs: &lt;for example., us-east-1 / us-east-1a, us-east-1b&gt;

Action required:
Please confirm when Red Hat has initiated the connection request so we can approve it in our AWS Console.

Thank you.
```


<span id="idm140547383478672"></span>

# 7. Red Hat Ansible Automation Platform Service on AWS Private Link Connectivity
## 7.4. Enabling AWS PrivateLink connectivity
### 7.4.1. Configuring AWS PrivateLink connectivity from customer VPC to Red Hat managed control plane




This configuration allows your internal users and automation to access the Ansible Automation Platform UI and API over PrivateLink.

**Procedure**

1. To request Ingress PrivateLink submit a [Customer support](https://access.redhat.com/support/cases/?extIdCarryOver=true&sc_cid=RHCTG0250000454096#/case/new/get-support?caseCreate=true) case to Red Hat using the **Ingress AWS PrivateLink request template** step 2.
1. You must include your:


-  **AWS Account ID** .
-  **Region** .
-  **Deployment URL** .
- After Red Hat provides you with a VPC Endpoint Service Name, you must create a VPC Endpoint in your AWS account that points to the provided service name.

1. For your **Ingress AWS PrivateLink request template** :


- Select "Endpoint services that use NLBs and GWLBs".


- In the **Service name** field, paste the VPC Endpoint Service Name provided by Red Hat and clickVerify service.

- Complete the network and security group configuration as required by your organization.


```
Subject:        Request for Ingress PrivateLink Connection: &lt;Your Company Name&gt; - &lt;Deployment ID&gt;                Body:        Hello Red Hat Support,                We would like to enable Ingress PrivateLink connectivity for our AAP on AWS instance. This will allow our internal users and automation tools to access the AAP Control Plane (UI/API) securely from our VPC without traversing the public internet.                Deployment details:        AAP Deployment Name/ID: &lt;for example., ans-123456&gt;        AAP Deployment URL: &lt;for example, https://ans-123456.ansible.redhat.com&gt;        Our Network Information:        Our AWS Account ID: &lt;Your 12-digit AWS Account ID&gt;        Target Region: &lt;for example, us-east-1&gt;                Action required:        Please create the Endpoint Service configuration on the Control Plane side and provide us with the VPC Endpoint Service Name so we can create the interface endpoint in our VPC.                Thank you.
```






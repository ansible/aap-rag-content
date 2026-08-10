# 7. Red Hat Ansible Automation Platform Service on AWS Private Link Connectivity
## 7.5. Enabling AWS PrivateLink connectivity
### 7.5.1. Configuring AWS PrivateLink connectivity from customer VPC to Red Hat managed control plane

This configuration allows your internal users and automation to access the Ansible Automation Platform UI and API over PrivateLink.

**Procedure**

1. Submit the Ingress PrivateLink support request

Copy the following **Ingress AWS PrivateLink request template**, fill in your deployment details, and submit a [Customer support](https://access.redhat.com/support/cases/?extIdCarryOver=true&sc_cid=RHCTG0250000454096#/case/new/get-support?caseCreate=true) case to Red Hat.

You must include your: * **AWS Account ID** * **Region** * **Deployment URL**

+

```
Subject:
Request for Ingress PrivateLink Connection: <Your Company Name> - <Deployment ID>

Body:
Hello Red Hat Support,

We would like to enable Ingress PrivateLink connectivity for our AAP on AWS instance. This will allow our internal users and automation tools to access the AAP Control Plane (UI/API) securely from our VPC without traversing the public internet.

Deployment details:
AAP Deployment Name/ID: <for example., ans-123456>
AAP Deployment URL: <for example, https://ans-123456.ansible.redhat.com>
Our Network Information:
Our AWS Account ID: <Your 12-digit AWS Account ID>
Target Region: <for example, us-east-1>

Action required:
Please create the Endpoint Service configuration on the Control Plane side and provide us with the VPC Endpoint Service Name so we can create the interface endpoint in our VPC.

Thank you.
```

2. Create a VPC Endpoint after Red Hat Support responds with your Service Name

After Red Hat provides you with a VPC Endpoint Service Name, create a VPC Endpoint in your AWS account that points to the provided service name:

1. In the AWS console, navigate to VPC → Endpoints and click Create endpoint.
2. Select "Endpoint services that use NLBs and GWLBs".
3. In the **Service name** field, paste the VPC Endpoint Service Name provided by Red Hat and click Verify service.
4. Complete the network and security group configuration as required by your organization.


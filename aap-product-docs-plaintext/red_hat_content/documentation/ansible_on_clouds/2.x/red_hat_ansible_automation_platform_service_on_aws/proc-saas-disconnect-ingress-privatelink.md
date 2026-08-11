# 7. Red Hat Ansible Automation Platform Service on AWS Private Link Connectivity
## 7.6. Disconnecting and deleting AWS PrivateLink connectivity
### 7.6.1. Disconnecting Ingress AWS PrivateLink connectivity (PULL model)

This procedure removes Ingress PrivateLink connectivity used for the PULL model, including access to the Ansible Automation Platform UI, API, and mesh ingress from your VPC.

**Procedure**

1. Submit a [Customer support](https://access.redhat.com/support/cases/?extIdCarryOver=true&sc_cid=RHCTG0250000454096#/case/new/get-support?caseCreate=true) case to request Ingress PrivateLink disconnection. Include the following in your request:

- **AWS Account ID**
- **Region**
- **Deployment URL**
- **VPC Endpoint ID** (if known)

2. Wait for Red Hat to complete teardown on the control plane side and confirm that you can proceed.

3. After Red Hat confirms removal, delete the AWS VPC Endpoint (Interface) in your VPC that connects to the Ansible Automation Platform control plane.

4. If you configured a custom domain with PrivateLink, remove the Private DNS or split-horizon DNS records for the platform and mesh-ingress hostnames.

5. Update the security group attached to your VPC subnets or endpoints as required by your organization.

6. Verify connectivity:

- If public internet access to the deployment is still enabled, confirm that users and PULL model execution nodes can reach the UI, API, and mesh ingress over the public route before you decommission PrivateLink-only paths.
- If PrivateLink is your only access path, plan alternate connectivity before you delete the VPC Endpoint.

**Ingress PrivateLink disconnection request template**

+

```
Subject:
Request to Disconnect Ingress PrivateLink: <Your Company Name> - <Deployment ID>

Body:
Hello Red Hat Support,

We would like to disconnect Ingress PrivateLink connectivity for our AAP on AWS instance. This PrivateLink connection is used for PULL model access to the AAP Control Plane (UI/API and mesh ingress) from our VPC.

Deployment details:
AAP Deployment Name/ID: <for example, ans-123456>
AAP Deployment URL: <for example, https://ans-123456.ansible.redhat.com>

Our Network Information:
Our AWS Account ID: <Your 12-digit AWS Account ID>
Target Region: <for example, us-east-1>
VPC Endpoint ID: <for example, vpce-xxxxxxxxxxxxxxxxx>

Action required:
Please complete teardown on the control plane side and confirm when we can safely delete the VPC Endpoint in our AWS account.

Thank you.
```


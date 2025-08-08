# 5. Red Hat Ansible Automation Platform Service on AWS Service Definition
## 5.2. Control plane
### 5.2.10. Custom domain




Ansible Automation Platform control plane is accessible through its user interfaces, APIs, and mesh ingresses. While each service instance has an auto-generated Red Hat URL, you can set up a custom domain. This customization process varies based on whether you plan to use AWS PrivateLink or not.

To use custom domains, you must configure three DNS records according to your service’s connectivity model. These records will be explained in greater detail in the following sections. The conventions for these records are:

-  `    platform.&lt;optional_subdomain.<span class="emphasis"><em><span class="Role ARG Spec Role ARG Spec">exampledomain</span></em></span>.com&gt;`
-  `    mesh-ingress-0.&lt;optional_subdomain.<span class="emphasis"><em><span class="Role ARG Spec Role ARG Spec">exampledomain</span></em></span>.com&gt;`
-  `    mesh-ingress-1.&lt;optional_subdomain.<span class="emphasis"><em><span class="Role ARG Spec Role ARG Spec">exampledomain</span></em></span>.com&gt;`


You can create custom subdomains under the domain you own.

#### 5.2.10.1. Planning for your custom domain




To set up a custom domain for your deployment, you must complete several preparatory steps, including domain identification and TLS certificate creation. This procedure outlines the necessary planning activities to ensure a successful custom URL configuration with Red Hat SRE assistance.

**Prerequisites**

- Ensure that you have management over the domain or subdomain you intend to use in order to add multiple records.
- Ensure the DNS servers that you use to resolve the record must be accessible wherever you intend to use the domain.
- Ensure that you use the same domain for all URLs in the deployment (for example, use `    exampledomain.com` for custom URLs).


**Procedure**

1. Identify the domain or subdomain that you intend to use.
1. Create the TLS certificate.


1. To ensure the validity of a TLS certificate for a custom domain, you must confirm that the certificate is generated for the platform record and all mesh-ingress records are included in the Subject Alternative Name (SAN) parameter. Alternatively, you can opt to generate a wildcard certificate to cover the subdomains of your primary custom domain.

Important
TLS Certificate requirements for custom domains:


- Initial setup: When providing a new certificate, it must have an expiration date of at least one year or longer. This is a requirement for our certificate management process.
- Renewal: You are responsible for monitoring your certificate’s expiration. To ensure uninterrupted service, you must begin the support process to renew it at least 14 days before it expires.




1. Open a [support ticket](https://access.redhat.com/support/cases/#/case/new/get-support?caseCreate=true) with Red Hat requesting a custom URL configuration to your deployment and supply the following information:


- Company Name
- Deployment information (for example, `        cus-xxxx` )
- Custom domain (for example, `        <span class="emphasis"><em><span class="Role ARG Spec Role ARG Spec">exampledomain</span></em></span>.com` )

1. Allow the SRE team to apply the configuration to your deployment, verify the functionality, and collaborate with you on follow-up steps via the support ticket.
1. After your configuration is complete, apply the custom domain to your deployment.

Note
Your original mesh-ingresses will not be available; new ones using the custom domain are created instead.




1. Reconfigure your execution nodes if you configured them previously with the old domain.


#### 5.2.10.2. Setting up a custom domain without AWS PrivateLink




If you are not planning to connect to the Ansible Automation Platform UI or use automation mesh through AWS PrivateLink, complete the following steps to configure your DNS.

**Procedure**

1. Identify the canonical names of the load balancers of your deployment.

You can use a DNS lookup on the Red Hat-generated URL to identify the DNS names for both load balancers:


```
Shell        # Replace the URL with the "platform" URL of your deployment    dig platform.cus-&lt;id&gt;.aws.ansiblecloud.com
```


```
Shell        # Replace the URL with the "mesh-ingress" URL of your deployment    dig mesh-ingress-0.cus-&lt;id&gt;.aws.ansiblecloud.com
```


1. Create DNS CNAME records for your custom domain using the following hostnames pointing to the DNS names identified in the previous step:


- platform (for example, `        platform.<span class="emphasis"><em><span class="Role ARG Spec Role ARG Spec">exampledomain</span></em></span>.com` ) → `        cus-xxxxx-alb-11111111.us-east-1.elb.amazonaws.com`
- mesh-ingress-0 (for example, `        mesh-ingress-0.<span class="emphasis"><em><span class="Role ARG Spec Role ARG Spec">exampledomain</span></em></span>.com` ) → `        xxxxx.elb.us-east-1.amazonaws.com`
- mesh-ingress-1 (for example, `        mesh-ingress-1.<span class="emphasis"><em><span class="Role ARG Spec Role ARG Spec">exampledomain</span></em></span>.com` ) → `        xxxxx.elb.us-east-1.amazonaws.com`



#### 5.2.10.3. Setting up a custom domain with AWS PrivateLink




If you are planning to connect to the Ansible Automation Platform UI or use automation mesh through AWS PrivateLink, complete the following steps to configure your DNS.

**Procedure**

1. Retrieve the main DNS name of the Amazon Virtual Private Cloud (VPC) endpoint you created to connect to AWS PrivateLink endpoint service by perfoming the following steps:


1. Log in to the Amazon Web Services portal and selectVPC→Endpoints.
1. Click the **VPC** Endpoint for Red Hat Ansible Automation Platform Service on AWS.
1. Retrieve the **DNS names** in the Details tab.

There are a few entries. To find the correct DNS name, go to the **Details** tab and look for the entry that is not tied to a specific Availability Zone (AZ). For instance, choose `        vpce-xxxx-xxxx.vpce-svc-xxxx.us-east-1.vpce.amazonaws.com` rather than one that includes an AZ like `        us-east-1a` or `        us-east-1b` .

Alternatively, you can choose to use Amazon Web Services CLI to retrieve the DNS names of that endpoint by entering:


```
Shell        aws ec2 describe-vpc-endpoints --vpc-endpoint-ids vpce-xxxx --query 'VpcEndpoints[0].DnsEntries[*].DnsName'
```



1. After you have retrieved the DNS name, create the DNS CNAME records for your custom domain using the following hostnames pointing to the DNS name identified in the previous step:


1. platform (for example, `        platform.<span class="emphasis"><em><span class="Role ARG Spec Role ARG Spec">exampledomain</span></em></span>.com` ) → `        vpce-xxxx-xxxx.vpce-svc-xxxx.us-east-1.vpce.amazonaws.com`
1. mesh-ingress-0 (for example, `        mesh-ingress-0.<span class="emphasis"><em><span class="Role ARG Spec Role ARG Spec">exampledomain</span></em></span>.com` ) → `        vpce-xxxx-xxxx.vpce-svc-xxxx.us-east-1.vpce.amazonaws.com`
1. mesh-ingress-1 (for example, `        mesh-ingress-1.<span class="emphasis"><em><span class="Role ARG Spec Role ARG Spec">exampledomain</span></em></span>.com` ) → `        vpce-xxxx-xxxx.vpce-svc-xxxx.us-east-1.vpce.amazonaws.com`




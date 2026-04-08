# 5. Red Hat Ansible Automation Platform Service on AWS Service Definition
## 5.2. Control plane
### 5.2.11. Custom domain




Ansible Automation Platform control plane is accessible through its user interfaces, APIs, and mesh ingresses. While each service instance has an auto-generated Red Hat URL, you can set up a custom domain. This customization process varies based on whether you plan to use AWS PrivateLink or not.

To use custom domains, you must configure three DNS records according to your service’s connectivity model. These records will be explained in greater detail in the following sections. The conventions for these records are:

-  `    platform.&lt;optional_subdomain.<span class="emphasis"><em><span class="Role ARG Spec Role ARG Spec">exampledomain</span></em></span>.com&gt;`
-  `    mesh-ingress-0.&lt;optional_subdomain.<span class="emphasis"><em><span class="Role ARG Spec Role ARG Spec">exampledomain</span></em></span>.com&gt;`
-  `    mesh-ingress-1.&lt;optional_subdomain.<span class="emphasis"><em><span class="Role ARG Spec Role ARG Spec">exampledomain</span></em></span>.com&gt;`


You can create custom subdomains under the domain you own.

#### 5.2.11.1. Planning for your custom domain




You can configure a custom URL through Red Hat SRE assistance for your deployment. First, however, you must complete the preparatory steps, for domain identification and TLS certificate creation.

**Prerequisites**

- Ensure that you have management over the domain or subdomain you intend to use in order to add multiple records.
- Ensure the DNS servers that you use to resolve the record must be accessible wherever you intend to use the domain.
- Ensure that you use the same domain for all URLs in the deployment (for example, use `    exampledomain.com` for custom URLs).


**Procedure**

1. Identify the domain or subdomain to use.
1. Create the TLS certificate:


- Include all mesh-ingress records in the Subject Alternative Name (SAN) parameter.
- Alternatively, generate a wildcard certificate to cover subdomains (for example, `        *.exampledomain.com` ).

1. Bundle the certificate, private key, and any optional intermediary certificates into a zip.

Important
TLS Certificate requirements for custom domains:


-  **Private Key:** The private key must be unencrypted and cannot have a passphrase or be password protected.
-  **Expiration:** Initial certificates must be valid for at least one year.
-  **Renewal:** You must initiate a support ticket to renew the certificate at least 14 days before the expiration date. When renewing you must use one of the following formats for the certificate’s Subject Alternative Names (SANs):
-  **Explicit SANs:** List the required subdomains: `        platform` , `        mesh-ingress-0` , and `        mesh-ingress-1` . For example, if your domain is `        exampledomain.com` , include the following in the certificate’s SAN:


-  `            platform.exampledomain.com`
-  `            mesh-ingress-0.exampledomain.com`
-  `            mesh-ingress-1.exampledomain.com`
-  **Wildcard certificate:** Use a wildcard to cover all subdomains (for example, `            *.exampledomain.com` ).




1. Open a [support ticket](https://access.redhat.com/support/cases/#/case/new/get-support?caseCreate=true) with Red Hat requesting a custom URL configuration to your deployment and include the following information:


- Company Name
- Deployment information (for example, `        cus-xxxx` )
- Custom domain (for example, `        exampledomain.com` )
- Provide the zip file containing the certificates, or request a presigned URL for secure upload.

1. Allow the SRE team to apply the configuration to your deployment, verify the functionality, and collaborate with you on follow-up steps via the support ticket.
1. Update image URLs for **Execution Environments** and **Decision Environments** to point to the new platform domain address if images are sourced from the private automation hub on the same Ansible Automation Platform instance.
1. Reconfigure pull mode execution nodes if they were previously configured with the old domain:


1. Locate the `        group_vars/all.yml` file in the tar archive used to set up the execution node.
1. Modify the `        receptor_peers` address variable to point to the new mesh ingress node.
1. Rerun the `        install_receptor.yml` playbook.

Note
New mesh-ingresses using the custom domain replace the original ones.







#### 5.2.11.2. Setting up a custom domain without AWS PrivateLink




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



#### 5.2.11.3. Setting up a custom domain with AWS PrivateLink




If you are planning to connect to the Ansible Automation Platform UI or use automation mesh through AWS PrivateLink, complete the following steps to configure your DNS.

**Procedure**

1. Retrieve the main DNS name of the Amazon Virtual Private Cloud (VPC) endpoint you created to connect to AWS PrivateLink endpoint service by performing the following steps:


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




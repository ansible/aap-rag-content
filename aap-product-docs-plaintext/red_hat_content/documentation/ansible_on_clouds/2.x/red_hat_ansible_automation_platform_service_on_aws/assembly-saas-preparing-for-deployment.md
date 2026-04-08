# 5. Red Hat Ansible Automation Platform Service on AWS Service Definition
## 5.2. Control plane
### 5.2.1. Preparing for deployment




The following optional configurations include custom domains and AWS PrivateLink setup. You can implement these settings to meet your specific security and networking requirements.

#### 5.2.1.1. Prerequisites




Before initiating these configuration requests, ensure the following are available.

-  **Access:** You have access to Red Hat Customer Portal ( [Customer support](https://access.redhat.com/support/cases/?extIdCarryOver=true&sc_cid=RHCTG0250000454096#/case/new/get-support?caseCreate=true) ) and the AWS Console.
-  **Infrastructure:** You have an active Ansible Automation Platform Service on AWS deployment.
-  **Network:** You have an existing VPC with private subnets (for PrivateLink).
-  **DNS:** You have administrative access to your public or private DNS provider.


#### 5.2.1.2. Execution plane strategy




Red Hat strongly advises provisioning your own execution nodes and instance groups in your VPC.

-  **Cost Impact:** Workloads running on the control plane trigger auto-scaling of vCPUs, which are billed at a higher variable rate ($0.10/vCPU/hr). For more information see [Ansible Automation Platform Service on AWS: Infrastructure Metering Changes](https://access.redhat.com/articles/7133854) .
-  **Recommendation:** To maintain predictable costs and security isolation, use the control plane for management only and offload automation execution to your own EC2 instances.


#### 5.2.1.3. Configure AWS PrivateLink




AWS PrivateLink establishes secure connectivity between your VPC and the Red Hat managed control plane without traversing the public internet.

AWS PrivateLink connectivity is supported both into (ingress) and out of (egress) the Ansible Automation Platform control plane. Customers must work with the Red Hat SRE Team to set up the following AWS PrivateLink connectivity directions:

- From customer VPC to Red Hat managed control Plane
- From Red Hat managed control plane to customer VPC


To configure bi-directional connectivity, complete the following steps:

1. Submit [Customer support](https://access.redhat.com/support/cases/?extIdCarryOver=true&sc_cid=RHCTG0250000454096#/case/new/get-support?caseCreate=true) cases to Red Hat to begin this process.


1. A separate ticket must be created for ingress and egress

1. The Redhat SRE team will work together with the customer and enable AWS PrivateLink Connectivity via the support case.


To begin this process see [Enabling AWS PrivateLink connectivity](https://docs.redhat.com/en/documentation/ansible_on_clouds/2.x/html/red_hat_ansible_automation_platform_service_on_aws/saas-private-link#ref-saas-enabling-aws-privatelink) .

#### 5.2.1.4. Performance guidelines for Event-Driven Ansible on Ansible Automation Platform Service on AWS




Use this information to plan and configure [Event-Driven Ansible](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/using_automation_decisions/index) on Ansible Automation Platform Service on AWS.

All customer workloads differ, and performance results may vary. Red Hat recommends monitoring **Subscription Watch** for Ansible Automation Platform Service on AWS meters within Hybrid Cloud Console and creating cost alerts in AWS.

The following table reflects the observed performance and resource utilization for the tested configuration.

**Observed performance and resource utilization**

| Category | Metric | Value |
| --- | --- | --- |
| Tested configuration | Rulebook Activations | 5 |
| Events published per second | 120 |
| Actions per second | 20 |
| Derived metrics | Actions per activation (20 events/sec x 30 sec) | 600 |
| Total actions across all activations | 3,000 |
| Infrastructure | vCPUs | 12 |
| Observed performance | Total Events Sent | 3,000 |
| Job Events | 600 |
| Failed Iterations | 0 |
| Event Processing Time | 77.07 seconds |


Note
Performance metrics change as the control plane scales (up or down) based on the running workload.



#### 5.2.1.5. Configure a custom domain




Configure a custom domain, starting with generating a certificate and private key, submitting a support case for SRE configuration, and finalizing the setup with a required DNS update.

For help with this process see the [Custom domain](https://docs.redhat.com/en/documentation/ansible_on_clouds/2.x/html/red_hat_ansible_automation_platform_service_on_aws/saas-service-definition#con-saas-custom-domain) section.


# 5. Red Hat Ansible Automation Platform Service on AWS Service Definition
## 5.5. Multi-Region Active/Passive infrastructure
### 5.5.3. Customer notification and failover confirmation protocol

Failover to the secondary region does not occur automatically. To ensure the customer maintains full authority over their environment, the process requires customer approval.

#### 5.5.3.1. Notification timeline

If a critical failure event persists for at least 15 minutes, Red Hat initiates best-effort attempts to notify your designated deployment contacts by email or through the sales account teams. Ensure that your contact information is kept up to date by working with your account team, particularly if there are personnel changes within your organization.

#### 5.5.3.2. Request a regional failover

Although Red Hat attempts to notify the customer after the 15-minute threshold, the failover process does not begin until the customer opens a support case.

**Procedure**

1. Log in to the [Red Hat Customer Portal](https://access.redhat.com/support).

2. Open a support ticket requesting a regional failover to the secondary deployment footprint.

3. Ensure that you select **Red Hat Ansible Automation Platform On Clouds** as the product.

4. Use the following exact formatting for the support ticket subject and body to ensure rapid routing and execution by the Red Hat SRE team.

```
*SUBJECT*: Urgent: Request for Regional Failover Execution - MRBC

*Severity*: 1

*BODY*:

Hello SRE Team,

I am requesting the immediate execution of a regional failover for my managed Ansible Automation Platform environment from the primary deployment region to our designated secondary multi-region business continuity (MRBC) footprint.

--- TARGET ENVIRONMENT ---

- Company Name: [INSERT COMPANY NAME]

- Instance URL: [URL]
```

#### 5.5.3.3. Primary region retention

Until the failover request is received through the support ticket, the environment remains in the degraded primary region.

Important

During this retention window, where there is primary region degradation and no failover, the application and automation workloads in the environment will experience ongoing outages. Red Hat will not alter, terminate, or migrate the primary environment without your explicit written authorization.


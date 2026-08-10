# 5. Red Hat Ansible Automation Platform Service on AWS Service Definition
## 5.5. Multi-Region Active/Passive infrastructure
### 5.5.7. Scheduling failover tests

A customer can validate regional failover operations by scheduling a simulation once annually.

Important

To ensure platform stability and maintain operational availability, customers are restricted to scheduling a maximum of one failover test per calendar year.

#### 5.5.7.1. Initiate a Business Continuity test

Use the following procedure to initiate a Business Continuity test for your Red Hat Ansible Automation Platform service deployment.

**Procedure**

1. Open a standard support ticket through the Red Hat Customer Portal to coordinate the failover exercise with Red Hat.

2. Red Hat moves the environment to the secondary region only after receiving a customer’s explicit confirmation through the support ticket.


Note
During this window, the application and automation in the environment will experience expected outages.

3. Red Hat coordinates with you in the support ticket to confirm the failover was successful.

4. You must verify that the secondary environment is active and report back in the ticket when you are ready for the rollback.

5. Red Hat initiates the rollback to the primary region. After verifying with you that the environment is working as intended, Red Hat will close the support case.


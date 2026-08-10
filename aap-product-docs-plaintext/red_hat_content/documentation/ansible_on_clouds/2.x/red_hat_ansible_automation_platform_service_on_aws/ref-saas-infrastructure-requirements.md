# 5. Red Hat Ansible Automation Platform Service on AWS Service Definition
## 5.5. Multi-Region Active/Passive infrastructure
### 5.5.8. Infrastructure requirements

Multi-region active/passive deployment is a mandatory platform requirement for all customers running Ansible Automation Platform Service on AWS on plans above 50 nodes. It cannot be disabled or opted-out of.

#### 5.5.8.1. New customers

You must activate Multi-Region Business Continuity during the onboarding process.

- For all new deployments with more than 50 nodes created on or after the feature launch date, active/passive architecture is enabled by default. These environments automatically deploy with the infrastructure required to support regional failover.
- New deployments starting with exactly 50 nodes will default to a single-region architecture.
- Customers with a 50-node tier can move to a multi-region active passive architecture by submitting a support ticket.

#### 5.5.8.2. Existing customers

Existing customers must migrate their current infrastructure layout to the mandatory MRBC topology.

All customers with environments deployed prior to Aug 4, 2026 are on retired infrastructure that is deprecated as of Aug 4, 2026. This infrastructure shuts down on Aug 3, 2027. Existing customers must plan a migration of their current deployment to the new infrastructure on or before Aug 3, 2027

- You can request a migration at any time prior to Aug 3, 2027 to take advantage of the multi-region infrastructure.
- 50 node deployments that customers wish to keep on a single-region deployment must also migrate to the new infrastructure.
- 50 node deployment migrations will allow for selection of single region or multi-region during the migration.
- All deployments on tiers greater than 50 nodes will all be migrated to multi-region infrastructure.
- If an environment has not been migrated by Aug 3, 2027, Red Hat will automatically migrate the infrastructure to the mandatory active/passive topology.
- You must reconfigure custom DNS, AWS PrivateLink, and any other infrastructure-related configuration during the migrations.
- **Custom Domains**: If the customer has configured a custom (vanity) domain for their Ansible Automation Platform instance, they are required to perform manual DNS updates during a failover event.
- **The Impact**: Custom domain routing requires specific DNS configurations that do not automatically map to the secondary region infrastructure during a failover event.
- **Customer Action**: Customers must disclose their use of custom domains in their migration support ticket. During a failover event, customers are strictly responsible for updating their DNS CNAME records to route traffic to the secondary region.

**Procedure**

1. Log in to the Red Hat [Customer Portal](https://access.redhat.com/).

2. Open a support ticket requesting a regional failover to the secondary deployment footprint.

3. Ensure you have selected **Red Hat Ansible Automation Platform On Clouds** as the product.

4. Use the following formatting exactly for the support ticket subject and body to ensure rapid routing and execution by the Red Hat SRE team.

```
SUBJECT: Request for Migration to MRBC Infrastructure

Severity: 3
BODY:

Hello SRE Team,

I am requesting the migration of my existing managed Ansible Automation Platform environment to the MRBC infrastructure topology.

--- TARGET ENVIRONMENT ---
Instance/Cluster ID: [INSERT ID, e.g., cus-xxxx]
Instance URL: [URL]
```


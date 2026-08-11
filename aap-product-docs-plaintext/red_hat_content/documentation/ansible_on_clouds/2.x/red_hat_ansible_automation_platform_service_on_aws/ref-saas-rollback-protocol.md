# 5. Red Hat Ansible Automation Platform Service on AWS Service Definition
## 5.5. Multi-Region Active/Passive infrastructure
### 5.5.4. Rollback protocol

To minimize risk, returning to the primary region requires collaboration between the customer and the Red Hat SRE team.

#### 5.5.4.1. Return to the primary deployment footprint

The primary deployment footprint is the region where the customer’s Red Hat Ansible Automation Platform service is deployed and where the customer’s data is stored.

**Procedure**

1. Open a support ticket to request return to the primary region. Red Hat SRE will verify that the region is in a stable state and the service can be reverted back to the primary region.
2. Schedule an agreed-upon maintenance window to execute the rollback operation to mitigate any potential disruption to active automation workloads.
3. Allow the automated delta reconciliation process to synchronize and restore any platform content changes, job histories, or inventory modifications updated while running in the secondary region back to the primary environment before traffic is shifted.

#### 5.5.4.2. Network and DNS Routing

The platform uses automated networking mechanics to abstract failover shifts away from external calling systems.

- **Service endpoints and URLs**: The customer-facing Ansible Automation Platform endpoint URL does not change during or after a failover event. For deployments using standard ingress, you do not need to update bookmarks, API integrations, CI/CD pipelines, or automation mesh configurations. The URL used to access the primary region resolves smoothly to the secondary region after the cutover. AWS private link users should see [Ingress configuration with AWS PrivateLink](#proc-saas-standard-ingress-configuration "5.5.6.2.&nbsp;Configure ingress with AWS PrivateLink").
- **DNS-layer routing**: Traffic redirection from the primary region to the secondary region is handled natively at the DNS layer. When a failover is initiated, Red Hat-managed DNS records are updated so that the existing custom domain or auto-generated Red Hat URL resolves to the secondary region’s infrastructure footprint. This includes both default services URLs, and customer custom DNS records already configured with the primary region.


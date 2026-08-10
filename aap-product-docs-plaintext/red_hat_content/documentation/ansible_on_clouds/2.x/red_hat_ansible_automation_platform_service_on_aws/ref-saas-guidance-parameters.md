# 5. Red Hat Ansible Automation Platform Service on AWS Service Definition
## 5.5. Multi-Region Active/Passive infrastructure
### 5.5.1. Guidance parameters and service objectives

Ansible Automation Platform Service on AWS features an active-passive infrastructure topology designed to withstand long-term AWS regional outages. In the event of a critical disruption in a primary deployment region, traffic can be rerouted to a secondary regional pair to sustain business-critical operations.

- **Failover guidance window**: Regional failover is not automatic. The 15-minute downtime threshold serves solely as operational guidance for when Red Hat begins attempts to proactively communicate a primary region disruption to the impacted customer(s).
- **SLA**: The managed service SLA terms defined in [Red Hat Terms of Service Appendix 4](https://www.redhat.com/licenses/Appendix-4-Red-Hat-Online-Services-English-20250805.pdf) do not change with the addition of this capability. No guarantees are made regarding the speed of failover operations.


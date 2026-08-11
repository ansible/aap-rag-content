# 5. Red Hat Ansible Automation Platform Service on AWS Service Definition
## 5.5. Multi-Region Active/Passive infrastructure
### 5.5.9. Metering Implications of idle region

Red Hat Ansible Automation Platform Service on AWS uses a consumption-based metering model across the entire service. All active infrastructure components, including primary control planes and execution nodes, are metered at a variable rate based on vCPU utilization.

Maintaining a multi-region business continuity footprint involves an active-passive state layout. Understanding the distinction between active and idle components is necessary for evaluating your baseline infrastructure metering.

#### 5.5.9.1. What "idle" means in the secondary region

Ansible Automation Platform Service on AWS deployments use an active/passive warm standby state.

- 3 VM nodes run 24/7 to keep the Ansible Automation Platform pods healthy and ready to accept traffic instantly.
- The Ansible Automation Platform control plane operations remain running on the primary region until a failover is triggered, which then moves the workloads onto the infrastructure in the secondary region.

#### 5.5.9.2. Metering estimates

You can calculate total infrastructure cost. This can be done by multiplying your total metered vCPU hours by the variable infrastructure metering rate of $0.10 per vCPU hour.

| Metric                     | Primary AWS region | Secondary AWS region | Combined      |
| -------------------------- | ------------------ | -------------------- | ------------- |
| <br> **Hourly vCPU hours** | <br>  16           | <br>  12             | <br>  28      |
| <br> **Daily vCPU hours**  | <br>  384          | <br>  288            | <br>  672     |
| <br> **Annual vCPU hours** | <br>  140,160      | <br>  105,120        | <br>  245,280 |

Note

To increase security and reduce infrastructure costs, deploy all execution nodes within your infrastructure.

Important

If your instance is still using the legacy infrastructure metering unit of 1, migrating to the new multi-region infrastructure shape will convert the customer’s metering unit to a variable consumption-based rate of $0.10 per vCPU hour.


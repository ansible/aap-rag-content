# 5. Red Hat Ansible Automation Platform Service on AWS Service Definition
## 5.2. Control plane
### 5.2.7. Infrastructure metering for Ansible Automation Platform Service on AWS

Ansible Automation Platform Service on AWS uses two metering systems to calculate infrastructure usage and billing: control plane infrastructure metering and managed active node counting.

#### 5.2.7.1. Control plane infrastructure metering

The control plane infrastructure meter counts the peak simultaneously observed compute vCPUs used in the control plane per hour. The meter tracks the maximum vCPU usage during each hour, not continuous usage.

Ansible Automation Platform Service on AWS uses machine shapes with four vCPUs. As nodes are added and removed from the control plane cluster, the vCPU count changes in units of four.

#### 5.2.7.2. Base vCPU use by component configuration

The control plane cluster requires a minimum number of vCPUs based on which components you enable. The cluster may scale up to handle additional workload demands.

| <br>  Component enabled                                                             | <br>  Idle CPU count | <br>  Hourly price/unit | <br>  Hourly cost | <br>  Monthly cost | <br>  Annual Cost |
| ----------------------------------------------------------------------------------- | -------------------- | ----------------------- | ----------------- | ------------------ | ----------------- |
| <br>  Platform gateway, automation controller, automation hub                       | <br>  12             | <br>  $0.10             | <br>  $1.20       | <br>  $876.00      | <br>  $10,512.00  |
| <br>  Platform gateway, automation controller, automation hub, Event-Driven Ansible | <br>  16             | <br>  $0.10             | <br>  $1.60       | <br>  $1,168.00    | <br>  $14,016.00  |

Note

The cluster with Event-Driven Ansible enabled idles at 16 vCPUs, but may scale down to 12 vCPUs if the system workload is small. The cluster without Event-Driven Ansible idles at 12 vCPUs. Actual vCPU usage depends on your workload.

When you need to run Event-Driven Ansible, Red Hat Lightspeed, or control plane automation alongside core platform components, the variable metering model lets you pay only for the vCPUs your workload actually consumes, so you can enable additional capabilities without committing to a fixed infrastructure cost.

#### 5.2.7.3. Enable Event-Driven Ansible

When you want to enable Event-Driven Ansible on your Ansible Automation Platform Service on AWS deployment, contact Red Hat Support to request the change. Enabling Event-Driven Ansible increases the idle cluster baseline from 12 to 16 vCPUs. Allow for a brief service reconfiguration window when the change is applied.

#### 5.2.7.4. Workload impact on infrastructure metering

When you need to run automation workloads directly on the control plane, for example, to simplify your deployment or reduce operational overhead, the platform fully supports this configuration. If you want to optimize costs and strengthen security boundaries, you can configure an external execution plane to separate automation execution from platform management, which reduces control plane vCPU consumption and lowers your infrastructure metering charges.

Running automation workloads on the control plane increases vCPU usage. The infrastructure meter reflects the peak vCPU count observed during each hour as the cluster scales to meet workload demands.

#### 5.2.7.5. Monitor infrastructure use

Ansible Automation Platform Service on AWS reports platform metrics to Red Hat Hybrid Cloud Console. Use the Metrics Usage Reports to monitor infrastructure use and understand the impact of your workloads.

You can also create cost management alerts in AWS to monitor usage data for Ansible Automation Platform Service on AWS. Set appropriate cost boundaries to receive alerts for anomalies and expenditure thresholds. Ansible Automation Platform Service on AWS reports platform metrics to Red Hat Hybrid Cloud Console. Customers can reference usage metrics by logging in and navigating to <https://console.redhat.com>, then Subscription Services → Subscription Usage → Ansible

#### 5.2.7.6. Managed active node metering

A managed active node is a connection to a unique host per billing cycle. Ansible Automation Platform identifies each unique host based on the connection reference you use in your inventory or playbooks.

Multiple automation events against the same host count as one managed active node for the entire billing cycle. The billing cycle runs from the first day to the last day of each month.

#### 5.2.7.7. Unique host identification

Ansible Automation Platform determines unique hosts by the connection reference, which can be:

- Hostname or DNS record
- IP address
- Value in the `ansible_host` variable

Important

The same physical host referenced in multiple ways counts as multiple managed active nodes. For example, if you reference a single host as 10.0.0.0, vm, and vm.fully.qualified.domain in your inventory, Ansible Automation Platform counts three separate nodes.

#### 5.2.7.8. AWS infrastructure automation

When you automate AWS APIs or control planes using the amazon.aws collection, configure your playbooks to run from localhost. This configuration counts as only one managed active node per billing cycle, regardless of how many AWS resources you manage.

For example:

```
- name: Manage AWS EC2 instances
hosts: localhost
gather_facts: false
tasks:
- name: Create EC2 instance
amazon.aws.ec2_instance:
name: web-server
instance_type: t2.micro
state: present
```

In this example, all AWS automation tasks count as one managed active node because they run from localhost.

#### 5.2.7.9. Billing integration

Ansible Automation Platform Service on AWS integrates with AWS billing systems. Your infrastructure usage appears on your AWS bill with full cost visibility. A percentage of the cost counts toward your AWS spend agreements.

The AWS Marketplace displays two primary meters:

- **Control Plane Infrastructure and Service Fee Per Hour**: Charged at $0.10 per vCPU per hour based on peak hourly use.
- **Managed Active Nodes**: Charged per unique managed node per billing cycle

#### 5.2.7.10. Additional resources

- For details about monitoring platform metrics, customers should log in and navigate to <https://console.redhat.com>, then Subscription Services → Subscription Usage → Ansible
- For AWS cost management guidance, see the AWS Cost Management documentation. For AWS Marketplace details, see the Red Hat Ansible Automation Platform Service on AWS listing.


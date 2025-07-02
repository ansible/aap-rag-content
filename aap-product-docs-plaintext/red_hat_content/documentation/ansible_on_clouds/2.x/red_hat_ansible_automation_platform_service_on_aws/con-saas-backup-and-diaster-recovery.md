# 5. Red Hat Ansible Automation Platform Service on AWS Service Definition
## 5.2. Control plane
### 5.2.4. Backup and disaster recovery




Red Hat maintains daily database and file system snapshots in a separate region from each deployment.

| Component | Snapshot Frequency | Retention Policy |
| --- | --- | --- |
| Database | Daily | 7 days |
| File System | Daily | 7 days |


This recovery data is used if an AWS regional outage cannot be resolved in a reasonable time.

Customer data is replicated to a predefined secondary region based on the deployment region. The currently paired regions are:

| Primary Region | Business Continuity Region |
| --- | --- |
| us-east-1 | us-west-2 |
| us-east-2 | us-west-2 |
| us-west-2 | us-east-1 |
| eu-central-1 | eu-central-2 |
| eu-west-1 | eu-north-1 |
| eu-west-2 | eu-west-1 |
| ap-southeast-2 | ap-south-1 |
| ap-east-1 | ap-south-1 |
| ca-central-1 | us-east-2 |


To recover an Ansible Automation Platform deployment in a different AWS region, a customer must submit a request specifying their preferred deployment region from the available options. Red Hat evaluates the request and begins building an instance in that region. Data from the previous instance is recovered from the customer’s business continuity region. The customer is responsible for any necessary post-deployment network configuration to integrate the new instance into their environment.

Note
Backup data is not directly accessible to customers. The data is only used in the event of infrastructure failure, not customer configuration errors. Red Hat encourages using configuration-as-code practices to maintain a customer-hosted backup of your configuration.




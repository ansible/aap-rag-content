# 5. Red Hat Ansible Automation Platform Service on AWS Service Definition
## 5.2. Control plane
### 5.2.5. Backup and disaster recovery

Red Hat maintains daily database and file system snapshots in a separate region from each deployment.

| <br>  Component | <br>  Snapshot Frequency | <br>  Retention Policy |
| --- | --- | --- |
| <br>  Database | <br>  Daily | <br>  7 days |
| <br>  File System | <br>  Daily | <br>  7 days |

This recovery data is used if an AWS regional outage cannot be resolved in a reasonable time.

Customer data is replicated to a predefined secondary region based on the deployment region. The currently paired regions are:

| Primary Region | Business Continuity Region |
| --- | --- |
| <br>  af-south-1 (Cape Town) | <br>  ap-southeast-2 (Sydney) |
| <br>  ap-east-1 (Hong Kong) | <br>  ap-south-1 (Mumbai) |
| <br>  ap-northeast-1 (Tokyo) | <br>  ap-northeast-3 (Osaka) |
| <br>  ap-northeast-3 (Osaka) | <br>  ap-northeast-1 (Tokyo) |
| <br>  ap-southeast-2 (Sydney) | <br>  ap-south-1 (Mumbai) |
| <br>  ca-central-1 (Central Canada) | <br>  us-east-2 (Ohio) |
| <br>  ca-west-1 (Canada) | <br>  ca-central-1 (Central Canada) |
| <br>  eu-central-1 (Frankfurt) | <br>  eu-central-2 (Zurich) |
| <br>  eu-central-2 (Zurich) | <br>  eu-central-1 (Frankfurt) |
| <br>  eu-south-2 (Spain) | <br>  eu-west-3 (Paris) |
| <br>  eu-west-1 (Ireland) | <br>  eu-north-1 (Stockholm) |
| <br>  eu-west-2 (London) | <br>  eu-west-1 (Ireland) |
| <br>  eu-west-3 (Paris) | <br>  eu-south-2 (Spain) |
| <br>  sa-east-1 (São Paulo) | <br>  us-east-1 (N. Virginia) |
| <br>  us-east-1 (N. Virginia) | <br>  us-west-2 (Oregon) |
| <br>  us-east-2 (Ohio) | <br>  us-west-2 (Oregon) |
| <br>  us-west-2 (Oregon) | <br>  us-east-1 (N. Virginia) |

To recover an Ansible Automation Platform deployment in a different AWS region, a customer must submit a request specifying their preferred deployment region from the available options. Red Hat evaluates the request and begins building an instance in that region. Data from the previous instance is recovered from the customer’s business continuity region. The customer is responsible for any necessary post-deployment network configuration to integrate the new instance into their environment.

Note

Backup data is not directly accessible to customers. The data is only used in the event of infrastructure failure, not customer configuration errors. Red Hat encourages using configuration-as-code practices to maintain a customer-hosted backup of your configuration.


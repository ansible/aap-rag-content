# 4. Operator topologies
## 4.2. Operator enterprise topology
### 4.2.2. Tested system configurations




Red Hat has tested the following configurations to install and run Red Hat Ansible Automation Platform:


<span id="idm139891623160960"></span>
**Table 4.5. Tested system configurations**

| Type | Description |
| --- | --- |
| Subscription | Valid Red Hat Ansible Automation Platform subscription |
| Operating system | Red Hat Enterprise Linux 9.2 or later minor versions of Red Hat Enterprise Linux 9 |
| CPU architecture | x86_64, AArch64, s390x (IBM Z), ppc64le (IBM Power) |
| Red Hat OpenShift | - Red Hat OpenShift on AWS Hosted Control Planes 4.15.16


- 2 worker nodes in different availability zones (AZs) at t3.xlarge |
| Ansible-core | Ansible-core version 2.16 or later |
| Browser | A currently supported version of Mozilla Firefox or Google Chrome. |
| AWS RDS PostgreSQL service | - engine: "postgres"
- engine_version: 15"
- parameter_group_name: "default.postgres15"
- allocated_storage: 20
- max_allocated_storage: 1000
- storage_type: "gp2"
- storage_encrypted: true
- instance_class: "db.t4g.small"
- multi_az: true
- backup_retention_period: 5
- database: must have ICU support |
| AWS Memcached Service | - engine: "redis"
- engine_version: "6.2"
- auto_minor_version_upgrade: "false"
- node_type: "cache.t3.micro"
- parameter_group_name: "default.redis6.x.cluster.on"
- transit_encryption_enabled: "true"
- num_node_groups: 2
- replicas_per_node_group: 1
- automatic_failover_enabled: true |
| s3 storage | HTTPS only accessible through AWS Role assigned to automation hub SA at runtime by using AWS Pod Identity |





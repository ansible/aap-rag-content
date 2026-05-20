# 3. Operator topologies
## 3.2. Operator enterprise topology
### 3.2.2. Tested system configurations

Red Hat has tested these configurations to install and run Red Hat Ansible Automation Platform:

**Table 3.5. Tested system configurations**

| Type | Description |
| --- | --- |
| <br>  Subscription | <br>  Valid Red Hat Ansible Automation Platform subscription |
| <br>  Red Hat OpenShift | <br>       Red Hat OpenShift on AWS Hosted Control Planes 4.15.16    <br>    2 worker nodes in different availability zones (AZs) at t3.xlarge |
| <br>  Ansible-core | <br>  Ansible-core version 2.16 or later |
| <br>  Browser | <br>  A currently supported version of Mozilla Firefox or Google Chrome. |
| <br>  AWS RDS PostgreSQL service | <br>  engine: "postgres"   engine_version: 15"   parameter_group_name: "default.postgres15"   allocated_storage: 20   max_allocated_storage: 1000   storage_type: "gp2"   storage_encrypted: true   instance_class: "db.t4g.small"   multi_az: true   backup_retention_period: 5   database: must have International Components for Unicode (ICU) support       Minimum external database requirements   <br>  The external database must meet these minimum requirements:    <br>  4 vCPUs   16 GB RAM `max_connections`: 1024 (minimum). You might need more connections when scaling replicas.   200 GB storage on a volume capable of at least 3000 IOPS <br>  Database storage consumption depends on your workload, including job frequency, playbook task count, output verbosity, and the number of managed hosts per job. Start with a 200 GB baseline and monitor actual usage after deployment. Configure automated cleanup jobs to prevent unbounded database growth. <br>  These requirements ensure adequate database performance for the enterprise topology workload profile. |
| <br>  AWS Memcached Service | <br>  engine: "redis"   engine_version: "6.2"   auto_minor_version_upgrade: "false"   node_type: "cache.t3.micro"   parameter_group_name: "default.redis6.x.cluster.on"   transit_encryption_enabled: "true"   num_node_groups: 2   replicas_per_node_group: 1   automatic_failover_enabled: true |
| <br>  s3 storage | <br>  HTTPS only accessible through AWS Role assigned to automation hub SA at runtime by using AWS Pod Identity |
| <br>  IP version | <br>  IPv4, IPv6 (single-stack and dual-stack) |


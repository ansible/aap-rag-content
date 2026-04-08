# 2. Scaling the tested deployment models
## 2.1. Vertical scaling for performance
### 2.1.2. Drawbacks and other considerations for vertical scaling




- Extensive testing required: The installation program attempts to tune application and system configurations to use additional resources, but not all components of the application automatically scale in relation to machine size. Manually tuning each variable requires extensive testing. For this reason, after an instance size has been verified for an environment, horizontal scaling by adding more instances of the same size is recommended.
- Application-level limitations: For VM-based installation or Containerized deployments, instances with more than 64 CPU cores and 128 GB of RAM might not scale linearly due to system and application-level limits.
- Resource overcommit: Overcommitting virtual machine resources (for example, allocating more virtual CPU/RAM to guests than is physically available on the host) leads to unpredictable performance.
- CPU throttling: In OpenShift Container Platform, setting a CPU `    limit` without an equivalent `    request` can lead to CPU throttling, even if the node has spare CPU capacity. This throttling negatively impacts API latency.


- To mitigate this, always set CPU `        requests` equal to CPU `        limits` .
- Monitor CPU throttling using the `        container_cpu_cfs_throttled_seconds_total` metric.

- Database limitations: Scaling the application increases the maximum potential number of database connections from worker processes and the overall memory, I/O, and CPU utilization of the PostgreSQL instance. As you scale past the tested deployment models, deploy your separate Postgres instances per component (platform gateway, Event-Driven Ansible, automation controller, automation hub).



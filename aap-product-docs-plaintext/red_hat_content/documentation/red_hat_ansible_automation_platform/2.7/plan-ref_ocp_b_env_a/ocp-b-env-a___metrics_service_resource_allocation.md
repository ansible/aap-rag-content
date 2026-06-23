# Operator enterprise topology
## Metrics service resource allocation

Note:

Resource allocation can be configured in the AnsibleAutomationPlatform custom resource. If using external databases, configure database secrets before setting resource allocation.

In enterprise topology, metrics service runs as 3 pods with the following resource recommendations:

*Table 4. Metrics service resource allocation*

| Pod               | CPU Request | Memory Request | CPU Limit | Memory Limit | Replicas           |
| ----------------- | ----------- | -------------- | --------- | ------------ | ------------------ |
| metrics-web       | 500m        | 2 Gi           | 1000m     | 4 Gi         | 1-2                |
| metrics-tasks     | 500m        | 2 Gi           | 1000m     | 4 Gi         | 1                  |
| metrics-scheduler | 500m        | 2 Gi           | 1000m     | 4 Gi         | 1 (must not scale) |


**Scaling considerations:**

- **metrics-web pod:** Can be scaled to 2 replicas for high availability and load distribution
- **metrics-tasks pod:** Can not be scaled past 1 replica
- **metrics-scheduler pod:** Must remain at 1 replica to prevent duplicate scheduled tasks


Configure pod resource requests and limits in the AnsibleAutomationPlatform CR:

```
spec:
metrics:
disabled: false
web:
replicas: 2
resource_requirements:
requests:
cpu: 500m
memory: 2Gi
limits:
cpu: 1000m
memory: 4Gi
task:
replicas: 2
resource_requirements:
requests:
cpu: 500m
memory: 2Gi
limits:
cpu: 1000m
memory: 4Gi
scheduler:
replicas: 1  # Must be 1
resource_requirements:
requests:
cpu: 100m
memory: 512Mi
limits:
cpu: 200m
memory: 1Gi
```


Note:

For enterprise deployments, configure pod anti-affinity to spread metrics service pods across different worker nodes:

```
spec:
metrics:
web:
topology_spread_constraints:
- maxSkew: 1
topologyKey: kubernetes.io/hostname
whenUnsatisfiable: PreferNoSchedule
```


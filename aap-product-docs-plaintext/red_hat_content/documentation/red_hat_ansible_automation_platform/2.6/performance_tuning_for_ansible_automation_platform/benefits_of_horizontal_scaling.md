# 2. Scaling the tested deployment models
## 2.2. Horizontal scaling for performance
### 2.2.1. Benefits of horizontal scaling




- Improved availability: Distributes load across more instances to reduce the impact of a single slow or failing node.
- Redundancy: Provides extra capacity, allowing individual service nodes to recover or cool-off without impacting overall availability.
- Increased authentication capacity: Each platform gateway pod includes its own authentication service, so scaling the platform gateway directly increases the platform’s authentication throughput.
- Repeatable scaling procedure: After the instance size and configuration are verified for your environment, deploy identical instances to scale.



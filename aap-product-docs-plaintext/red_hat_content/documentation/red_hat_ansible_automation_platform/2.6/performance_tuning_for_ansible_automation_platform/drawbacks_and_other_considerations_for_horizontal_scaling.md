# 2. Scaling the tested deployment models
## 2.2. Horizontal scaling for performance
### 2.2.2. Drawbacks and other considerations for horizontal scaling




- Database limitations: Scaling the application increases the maximum potential number of database connections from worker processes, and the overall memory, I/O, and CPU utilization of the PostgreSQL instance. As you scale past the tested deployment models, deploy your separate Postgres instances per component (platform gateway, Event-Driven Ansible, automation controller, automation hub).
- Health Check Overhead: In a mesh architecture, each Envoy proxy sends health checks to every other cluster member. Horizontal scaling increases this baseline traffic, adding to system usage.



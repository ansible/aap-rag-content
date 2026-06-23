# Horizontally scale tested deployment models to improve performance
## Drawbacks and other considerations for horizontal scaling

- Database limitations: Scaling the application increases the maximum potential number of database connections from worker processes. This also increases the overall memory, I/O, and CPU utilization of the PostgreSQL instance. When you scale past the tested deployment models, deploy separate PostgreSQL instances per component (platform gateway, Event-Driven Ansible, automation controller, automation hub).
- Health Check Overhead: In a mesh architecture, each Envoy proxy sends health checks to every other cluster member. Horizontal scaling increases this baseline traffic, adding to system usage.

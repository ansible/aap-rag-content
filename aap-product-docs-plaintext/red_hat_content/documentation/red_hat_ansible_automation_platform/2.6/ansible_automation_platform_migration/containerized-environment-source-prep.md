# 6. Source environment
## 6.2. Container-based Ansible Automation Platform
### 6.2.1. Preparing and assessing the source environment

Document your current containerized deployment configuration, topology, and components to create a comprehensive reference for migration.

**Procedure**

1. Document the full topology of your current containerized deployment:


1. Map out all servers, nodes, and their roles (for example control nodes, execution nodes, database servers).
2. Note the hostname, IP address, and function of each server in your deployment.
3. Document the network configuration between components.

2. Ansible Automation Platform version information:


1. Record the exact Ansible Automation Platform version (X.Y) currently deployed.

3. Document the specific version of each component:


1. Automation controller version
2. Automation hub version
3. Platform gateway version

4. Database configuration:


1. Database names for each component
2. Database users and roles
3. Connection parameters and authentication methods
4. Any custom PostgreSQL configurations or optimizations

5. Identify all custom configurations and settings

6. Document container resource allocations and volumes


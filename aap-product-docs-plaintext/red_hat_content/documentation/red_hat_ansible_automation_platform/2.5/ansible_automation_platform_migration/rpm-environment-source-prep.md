# 6. Source environment
## 6.1. RPM-based Ansible Automation Platform
### 6.1.1. Preparing and assessing the source environment




Before beginning your migration, document your current RPM deployment to use as a reference throughout the migration process and when configuring your target environment.

**Procedure**

1. Document the full topology of your current RPM deployment:


1. Map out all servers, nodes, and their roles (for example control nodes, execution nodes, database servers).
1. Note the hostname, IP address, and function of each server in your deployment.
1. Document the network configuration between components.

1. Ansible Automation Platform version information:


1. Record the exact Ansible Automation Platform version (X.Y) currently deployed.

1. Document the specific version of each component:


1. Automation controller version
1. Automation hub version
1. Platform gateway version

1. Database configuration:


1. Database names for each component
1. Database users and roles
1. Connection parameters and authentication methods
1. Any custom PostgreSQL configurations or optimizations




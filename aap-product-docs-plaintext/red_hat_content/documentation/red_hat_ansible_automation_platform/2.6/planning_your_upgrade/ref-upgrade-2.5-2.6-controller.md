# 5. Identity access management data movement
## 5.2. Upgrades from Ansible Automation Platform 2.5 to 2.6
### 5.2.1. Automation controller




Customers upgrading from 2.5 to 2.6 must also begin moving away from using nested teams in automation controller APIs, as future releases will disable direct access to service APIs. After the upgrade, user data is synchronized between automation controller and the platform-wide authentication gateway.

Automation controller users, teams, roles, and organizations should become platform entities upon upgrade without the need to run additional "merge" processes. Customers that first upgraded from 2.4 to 2.5 will have teams that existed in 2.4 merged into platform gateway when they upgrade from 2.5 to 2.6.

Roles should apply the permission model for non-admin access to execution, content, and event services.


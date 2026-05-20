# 9. Patch releases
## 9.2. Ansible Automation Platform patch release March 25, 2026
### 9.2.4. Enhancements

#### 9.2.4.1. Ansible Automation Platform

- This update extends audit logging for identity lifecycle operations in the gateway by recording creation, modification, and deletion of users, teams, and organizations. AAP-66919
- This update adds audit logging for dynamic preference changes so that updates to registered preferences and settings are tracked over time. AAP-66800
- This update refines the login experience by removing the “show password” eye icon so that the password field remains masked during entry. AAP-67230
- This update improves diagnostics for connectivity issues with automation controller by enhancing logging behind the “Error connecting to Controller API” banner. AAP-64146

#### 9.2.4.2. Container-based installer Ansible Automation Platform

- This update improves compatibility of the containerized installer after the Django 5.2 upgrade, preventing controller install failures caused by changes in Django behavior and output. AAP-68587
- This update keeps TLS configuration accurate by ensuring the gateway certificate is regenerated when certificate data changes so that gateway_main_url and related fields are updated. AAP-66579
- This update improves observability for direct component access in containerized deployments by adding nginx log markers for controller, hub, and Event-Driven Ansible in the containerized installer. AAP-66106

#### 9.2.4.3. Automation controller

- This update increases observability for direct API access to automation controller by adding nginx log markers for requests containing X-Trusted-Proxy and X-DAB-JW-TOKEN headers. AAP-66102
- This update aligns automation controller with the supported framework baseline by upgrading its Django dependency to version 5.2 LTS. AAP-59873

#### 9.2.4.4. Django-ansible-base

- This update extends audit logging coverage by adding audit entries for user and team role assignment changes, improving visibility into permission updates. AAP-67042

#### 9.2.4.5. Event-Driven Ansible

- This update improves observability for API traffic to Event-Driven Ansible by adding nginx log markers for direct API access. AAP-66105

#### 9.2.4.6. Automation hub

- This update improves the robustness of the automation hub container registry by setting gunicorn and proxy timeouts to better handle varied workloads and network conditions. AAP-67759
- This update enhances logging parity across services by adding nginx log markers for direct API access to Automation hub so that traffic bypassing the gateway can be detected. AAP-66104
- This update prepares for future token management changes by adding a deprecation warning for the `ah_token` module in the ansible.hub collection on Ansible Automation Platform 2.6 (Hub 4.11) behind AAP gateway. AAP-65109
- This update modernizes automation hub by upgrading its Django dependency to version 5.2 LTS. AAP-60388


# 10. Patch releases
## 10.19. Ansible Automation Platform patch release January 15, 2025
### 10.19.1. Enhancements




#### 10.19.1.1. Ansible Automation Platform




- With this update, the `    ansible.controller` collection has been updated to 4.6.6.(AAP-38443)
- Enhanced the **status API** , `    /api/gateway/v1/status/` , from the **services** property within the JSON to an array. Consumers of this API can still request the previous format with a URL query parameter `    service_keys=true` .(AAP-37903)


#### 10.19.1.2. Ansible Automation Platform Operator




- Added the ability to configure `    topology_spread_constraints, `node_selector, and `tolerations` for gateway deployments. (AAP-37193)


#### 10.19.1.3. Container-based Ansible Automation Platform




- TLS certificate and key files are now validated during the preflight role execution.


- If the TLS certificate file is provided then the TLS key file must be provided.
- If the TLS key file is provided then the TLS certificate file must be provided.
- Both TLS certificate and key modulus should match.(AAP-37845)




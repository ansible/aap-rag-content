# 6. Configuring Ansible Automation Platform
## 6.3. Understanding the platform gateway OpenAPI specification




Platform gateway serves as the single entry point for Ansible Automation Platform, unifying the user interface and routing all API traffic to services such as automation controller, Event-Driven Ansible, and automation hub.

The OpenAPI specification provides a standardized, machine-readable definition of the unified API endpoints available through platform gateway. It is essential for external developers and automation engineers building reliable custom integrations.

**Key roles of the specification**

The OpenAPI specification ensures successful integration by fulfilling the following roles:

-  **Enables custom integrations** : Developers use the specification to understand endpoint structures, required parameters, and response schemas, which is needed for building custom applications and third-party tools.
-  **Ensures API longevity** : Integration with the platform gateway API future-proofs custom applications against disruptions that might occur when legacy, direct-access component APIs are retired.
-  **Defines core functions** : The specification details endpoints that support fundamental operational and administrative functions, including:


- Platform health, such as `        /api/gateway/v1/status/` .
- Activity monitoring, such as `        /api/gateway/v1/activitystream/` .
- Configuration management, such as authentication configuration and role-based access control assignments.




# API changes for platform gateway

Ansible Automation Platform uses a platform gateway that provides centralized API access to all services. While APIs for automation controller, automation hub, and Event-Driven Ansible remain accessible directly for backward compatibility, this direct access will be removed in a future release.

These changes impact your organization if you have API calls implemented directly with automation controller or private automation hub, or if you are integrating directly with automation controller or private automation hub hosts. You must migrate these integrations to the API endpoints exposed through the platform gateway to ensure they are not disrupted when direct service API access is removed in a future Ansible Automation Platform release.

For detailed API reference information, see the following sources:

- For platform gateway APIs, see the browsable API at `https://<gateway server name>/api/gateway/v1`.
- For automation controller APIs, see the browsable API at `https://<gateway server name>/api/controller/v2`.
- For automation hub APIs, see **Automation Hub API** in *API Catalog and Documentation*.
- For Event-Driven Ansible APIs, see the browsable API at `https://<gateway server name>/api/eda/v1`.

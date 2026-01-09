# 2. New features and enhancements
## 2.11. Enhancements




- Added the ability to provide `    mounts.conf` or copy from a local or remote source when installing Podman. (AAP-16214)
- Updated the inventory file to include the SSL key and certificate parameters for provided SSL web certificates. (AAP-13728)
- Added an Ansible Automation Platform operator-version label on Kubernetes resources created by the operator. (AAP-31058)
- Added installation variables to support PostgreSQL certificate authentication for user-provided databases. (AAP-1095)
- Updated NGINX to version 1.22. (AAP-15128)
- Added a new configuration endpoint for the REST API. (AAP-13639)
- Allowed adjustment of **RuntimeDirectorySize** for Podman environments at the time of installation. (AAP-11597)
- Added support for the **SAFE_PLUGINS_FOR_PORT_FORWARD** setting for **eda-server** to the installation program. (AAP-21503)
- Aligned inventory content to tested topologies and added comments for easier access to groups and variables when custom configurations are required. (AAP-30242)
- The variable ** `    automationedacontroller_allowed_hostnames` ** is no longer needed and is no longer supported for Event-Driven Ansible installations. (AAP-24421)
- The **eda-server** now opens the ports for a rulebook with a source plugin that requires inbound connections only if that plugin is allowed in the settings. (AAP-17416)
- The Event-Driven Ansible settings are now moved to a dedicated YAML file. (AAP-13276)
- Starting with Ansible Automation Platform 2.5, customers using the controller collection ( `    ansible.controller` ) have the platform collection ( `    ansible.platform` ) as a single point of entry, and must use the platform collection to seed organizations, users, and teams. (AAP-31517)
- Users are opted in for Automation Analytics by default when activating automation controller on first time log in. (ANSTRAT-875)



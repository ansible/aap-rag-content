# 5. Using custom actions and UI components in Backstage Software Templates
## 5.2. Ansible backstage plugins




The portal’s capabilities are delivered through **Ansible Backstage Plugins** that extend Red Hat Developer Hub functionality; the base Red Hat Developer Hub image is not customized. These plugins provide additional Backstage actions and filters that you use to create custom software templates.

| Plugin | Functionality |
| --- | --- |
| auth-backend-module-rhaap-provider | Provides OAuth 2.0 authentication with Ansible Automation Platform. |
| catalog-backend-module-rhaap | Synchronizes Ansible Automation Platform job templates as Backstage Software Templates. |
| scaffolder-backend-module-backstage-rhaap | Provides the `rhaap:launch-job-template` action. |
| backstage-rhaap-common | Contains shared libraries and utilities for Ansible Automation Platform integration. |
| self-service | Provides the user interface for all listed functionality. |



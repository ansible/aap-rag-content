# 5. Using custom actions and UI components in Backstage Software Templates
## 5.2. Ansible backstage plugins

The portal’s capabilities are delivered through **Ansible Backstage Plugins** that extend Red Hat Developer Hub functionality; the base Red Hat Developer Hub image is not customized. These plugins provide additional Backstage actions and filters that you use to create custom software templates.

| Plugin | Functionality |
| --- | --- |
| <br>  auth-backend-module-rhaap-provider | <br>  Provides OAuth 2.0 authentication with Ansible Automation Platform. |
| <br>  catalog-backend-module-rhaap | <br>  Synchronizes Ansible Automation Platform job templates as Backstage Software Templates. |
| <br>  scaffolder-backend-module-backstage-rhaap | <br>  Provides the `rhaap:launch-job-template` action. |
| <br>  backstage-rhaap-common | <br>  Contains shared libraries and utilities for Ansible Automation Platform integration. |
| <br>  self-service | <br>  Provides the user interface for all listed functionality. |


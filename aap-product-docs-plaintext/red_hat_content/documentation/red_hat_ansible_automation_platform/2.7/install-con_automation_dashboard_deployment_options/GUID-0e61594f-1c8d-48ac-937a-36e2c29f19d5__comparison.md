# Automation dashboard deployment options
## Comparison

*Table 1. Integrated vs. standalone automation dashboard*

| Consideration                                    | Integrated automation dashboard                                 | Standalone utility (RHEL only)                                                                         |
| ------------------------------------------------ | --------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------ |
| Where it is deployed                             | Part of the platform installation                               | Installed separately on RHEL                                                                           |
| Supported install methods                        | Containerized (RHEL) or Operator (OpenShift)                    | RHEL only                                                                                              |
| Lifecycle management                             | Upgraded and maintained with the platform                       | Installed, configured, upgraded, and uninstalled independently                                         |
| Data source                                      | The Ansible Automation Platform deployment it is installed with | One or more clusters or Ansible Automation Platform deployments, connected using cluster access tokens |
| Ansible Automation Platform version availability | Ansible Automation Platform 2.7 onwards                         | Utility can connect to Ansible Automation Platform versions 2.4 onwards                                |


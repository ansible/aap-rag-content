# Understand metrics service architecture
## Deployment method comparison

Metrics service supports two deployment methods with different configuration complexity and automation levels:

| Aspect                       | Containerized Installer                                                      | Operator (OpenShift)                                                                       |
| ---------------------------- | ---------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------ |
| **Deployment method**        | Ansible role (`automationmetrics`) in containerized installation program     | Kubernetes operator (`automation-metrics-operator`) managed by AAP gateway operator        |
| **Configuration complexity** | Manual: requires inventory file edits, database passwords, network variables | Automatic: single CR field (`metrics.disabled: false`)                                     |
| **Database provisioning**    | Administrator provisions databases and configures credentials in inventory   | Operator automatically provisions databases and manages credentials via Kubernetes secrets |
| **Container management**     | Podman with systemd user-scope units                                         | Kubernetes deployments managed by operator                                                 |
| **Network configuration**    | Manual firewall rules, port configuration in inventory                       | Automatic Kubernetes services and Envoy routing through gateway                            |
| **OAuth integration**        | Manual configuration if needed                                               | Automatic integration with platform gateway OAuth                                          |
| **Upgrades**                 | Re-run installer with updated inventory                                      | Operator handles upgrades automatically via CR updates                                     |
| **Backup/restore**           | Manual playbook execution                                                    | Operator-managed backup/restore via AutomationMetricsBackup CR (when available)            |

Tip:

For OpenShift deployments, use the operator method for simplified configuration and automatic lifecycle management. For RHEL-based containerized deployments, use the containerized installer method.


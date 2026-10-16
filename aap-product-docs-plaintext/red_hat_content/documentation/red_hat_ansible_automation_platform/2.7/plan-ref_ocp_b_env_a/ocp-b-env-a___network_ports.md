# Operator enterprise topology
## Network ports

Red Hat Ansible Automation Platform uses several ports to communicate with its services. These ports must be open and available for Red Hat Ansible Automation Platform to work. Ensure that these ports are available and are not blocked by a firewall.

*Table 5. Network ports and protocols*

| Port number | Protocol   | Service        | Source                               | Destination                                                                                 |
| ----------- | ---------- | -------------- | ------------------------------------ | ------------------------------------------------------------------------------------------- |
| 80/443      | HTTP/HTTPS | Object storage | OpenShift Container Platform cluster | External object storage service                                                             |
| 80/443      | HTTP/HTTPS | Receptor       | Execution node                       | OpenShift Container Platform ingress                                                        |
| 80/443      | HTTP/HTTPS | Receptor       | Hop node                             | OpenShift Container Platform ingress                                                        |
| 5432        | TCP        | PostgreSQL     | OpenShift Container Platform cluster | External database service                                                                   |
| 5432        | TCP        | PostgreSQL     | OpenShift Container Platform cluster | External database service (`metrics_service` database)                                      |
| 5432        | TCP        | PostgreSQL     | OpenShift Container Platform cluster | External database service (`automationcontroller` database - read-only for metrics service) |
| 6379        | TCP        | Redis          | OpenShift Container Platform cluster | External Redis service                                                                      |
| 27199       | TCP        | Receptor       | OpenShift Container Platform cluster | Execution node                                                                              |
| 27199       | TCP        | Receptor       | OpenShift Container Platform cluster | Hop node                                                                                    |

Note:

Metrics service pods communicate internally within the OpenShift cluster via the platform gateway. The `/api/metrics/` path is routed through the standard Ansible Automation Platform gateway and does not require a separate external ingress. Metrics service requires outbound connectivity on port 5432 to both the `metrics_service` database and the `automationcontroller` database (read-only).

The Ansible Automation Platform Operator also creates Kubernetes NetworkPolicy resources to control pod-to-pod communication within the namespace. For more information, see [Operator-managed NetworkPolicies](/documentation/en-us/red_hat_ansible_automation_platform/2.7/plan-operator_managed_networkpolicies#GUID-1d94c84c-9350-4ae8-a8f9-87da56d0cc86 "When you deploy Ansible Automation Platform on Red Hat OpenShift Container Platform, the Ansible Automation Platform Operator automatically creates and manages Kubernetes NetworkPolicy resources to enforce least-privilege networking within the Ansible Automation Platform namespace.").

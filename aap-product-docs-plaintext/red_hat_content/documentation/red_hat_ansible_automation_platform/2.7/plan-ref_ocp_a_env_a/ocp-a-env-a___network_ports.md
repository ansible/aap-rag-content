# Operator growth topology
## Network ports

Red Hat Ansible Automation Platform uses several ports to communicate with its services. These ports must be open and available for Red Hat Ansible Automation Platform to work. Ensure that these ports are available and are not blocked by a firewall.

*Table 4. Network ports and protocols*

| Port number | Protocol   | Service  | Source                               | Destination                          |
| ----------- | ---------- | -------- | ------------------------------------ | ------------------------------------ |
| 80/443      | HTTP/HTTPS | Receptor | Execution node                       | OpenShift Container Platform ingress |
| 80/443      | HTTP/HTTPS | Receptor | Hop node                             | OpenShift Container Platform ingress |
| 80/443      | HTTP/HTTPS | Platform | Customer clients                     | OpenShift Container Platform ingress |
| 27199       | TCP        | Receptor | OpenShift Container Platform cluster | Execution node                       |
| 27199       | TCP        | Receptor | OpenShift Container Platform cluster | Hop node                             |

Note:

Metrics service communication in operator deployments:

- Platform gateway routes dashboard requests to metrics service via internal Kubernetes service
- Metrics service connects to PostgreSQL via Kubernetes service (port 5432)
- All communication is internal to the OpenShift cluster
- No additional external ports required for metrics service

The Ansible Automation Platform Operator also creates Kubernetes NetworkPolicy resources to control pod-to-pod communication within the namespace. For more information, see [Operator-managed NetworkPolicies](/documentation/en-us/red_hat_ansible_automation_platform/2.7/plan-operator_managed_networkpolicies#GUID-1d94c84c-9350-4ae8-a8f9-87da56d0cc86 "When you deploy Ansible Automation Platform on Red Hat OpenShift Container Platform, the Ansible Automation Platform Operator automatically creates and manages Kubernetes NetworkPolicy resources to enforce least-privilege networking within the Ansible Automation Platform namespace.").

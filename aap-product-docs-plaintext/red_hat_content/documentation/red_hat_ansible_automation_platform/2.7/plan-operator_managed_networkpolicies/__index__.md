# Operator-managed NetworkPolicies

When you deploy Ansible Automation Platform on Red Hat OpenShift Container Platform, the Ansible Automation Platform Operator automatically creates and manages Kubernetes NetworkPolicy resources to enforce least-privilege networking within the Ansible Automation Platform namespace.

The operator creates and updates these policies during reconciliation. You do not need to create or maintain them manually.

The operator uses a layered approach: a default-deny policy blocks all ingress and egress traffic for Ansible Automation Platform-managed pods first, followed by per-component allow policies that explicitly permit only the traffic each component requires. Because Ansible Automation Platform is a layered product that might share a namespace with other workloads, these policies target only pods managed by the Ansible Automation Platform Operator and do not affect other applications in the same namespace.


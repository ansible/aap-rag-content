# Operator-managed NetworkPolicies
## Restricted network environments

If you are deploying Ansible Automation Platform in a restricted network environment, be aware of the following considerations:

- All Ansible Automation Platform-managed pods require egress for DNS resolution. Most components require egress to the `openshift-dns` namespace on port 5353 TCP and UDP. See the NetworkPolicy specifications tables for the exact DNS egress rules per component.
- Components with unrestricted egress must be able to reach their user-configured external services. If your environment applies additional network controls outside of Kubernetes NetworkPolicies, such as egress firewalls or service mesh policies, you must permit these components to reach the relevant destinations.
- If you use an external PostgreSQL database or Redis instance, ensure your network controls allow traffic from the Ansible Automation Platform namespace to those endpoints on ports 5432 and 6379 respectively.
- The operator manages these NetworkPolicies automatically and restores them to their expected state during each reconciliation cycle. If you require custom network controls, apply them as separate NetworkPolicies that do not overlap with the operator-managed set.


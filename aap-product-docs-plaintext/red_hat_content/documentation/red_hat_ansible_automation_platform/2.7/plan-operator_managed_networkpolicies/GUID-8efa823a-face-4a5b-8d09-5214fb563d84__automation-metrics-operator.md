# Operator-managed NetworkPolicies
## NetworkPolicy specifications for operator deployments
### Automation metrics operator

The following table lists the NetworkPolicy resources created by the automation metrics operator.

*Table 5. Automation metrics operator NetworkPolicies*

| NetworkPolicy                 | Component                                    | Ingress allowed                                                                                                                          | Egress allowed                                                                                                                                                                                           |
| ----------------------------- | -------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `<metrics-name>-default-deny` | All automation metrics operator-managed pods | None                                                                                                                                     | None                                                                                                                                                                                                     |
| `<metrics-name>-web`          | Automation metrics web                       | OpenShift router (port 8080)Platform gateway pods, automation metrics operator-managed pods, and operator controller-manager (port 8080) | Platform gateway pods (port 8000, for JWT key fetch)Unrestricted egress on port 5432 (metrics database and automation controller read-only database; destination is not managed by this operator)`openshift-dns` and `kube-system` namespaces (ports 53 and 5353 TCP and UDP) |
| `<metrics-name>-tasks`        | Automation metrics tasks                     | None                                                                                                                                     | `openshift-dns` and `kube-system` namespaces (ports 53 and 5353 TCP and UDP)Unrestricted egress (PostgreSQL, platform gateway JWT key fetch, and telemetry service connections cannot be enumerated at policy creation time) |
| `<metrics-name>-scheduler`    | Automation metrics scheduler                 | None                                                                                                                                     | `openshift-dns` and `kube-system` namespaces (ports 53 and 5353 TCP and UDP)Unrestricted egress (PostgreSQL by using `pg_notify` and platform gateway JWT key fetch cannot be enumerated at policy creation time) |


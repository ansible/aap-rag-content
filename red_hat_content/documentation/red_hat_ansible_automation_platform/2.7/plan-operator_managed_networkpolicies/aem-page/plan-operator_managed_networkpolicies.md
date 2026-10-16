+++
title = "Operator-managed NetworkPolicies - Red Hat Ansible Automation Platform 2.7"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/plan-operator_managed_networkpolicies"
template = "docs/aem-title.html"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/plan-assembly_overview_tested_deployment_models/", "Choose a deployment method and topology"]]
category = "Plan"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/plan-operator_managed_networkpolicies/aem-page/plan-operator_managed_networkpolicies.html"
last_crumb = "Operator-managed NetworkPolicies"
latest = "true"
modified = "2026-10-06T15:21:13.207Z"
multi_page_path = ""
name = "Operator-managed NetworkPolicies"
oversized = "false"
page_slug = "plan-operator_managed_networkpolicies"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/plan-operator_managed_networkpolicies"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/plan-operator_managed_networkpolicies/toc/toc.json"
type = "aem-page"
+++

# Operator-managed NetworkPolicies

When you deploy Ansible Automation Platform on Red Hat OpenShift Container Platform, the Ansible Automation Platform Operator automatically creates and manages Kubernetes NetworkPolicy resources to enforce least-privilege networking within the Ansible Automation Platform namespace.

The operator creates and updates these policies during reconciliation. You do not need to create or maintain them manually.

The operator uses a layered approach: a default-deny policy blocks all ingress and egress traffic for Ansible Automation Platform-managed pods first, followed by per-component allow policies that explicitly permit only the traffic each component requires. Because Ansible Automation Platform is a layered product that might share a namespace with other workloads, these policies target only pods managed by the Ansible Automation Platform Operator and do not affect other applications in the same namespace.

## Unrestricted egress for user-configured destinations

Several Ansible Automation Platform components connect to external services whose destinations and ports are entirely user-configured and cannot be predicted at policy creation time. For these components, the NetworkPolicy permits unrestricted egress in addition to any specific per-component allow rules. Components with unrestricted egress are noted in the following tables.

Examples of user-configured external destinations include:

- Platform gateway: Red Hat Subscription Management (RHSM), Lightweight Directory Access Protocol (LDAP) and LDAP over TLS (LDAPS) directories, Security Assertion Markup Language (SAML) and OAuth identity providers, webhooks
- Automation controller: source control management (SCM) hosts, receptor mesh peers, execution environments
- Automation hub: external collection registries, signing services
- Event-Driven Ansible: External Secret Management System, user-defined event sources

## External databases and Redis

When you use an external (customer-managed) PostgreSQL database or Redis instance instead of the operator-deployed defaults, the relevant NetworkPolicy allows egress to the configured port to any destination.

- If you use an external PostgreSQL database, components that connect to it require egress on port 5432 to any destination.
- If you use an external Redis instance, the platform gateway requires egress on port 6379 to any destination.

## Restricted network environments

If you are deploying Ansible Automation Platform in a restricted network environment, be aware of the following considerations:

- All Ansible Automation Platform-managed pods require egress for DNS resolution. Most components require egress to the `openshift-dns` namespace on port 5353 TCP and UDP. See the NetworkPolicy specifications tables for the exact DNS egress rules per component.
- Components with unrestricted egress must be able to reach their user-configured external services. If your environment applies additional network controls outside of Kubernetes NetworkPolicies, such as egress firewalls or service mesh policies, you must permit these components to reach the relevant destinations.
- If you use an external PostgreSQL database or Redis instance, ensure your network controls allow traffic from the Ansible Automation Platform namespace to those endpoints on ports 5432 and 6379 respectively.
- The operator manages these NetworkPolicies automatically and restores them to their expected state during each reconciliation cycle. If you require custom network controls, apply them as separate NetworkPolicies that do not overlap with the operator-managed set.

## NetworkPolicy specifications for operator deployments

The Ansible Automation Platform Operator creates a NetworkPolicy resource for each component in your deployment, controlling the ingress and egress traffic the component is permitted to send and receive.

Each operator uses the name of its own custom resource (CR) as the NetworkPolicy name prefix, using the following conventions:

- `<aap-name>` is the name of your `AnsibleAutomationPlatform` CR
- `<controller-name>` is the name of your `AutomationController` CR
- `<hub-name>` is the name of your `AutomationHub` CR
- `<eda-name>` is the name of your `EDAServer` CR
- `<metrics-name>` is the name of your `MetricsService` CR

In a standard Ansible Automation Platform Operator deployment, the sub-operator CRs are created automatically with names derived from the `AnsibleAutomationPlatform` CR.

### Platform gateway operator

The following table lists the NetworkPolicy resources created by the platform gateway operator.

*Table 1. Platform gateway operator NetworkPolicies*

| NetworkPolicy                   | Component                                             | Ingress allowed                                                                                                                      | Egress allowed                                                                                                                                                                                           |
| ------------------------------- | ----------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `<aap-name>-default-deny`       | All platform gateway operator-managed pods            | None                                                                                                                                 | None                                                                                                                                                                                                     |
| `<aap-name>-gateway`            | Platform gateway                                      | OpenShift router (port 8000)Ansible Automation Platform component pods (port 8000)Operator controller-manager (port 8080)            | Unrestricted egress (RHSM, LDAP, LDAPS, SAML, OpenID Connect (OIDC), OAuth, and webhook destinations are user-configured and cannot be enumerated at policy creation time). Specific egress to managed PostgreSQL (port 5432), managed Redis (port 6379), and `openshift-dns` namespace (port 5353 TCP and UDP). |
| `<aap-name>-postgres-<version>` | Managed PostgreSQL                                    | All Ansible Automation Platform component pods (port 5432)Operator controller-manager (port 5432)EDA activation Job pods (port 5432) | `openshift-dns` namespace (port 5353 TCP and UDP)                                                                                                                                                        |
| `<aap-name>-redis`              | Managed Redis (standalone mode)                       | Platform gateway (port 6379)                                                                                                         | `openshift-dns` namespace (port 5353 TCP and UDP)                                                                                                                                                        |
| `<aap-name>-redis-cluster`      | Managed Redis (cluster mode)                          | Platform gateway (port 6379)Redis cluster inter-node traffic (ports 6379 and 16379)Redis cluster init Job (port 6379)                | Redis cluster inter-node traffic (ports 6379 and 16379)Platform gateway pods on an unrestricted port (required for direct pod IP connections after Redis `CLUSTER SLOTS` discovery)`openshift-dns` namespace (port 5353 TCP and UDP) |
| `<aap-name>-redis-cluster-init` | Redis cluster init Job (cluster mode only, ephemeral) | None                                                                                                                                 | Redis cluster nodes (port 6379)`openshift-dns` namespace (port 5353 TCP and UDP)                                                                                                                         |
| `<aap-name>-db-management`      | Platform backup and restore pods                      | None                                                                                                                                 | Managed PostgreSQL (port 5432)`openshift-dns` namespace (port 5353 TCP and UDP)Unrestricted egress on port 5432 if external PostgreSQL is configured                                                     |

### Automation controller operator

The following table lists the NetworkPolicy resources created by the automation controller operator.

*Table 2. Automation controller operator NetworkPolicies*

| NetworkPolicy                          | Component                                                                                                         | Ingress allowed                                                                                                                                                                     | Egress allowed                                                                                                                                                                                           |
| -------------------------------------- | ----------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `<controller-name>-default-deny`       | All automation controller operator-managed pods                                                                   | None                                                                                                                                                                                | None                                                                                                                                                                                                     |
| `<controller-name>-web`                | Automation controller web                                                                                         | Any source (port 8052; port 8053 for TLS passthrough routes)                                                                                                                        | `openshift-dns` namespace (port 5353 TCP and UDP)Unrestricted egress (LDAP, SAML, webhooks, and external PostgreSQL connections are user-configured and cannot be enumerated at policy creation time)    |
| `<controller-name>-task`               | Automation controller task                                                                                        | None                                                                                                                                                                                | `openshift-dns` namespace (port 5353 TCP and UDP)Unrestricted egress (receptor mesh peers, SCM hosts, execution environments, Kubernetes API, and PostgreSQL connections are user-configured and cannot be enumerated at policy creation time) |
| `<controller-name>-mesh-ingress`       | Automation controller mesh ingress (conditional; present only when an`AutomationControllerMeshIngress` CR exists) | Any source (port 27199)                                                                                                                                                             | `openshift-dns` namespace (port 5353 TCP and UDP)Unrestricted egress (receptor mesh peers are user-configured and cannot be enumerated at policy creation time)                                          |
| `<controller-name>-postgres-<version>` | Automation controller managed PostgreSQL                                                                          | Automation controller operator-managed pods (port 5432)Operator controller-manager (port 5432)Pods in the backup namespace, if backup storage uses a separate namespace (port 5432) | Other automation controller PostgreSQL pods during major version upgrades (port 5432)Ports 53 and 5353 TCP and UDP (no destination restriction)                                                          |
| `<controller-name>-db-management`      | Automation controller backup and restore pods                                                                     | None                                                                                                                                                                                | Managed PostgreSQL (port 5432)Ports 53 and 5353 TCP and UDP (no destination restriction)Unrestricted egress on port 5432 if external PostgreSQL is configured                                            |

### Automation hub operator

The following table lists the NetworkPolicy resources created by the automation hub operator.

*Table 3. Automation hub operator NetworkPolicies*

| NetworkPolicy                   | Component                                | Ingress allowed                                                                                                                                         | Egress allowed                                                                                                                                                                                       |
| ------------------------------- | ---------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `<hub-name>-default-deny`       | All automation hub operator-managed pods | None                                                                                                                                                    | None                                                                                                                                                                                                 |
| `<hub-name>-api`                | Automation hub API                       | OpenShift router (port 8000)Automation hub operator-managed pods, platform gateway pods, and operator controller-manager (port 8000)                    | `openshift-dns` namespace (port 5353 TCP and UDP)Unrestricted egress (signing services, LDAP, and Red Hat SSO connections are user-configured and cannot be enumerated at policy creation time)      |
| `<hub-name>-web`                | Automation hub web                       | OpenShift router (port 8080)Automation hub operator-managed pods, platform gateway pods, and operator controller-manager from any namespace (port 8080) | Automation hub API pod (port 8000)Automation hub content pod (port 24816)`openshift-dns` namespace (port 5353 TCP and UDP)                                                                           |
| `<hub-name>-content`            | Automation hub content                   | Automation hub operator-managed pods and operator controller-manager (port 24816)                                                                       | `openshift-dns` namespace (port 5353 TCP and UDP)Unrestricted egress (external collection registries are user-configured and cannot be enumerated at policy creation time)                           |
| `<hub-name>-worker`             | Automation hub worker                    | None                                                                                                                                                    | `openshift-dns` namespace (port 5353 TCP and UDP)Unrestricted egress (collection import tasks and signing service destinations are user-configured and cannot be enumerated at policy creation time) |
| `<hub-name>-postgres-<version>` | Automation hub managed PostgreSQL        | Automation hub operator-managed pods, platform gateway pods, and operator controller-manager (port 5432)                                                | `openshift-dns` namespace (port 5353 TCP and UDP)                                                                                                                                                    |
| `<hub-name>-redis`              | Automation hub managed Redis             | Automation hub operator-managed pods (port 6379)                                                                                                        | `openshift-dns` namespace (port 5353 TCP and UDP)                                                                                                                                                    |
| `<hub-name>-db-management`      | Automation hub backup and restore pods   | None                                                                                                                                                    | Managed PostgreSQL (port 5432)`openshift-dns` namespace (port 5353 TCP and UDP)Unrestricted egress on port 5432 if external PostgreSQL is configured                                                 |

### Event-Driven Ansible operator

The following table lists the NetworkPolicy resources created by the Event-Driven Ansible operator.

*Table 4. Event\-Driven Ansible operator NetworkPolicies*

| NetworkPolicy                   | Component                                      | Ingress allowed                                                                                                                                                | Egress allowed                                                                                                                                                                  |
| ------------------------------- | ---------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `<eda-name>-default-deny`       | All Event-Driven Ansible operator-managed pods | None                                                                                                                                                           | None                                                                                                                                                                            |
| `<eda-name>-api`                | EDA API                                        | OpenShift router (port 8000)Platform gateway and Ansible Automation Platform component pods (ports 8000 and 8001)EDA activation Job pods (ports 8000 and 8001) | Unrestricted egress (JWT key fetch, external secret management services, and external service connections are user-configured and cannot be enumerated at policy creation time) |
| `<eda-name>-activation-worker`  | EDA activation worker                          | None                                                                                                                                                           | Unrestricted egress (Kubernetes API calls, user-defined event source destinations, and external services cannot be enumerated at policy creation time)                          |
| `<eda-name>-default-worker`     | EDA default worker                             | None                                                                                                                                                           | Unrestricted egress (rulebook tasks and external service destinations cannot be enumerated at policy creation time)                                                             |
| `<eda-name>-event-stream`       | EDA event stream                               | OpenShift router (port 8000)Platform gateway and Ansible Automation Platform component pods (port 8000)                                                        | Unrestricted egress (JWT key fetch, PostgreSQL by using`pg_notify`, and external event source destinations cannot be enumerated at policy creation time)                        |
| `<eda-name>-postgres-<version>` | EDA managed PostgreSQL                         | EDA and Ansible Automation Platform component pods (port 5432)EDA activation Job pods (port 5432)Operator controller-manager (port 5432)                       | `openshift-dns` namespace (port 5353 TCP and UDP)                                                                                                                               |
| `<eda-name>-db-management`      | EDA backup and restore pods                    | None                                                                                                                                                           | EDA PostgreSQL (port 5432)`openshift-dns` namespace (port 5353 TCP and UDP)Unrestricted egress on port 5432 if external PostgreSQL is configured                                |

### Automation metrics operator

The following table lists the NetworkPolicy resources created by the automation metrics operator.

*Table 5. Automation metrics operator NetworkPolicies*

| NetworkPolicy                 | Component                                    | Ingress allowed                                                                                                                          | Egress allowed                                                                                                                                                                                           |
| ----------------------------- | -------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `<metrics-name>-default-deny` | All automation metrics operator-managed pods | None                                                                                                                                     | None                                                                                                                                                                                                     |
| `<metrics-name>-web`          | Automation metrics web                       | OpenShift router (port 8080)Platform gateway pods, automation metrics operator-managed pods, and operator controller-manager (port 8080) | Platform gateway pods (port 8000, for JWT key fetch)Unrestricted egress on port 5432 (metrics database and automation controller read-only database; destination is not managed by this operator)`openshift-dns` and `kube-system` namespaces (ports 53 and 5353 TCP and UDP) |
| `<metrics-name>-tasks`        | Automation metrics tasks                     | None                                                                                                                                     | `openshift-dns` and `kube-system` namespaces (ports 53 and 5353 TCP and UDP)Unrestricted egress (PostgreSQL, platform gateway JWT key fetch, and telemetry service connections cannot be enumerated at policy creation time) |
| `<metrics-name>-scheduler`    | Automation metrics scheduler                 | None                                                                                                                                     | `openshift-dns` and `kube-system` namespaces (ports 53 and 5353 TCP and UDP)Unrestricted egress (PostgreSQL by using `pg_notify` and platform gateway JWT key fetch cannot be enumerated at policy creation time) |

### Automation orchestrator operator

The automation orchestrator operator creates its own set of NetworkPolicy resources for the pods it manages. For the full NetworkPolicy specification for automation orchestrator deployments, see operator managed network policies in the automation orchestrator documentation

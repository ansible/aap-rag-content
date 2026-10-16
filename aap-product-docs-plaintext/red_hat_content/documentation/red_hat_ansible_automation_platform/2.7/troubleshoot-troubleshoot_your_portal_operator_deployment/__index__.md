# Troubleshoot your portal operator deployment

Diagnose and resolve common issues when deploying or operating the automation portal operator on OpenShift, including status condition interpretation, log collection, and cleanup procedures.

Important:

The automation portal operator is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production.

## Check the deployment status

The operator reports five status conditions on the `AutomationPortal` custom resource. Check all conditions with:

**Using the CLI:**

```terminal
$ oc get automationportal <name> -o jsonpath='{.status.conditions}' | jq '.'
```

To identify which condition is preventing the automation portal from reaching `Running` phase:

```terminal
$ oc get automationportal <name> -o jsonpath='{.status.conditions[?(@.status=="False")]}'
```

**Using the OpenShift web console:**

Navigate to **Ecosystem** > **Installed Operators** > **Ansible automation portal operator** > **Automation Portal** tab, click the portal instance name, and review the **Conditions** section in the **Details** tab.

## RHDH Operator not installing

The automation portal operator automatically installs the RHDH Operator via OLM. If the `RHDHOperatorReady` condition is `False`, check the OLM Subscription and InstallPlan:

```terminal
$ oc get subscription rhdh -n openshift-operators -o yaml
$ oc get installplan -n openshift-operators
```

On clusters running OLM v1 (OpenShift 4.18 and later), the operator uses a `ClusterExtension` instead. If the condition message references `ServiceAccountRequired`, create the required ServiceAccount with `cluster-admin` role in the `openshift-operators` namespace.

## Secret validation failures

The `SecretsValid` condition message identifies exactly which Secret or key is problematic:

**Using the CLI:**

```terminal
$ oc get automationportal <name> -o jsonpath='{.status.conditions[?(@.type=="SecretsValid")].message}'
```

Common causes:

- The Secret does not exist in the namespace.
- A required key is missing from the Secret.
- A key exists but has an empty value.
- Placeholder values such as `<placeholder>` or `changeme` were not replaced with real credentials.

To verify the Secret contents:

```terminal
$ oc get secret secrets-rhaap-portal -n <namespace> -o jsonpath='{.data}' | jq 'to_entries[] | {key: .key, value: (.value | @base64d)}'
```

**Using the OpenShift web console:**

Navigate to **Workloads** > **Secrets**, select the appropriate namespace, and click the Secret name to view its keys and values.

## Automation portal pods not starting

If the `BackstageReady` condition is `False`, check the automation portal pods managed by the RHDH Operator:

**Using the CLI:**

```terminal
$ oc get pods -l rhdh.redhat.com/app -n <namespace>
$ oc logs -l rhdh.redhat.com/app -n <namespace> -c backstage-backend
```

Common causes:

- **Image pull failures** — registry credentials are missing or the image path is incorrect. In disconnected environments, verify that all images are mirrored and the pull secret is linked to the default service account.
- **Plugin download failures** — the OCI plugin registry is unreachable. Check the `spec.plugins.registry` value and network connectivity.
- **Database connection issues** — if using an external database (`enableLocalDb: false`), verify the database Secret keys and network reachability on port 5432.

**Using the OpenShift web console:**

Navigate to **Workloads** > **Pods**, select the namespace, locate the backstage pod, and click it to view logs in the **Logs** tab. You can also access logs from **Workloads** > **Deployments**, select the deployment, and view logs from the pod details.

## Host validation errors

The operator validates all host fields to prevent SSRF attacks. If a host value is rejected, check the operator logs:

```terminal
$ oc logs -l app=portal-operator -n <namespace> | grep "host validation"
```

The following host values are blocked:

- `169.254.169.254` (cloud metadata endpoint)
- `metadata.google.internal`
- `localhost`, `127.0.0.1`, `0.0.0.0`, `::1`

## NetworkPolicy blocking traffic

The operator creates a NetworkPolicy that restricts automation portal pod traffic to specific ports. If the automation portal cannot reach external services, inspect the NetworkPolicy:

**Using the CLI:**

```terminal
$ oc get networkpolicy -n <namespace>
$ oc describe networkpolicy <name>-network-policy -n <namespace>
```

Allowed egress traffic:

- TCP 443 (HTTPS)
- TCP 5432 (PostgreSQL)
- UDP and TCP 53 (DNS)

**Using the OpenShift web console:**

Navigate to **Networking** > **NetworkPolicies**, select the namespace, and click the NetworkPolicy name to view its egress rules.

## Collect operator logs

**Using the CLI:**

View the most recent operator logs:

```terminal
$ oc logs -l app=portal-operator -n <namespace> --tail=50
```

Check reconciliation timing to identify performance issues:

```terminal
$ oc logs -l app=portal-operator -n <namespace> | grep "reconciliation complete"
```

Expected output shows reconciliation duration under 1 second. Consistently long durations (over 5 seconds) may indicate API server latency.

**Using the OpenShift web console:**

Navigate to **Workloads** > **Pods**, select the namespace, locate the portal-operator pod, click it, and view logs in the **Logs** tab.

## Remove the automation portal deployment

Delete the `AutomationPortal` custom resource to remove the automation portal and all managed resources:

```terminal
$ oc delete automationportal <name> -n <namespace>
```

Owner references automatically delete the ConfigMaps, Secrets, custom resource, and NetworkPolicy created by the operator. The Operator then cleans up the Deployment, Service, Route, and PostgreSQL instance.

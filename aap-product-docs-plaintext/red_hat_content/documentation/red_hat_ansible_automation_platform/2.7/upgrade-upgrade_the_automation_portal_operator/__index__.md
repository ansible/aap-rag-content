# Upgrade the automation portal operator

Upgrade the automation portal operator through OLM and verify your portal instances are healthy after the upgrade.

## Before you begin

- An OpenShift Container Platform 4.18 through 4.23 cluster with `cluster-admin` access.
- The `oc` CLI installed and authenticated to your OpenShift cluster.

## About this task

Important:

The automation portal operator is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production.

The automation portal operator is installed through Operator Lifecycle Manager (OLM) on the `fast` channel. OLM manages operator upgrades based on the approval strategy you selected during installation.

## Procedure

Upgrade the operator

1. Check your current approval strategy.


```terminal
$ oc get subscription automation-portal-operator -n <namespace> -o jsonpath='{.spec.installPlanApproval}'
```

- `Automatic` -- OLM installs new versions as they become available. No action is needed for upgrades.
- `Manual` -- OLM creates an InstallPlan that requires your approval before each upgrade.

2. If you use manual approval, check for pending upgrades and approve them.
**Using the CLI:**



```terminal
$ oc get installplan -n <namespace>
```

To approve a pending InstallPlan:



```terminal
$ oc patch installplan <plan-name> -n <namespace> --type merge -p '{"spec":{"approved":true}}'
```

**Using the OpenShift web console:**

1. Navigate to **Ecosystem** > **Installed Operators**.
2. Select the namespace where the operator is installed.
3. Click **Ansible automation portal operator**.
4. Click the **Subscriptions** tab.
5. Click the **automation-portal-operator** subscription.
6. In the **Upgrade Status** section, review any pending InstallPlans.
7. Click the pending InstallPlan link, then click **Preview** to review the changes.
8. Return to the InstallPlan details and click **Approve**.

3. Verify the upgrade completed successfully.
**Using the CLI:**



```terminal
$ oc get csv -n <namespace> | grep automation-portal
```

**Using the OpenShift web console:**

Navigate to **Ecosystem** > **Installed Operators**, select the namespace, and verify that **Ansible automation portal operator** shows the updated version with status **Succeeded**.

The output shows the new operator version with `Phase: Succeeded`.

4. Verify that your portal instances are healthy after the upgrade.
**Using the CLI:**



```terminal
$ oc get automationportal -n <namespace>
```

**Using the OpenShift web console:**

Navigate to **Ecosystem** > **Installed Operators** > **Ansible automation portal operator** > **Automation Portal** tab, and verify all instances show **Running** status.

All instances should show `Phase: Running`. The operator re-reconciles all `AutomationPortal` custom resources after an upgrade, regenerating ConfigMaps and updating the automation portal deployment.

5. **Optional:** If upgrading from operator version 2.2.7 or earlier, delete the previous Backstage custom resource.
In operator version 2.2.8 and later, the managed Backstage custom resource name changed from `<name>-backstage` to `<name>`. The operator automatically creates the new custom resource during reconciliation, but does not remove the previous custom resource.



```terminal
$ oc delete backstage <name>-backstage -n <namespace>
```

6. **Optional:** If a portal instance is not healthy after the upgrade, check the status conditions for details.


```terminal
$ oc get automationportal <name> -n <namespace> -o jsonpath='{.status.conditions}' | jq '.'
```

CRD field defaults can change between operator versions. If your deployment relied on a previous default value, you may need to set the field explicitly in your custom resource. For example, `spec.aap.checkSSL` changed from `false` to `true`. Review the operator release notes before upgrading. See [Troubleshoot your portal operator deployment](/documentation/en-us/red_hat_ansible_automation_platform/2.7/troubleshoot-troubleshoot_your_portal_operator_deployment#troubleshoot-portal-operator "Diagnose and resolve common issues when deploying or operating the automation portal operator on OpenShift, including status condition interpretation, log collection, and cleanup procedures.").

Remove the automation portal deployment

7. Delete the `AutomationPortal` custom resource to remove the automation portal and all operator-managed resources.


```terminal
$ oc delete automationportal <name> -n <namespace>
```

Owner references automatically delete the following resources created by the operator:

- ConfigMaps (`<name>-app-config`, `<name>-dynamic-plugins`)
- Secrets (`<name>-portal-env`, `<name>-registry-auth`)
- Custom resource (`<name>`, or `<name>-backstage` in operator versions earlier than 2.2.8)
The Operator then cleans up the deployment resources: Deployment, Service, Route, and PostgreSQL instance.

Secrets you created manually (`secrets-rhaap-portal`, `secrets-scm`, TLS secrets, database secrets) are **not deleted**. Remove them separately if they are no longer needed.

8. **Optional:** To remove the operator itself, delete the OLM Subscription and ClusterServiceVersion.


```terminal
$ oc delete subscription automation-portal-operator -n <namespace>
$ oc delete csv -n <namespace> -l operators.coreos.com/automation-portal-operator.<namespace>=
```

The RHDH Operator Subscription created by the automation portal operator is **not removed** automatically. If you no longer need the RHDH Operator, delete its Subscription separately:



```terminal
$ oc delete subscription rhdh -n openshift-operators
```

## Results

After an upgrade, the operator re-reconciles all portal instances: regenerating ConfigMaps, updating the custom resource, and triggering a pod rollout. After removal, all operator-managed resources are cleaned up through cascade deletion.

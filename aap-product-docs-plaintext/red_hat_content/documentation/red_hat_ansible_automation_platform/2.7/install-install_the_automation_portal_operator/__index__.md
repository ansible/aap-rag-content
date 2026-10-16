# Install the automation portal operator

Install the automation portal operator from the Software Catalog on OpenShift and deploy a portal instance by creating an `AutomationPortal` custom resource.

## Before you begin

- An OpenShift Container Platform cluster with `cluster-admin` access.
- An Ansible Automation Platform (AAP) instance with an OAuth application configured. You need the client ID, client secret, AAP base URL, and an API token. For how to create the OAuth application and API token, see [Configure credentials and secrets for the automation portal operator](/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-configure_credentials_and_secrets_for_the_automation_portal_operator#configure-credentials-portal-operator "Configure the Kubernetes Secrets required by the automation portal operator, including AAP OAuth credentials, OCI plugin registry credentials, and optional SCM credentials.").
- The `oc` CLI installed and authenticated to your OpenShift cluster.

Important:

The automation portal operator is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production.

## About this task

The automation portal operator is available from the Software Catalog on OpenShift. When you create an `AutomationPortal` custom resource, the operator automatically installs the Red Hat Developer Hub (RHDH) Operator if it is not already present on the cluster.

## Procedure

1. Create a namespace for the automation portal deployment.


```terminal
$ oc new-project automation-portal
```

2. If not already created, create a Secret with your AAP OAuth credentials.
**Using the CLI:**



```terminal
$ oc create secret generic secrets-rhaap-portal \
--namespace automation-portal \
--from-literal=aap-host-url='https://<aap-host>' \
--from-literal=oauth-client-id='<client-id>' \
--from-literal=oauth-client-secret='<client-secret>' \
--from-literal=aap-token='<api-token>'
```

Replace the placeholder values with your AAP instance details:

- `aap-host-url` — the base URL of your AAP instance, for example `https://aap.example.com`.
- `oauth-client-id` and `oauth-client-secret` — from the OAuth application you created in AAP.
- `aap-token` — an API token with Write scope for catalog synchronization.
**Using the OpenShift web console:**

1. Create or select an OpenShift project.
2. Navigate to **Workloads** > **Secrets**.
3. Select the **automation-portal** namespace from the dropdown.
4. Click **Create** > **Key/value secret**.
5. Set the secret name to `secrets-rhaap-portal`.
6. Add the following keys and values:
- **Key:** `aap-host-url`, **Value:** `https://<aap-host>`
- **Key:** `oauth-client-id`, **Value:** `<client-id>`
- **Key:** `oauth-client-secret`, **Value:** `<client-secret>`
- **Key:** `aap-token`, **Value:** `<api-token>`
7. Click **Create**.

3. Install the operator from the Software Catalog.
1. In the OpenShift web console, navigate to **Ecosystem** > **Software Catalog**.
2. Search for **Ansible automation portal**. Filter by Type: Operators if needed.
3. Select the operator and click **Install**.
4. Choose the installation namespace and approval strategy, then click **Install**.
When you create an `AutomationPortal` custom resource in the next step, the operator checks whether the RHDH Operator is installed. If not, it creates an OLM `Subscription` to install it automatically. On clusters running OLM v1, the operator uses a `ClusterExtension` resource instead.

4. Verify that the operator is running.
**Using the CLI:**



```terminal
$ oc get csv -n automation-portal
```

**Using the OpenShift web console:**

Navigate to **Ecosystem** > **Installed Operators**, select the **automation-portal** namespace, and verify that **Ansible automation portal operator** shows **Succeeded** in the **Status** column.

The output shows the operator with `Phase: Succeeded`.

5. Create an `AutomationPortal` custom resource to deploy the automation portal.
**Using the CLI:**

The following minimal example deploys a portal with default settings and a local PostgreSQL database:



```yaml
apiVersion: automationportal.aap.redhat.com/v1alpha1
kind: AutomationPortal
metadata:
name: portal
namespace: automation-portal
spec:
aap:
credentials:
secretRef: secrets-rhaap-portal
```

Save this as `portal.yaml` and apply it:



```terminal
$ oc apply -f portal.yaml
```

**Using the OpenShift web console:**

1. Navigate to **Ecosystem** > **Installed Operators**.
2. Select the **automation-portal** namespace.
3. Click **Ansible automation portal operator**.
4. Click the **Automation Portal** tab.
5. Click **Create Automation Portal**.
6. In the YAML view, replace the default content with the example above, updating `secretRef` if you used a different Secret name.
7. Click **Create**.

6. Monitor the deployment status.
**Using the CLI:**



```terminal
$ oc get automationportal portal -n automation-portal -w
```

**Using the OpenShift web console:**

Navigate to **Ecosystem** > **Installed Operators** > **Ansible automation portal operator** > **Automation Portal** tab, and monitor the **Status** column. Wait for the status to show **Running**.

Wait for `Phase: Running`. The operator progresses through the following phases:

1. `Pending` — validating credentials and ensuring the RHDH Operator is installed.
2. `Running` — all status conditions are `True` and the automation portal is serving traffic.

7. Retrieve the automation portal URL and sign in.
**Using the CLI:**



```terminal
$ oc get route -n <namespace> -o jsonpath='{.items[0].spec.host}{"\n"}'
```

**Using the OpenShift web console:**

Navigate to **Networking** > **Routes**, select the **automation-portal** namespace, and click the URL in the **Location** column for the portal route.

8. Update the **Redirect URI** in your AAP OAuth application.
In your AAP instance, go to **Administration** > **Applications**, open the OAuth application you created for the automation portal, and set the **Redirect URI** to `https://<actual-portal-url>/api/auth/rhaap/handler/frame`, using the automation portal URL you retrieved in the previous step.

Important:
OAuth sign-in fails until the Redirect URI matches the actual portal URL.

9. Open the URL in a browser and sign in with your AAP credentials.

## Results

The automation portal is deployed and accessible. The operator manages the automation portal lifecycle, including configuration updates and upgrades.

## What to do next

- To configure SCM integration (GitHub or GitLab), create a `secrets-scm` Secret and update the `AutomationPortal` custom resource. See [Configure your automation portal operator deployment](/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-configure_your_automation_portal_operator_deployment#configure-portal-operator "Customize your automation portal deployment by modifying the AutomationPortal custom resource fields for authentication, plugins, networking, and infrastructure.").
- To customize resources, scheduling, or TLS settings, see [Automation portal operator configuration reference](/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-automation_portal_operator_configuration_reference#portal-operator-configuration-reference "Reference for all AutomationPortal custom resource fields, including Ansible Automation Platform (AAP) connectivity, SCM integration, authentication providers, plugins, infrastructure, and status conditions.").
- If the automation portal does not reach `Running` phase, check the status conditions. See [Troubleshoot your portal operator deployment](/documentation/en-us/red_hat_ansible_automation_platform/2.7/troubleshoot-troubleshoot_your_portal_operator_deployment#troubleshoot-portal-operator "Diagnose and resolve common issues when deploying or operating the automation portal operator on OpenShift, including status condition interpretation, log collection, and cleanup procedures.").

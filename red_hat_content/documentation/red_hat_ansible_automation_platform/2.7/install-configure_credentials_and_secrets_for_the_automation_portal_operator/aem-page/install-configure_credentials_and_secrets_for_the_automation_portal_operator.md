+++
title = "Configure credentials and secrets for the automation portal operator - Red Hat Ansible Automation Platform 2.7"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-configure_credentials_and_secrets_for_the_automation_portal_operator"
template = "docs/aem-title.html"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-install_automation_portal_on_openshift_container_platform/", "Install automation portal on OpenShift Container Platform"]]
category = "Install"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/install-configure_credentials_and_secrets_for_the_automation_portal_operator/aem-page/install-configure_credentials_and_secrets_for_the_automation_portal_operator.html"
last_crumb = "Configure credentials and secrets for the automation portal operator"
latest = "true"
modified = "2026-10-06T15:21:13.207Z"
multi_page_path = ""
name = "Configure credentials and secrets for the automation portal operator"
oversized = "false"
page_slug = "install-configure_credentials_and_secrets_for_the_automation_portal_operator"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/install-configure_credentials_and_secrets_for_the_automation_portal_operator"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/install-configure_credentials_and_secrets_for_the_automation_portal_operator/toc/toc.json"
type = "aem-page"
+++

# Configure credentials and secrets for the automation portal operator

Configure the Kubernetes Secrets required by the automation portal operator, including AAP OAuth credentials, OCI plugin registry credentials, and optional SCM credentials.

## Before you begin

- An Ansible Automation Platform instance with administrator access.
- The `oc` CLI installed and authenticated to your OpenShift cluster.
- The automation portal operator installed on your cluster. See [Install the automation portal operator](/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-install_the_automation_portal_operator#install-portal-operator "Install the automation portal operator from the Software Catalog on OpenShift and deploy a portal instance by creating an AutomationPortal custom resource.").

## About this task

The automation portal operator requires two Kubernetes Secrets with AAP OAuth credentials and OCI plugin registry credentials. If you enable GitHub or GitLab SCM integration, you also need an SCM credentials Secret. These are the same secrets used by the Helm chart deployment.

Important:

The automation portal operator is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production.

## Procedure

1. Create an OAuth application in your AAP instance.
  1. Log in to your AAP instance as an administrator.
  2. Navigate to **Administration** > **Applications**.
  3. Click **Add** and configure the following settings:

    - **Name**: `automation-portal`
    - **Authorization grant type**: `Authorization code`
    - **Redirect URIs**: `https://<portal-url>/api/auth/rhaap/handler/frame`
      Note:
      The automation portal URL does not display until after deployment. Enter a placeholder value now. After you deploy the automation portal and retrieve the URL, return to this OAuth application and update the Redirect URI to `https://<actual-portal-url>/api/auth/rhaap/handler/frame`. See [Install the automation portal operator](/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-install_the_automation_portal_operator#install-portal-operator "Install the automation portal operator from the Software Catalog on OpenShift and deploy a portal instance by creating an AutomationPortal custom resource.") for how to retrieve the automation portal URL after deployment.

    - **Client type**: `Confidential`

  4. Save the application and note the **Client ID** and **Client Secret**.
      For more information about creating an OAuth application in Ansible Automation Platform, see [Create an OAuth application](/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-proc_self_service_create_oauth_app#self-service-create-oauth-app "To use the Helm chart to deploy Ansible automation portal, you must have set up an OAuth application on your Ansible Automation Platform instance.").

2. Generate an API token for catalog synchronization.
  1. Navigate to **Users** > your user > **Tokens**.
  2. Create a new token with **Scope: Write**.
  3. Note the token value. You cannot retrieve it after closing the dialog.
      Create the token with Write scope for catalog synchronization. For more information about API tokens, see [OAuth 2 token authentication](/documentation/en-us/red_hat_ansible_automation_platform/2.7/secure-con_controller_api_oauth2_token#controller-api-oauth2-token "OAuth (Open Authorization) is an open standard for token-based authentication and authorization. OAuth 2 authentication is commonly used when interacting with the platform gateway API programmatically."). For the automation portal permissions that govern access, see [Configure role-based access control for Ansible automation portal](/documentation/en-us/red_hat_ansible_automation_platform/2.7/secure-configure_portal_rbac#configure-portal-rbac "Configure RBAC permissions in Ansible automation portal to control which users can view and execute templates, and which sidebar items are visible to non-admin users.").

3. Log in to your OpenShift cluster from the command line.
      You can copy a login command that includes a token from the OpenShift web console, under your username menu, by selecting **Copy login command**.

  

```terminal
$ oc login --token=<token> --server=https://<openshift-api-url>:6443
```

4. Create the AAP credentials Secret on your OpenShift cluster.
      **Using the CLI:**

  

```terminal
$ oc create secret generic secrets-rhaap-portal \
  --namespace automation-portal \
  --from-literal=aap-host-url='https://<aap-host>' \
  --from-literal=oauth-client-id='<client-id>' \
  --from-literal=oauth-client-secret='<client-secret>' \
  --from-literal=aap-token='<api-token>'
```

      Replace the placeholder values with your AAP instance details. The operator validates these keys and blocks deployment if any key is missing, empty, or contains a placeholder value such as `<placeholder>` or `changeme`.

    | Key                   | Description                                                          |
    | --------------------- | -------------------------------------------------------------------- |
    | `aap-host-url`        | AAP base URL, for example`https://aap.example.com`.                  |
    | `oauth-client-id`     | Client ID from the OAuth application you created in step 1.          |
    | `oauth-client-secret` | Client Secret from the OAuth application you created in step 1.      |
    | `aap-token`           | API token with Write scope for catalog synchronization, from step 2. |
      **Using the OpenShift web console:**

  1. Navigate to **Workloads** > **Secrets**.
  2. Select the **automation-portal** namespace.
  3. Click **Create** > **Key/value secret**.
  4. Set the secret name to `secrets-rhaap-portal`.
  5. Add the following key-value pairs:
    - **Key:** `aap-host-url`, **Value:** `https://<aap-host>`
    - **Key:** `oauth-client-id`, **Value:** `<client-id>`
    - **Key:** `oauth-client-secret`, **Value:** `<client-secret>`
    - **Key:** `aap-token`, **Value:** `<api-token>`
  6. Click **Create**.

5. **Optional:** If you plan to use GitHub or GitLab SCM integration, create the unified SCM Secret.
      The SCM Secret stores credentials for source control integration and authentication providers. Include only the keys for the providers you enable.

    **Using the CLI:**

    **Minimal example** (PAT-only access for GitHub and GitLab):

  

```terminal
$ oc create secret generic secrets-scm \
  --namespace automation-portal \
  --from-literal=github-token='<github-pat>' \
  --from-literal=gitlab-token='<gitlab-pat>'
```

      **Full example** (OAuth + GitHub App):

```terminal
$ oc create secret generic secrets-scm \
  --namespace automation-portal \
  --from-literal=github-oauth-client-id='<github-oauth-id>' \
  --from-literal=github-oauth-client-secret='<github-oauth-secret>' \
  --from-literal=gitlab-oauth-client-id='<gitlab-oauth-id>' \
  --from-literal=gitlab-oauth-client-secret='<gitlab-oauth-secret>' \
  --from-literal=github-app-id='<app-id>' \
  --from-literal=github-app-client-id='<app-client-id>' \
  --from-literal=github-app-client-secret='<app-client-secret>' \
  --from-literal=github-app-private-key='<private-key-pem>'
```

  Note:
  GitHub App authentication is the preferred method for GitHub integration in production environments. Personal access tokens (for example, github-token) can be used as an alternative but provide less granular access in non-production environments.
    | Key                          | Required when                  | Description                                  |
    | ---------------------------- | ------------------------------ | -------------------------------------------- |
    | `gitlab-token`               | GitLab enabled                 | GitLab personal access token for API access. |
    | `github-oauth-client-id`     | GitHub SCM integration enabled | GitHub OAuth application client ID.          |
    | `github-oauth-client-secret` | GitHub SCM integration enabled | GitHub OAuth application client secret.      |
    | `gitlab-oauth-client-id`     | GitLab SCM integration enabled | GitLab OAuth application client ID.          |
    | `gitlab-oauth-client-secret` | GitLab SCM integration enabled | GitLab OAuth application client secret.      |
    | `github-app-id`              | `authType: app`                | GitHub App ID.                               |
    | `github-app-client-id`       | `authType: app`                | GitHub App client ID.                        |
    | `github-app-client-secret`   | `authType: app`                | GitHub App client secret.                    |
    | `github-app-private-key`     | `authType: app`                | GitHub App private key in PEM format.        |
      **Using the OpenShift web console:**

  1. Navigate to **Workloads** > **Secrets**.
  2. Select the **automation-portal** namespace.
  3. Click **Create** > **Key/value secret**.
  4. Set the secret name to `secrets-scm`.
  5. Add the relevant key-value pairs for your providers.
  6. Click **Create**.

6. Reference the Secrets in your `AutomationPortal` custom resource.
      The AAP credentials Secret is required. The SCM Secret is needed only if you enable GitHub or GitLab integration.

    **Using the CLI:**

  

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
  scm:
    credentials:
      secretRef: secrets-scm
    github:
      enabled: true
```

      **Using the OpenShift web console:**

  1. Navigate to **Ecosystem** > **Installed Operators**.
  2. Select the **automation-portal** namespace.
  3. Click **Ansible automation portal operator**.
  4. Click the **Automation Portal** tab.
  5. Click the portal instance name, then select the **YAML** tab.
  6. Add the `secretRef` fields for your Secrets under the appropriate `spec` keys.
  7. Click **Save**.

7. Create a registry credential secret for pulling OCI dynamic plugin artifacts.
      The operator uses an authentication file to pull dynamic plugins from an OCI registry. This secret is required in all environments, including connected and disconnected deployments. The `install-dynamic-plugins` init container uses skopeo to pull plugins and does not use Kubernetes `imagePullSecrets`.

  1. Create an authentication file for your registry:
  

```
$ cat > auth.json <<EOF
{
    "auths": {
        "registry.redhat.io": {
            "auth": "$(echo -n '<username>:<password>' | base64)"
         }
        }
       }
EOF
```

  2. Replace `<username>` and `<password>` with your Red Hat registry credentials. In disconnected environments, add your mirror registry credentials instead of, or in addition to, `registry.redhat.io`.
  3. Create the Secret from the authentication file:
  

```
$ oc create secret generic portal-registry-auth \
--namespace automation-portal \
--from-file=auth.json=auth.json
```

        The operator mounts this Secret at `/opt/app-root/src/.config/containers/auth.json` in the automation portal containers. The Secret name follows the pattern `<portal-cr-name>-registry-auth`.

## Results

The automation portal operator validates the Secrets on each reconciliation cycle. Check the `SecretsValid` status condition to verify validation:

```terminal
$ oc get automationportal portal -o jsonpath='{.status.conditions[?(@.type=="SecretsValid")]}'
```

If validation fails, the condition message identifies the specific Secret or key that is problematic. See [Troubleshoot your portal operator deployment](/documentation/en-us/red_hat_ansible_automation_platform/2.7/troubleshoot-troubleshoot_your_portal_operator_deployment#troubleshoot-portal-operator "Diagnose and resolve common issues when deploying or operating the automation portal operator on OpenShift, including status condition interpretation, log collection, and cleanup procedures.").

## What to do next

- To rotate credentials, update the Secret using the dry-run and apply pattern. This replaces all keys in the Secret, so include every key you need:

```terminal
$ oc create secret generic secrets-rhaap-portal \
  --namespace automation-portal \
  --from-literal=aap-host-url='https://<aap-host>' \
  --from-literal=oauth-client-id='<new-client-id>' \
  --from-literal=oauth-client-secret='<new-client-secret>' \
  --from-literal=aap-token='<new-token>' \
  --dry-run=client -o yaml | oc apply -f -
```

To update a single key without replacing the entire Secret, use `oc edit secret secrets-rhaap-portal` instead.

- If your AAP instance uses self-signed certificates, set `spec.aap.checkSSL: false` in the custom resource. The default is `true`. For air-gapped environments with a private CA, use `spec.backstage.caCertificates.secretRef` instead of disabling SSL verification. See [Configure custom TLS certificates for the automation portal operator](/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-configure_custom_tls_certificates_for_the_automation_portal_operator#configure-tls-certificates-portal-operator "Configure a custom CA certificate bundle or a custom TLS certificate for the automation portal route when your environment uses certificates signed by a private certificate authority.").
- To use an external PostgreSQL database instead of the local instance, create a Secret containing the `POSTGRES_HOST`, `POSTGRES_PORT`, `POSTGRES_USER`, and `POSTGRES_PASSWORD` keys, then set `spec.database.enableLocalDb` to `false` and `spec.database.authSecretName` to the name of that Secret. The database user must have the `CREATEDB` privilege. For guidance on provisioning the external PostgreSQL server and creating the database user, see [Configure an external PostgreSQL database for the automation portal operator](/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-configure_an_external_postgresql_database_for_the_automation_portal_operator#configure-external-database-portal-operator "Configure the automation portal operator to use an external PostgreSQL database instead of the local database instance managed by the Red Hat Developer Hub Operator.").
- To configure GitHub or GitLab OAuth SCM integration, see [Configure source control management provider authentication](/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-configure_authentication_providers_for_the_automation_portal_operator#configure-auth-providers-portal-operator "Configure GitHub or GitLab OAuth to allow the automation portal to access source control repositories on behalf of users.").

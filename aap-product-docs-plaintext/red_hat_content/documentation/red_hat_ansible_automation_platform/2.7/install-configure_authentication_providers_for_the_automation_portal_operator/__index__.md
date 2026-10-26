# Configure source control management provider authentication

Configure GitHub or GitLab OAuth to allow the automation portal to access source control repositories on behalf of users.

## Before you begin

Note:

The automation portal uses AAP as the primary and only sign-in authentication provider. The GitHub and GitLab authentication providers configured in this section do not appear on the sign-in page. These providers enable SCM integration for the execution environment builder feature.

- The automation portal operator installed and running on your OpenShift cluster.
- AAP credentials configured. See [Configure credentials and secrets for the automation portal operator](/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-configure_credentials_and_secrets_for_the_automation_portal_operator#configure-credentials-portal-operator "Configure the Kubernetes Secrets required by the automation portal operator, including AAP OAuth credentials, OCI plugin registry credentials, and optional SCM credentials.").
- Administrator access to your GitHub or GitLab instance to create OAuth applications.

## About this task

Important:

The automation portal operator is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production.

The automation portal supports three authentication providers:

- **AAP (RHAAP)** — the only sign-in method. Users always authenticate to automation portal using their Ansible Automation Platform credentials.
- **GitHub OAuth** — optional. Allows automation portal to access GitHub repositories on behalf of users.
- **GitLab OAuth** — optional. Allows automation portal to access GitLab repositories on behalf of users.

GitHub and GitLab OAuth grant automation portal access to source repositories. This is not a sign-in method — users always sign in with their AAP credentials.

If you already configured a GitHub or GitLab OAuth application for EE Builder, you can reuse the same application. The redirect URI and credentials are the same.

## Procedure

1. **Optional:** To enable GitHub SCM integration, create a GitHub OAuth application if you do not already have one.
1. In GitHub, navigate to **Settings** > **Developer settings** > **OAuth Apps** and click **New OAuth App**.
2. Set the **Authorization callback URL** to your portal URL with the GitHub auth handler path:


```
https://<portal-url>/api/auth/github/handler/frame
```

Replace `<portal-url>` with your portal Route hostname. To retrieve it, run:

```terminal
$ oc get automationportal portal -n automation-portal -o jsonpath='{.status.url}'
```

3. Click **Register application** and note the **Client ID**.
4. Click **Generate a new client secret** and note the value.
For GitHub Enterprise Server, use your server's URL in place of `github.com` and set `spec.scm.github.host` in the custom resource.

2. **Optional:** To enable GitLab SCM integration, create a GitLab OAuth application if you do not already have one.
1. In GitLab, navigate to **Admin Area** > **Applications** (or **User Settings** > **Applications** for group-level access) and click **New application**.
2. Set the **Redirect URI** to:


```
https://<portal-url>/api/auth/gitlab/handler/frame
```

3. Select the following scopes: `read_user`, `openid`, `profile`, `email`.
4. Click **Save application** and note the **Application ID** and **Secret**.
For self-managed GitLab, use your server's URL and set `spec.scm.gitlab.host` in the custom resource.

3. Add the OAuth credentials to your Secrets.
You have two options:

- **Unified SCM Secret** (recommended if you also use SCM integration) — add the OAuth keys to the existing `secrets-scm` Secret. See [Configure credentials and secrets for the automation portal operator](/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-configure_credentials_and_secrets_for_the_automation_portal_operator#configure-credentials-portal-operator "Configure the Kubernetes Secrets required by the automation portal operator, including AAP OAuth credentials, OCI plugin registry credentials, and optional SCM credentials.") for the full key reference.
- **Per-provider Secret** (if you want separate credential management) — create a dedicated Secret for each provider with keys `client-id` and `client-secret`.
To create a per-provider Secret for GitHub:



```terminal
$ oc create secret generic github-oauth-credentials \
--namespace automation-portal \
--from-literal=client-id='<github-client-id>' \
--from-literal=client-secret='<github-client-secret>'
```

To create a per-provider Secret for GitLab:



```terminal
$ oc create secret generic gitlab-oauth-credentials \
--namespace automation-portal \
--from-literal=client-id='<gitlab-application-id>' \
--from-literal=client-secret='<gitlab-secret>'
```

Per-provider Secrets use generic key names (`client-id`, `client-secret`) and override the corresponding keys from the unified SCM Secret.

4. Enable the authentication providers in the `AutomationPortal` custom resource.
**Using the unified SCM Secret** (credentials in `secrets-scm`):



```yaml
spec:
scm:
credentials:
secretRef: secrets-scm
auth:
providers:
github:
enabled: true
gitlab:
enabled: true
```

**Using per-provider Secrets**:



```yaml
spec:
auth:
providers:
github:
enabled: true
credentials:
secretRef: github-oauth-credentials
gitlab:
enabled: true
credentials:
secretRef: gitlab-oauth-credentials
```

5. Apply the updated custom resource.


```terminal
$ oc apply -f portal.yaml -n automation-portal
```

The operator regenerates the Ansible automation portal configuration and restarts the automation portal pod.

## Results

The automation portal can now access GitHub or GitLab repositories on behalf of users. The operator resolves credentials in this order:

1. **Per-provider Secret** (`spec.auth.providers.<provider>.credentials.secretRef`) — highest priority.
2. **Unified SCM Secret** (`spec.scm.credentials.secretRef`) — fallback.
3. **Error** — if neither is configured and the provider is enabled, the `SecretsValid` condition is set to `False`.

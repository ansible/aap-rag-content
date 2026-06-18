# Configure a GitHub App for content discovery

Create and install a GitHub App so that execution environment builder can scan your organization's repositories for Ansible collections.

## Before you begin

- You have owner or admin permissions in your GitHub organization.

## About this task

GitHub Apps provide organization-scoped permissions that do not depend on individual user accounts. Choose this option or a Personal Access Token (PAT) for content discovery. GitHub App and PAT are mutually exclusive.

## Procedure

1.  In a browser, log in to GitHub.
2.  Navigate to your organization settings.
3.  Select **Developer settings > GitHub Apps**.
4.  Click **New GitHub App**.
5.  Enter the following details:

- **GitHub App name:** A descriptive name, for example `ansible-portal-content-discovery`.
- **Homepage URL:** The URL of your automation portal deployment.
- **Webhook:** Clear the **Active** checkbox if you do not require webhook events.
- **Authorization callback URL:** `https://<my_portal_domain>/api/auth/github/handler/frame`

6.  In the **Permissions** section, set the following repository permissions:

- **Contents:** Read-only
- **Actions:** Read-only

7.  In the **Where can this GitHub App be installed?** section, select **Only on this account**.
8.  Click **Create GitHub App**.
9.  Note the **App ID** from the GitHub App settings page.
10.  In the **Private keys** section, click **Generate a private key**. Store the downloaded `.pem` file securely.
11.  In the **Client secrets** section, click **Generate a new client secret**. Save the client secret value immediately — you cannot view it again.
12.  Install the GitHub App in your organization:
1.  On the GitHub App settings page, click **Install App**.
2.  Select your organization.
3.  Select **All repositories** or specific repositories that automation portal requires access to.
4.  Click **Install**.

## Results

On the GitHub App settings page, the **Install App** section shows your organization with an **Installed** status.

## What to do next

After creating the GitHub App, add the credentials and update your configuration. See Create the secrets below.

**Create the secrets**

**OpenShift — CLI:**

```
$ oc create secret generic secrets-scm \
--from-literal=github-app-id=<app_id> \
--from-literal=github-app-client-id=<client_id> \
--from-literal=github-app-client-secret=<client_secret> \
--from-literal=github-app-private-key="$(cat <path_to_private_key>.pem)" \
-n <namespace>
```
**OpenShift — web console:**

1. Navigate to **Workloads > Secrets > Create > Key/value secret**.
2. Set the name to `secrets-scm`.
3. Add keys: `github-app-id`, `github-app-client-id`, `github-app-client-secret`, `github-app-private-key` (paste the `.pem` file contents as the value).


**RHEL appliance:**

```
$ echo -n '<app_id>' | sudo podman secret create portal_github_app_id -
$ echo -n '<client_id>' | sudo podman secret create portal_github_app_client_id -
$ echo -n '<client_secret>' | sudo podman secret create portal_github_app_client_secret -
$ sudo podman secret create portal_github_app_private_key <path_to_private_key>.pem
```
Create (or update) the Quadlet drop-in file so the portal container can read these secrets as environment variables:

```
$ sudo tee /etc/containers/systemd/portal.container.d/ee-builder-secrets.conf << 'EOF'
[Container]
Secret=portal_github_app_id,type=env,target=GITHUB_APP_ID
Secret=portal_github_app_client_id,type=env,target=GITHUB_APP_CLIENT_ID
Secret=portal_github_app_client_secret,type=env,target=GITHUB_APP_CLIENT_SECRET
Secret=portal_github_app_private_key,type=env,target=GITHUB_APP_PRIVATE_KEY
EOF
```


Note:

All EE Builder secrets use a single drop-in file (`ee-builder-secrets.conf`). If you configure additional SCM integrations later (for example, GitHub OAuth or GitLab OAuth), append the new `Secret=` lines to this file.

**Update the Helm chart configuration**

In your Helm chart configuration, update the `integrations.github` section. The PAT and GitHub App configurations are mutually exclusive:

```
upstream:
backstage:
appConfig:
integrations:
github:
## Option A: PAT-based integration (default)
- host: github.com
token: ${GITHUB_TOKEN}

## Option B: GitHub App integration (recommended)
## To use GitHub App, comment out the token line above
## and uncomment the following block:
# - host: github.com
#   apps:
#     - appId: ${GITHUB_APP_ID}
#       clientId: ${GITHUB_APP_CLIENT_ID}
#       clientSecret: ${GITHUB_APP_CLIENT_SECRET}
#       privateKey: ${GITHUB_APP_PRIVATE_KEY}
```


Important:

Configure either a PAT or a GitHub App, not both. If using a GitHub App, comment out the `token` line and uncomment the `apps` block.

**RHEL appliance:** Add the equivalent `integrations.github` block to `/etc/portal/configs/app-config/app-config.production.yaml` (without the `upstream.backstage.appConfig` nesting):

```
integrations:
github:
- host: github.com
apps:
- appId: ${GITHUB_APP_ID}
clientId: ${GITHUB_APP_CLIENT_ID}
clientSecret: ${GITHUB_APP_CLIENT_SECRET}
privateKey: ${GITHUB_APP_PRIVATE_KEY}
```
The `${...}` references are resolved from the Podman secrets you created above, through the Quadlet drop-in.

Important:

Adding an `integrations:` section to `app-config.production.yaml` replaces the auto-generated PAT-based integration from cloud-init. If you are switching from a PAT to a GitHub App, the PAT is no longer used for content discovery. To keep both, include the PAT configuration alongside the GitHub App in your `integrations:` block:

```
integrations:
github:
- host: github.com
token: ${GITHUB_TOKEN}
apps:
- appId: ${GITHUB_APP_ID}
clientId: ${GITHUB_APP_CLIENT_ID}
clientSecret: ${GITHUB_APP_CLIENT_SECRET}
privateKey: ${GITHUB_APP_PRIVATE_KEY}
```
**Configure CORS for self-hosted GitHub Enterprise**

If the `host` is a self-hosted GitHub Enterprise instance (not `github.com`), add its URL to the CORS allowed origins so that OAuth redirects are accepted.

**OpenShift:**

```
upstream:
backstage:
appConfig:
backend:
cors:
origin:
- ${BASE_URL}
- https://github.internal.example.com
```
**RHEL appliance** — add to the existing `backend:` block in `app-config.production.yaml`:

```
backend:
cors:
origin:
- "https://portal.example.com"
- "https://github.internal.example.com"
```


Important:

On RHEL appliances, `app.baseUrl`, `backend.baseUrl`, and `backend.cors.origin` must all use the same portal URL. If any of these values are inconsistent, OAuth callbacks and API requests fail. Do not create a duplicate `backend:` block — add `cors` to the existing one.

Note:

If you only use `github.com`, no CORS changes are needed.

For a complete working example of all settings in context, see [Complete Helm chart values reference](/documentation/en-us/red_hat_ansible_automation_platform/2.7/develop-ref_ee_builder_helm_values "A complete Helm chart values configuration for execution environment builder with GitHub App authentication, content discovery, and private automation hub enabled.").

# Automation portal operator configuration reference

Reference for all `AutomationPortal` custom resource fields, including Ansible Automation Platform (AAP) connectivity, SCM integration, authentication providers, plugins, infrastructure, and status conditions.

Important:

The automation portal operator is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production.

## AAP configuration

| Field                            | Type   | Default | Description                                                                                                                                                                                              |
| -------------------------------- | ------ | ------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `spec.aap.host`                  | string | --      | AAP base URL. Resolved from the credentials Secret`aap-host-url` key if empty.                                                                                                                           |
| `spec.aap.checkSSL`              | bool   | `true`  | Validate SSL certificates for AAP connections. Default is`true`. If your AAP instance uses a private CA or self-signed certificate, configure`spec.backstage.caCertificates.secretRef` to provide the CA certificate. Set`checkSSL` to`false` only if you cannot provide the CA certificate. |
| `spec.aap.credentials.secretRef` | string | --      | **Required.** Name of the Secret with keys:`aap-host-url`,`oauth-client-id`,`oauth-client-secret`,`aap-token`.                                                                                           |

## SCM configuration

| Field                            | Type   | Default      | Description                                               |
| -------------------------------- | ------ | ------------ | --------------------------------------------------------- |
| `spec.scm.credentials.secretRef` | string | --           | Unified Secret for all SCM and auth credentials.          |
| `spec.scm.github.enabled`        | bool   | `false`      | Enable GitHub SCM integration.                            |
| `spec.scm.github.host`           | string | `github.com` | GitHub server hostname.                                   |
| `spec.scm.github.authType`       | string | `app`        | Authentication method:`token` (PAT) or`app` (GitHub App). |
| `spec.scm.gitlab.enabled`        | bool   | `false`      | Enable GitLab SCM integration.                            |
| `spec.scm.gitlab.host`           | string | `gitlab.com` | GitLab server hostname.                                   |

## Authentication providers

| Field                                              | Type   | Default | Description                                                                           |
| -------------------------------------------------- | ------ | ------- | ------------------------------------------------------------------------------------- |
| `spec.auth.providers.github.enabled`               | bool   | `false` | Enable GitHub SCM integration.                                                        |
| `spec.auth.providers.github.credentials.secretRef` | string | --      | Per-provider auth Secret. Overrides the SCM secret. Keys:`client-id`,`client-secret`. |
| `spec.auth.providers.gitlab.enabled`               | bool   | `false` | Enable GitLab SCM integration.                                                        |
| `spec.auth.providers.gitlab.credentials.secretRef` | string | --      | Per-provider auth Secret. Overrides the SCM secret. Keys:`client-id`,`client-secret`. |

## Base configuration

| Field                                      | Type                       | Default               | Description                                                                                                                                                                                              |
| ------------------------------------------ | -------------------------- | --------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `spec.backstage.image.registry`            | string                     | `registry.redhat.io`  | Container image registry.                                                                                                                                                                                |
| `spec.backstage.image.repository`          | string                     | `rhdh/rhdh-hub-rhel9` | Container image repository.                                                                                                                                                                              |
| `spec.backstage.image.tag`                 | string                     | `1.10`                | Container image tag.                                                                                                                                                                                     |
| `spec.backstage.replicas`                  | int                        | --                    | Number of pod replicas. Unset lets the Operator manage scaling.                                                                                                                                          |
| `spec.backstage.resources`                 | ResourceRequirements       | --                    | CPU and memory requests and limits for the automation portal container.                                                                                                                                  |
| `spec.backstage.nodeSelector`              | map[string]string          | --                    | Schedule pods on nodes with matching labels.                                                                                                                                                             |
| `spec.backstage.tolerations`               | []Toleration               | --                    | Tolerate node taints.                                                                                                                                                                                    |
| `spec.backstage.affinity`                  | Affinity                   | --                    | Pod scheduling constraints (node and pod affinity).                                                                                                                                                      |
| `spec.backstage.topologySpreadConstraints` | []TopologySpreadConstraint | --                    | Distribute pods across topology domains.                                                                                                                                                                 |
| `spec.backstage.priorityClassName`         | string                     | --                    | Pod scheduling priority class.                                                                                                                                                                           |
| `spec.backstage.route.enabled`             | bool                       | `true`                | Create an OpenShift Route.                                                                                                                                                                               |
| `spec.backstage.route.host`                | string                     | --                    | Custom Route hostname. Auto-derived from cluster ingress domain if empty.                                                                                                                                |
| `spec.backstage.route.tls.secretRef`       | string                     | --                    | Secret containing TLS certificate data. Keys:`tls.crt`,`tls.key`,`ca.crt` (optional).                                                                                                                    |
| `spec.backstage.caCertificates.secretRef`  | string                     | --                    | Name of a Kubernetes Secret containing CA certificates for private registries and internal services. The operator mounts the certificates in the Ansible automation portal containers. Use this in environments with self-signed certificates or private CAs instead of disabling SSL verification. See**Configure custom TLS certificates for the automation portal operator**. |

## Database configuration

| Field                          | Type   | Default | Description                                                                                                                                                                                              |
| ------------------------------ | ------ | ------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `spec.database.enableLocalDb`  | bool   | `true`  | Deploy a local PostgreSQL instance.                                                                                                                                                                      |
| `spec.database.authSecretName` | string | --      | Secret for external database authentication. Required when`enableLocalDb` is`false`. Keys:`POSTGRES_HOST`,`POSTGRES_PORT`,`POSTGRES_USER`,`POSTGRES_PASSWORD`. The database user must have the`CREATEDB` privilege. The operator creates application databases during deployment and cannot proceed without this privilege. |

## DevTools configuration

| Field                            | Type                 | Default                                                  | Description                              |
| -------------------------------- | -------------------- | -------------------------------------------------------- | ---------------------------------------- |
| `spec.devtools.enabled`          | bool                 | `true`                                                   | Deploy the Ansible DevTools sidecar.     |
| `spec.devtools.image.registry`   | string               | `registry.redhat.io`                                     | DevTools image registry.                 |
| `spec.devtools.image.repository` | string               | `ansible-automation-platform-27/ansible-dev-tools-rhel9` | DevTools image repository.               |
| `spec.devtools.image.tag`        | string               | `latest`                                                 | DevTools image tag.                      |
| `spec.devtools.resources`        | ResourceRequirements | --                                                       | CPU and memory for the DevTools sidecar. |

## Automation portal plug-ins configuration

| Field                                             | Type     | Default                                                                       | Description                                                                                                                                                                                              |
| ------------------------------------------------- | -------- | ----------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `spec.plugins.registry`                           | string   | `registry.redhat.io`                                                          | OCI plugin image registry.                                                                                                                                                                               |
| `spec.plugins.ociPluginImage`                     | string   | --                                                                            | Full OCI plugin image path. Overrides`registry`.                                                                                                                                                         |
| `spec.plugins.ghcrRegistry`                       | string   | `ghcr.io`                                                                     | GHCR registry for community auth plugins. Override for air-gapped deployments.                                                                                                                           |
| `spec.plugins.overrides`                          | []string | --                                                                            | Built-in plugin slots to disable. Valid values:`selfService`,`catalog`,`rbac`,`scaffolder`,`lightspeed`. To replace a built-in plugin, list its slot name here and supply the replacement with`spec.plugins.customPluginsRef`. |
| `spec.plugins.customPluginsRef`                   | string   | --                                                                            | Name of a ConfigMap containing additional dynamic plugin entries. The ConfigMap must be in the same namespace as the`AutomationPortal` custom resource and contain a`dynamic-plugins.yaml` key. Entries are merged with the built-in plugins. |
| `spec.plugins.customAppConfigRef`                 | string   | --                                                                            | Name of a ConfigMap containing additional Backstage app-config YAML. Loaded after the operator-generated app-config, so its values override the operator defaults.                                       |
| `spec.plugins.selfService.enabled`                | bool     | `true`                                                                        | Self-service plugin.                                                                                                                                                                                     |
| `spec.plugins.catalog.enabled`                    | bool     | `true`                                                                        | Catalog plugin.                                                                                                                                                                                          |
| `spec.plugins.catalog.syncInterval`               | int      | `60`                                                                          | Catalog sync frequency in minutes.                                                                                                                                                                       |
| `spec.plugins.catalog.templateBaseURL`            | string   | `https://github.com/ansible/ansible-rhdh-templates/blob/<version>/templates/` | Overrides the base URL for the built-in Ansible scaffold templates (`ee-start-from-scratch`,`ee-cloud-automation`,`ee-network-automation`). Set this to an internal mirror URL for air-gapped environments where github.com is unreachable. The URL must end with a trailing slash and point to a directory containing the same template YAML files as the default path. See*Deploy automation portal in disconnected environments*. |
| `spec.plugins.catalog.additionalTemplateURLs`     | []string | --                                                                            | A list of extra scaffold template URLs to add to the catalog alongside the built-in Ansible templates. Each entry must be a fully qualified URL to a template definition YAML file, for example from an internal source control server or mirror. The host of each URL is automatically allowed for reading. Maximum 50 entries. |
| `spec.plugins.catalog.skipTlsVerifyForHosts`      | []string | --                                                                            | Hostnames to skip TLS verification for. No wildcards. Maximum 10 entries.                                                                                                                                |
| `spec.plugins.catalog.jobTemplates.enabled`       | bool     | `true`                                                                        | Sync job templates from AAP.                                                                                                                                                                             |
| `spec.plugins.catalog.jobTemplates.labels`        | []string | --                                                                            | Only sync templates with all of these labels.                                                                                                                                                            |
| `spec.plugins.catalog.jobTemplates.excludeLabels` | []string | --                                                                            | Exclude templates with any of these labels.                                                                                                                                                              |
| `spec.plugins.catalog.collections.enabled`        | bool     | `false`                                                                       | Sync PAH and Galaxy collections.                                                                                                                                                                         |
| `spec.plugins.catalog.gitContents.enabled`        | bool     | `false`                                                                       | Discover Ansible content from Git repositories.                                                                                                                                                          |
| `spec.plugins.rbac.enabled`                       | bool     | `true`                                                                        | RBAC plugin.                                                                                                                                                                                             |
| `spec.plugins.scaffolder.enabled`                 | bool     | `true`                                                                        | Scaffolder plugin.                                                                                                                                                                                       |
| `spec.plugins.lightspeed.enabled`                 | bool     | `false`                                                                       | Lightspeed AI plugin.                                                                                                                                                                                    |

## Permissions

| Field                         | Type     | Default                                        | Description                  |
| ----------------------------- | -------- | ---------------------------------------------- | ---------------------------- |
| `spec.permissions.enabled`    | bool     | --                                             | Enable RBAC permissions.     |
| `spec.permissions.adminUsers` | []string | `user:default/admin, group:default/aap-admins` | RBAC admin users and groups. |
| `spec.permissions.superUsers` | []string | `user:default/admin`                           | RBAC super users.            |

## Status fields

| Field                | Type        | Description                                                                    |
| -------------------- | ----------- | ------------------------------------------------------------------------------ |
| `status.phase`       | string      | Current lifecycle phase:`Pending`,`Running`,`Failed`.                          |
| `status.url`         | string      | Portal access URL from the OpenShift Route.                                    |
| `status.version`     | string      | Deployed portal version.                                                       |
| `status.backstageCR` | string      | Name of the managed custom resource.                                           |
| `status.conditions`  | []Condition | Detailed status conditions. See*Troubleshoot your portal operator deployment*. |

## Examples

The smallest valid custom resource requires only the AAP credentials Secret:

```yaml
apiVersion: automationportal.aap.redhat.com/v1alpha1
kind: AutomationPortal
metadata:
name: portal
spec:
aap:
credentials:
secretRef: secrets-rhaap-portal
```

A complete custom resource with GitHub App integration, external database, custom TLS, and DevTools enabled:

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
authType: app
auth:
providers:
github:
enabled: true
plugins:
registry: registry.redhat.io
catalog:
syncInterval: 120
gitContents:
enabled: true
collections:
enabled: true
backstage:
replicas: 2
image:
tag: "1.10"
route:
tls:
secretRef: portal-tls
resources:
requests:
cpu: "500m"
memory: "1Gi"
limits:
cpu: "2"
memory: "4Gi"
database:
enableLocalDb: false
authSecretName: portal-db-credentials
devtools:
enabled: true
permissions:
enabled: true
```

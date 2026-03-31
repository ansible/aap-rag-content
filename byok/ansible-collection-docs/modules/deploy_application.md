---
title: "Module: mycompany.infrastructure.deploy_application"
url: "https://github.com/ansible/aap-rag-content/blob/main/byok/ansible-collection-docs/modules/deploy_application.md"
---
# Module: mycompany.infrastructure.deploy_application

**Short description:** Deploy or update an application on a target environment
**Collection:** mycompany.infrastructure
**Version added:** 1.2.0

---

## Synopsis

- Deploys or updates a containerised or package-based application to a target compute environment (ECS, AKS, GKE, or bare-metal/VM via RPM/DEB packages).
- For container-based targets, pulls the specified `image` from an internal container registry and updates the running service with a zero-downtime rolling deployment.
- For package-based targets, installs or upgrades the specified `package` using the system package manager.
- Supports automatic rollback via the `rollback_on_failure` option, which redeploys the previous version if health checks fail.

---

## Requirements

The following must be installed on the host executing this module:

- python >= 3.9
- boto3 >= 1.26 *(for `target=ecs`)*
- kubernetes >= 26.1 *(for `target=aks` or `target=gke`)*
- requests >= 2.28

---

## Parameters

| Parameter | Type | Required | Default | Choices | Description |
|---|---|---|---|---|---|
| `name` | string | yes | | | Name of the application service or unit to deploy. |
| `target` | string | yes | | `ecs`, `aks`, `gke`, `vm` | Deployment target type. `ecs` = AWS Elastic Container Service. `aks` = Azure Kubernetes Service. `gke` = Google Kubernetes Engine. `vm` = bare-metal or VM via SSH and package manager. |
| `image` | string | no | | | Container image reference including tag (e.g. `registry.mycompany.example/myapp:1.4.2`). Required for `ecs`, `aks`, `gke` targets. |
| `package` | string | no | | | RPM or DEB package name and optional version (e.g. `myapp-1.4.2`). Required for `vm` target. |
| `environment` | string | no | `production` | `development`, `staging`, `production` | Logical environment used to look up cluster and namespace configuration. |
| `replicas` | integer | no | `2` | | Desired replica count. Applies to container targets only; ignored for `vm`. |
| `env_vars` | dictionary | no | `{}` | | Environment variables to set in the deployed container or service unit. For `vm` targets, written to a systemd drop-in environment file. *(Added in 1.3.0)* |
| `health_check_path` | string | no | `/healthz` | | HTTP path used for post-deployment health checks. The module polls this endpoint until it returns HTTP 200 or until `health_check_timeout` is reached. |
| `health_check_timeout` | integer | no | `120` | | Seconds to wait for health checks to pass after deployment. |
| `rollback_on_failure` | boolean | no | `true` | `true`, `false` | Automatically roll back to the previous deployed version if health checks fail. |
| `state` | string | no | `present` | `present`, `absent` | `present` deploys or updates the application. `absent` removes the deployment. |

---

## Attributes

| Attribute | Support | Description |
|---|---|---|
| check_mode | partial | Validates configuration and connectivity but does not perform the actual deployment. |
| diff_mode | partial | Shows image/package version diff only. |
| platform | all | No target-host OS restrictions (depends on `target` type). |

---

## Notes

- For ECS deployments, the task definition is updated in-place with the new image. The previous task definition revision is preserved for rollback purposes.
- For Kubernetes targets (`aks`, `gke`), the module performs a rolling update by patching the `Deployment` manifest. PodDisruptionBudgets are respected.
- The `rollback_on_failure` option only applies to the deployment step. A failed rollback will not trigger a further automatic rollback.
- When `state=absent` for Kubernetes targets, the `Deployment`, `Service`, and `HorizontalPodAutoscaler` resources are all deleted.

---

## See Also

- [create_server](create_server.md) — Provision the VM target before using this module with `target=vm`.
- [vault_secret lookup](../lookup/vault_secret.md) — Retrieve registry credentials or API tokens needed for deployment.

---

## Examples

```yaml
# Deploy a containerised app to ECS production
- name: Deploy myapp to ECS
  mycompany.infrastructure.deploy_application:
    name: myapp-api
    target: ecs
    environment: production
    image: "registry.mycompany.example/myapp:{{ app_version }}"
    replicas: 4
    env_vars:
      LOG_LEVEL: info
      DB_HOST: "{{ db_result.database.endpoint }}"
    health_check_path: /api/healthz
    health_check_timeout: 180
    rollback_on_failure: true
    state: present
  register: deploy_result

# Deploy a package-based app to a VM
- name: Deploy RPM package to VM
  mycompany.infrastructure.deploy_application:
    name: myapp-worker
    target: vm
    environment: staging
    package: "myapp-worker-{{ app_version }}"
    env_vars:
      WORKER_CONCURRENCY: "4"
      QUEUE_URL: "{{ queue_url }}"
    health_check_path: /status
    state: present

# Remove a deployment from staging
- name: Remove staging deployment
  mycompany.infrastructure.deploy_application:
    name: myapp-api
    target: gke
    environment: staging
    state: absent
```

---

## Return Values

| Key | Description | Returned | Type |
|---|---|---|---|
| `deployment` | Details of the deployment result. | when `state=present` | dict |
| `deployment.name` | Application service name. | always | string |
| `deployment.image` | Container image deployed. | container targets | string — e.g. `"registry.mycompany.example/myapp:1.4.2"` |
| `deployment.package` | Package name and version deployed. | VM targets | string — e.g. `"myapp-worker-1.4.2"` |
| `deployment.replicas` | Number of running replicas after deployment. | container targets | integer |
| `deployment.previous_image` | Previous container image; available for manual rollback reference. | container targets when a prior state existed | string |
| `deployment.health_check_status` | HTTP status code returned by the health check endpoint. | always | integer — e.g. `200` |
| `deployment.rolled_back` | Whether an automatic rollback was triggered. | always | bool |
| `changed` | Whether the deployment resulted in changes. | always | bool |

---

## Authors

- Alice Nguyen (@alice-n) — alice.nguyen@mycompany.example
- Bob Ramirez (@bob-r) — bob.ramirez@mycompany.example
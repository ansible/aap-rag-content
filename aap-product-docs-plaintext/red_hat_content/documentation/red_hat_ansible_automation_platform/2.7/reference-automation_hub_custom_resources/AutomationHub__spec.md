# Automation hub custom resources
## AutomationHub [automationhub.ansible.com/v1beta1]
### Specification

| Field                           | Type   | Description                                                                                                                        | Default        |
| ------------------------------- | ------ | ---------------------------------------------------------------------------------------------------------------------------------- | -------------- |
| `image_pull_policy`             | String | Image pull policy for automation hub pods. Options: `Always`, `Never`, `IfNotPresent`.                                             | `IfNotPresent` |
| `postgres_configuration_secret` | String | Name of a Kubernetes secret containing external PostgreSQL connection details for the automation hub database.                     | -              |
| `storage_type`                  | String | Storage backend type for automation hub content. Options: `file`, `S3`, `azure`.                                                   | -              |
| `file_storage_storage_class`    | String | Kubernetes storage class for file-based storage. Must support `ReadWriteMany` access mode. Required when `storage_type` is `file`. | -              |
| `file_storage_size`             | String | Size of the persistent volume for file-based storage, for example `50Gi`. Required when `storage_type` is `file`.                  | -              |
| `object_storage_s3_secret`      | String | Name of a Kubernetes secret containing S3-compatible object storage credentials. Required when `storage_type` is `S3`.             | -              |
| `object_storage_azure_secret`   | String | Name of a Kubernetes secret containing Azure Blob Storage credentials. Required when `storage_type` is `azure`.                    | -              |
| `pulp_settings`                 | Object | Custom Pulp configuration settings as key-value pairs, for example `MAX_PAGE_SIZE` or `cache_enabled`.                             | -              |
| `api`                           | Object | Automation hub API pod configuration. Contains `replicas` (Integer) and `resource_requirements` (Object).                          | 1 replica      |
| `content`                       | Object | Automation hub content pod configuration. Contains `replicas` (Integer) and `resource_requirements` (Object).                      | 1 replica      |
| `worker`                        | Object | Automation hub worker pod configuration. Contains `replicas` (Integer) and `resource_requirements` (Object).                       | 1 replica      |
| `web`                           | Object | Automation hub web pod configuration. Contains `replicas` (Integer) and `resource_requirements` (Object).                          | 1 replica      |
| `redis`                         | Object | Automation hub Redis pod configuration. Contains `replicas` (Integer) and `resource_requirements` (Object).                        | 1 replica      |


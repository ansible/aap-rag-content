# Operator enterprise topology
## Example custom resource file

For example CR files, see the [ocp-b.env-a](https://github.com/ansible/test-topologies/blob/aap-2.5/ocp-b.env-a/README.md) directory in the `test-topologies` GitHub repository.

The following example shows an AnsibleAutomationPlatform custom resource configured for enterprise topology with external databases.

```
apiVersion: aap.ansible.com/v1alpha1
kind: AnsibleAutomationPlatform
metadata:
name: aap
namespace: aap
spec:
controller:
postgres_configuration_secret: <controller-db-secret>

hub:
storage_type: s3
object_storage_s3_secret: <s3-secret>

eda:
automation_server_ssl_verify: "no"

metrics:
database:
database_secret: aap-metrics-postgres-configuration
externally_managed: true
ms_awx_readonly_user_secret: aap-metrics-read-token
ms_awx_readonly_user:
externally_managed: true
```


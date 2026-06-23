# Configure an external database for Ansible Automation Platform
## Configure an external database for automation hub on Red Hat Ansible Automation Platform Operator

For users who prefer to deploy Ansible Automation Platform with an external database, they can do so by configuring a secret with instance credentials and connection information, then applying it to their cluster using the `oc create` command.

### Before you begin

The external database must be a PostgreSQL database that is the version supported by the current release of Ansible Automation Platform. The external postgres instance credentials and connection information will need to be stored in a secret, which will then be set on the automation hub spec.

Note:

Ansible Automation Platform supports PostgreSQL 15 for its managed databases and additionally supports PostgreSQL 15, 16, and 17 for external databases.

If you choose to use an externally managed database with version 16 or 17 you must also rely on external backup and restore processes.

### About this task

By default, the Ansible Automation Platform Operator automatically creates and configures a managed PostgreSQL pod in the same namespace as your Ansible Automation Platform deployment.

You can choose to use an external database instead if you prefer to use a dedicated node to ensure dedicated resources or to manually manage backups, upgrades, or performance tweaks.

Note:

The same external database (PostgreSQL instance) can be used for both automation hub, automation controller, and platform gateway as long as the database names are different. In other words, you can have multiple databases with different names inside a single PostgreSQL instance.

The following section outlines the steps to configure an external database for your automation hub on a Ansible Automation Platform Operator.

### Procedure

1.  Create a `postgres_configuration_secret` YAML file, following the template below:


```
apiVersion: v1
kind: Secret
metadata:
name: external-postgres-configuration
namespace: <target_namespace> ①
stringData:
host: "<external_ip_or_url_resolvable_by_the_cluster>" ②
port: "<external_port>" ③
database: "<desired_database_name>"
username: "<username_to_connect_as>"
password: "<password_to_connect_with>" ④
sslmode: "prefer" ⑤
type: "unmanaged"
type: Opaque
```
1.  Namespace to create the secret in. This should be the same namespace you want to deploy to.
2.  The resolvable hostname for your database node.
3.  External port defaults to `5432`.
4.  Value for variable `password` should not contain single or double quotes (', ") or backslashes (\) to avoid any issues during deployment, backup or restoration.
5.  The variable `sslmode` is valid for `external` databases only. The allowed values are: `prefer`, `disable`, `allow`, `require`, `verify-ca`, and `verify-full`.

2.  Apply `external-postgres-configuration-secret.yml` to your cluster using the `oc create` command.

```
$ oc create -f external-postgres-configuration-secret.yml
```

3.  When creating your `AnsibleAutomationPlatform` custom resource object, specify the secret under the `hub` section in your spec, following the example below:


```
apiVersion: aap.ansible.com/v1alpha1
kind: AnsibleAutomationPlatform
metadata:
name: myaap
spec:
hub:
name: hub-dev  # Optional: specify existing instance or custom name
postgres_configuration_secret: external-postgres-configuration
storage_type: file
file_storage_storage_class: <your-read-write-many-storage-class>
file_storage_size: 10Gi
```

Note:
If you have an existing automation hub instance, specify its name under `hub.name` to apply these settings to the existing instance. If you omit the `name` field, the operator will create a new instance with the default name pattern `<aap-instance-name>-hub`.

For more examples of Ansible Automation Platform custom resources, see [Red Hat Ansible Automation Platform custom resources](/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-assembly_appendix_operator_crs#appendix-operator-crs_appendix-operator-crs "This appendix provides a reference for the Ansible Automation Platform custom resources for various deployment scenarios.")


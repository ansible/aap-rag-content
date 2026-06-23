# Configure an external database for Ansible Automation Platform
## Configure an external database for automation controller on Red Hat Ansible Automation Platform Operator

For users who prefer to deploy Ansible Automation Platform with an external database, they can do so by configuring a secret with instance credentials and connection information, then applying it to their cluster using the `oc create` command.

### Before you begin

The external database must be a PostgreSQL database that is the version supported by the current release of Ansible Automation Platform. The external postgres instance credentials and connection information must be stored in a secret, which is then set on the automation controller spec.

Note:

Ansible Automation Platform supports PostgreSQL 15 for its managed databases and additionally supports PostgreSQL 15, 16, and 17 for external databases.

If you choose to use an externally managed database with version 16 or 17 you must also rely on external backup and restore processes.

### About this task

By default, the Ansible Automation Platform Operator automatically creates and configures a managed PostgreSQL pod in the same namespace as your Ansible Automation Platform deployment. You can deploy Ansible Automation Platform with an external database instead of the managed PostgreSQL pod that the Ansible Automation Platform Operator automatically creates.

Using an external database lets you share and reuse resources and manually manage backups, upgrades, and performance optimizations.

Note:

The same external database (PostgreSQL instance) can be used for both automation hub, automation controller, platform gateway, and metrics service as long as the database names are different. In other words, you can have multiple databases with different names inside a single PostgreSQL instance.

The following section outlines the steps to configure an external database for your automation controller on a Ansible Automation Platform Operator.

### Procedure

1.  Create a `postgres_configuration_secret` YAML file, following the template below:


```
apiVersion: v1
kind: Secret
metadata:
name: external-postgres-configuration
namespace: <target_namespace>
stringData:
host: "<external_ip_or_url_resolvable_by_the_cluster>"
port: "<external_port>"
database: "<desired_database_name>"
username: "<username_to_connect_as>"
password: "<password_to_connect_with>"
sslmode: "prefer"
type: "unmanaged"
type: Opaque
```
When configuring the secret:

- `namespace`: Specify the namespace to create the secret in. This should be the same namespace you want to deploy to.
- `host`: Specify the resolvable hostname for your database node.
- `port`: Specify the external port. The default is `5432`.
- `password`: Ensure the password does not contain single or double quotes (', ") or backslashes (\) to avoid any issues during deployment, backup or restoration.
- `sslmode`: This variable is valid for external databases only. The allowed values are: `prefer`, `disable`, `allow`, `require`, `verify-ca`, and `verify-full`.

2.  Apply `external-postgres-configuration-secret.yml` to your cluster using the `oc create` command.

```
$ oc create -f external-postgres-configuration-secret.yml
```

3.  When creating your `AnsibleAutomationPlatform` custom resource object, specify the secret under the `controller` section in your spec, following the example below:


```
apiVersion: aap.ansible.com/v1alpha1
kind: AnsibleAutomationPlatform
metadata:
name: myaap
spec:
controller:
name: controller-dev  # Optional: specify existing instance or custom name
postgres_configuration_secret: external-postgres-configuration
```

Note:
If you have an existing automation controller instance, specify its name under `controller.name` to apply these settings to the existing instance. If you omit the `name` field, the operator will create a new instance with the default name pattern `<aap-instance-name>-controller`.

For more examples of Ansible Automation Platform custom resources, see [Red Hat Ansible Automation Platform custom resources](/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-assembly_appendix_operator_crs#appendix-operator-crs_appendix-operator-crs "This appendix provides a reference for the Ansible Automation Platform custom resources for various deployment scenarios.")


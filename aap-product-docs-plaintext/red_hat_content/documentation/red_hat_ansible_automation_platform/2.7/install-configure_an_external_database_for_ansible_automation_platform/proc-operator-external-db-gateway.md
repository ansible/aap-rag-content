# Configure an external database for Ansible Automation Platform
## Configure an external database for platform gateway on Red Hat Ansible Automation Platform Operator

There are two scenarios for deploying Ansible Automation Platform with an external database:

### Before you begin

The external database must be a PostgreSQL database that is the version supported by the current release of Ansible Automation Platform. The external postgres instance credentials and connection information must be stored in a secret, which is then set on the platform gateway spec.

Note:

Ansible Automation Platform supports PostgreSQL 15 for its managed databases and additionally supports PostgreSQL 15, 16, and 17 for external databases.

If you choose to use an externally managed database with version 16 or 17 you must also rely on external backup and restore processes.

### About this task

| Scenario                              | Action required                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| ------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| <br>Fresh install                     | <br>You must specify a single external database instance for the platform to use for the following:<br>Platform gatewayAutomation controllerAutomation hubEvent-Driven AnsibleMetrics serviceRed Hat Ansible Lightspeed (If enabled)<br>See the *aap-configuring-external-db-all-default-components.yml* example in the [Custom resources](/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-assembly_appendix_operator_crs#unique_2099983463 "Refer to the following custom resources you can use for various Ansible Automation Platform deployment scenarios.") section for help with this.<br>If using Red Hat Ansible Lightspeed, use the *aap-configuring-external-db-with-lightspeed-enabled.yml* example. |
| <br>Existing external database in 2.4 | <br>Your existing external database remains the same after upgrading but you must specify the `external-postgres-configuration-gateway` (spec.database.database\_secret) on the Ansible Automation Platform custom resource.<br>For detailed steps, see [Upgrading an external database for platform gateway on on Ansible Automation Platform](/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-configure_an_external_database_for_ansible_automation_platform#GUID-b94a38e1-9266-4338-a29a-1fd21ee08f5a "To upgrade from Ansible Automation Platform 2.4 to 2.6 with an external database, you must scale down your Operator deployment, upgrade your PostgreSQL, then scale your deployment back up.")        |


To deploy Ansible Automation Platform with an external database, you must first create a Kubernetes secret with credentials for connecting to the database.

By default, the Ansible Automation Platform Operator automatically creates and configures a managed PostgreSQL pod in the same namespace as your Ansible Automation Platform deployment. You can deploy Ansible Automation Platform with an external database instead of the managed PostgreSQL pod that the Ansible Automation Platform Operator automatically creates.

Using an external database lets you share and reuse resources and manually manage backups, upgrades, and performance optimizations.

Note:

The same external database (PostgreSQL instance) can be used for both automation hub, automation controller, platform gateway, and metrics service as long as the database names are different. In other words, you can have multiple databases with different names inside a single PostgreSQL instance.

The following section outlines the steps to configure an external database for your platform gateway on a Ansible Automation Platform Operator.

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
type: "unmanaged"
type: Opaque
```
Where:

<target_namespace>
Namespace to create the secret in. This should be the same namespace you want to deploy to.

<external_ip_or_url_resolvable_by_the_cluster>
The resolvable hostname for your database node.

<external_port>
External port defaults to `5432`.

<password_to_connect_with>
Value for variable `password` should not contain single or double quotes (', ") or backslashes (\) to avoid any issues during deployment, backup or restoration.

2.  Apply `external-postgres-configuration-secret.yml` to your cluster using the `oc create` command.

```
$ oc create -f external-postgres-configuration-secret.yml
```
Note:
The following example is for a platform gateway deployment. To configure an external database for all components, use the *aap-configuring-external-db-all-default-components.yml* example in the [Custom resources](/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-assembly_appendix_operator_crs#unique_2099983463 "Refer to the following custom resources you can use for various Ansible Automation Platform deployment scenarios.") section.

3.  When creating your `AnsibleAutomationPlatform` custom resource object, specify the secret on your spec, following the example below:


```
apiVersion: aap.ansible.com/v1alpha1
kind: AnsibleAutomationPlatform
metadata:
name: example-aap
Namespace: aap
spec:
database:
database_secret: automation-platform-postgres-configuration
```


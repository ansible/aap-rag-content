# 5. Configuring Red Hat Ansible Automation Platform components on Red Hat Ansible Automation Platform Operator
## 5.1. Configuring platform gateway on Red Hat OpenShift Container Platform web console
### 5.1.1. Configuring an external database for platform gateway on Red Hat Ansible Automation Platform Operator

There are two scenarios for deploying Ansible Automation Platform with an external database:

| <br>  Scenario | <br>  Action required |
| --- | --- |
| <br>  Fresh install | <br>  You must specify a single external database instance for the platform to use for the following:    <br>  Platform gateway   Automation controller   Automation hub   Event-Driven Ansible   Red Hat Ansible Lightspeed (If enabled) <br>  See the *aap-configuring-external-db-all-default-components.yml* example in the [14.1. Custom resources](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html-single/installing_on_openshift_container_platform/index#operator-crs) section for help with this. <br>  If using Red Hat Ansible Lightspeed, use the *aap-configuring-external-db-with-lightspeed-enabled.yml* example. |
| <br>  Existing external database in 2.4 | <br>  Your existing external database remains the same after upgrading but you must specify the `external-postgres-configuration-gateway` (spec.database.database_secret) on the Ansible Automation Platform custom resource. For detailed steps, see [Upgrading an external database for platform gateway on Red Hat Ansible Automation Platform Operator](#proc-operator-upgrade-external-db-gateway "10.7.&nbsp;Upgrading an external database for platform gateway on Red Hat Ansible Automation Platform Operator"). |

To deploy Ansible Automation Platform with an external database, you must first create a Kubernetes secret with credentials for connecting to the database.

By default, the Ansible Automation Platform Operator automatically creates and configures a managed PostgreSQL pod in the same namespace as your Ansible Automation Platform deployment. You can deploy Ansible Automation Platform with an external database instead of the managed PostgreSQL pod that the Ansible Automation Platform Operator automatically creates.

Using an external database lets you share and reuse resources and manually manage backups, upgrades, and performance optimizations.

Note

The same external database (PostgreSQL instance) can be used for both automation hub, automation controller, and platform gateway as long as the database names are different. In other words, you can have multiple databases with different names inside a single PostgreSQL instance.

The following section outlines the steps to configure an external database for your platform gateway on a Ansible Automation Platform Operator.

**Prerequisite**

The external database must be a PostgreSQL database that is the version supported by the current release of Ansible Automation Platform. The external postgres instance credentials and connection information must be stored in a secret, which is then set on the platform gateway spec.

Note

Ansible Automation Platform 2.6 supports PostgreSQL 15 for its managed databases and additionally supports PostgreSQL 15, 16, and 17 for external databases.

If you choose to use an externally managed database with version 16 or 17 you must also rely on external backup and restore processes.

**Procedure**

1. Create a `postgres_configuration_secret` YAML file, following the template below:

apiVersion: v1
kind: Secret
metadata:
name: external-postgres-configuration
namespace: <target_namespace> 1
stringData:
host: "<external_ip_or_url_resolvable_by_the_cluster>" 2
port: "<external_port>" 3
database: "<desired_database_name>"
username: "<username_to_connect_as>"
password: "<password_to_connect_with>" 4
type: "unmanaged"
type: Opaque


1. Namespace to create the secret in. This should be the same namespace you want to deploy to.
2. The resolvable hostname for your database node.
3. External port defaults to `5432`.
4. Value for variable `password` should not contain single or double quotes (', ") or backslashes (\) to avoid any issues during deployment, backup or restoration.

2. Apply `external-postgres-configuration-secret.yml` to your cluster using the `oc create` command.

$ oc create -f external-postgres-configuration-secret.yml


Note
The following example is for a platform gateway deployment. To configure an external database for all components, use the *aap-configuring-external-db-all-default-components.yml* example in the [14.1. Custom resources](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html-single/installing_on_openshift_container_platform/index#operator-crs) section.

3. When creating your `AnsibleAutomationPlatform` custom resource object, specify the secret on your spec, following the example below:

apiVersion: aap.ansible.com/v1alpha1
kind: AnsibleAutomationPlatform
metadata:
name: example-aap
Namespace: aap
spec:
database:
database_secret: automation-platform-postgres-configuration


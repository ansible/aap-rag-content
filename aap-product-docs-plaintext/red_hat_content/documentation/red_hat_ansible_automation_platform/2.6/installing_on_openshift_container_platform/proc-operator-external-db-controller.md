# 5. Configuring Red Hat Ansible Automation Platform components on Red Hat Ansible Automation Platform Operator
## 5.2. Configuring automation controller on Red Hat OpenShift Container Platform web console
### 5.2.2. Configuring an external database for automation controller on Red Hat Ansible Automation Platform Operator




For users who prefer to deploy Ansible Automation Platform with an external database, they can do so by configuring a secret with instance credentials and connection information, then applying it to their cluster using the `oc create` command.

By default, the Ansible Automation Platform Operator automatically creates and configures a managed PostgreSQL pod in the same namespace as your Ansible Automation Platform deployment. You can deploy Ansible Automation Platform with an external database instead of the managed PostgreSQL pod that the Ansible Automation Platform Operator automatically creates.

Using an external database lets you share and reuse resources and manually manage backups, upgrades, and performance optimizations.

Note
The same external database (PostgreSQL instance) can be used for both automation hub, automation controller, and platform gateway as long as the database names are different. In other words, you can have multiple databases with different names inside a single PostgreSQL instance.



The following section outlines the steps to configure an external database for your automation controller on a Ansible Automation Platform Operator.

**Prerequisite**

The external database must be a PostgreSQL database that is the version supported by the current release of Ansible Automation Platform. The external postgres instance credentials and connection information must be stored in a secret, which is then set on the automation controller spec.


Note
Ansible Automation Platform 2.6 supports PostgreSQL 15 for its managed databases and additionally supports PostgreSQL 15, 16, and 17 for external databases.

If you choose to use an externally managed database with version 16 or 17 you must also rely on external backup and restore processes.



**Procedure**

1. Create a `    postgres_configuration_secret` YAML file, following the template below:


```
apiVersion: v1    kind: Secret    metadata:      name: external-postgres-configuration      namespace: &lt;target_namespace&gt;    stringData:      host: "&lt;external_ip_or_url_resolvable_by_the_cluster&gt;"      port: "&lt;external_port&gt;"      database: "&lt;desired_database_name&gt;"      username: "&lt;username_to_connect_as&gt;"      password: "&lt;password_to_connect_with&gt;"      sslmode: "prefer"      type: "unmanaged"    type: Opaque
```

When configuring the secret:


-  `        namespace` : Specify the namespace to create the secret in. This should be the same namespace you want to deploy to.
-  `        host` : Specify the resolvable hostname for your database node.
-  `        port` : Specify the external port. The default is `        5432` .
-  `        password` : Ensure the password does not contain single or double quotes (', ") or backslashes (\) to avoid any issues during deployment, backup or restoration.
-  `        sslmode` : This variable is valid for external databases only. The allowed values are: `        prefer` , `        disable` , `        allow` , `        require` , `        verify-ca` , and `        verify-full` .

1. Apply `    external-postgres-configuration-secret.yml` to your cluster using the `    oc create` command.


```
$ oc create -f external-postgres-configuration-secret.yml
```


1. When creating your `    AutomationController` custom resource object, specify the secret on your spec, following the example below:


```
apiVersion: automationcontroller.ansible.com/v1beta1    kind: AutomationController    metadata:      name: controller-dev    spec:      postgres_configuration_secret: external-postgres-configuration
```





# 5. Configuring Red Hat Ansible Automation Platform components on Red Hat Ansible Automation Platform Operator
## 5.1. Configuring platform gateway on Red Hat OpenShift Container Platform web console
### 5.1.1. Configuring an external database for platform gateway on Red Hat Ansible Automation Platform Operator




There are two scenarios for deploying Ansible Automation Platform with an external database:

| Scenario | Action required |
| --- | --- |
| Fresh install | You must specify a single external database instance for the platform to use for the following:

- Platform gateway
- Automation controller
- Automation hub
- Event-Driven Ansible
- Red Hat Ansible Lightspeed (If enabled)


See the _aap-configuring-external-db-all-default-components.yml_ example in the [14.1. Custom resources](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/installing_on_openshift_container_platform/index#operator-crs) section for help with this.

If using Red Hat Ansible Lightspeed, use the _aap-configuring-external-db-with-lightspeed-enabled.yml_ example. |
| Existing external database in 2.4 | Your existing external database remains the same after upgrading but you must specify the `external-postgres-configuration-gateway` (spec.database.database_secret) on the Ansible Automation Platform custom resource. |


To deploy Ansible Automation Platform with an external database, you must first create a Kubernetes secret with credentials for connecting to the database.

By default, the Ansible Automation Platform Operator automatically creates and configures a managed PostgreSQL pod in the same namespace as your Ansible Automation Platform deployment. You can deploy Ansible Automation Platform with an external database instead of the managed PostgreSQL pod that the Ansible Automation Platform Operator automatically creates.

Using an external database lets you share and reuse resources and manually manage backups, upgrades, and performance optimizations.

Note
The same external database (PostgreSQL instance) can be used for both automation hub, automation controller, and platform gateway as long as the database names are different. In other words, you can have multiple databases with different names inside a single PostgreSQL instance.



The following section outlines the steps to configure an external database for your platform gateway on a Ansible Automation Platform Operator.

**Prerequisite**

The external database must be a PostgreSQL database that is the version supported by the current release of Ansible Automation Platform. The external postgres instance credentials and connection information must be stored in a secret, which is then set on the platform gateway spec.


Note
Ansible Automation Platform 2.5 supports PostgreSQL 15.



**Procedure**

1. Create a `    postgres_configuration_secret` YAML file, following the template below:


```
apiVersion: v1    kind: Secret    metadata:      name: external-postgres-configuration      namespace: &lt;target_namespace&gt;<span id="CO1-1"><!--Empty--></span><span class="callout">1</span>stringData:      host: "&lt;external_ip_or_url_resolvable_by_the_cluster&gt;"<span id="CO1-2"><!--Empty--></span><span class="callout">2</span>port: "&lt;external_port&gt;"<span id="CO1-3"><!--Empty--></span><span class="callout">3</span>database: "&lt;desired_database_name&gt;"      username: "&lt;username_to_connect_as&gt;"      password: "&lt;password_to_connect_with&gt;"<span id="CO1-4"><!--Empty--></span><span class="callout">4</span>type: "unmanaged"    type: Opaque
```


1. Namespace to create the secret in. This should be the same namespace you want to deploy to.
1. The resolvable hostname for your database node.
1. External port defaults to `        5432` .
1. Value for variable `        password` should not contain single or double quotes (', ") or backslashes (\) to avoid any issues during deployment, backup or restoration.

1. Apply `    external-postgres-configuration-secret.yml` to your cluster using the `    oc create` command.


```
$ oc create -f external-postgres-configuration-secret.yml
```

Note
The following example is for a platform gateway deployment. To configure an external database for all components, use the _aap-configuring-external-db-all-default-components.yml_ example in the [14.1. Custom resources](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/installing_on_openshift_container_platform/index#operator-crs) section.




1. When creating your `    AnsibleAutomationPlatform` custom resource object, specify the secret on your spec, following the example below:


```
apiVersion: aap.ansible.com/v1alpha1    kind: AnsibleAutomationPlatform    metadata:      name: example-aap      Namespace: aap    spec:      database:         database_secret: automation-platform-postgres-configuration
```





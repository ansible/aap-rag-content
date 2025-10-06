# 4. Configuring Red Hat Ansible Automation Platform components on Red Hat Ansible Automation Platform Operator
## 4.2. Configuring automation controller on Red Hat OpenShift Container Platform web console
### 4.2.2. Configuring an external database for automation controller on Red Hat Ansible Automation Platform Operator




For users who prefer to deploy Ansible Automation Platform with an external database, they can do so by configuring a secret with instance credentials and connection information, then applying it to their cluster using the `oc create` command.

By default, the Ansible Automation Platform Operator automatically creates and configures a managed PostgreSQL pod in the same namespace as your Ansible Automation Platform deployment. You can deploy Ansible Automation Platform with an external database instead of the managed PostgreSQL pod that the Ansible Automation Platform Operator automatically creates.

Using an external database lets you share and reuse resources and manually manage backups, upgrades, and performance optimizations.

Note
The same external database (PostgreSQL instance) can be used for both automation hub, automation controller, and platform gateway as long as the database names are different. In other words, you can have multiple databases with different names inside a single PostgreSQL instance.



The following section outlines the steps to configure an external database for your automation controller on a Ansible Automation Platform Operator.

**Prerequisite**

The external database must be a PostgreSQL database that is the version supported by the current release of Ansible Automation Platform. The external postgres instance credentials and connection information must be stored in a secret, which is then set on the automation controller spec.


Note
Ansible Automation Platform 2.5 supports PostgreSQL 15.



**Procedure**

1. Create a `    postgres_configuration_secret` YAML file, following the template below:


```
apiVersion: v1    kind: Secret    metadata:      name: external-postgres-configuration      namespace: &lt;target_namespace&gt;<span id="CO2-1"><!--Empty--></span><span class="callout">1</span>stringData:      host: "&lt;external_ip_or_url_resolvable_by_the_cluster&gt;"<span id="CO2-2"><!--Empty--></span><span class="callout">2</span>port: "&lt;external_port&gt;"<span id="CO2-3"><!--Empty--></span><span class="callout">3</span>database: "&lt;desired_database_name&gt;"      username: "&lt;username_to_connect_as&gt;"      password: "&lt;password_to_connect_with&gt;"<span id="CO2-4"><!--Empty--></span><span class="callout">4</span>sslmode: "prefer"<span id="CO2-5"><!--Empty--></span><span class="callout">5</span>type: "unmanaged"    type: Opaque
```


1. Apply `    external-postgres-configuration-secret.yml` to your cluster using the `    oc create` command.


```
$ oc create -f external-postgres-configuration-secret.yml
```


1. When creating your `    AutomationController` custom resource object, specify the secret on your spec, following the example below:


```
apiVersion: automationcontroller.ansible.com/v1beta1    kind: AutomationController    metadata:      name: controller-dev    spec:      postgres_configuration_secret: external-postgres-configuration
```





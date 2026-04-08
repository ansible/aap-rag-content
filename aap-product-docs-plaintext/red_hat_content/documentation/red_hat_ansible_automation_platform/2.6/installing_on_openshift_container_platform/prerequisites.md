# 5. Configuring Red Hat Ansible Automation Platform components on Red Hat Ansible Automation Platform Operator
## 5.2. Configuring automation controller on Red Hat OpenShift Container Platform web console
### 5.2.1. Prerequisites




- You have installed the Red Hat Ansible Automation Platform catalog in Operator Hub.
- For automation controller, a default StorageClass must be configured on the cluster for the operator to dynamically create needed PVCs. This is not necessary if an external PostgreSQL database is configured.
- For Hub a StorageClass that supports ReadWriteMany must be available on the cluster to dynamically created the PVC needed for the content, redis and api pods. If it is not the default StorageClass on the cluster, you can specify it when creating your AutomationHub object.


#### 5.2.1.1. Configuring your controller image pull policy




Use this procedure to configure the image pull policy on your automation controller.

**Procedure**

1. Log in to Red Hat OpenShift Container Platform.
1. Go toOperators→Installed Operators.
1. Select your Ansible Automation Platform Operator deployment.
1. Select the **Ansible Automation Platform** tab.
1. Click the ⋮ icon next to your Ansible Automation Platform instance and selectEdit AnsibleAutomationPlatform.
1. ClickYAML viewand locate the `    spec.controller:` section.
1. Configure the image pull policy and resource requirements under the `    controller:` section:


```
spec:      controller:        image_pull_policy: IfNotPresent  # Options: Always, Never, IfNotPresent        image_pull_secrets:          - pull-secret-name        web_resource_requirements:          limits:            cpu: 1000m            memory: 2Gi          requests:            cpu: 500m            memory: 1Gi        task_resource_requirements:          limits:            cpu: 2000m            memory: 4Gi          requests:            cpu: 1000m            memory: 2Gi        ee_resource_requirements:          limits:            cpu: 500m            memory: 1Gi          requests:            cpu: 250m            memory: 512Mi        redis_resource_requirements:          limits:            cpu: 500m            memory: 1Gi          requests:            cpu: 250m            memory: 512Mi        postgres_resource_requirements:          limits:            cpu: 1000m            memory: 2Gi          requests:            cpu: 500m            memory: 1Gi        postgres_storage_requirements:          limits:            storage: 10Gi          requests:            storage: 8Gi        replicas: 1        garbage_collect_secrets: false        create_preload_data: true
```


1. ClickSave.

Note
These settings apply to the automation controller component managed by this Ansible Automation Platform instance. If you specified an existing controller under `    controller.name` , these settings will update that instance.

For more examples of Ansible Automation Platform custom resources, see [Appendix: Red Hat Ansible Automation Platform custom resources](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html-single/installing_on_openshift_container_platform/index#appendix-operator-crs_operator-platform-doc) .






#### 5.2.1.2. Configuring your controller LDAP security




You can configure your LDAP SSL configuration for automation controller through any of the following options:

- The automation controller user interface.
- The platform gateway user interface. See the [Configuring LDAP authentication](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html-single/access_management_and_authentication/index#controller-set-up-LDAP) section of the _Access management and authentication_ guide for additional steps.
- The following procedure steps.


**Procedure**

1. Create a secret in your Ansible Automation Platform namespace for the `    bundle-ca.crt` file (the filename must be `    bundle-ca.crt` ):


```
$ oc create secret -n aap generic bundle-ca-secret --from-file=bundle-ca.crt
```

Note
The target filename for this operation must be `    bundle-ca.crt` and the secret name should be `    bundle-ca-secret` .




1. Add the `    bundle_cacert_secret` to the Ansible Automation Platform customer resource:


```
...    spec:      bundle_cacert_secret: bundle-ca-secret    ...
```

**Verification**

You can verify the expected certificate by running:



```
oc get deployments -l 'app.kubernetes.io/component=aap-gateway'
```

Followed by:


```
oc exec -it deployment.apps/&lt;gateway-deployment-name-from-above&gt; -- openssl x509 -in /etc/pki/tls/certs/ca-bundle.crt -noout -text
```




#### 5.2.1.3. Configure automation controller operator route options




The Red Hat Ansible Automation Platform Operator installation form provides advanced options to configure your automation controller operator route.

Important
You must assign a unique `metadata.name` to each custom resource (CR) in your namespace. If you assign an `AutomationControllerMeshIngress` the same name as your `Ansible Automation Platform` installation, the operator overrides default routes and services. This conflict causes the platform installation to fail.



**Procedure**

1. Log in to Red Hat OpenShift Container Platform.
1. Navigate toOperators→Installed Operators.
1. Select your Ansible Automation Platform Operator deployment.
1. Select the **Ansible Automation Platform** tab.
1. Click the ⋮ icon next to your Ansible Automation Platform instance and selectEdit AnsibleAutomationPlatform.
1. ClickYAML viewand locate the `    spec.controller:` section.
1. Configure the route options under the `    controller:` section:


```
spec:      controller:        ingress_type: Route        route_host: controller.example.com  # Custom hostname for the route        route_tls_termination_mechanism: Edge  # Options: Edge, Passthrough        route_tls_secret: controller-tls-secret  # Optional: TLS credential secret        projects_persistence: false  # Enable/disable persistence for /var/lib/projects
```


1. ClickSave.

Note
Edge termination is recommended for most instances. After configuring your route, you can customize additional route settings by adding them to the `    controller:` section in the Ansible Automation Platform custom resource.

For more examples of Ansible Automation Platform custom resources, see [Appendix: Red Hat Ansible Automation Platform custom resources](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html-single/installing_on_openshift_container_platform/index#appendix-operator-crs_operator-platform-doc) .






#### 5.2.1.4. Configuring the ingress type for your automation controller operator




The Ansible Automation Platform Operator installation form allows you to further configure your automation controller operator ingress under **Advanced configuration** .

**Procedure**

1. Log in to Red Hat OpenShift Container Platform.
1. Navigate toOperators→Installed Operators.
1. Select your Ansible Automation Platform Operator deployment.
1. Select the **Ansible Automation Platform** tab.
1. Click the ⋮ icon next to your Ansible Automation Platform instance and selectEdit AnsibleAutomationPlatform.
1. ClickYAML viewand locate the `    spec.controller:` section.
1. Configure the ingress options under the `    controller:` section:


```
spec:      controller:        ingress_type: Ingress        ingress_annotations: |          nginx.ingress.kubernetes.io/proxy-body-size: "0"          nginx.ingress.kubernetes.io/proxy-connect-timeout: "600"        ingress_tls_secret: controller-ingress-tls-secret
```


1. ClickSave.

Note
These ingress settings apply to the automation controller component managed by this Ansible Automation Platform instance. The operator automatically updates the ingress configuration for the controller.

For more examples of Ansible Automation Platform custom resources, see [Appendix: Red Hat Ansible Automation Platform custom resources](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html-single/installing_on_openshift_container_platform/index#appendix-operator-crs_operator-platform-doc) .






**Verification**

After you have configured your automation controller ingress settings, Red Hat OpenShift Container Platform updates the pods. This may take a few minutes.


You can view the progress by navigating toWorkloads→Podsand locating the newly created instance.

Verify that the following operator pods provided by the Ansible Automation Platform Operator installation from automation controller are running:

| Operator manager controllers | Automation controller | Automation hub | Event-Driven Ansible (EDA) |
| --- | --- | --- | --- |
| The operator manager controllers for each of the three operators, include the following:

- automation-controller-operator-controller-manager
- automation-hub-operator-controller-manager
- resource-operator-controller-manager
- aap-gateway-operator-controller-manager
- ansible-lightspeed-operator-controller-manager
- eda-server-operator-controller-manager | After deploying automation controller, you can see the addition of the following pods:

- controller
- controller-postgres
- controller-web
- controller-task | After deploying automation hub, you can see the addition of the following pods:

- hub-api
- hub-content
- hub-postgres
- hub-redis
- hub-worker | After deploying EDA, you can see the addition of the following pods:

- eda-activation-worker
- da-api
- eda-default-worker
- eda-event-stream
- eda-scheduler |


Note
A missing pod can indicate the need for a pull secret. Pull secrets are required for protected or private image registries. See [Using image pull secrets](https://docs.openshift.com/container-platform/4.11/openshift_images/managing_images/using-image-pull-secrets.html) for more information. You can diagnose this issue further by running `oc describe pod &lt;pod-name&gt;` to see if there is an ImagePullBackOff error on that pod.




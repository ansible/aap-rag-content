+++
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.6/install-assembly_installing_controller_operator"
title = "Configure automation controller - Red Hat Ansible Automation Platform 2.6"
template = "docs/aem-title.html"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6", "2.6"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6/install-assembly_operator_install_operator/", "Install on OpenShift Container Platform"]]
category = "Install"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/install-assembly_installing_controller_operator/aem-page/install-assembly_installing_controller_operator.html"
last_crumb = "Configure automation controller"
modified = "2026-05-21T14:12:12.122Z"
multi_page_path = ""
name = "Configure automation controller"
oversized = "false"
page_slug = "install-assembly_installing_controller_operator"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.6"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/install-assembly_installing_controller_operator"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/install-assembly_installing_controller_operator/toc/toc.json"
type = "aem-page"
+++

# Configure automation controller

You can use these instructions to configure the automation controller operator on Red Hat OpenShift Container Platform, specify custom resources, and deploy Ansible Automation Platform with an external database.

Automation controller configuration can be done through the automation controller extra_settings or directly in the user interface after deployment. However, it is important to note that configurations made in extra_settings take precedence over settings made in the user interface.

Note:

When an instance of automation controller is removed, the associated PVCs are not automatically deleted. This can cause issues during migration if the new deployment has the same name as the previous one. Therefore, it is recommended that you manually remove old PVCs before deploying a new automation controller instance in the same namespace.

## Prerequisites

- You have installed the Red Hat Ansible Automation Platform catalog in Operator Hub.
- For automation controller, a default StorageClass must be configured on the cluster for the operator to dynamically create needed PVCs. This is not necessary if an external PostgreSQL database is configured.
- For Hub a StorageClass that supports ReadWriteMany must be available on the cluster to dynamically created the PVC needed for the content, redis and api pods. If it is not the default StorageClass on the cluster, you can specify it when creating your AutomationHub object.

## Configure your automation controller image pull policy

Use this procedure to configure the image pull policy on your automation controller.

### About this task

### Procedure

1.  Log in to Red Hat OpenShift Container Platform.
2.  Go to Operators> (and then)Installed Operators.
3.  Select your Ansible Automation Platform Operator deployment.
4.  Select the **Ansible Automation Platform** tab.
5.  Click the ⋮ icon next to your Ansible Automation Platform instance and select **Edit AnsibleAutomationPlatform**.
6.  Click **YAML view** and locate the `spec.controller:` section.

7.  Configure the image pull policy and resource requirements under the `controller:` section:
  

```
spec:
  controller:
    image_pull_policy: IfNotPresent  # Options: Always, Never, IfNotPresent
    image_pull_secrets:
      - pull-secret-name
    web_resource_requirements:
      limits:
        cpu: 1000m
        memory: 2Gi
      requests:
        cpu: 500m
        memory: 1Gi
    task_resource_requirements:
      limits:
        cpu: 2000m
        memory: 4Gi
      requests:
        cpu: 1000m
        memory: 2Gi
    ee_resource_requirements:
      limits:
        cpu: 500m
        memory: 1Gi
      requests:
        cpu: 250m
        memory: 512Mi
    redis_resource_requirements:
      limits:
        cpu: 500m
        memory: 1Gi
      requests:
        cpu: 250m
        memory: 512Mi
    postgres_resource_requirements:
      limits:
        cpu: 1000m
        memory: 2Gi
      requests:
        cpu: 500m
        memory: 1Gi
    postgres_storage_requirements:
      limits:
        storage: 10Gi
      requests:
        storage: 8Gi
    replicas: 1
    garbage_collect_secrets: false
    create_preload_data: true
```

8.  Click **Save**.
  
  Note:
      These settings apply to the automation controller component managed by this Ansible Automation Platform instance. If you specified an existing controller under `controller.name`, these settings will update that instance.

    For more examples of Ansible Automation Platform custom resources, see [Red Hat Ansible Automation Platform custom resources](/documentation/en-us/red_hat_ansible_automation_platform/2.6/install-assembly_appendix_operator_crs#appendix-operator-crs_appendix-operator-crs "This appendix provides a reference for the Ansible Automation Platform custom resources for various deployment scenarios.")

## Configure your LDAP for automation controller

You can configure your LDAP SSL configuration for automation controller through any of the following options:

### About this task

- The automation controller user interface. The platform gateway user interface. See [Configure LDAP authentication](/documentation/en-us/red_hat_ansible_automation_platform/2.6/secure-proc_controller_set_up_ldap#controller-set-up-LDAP "As a platform administrator, you can configure LDAP as the source for account authentication information for Ansible Automation Platform users.") for additional steps.

- The following procedure steps.

### Procedure

1.  Create a secret in your Ansible Automation Platform namespace for the `bundle-ca.crt` file (the filename must be `bundle-ca.crt`):
  

```
$ oc create secret -n aap generic bundle-ca-secret --from-file=bundle-ca.crt
```
  Note:
      The target filename for this operation must be `bundle-ca.crt` and the secret name should be `bundle-ca-secret`.

2.  Add the `bundle_cacert_secret` to the Ansible Automation Platform customer resource:
  

```
...
spec:
  bundle_cacert_secret: bundle-ca-secret
...
```

### Results

You can verify the expected certificate by running:

```
oc get deployments -l 'app.kubernetes.io/component=aap-gateway'
```
Followed by:

```
oc exec -it deployment.apps/<gateway-deployment-name-from-above> -- openssl x509 -in /etc/pki/tls/certs/ca-bundle.crt -noout -text
```

## Configure automation controller route options

The Red Hat Ansible Automation Platform operator installation form allows you to further configure your automation controller operator route options under **Advanced configuration**.

### About this task

Important:

You must assign a unique metadata.name to each custom resource (CR) in your namespace. If you assign an `AutomationControllerMeshIngress` the same name as your `AnsibleAutomationPlatform` installation, the operator overrides default routes and services. This conflict causes the platform installation to fail.

### Procedure

1.  Log in to Red Hat OpenShift Container Platform.
2.  Navigate to Operators> (and then)Installed Operators.
3.  Select your Ansible Automation Platform Operator deployment.
4.  Select the **Ansible Automation Platform** tab.
5.  Click the ⋮ icon next to your Ansible Automation Platform instance and select **Edit AnsibleAutomationPlatform** .
6.  Click **YAML view** and locate the `spec.controller:` section..
7.  Configure the route options under the `controller:` section:
  

```
spec:
  controller:
    ingress_type: Route
    route_host: controller.example.com  # Custom hostname for the route
    route_tls_termination_mechanism: Edge  # Options: Edge, Passthrough
    route_tls_secret: controller-tls-secret  # Optional: TLS credential secret
    projects_persistence: false  # Enable/disable persistence for /var/lib/projects
```

8.  Click **Save.**
  
  Note:
      Edge termination is recommended for most instances. After configuring your route, you can customize additional route settings by adding them to the `controller:` section in the Ansible Automation Platform custom resource.

    For more examples of Ansible Automation Platform custom resources, see [Red Hat Ansible Automation Platform custom resources](/documentation/en-us/red_hat_ansible_automation_platform/2.6/install-assembly_appendix_operator_crs#appendix-operator-crs_appendix-operator-crs "This appendix provides a reference for the Ansible Automation Platform custom resources for various deployment scenarios.") .

## Configure ingress options for automation controller

The Ansible Automation Platform Operator installation form allows you to further configure your automation controller operator ingress under **Advanced configuration**.

### About this task

### Procedure

1.  Log in to Red Hat OpenShift Container Platform.
2.  Navigate to Operators> (and then)Installed Operators.
3.  Select your Ansible Automation Platform Operator deployment.
4.  Select the **Ansible Automation Platform** tab.
5.  Click the ⋮ icon next to your Ansible Automation Platform instance and select **Edit AnsibleAutomationPlatform** .
6.  Click **YAML view** and locate the `spec.controller:` section..
7.  Configure the route options under the `controller:` section:
  

```
spec:
  controller:
    ingress_type: Ingress
    ingress_annotations: |
      nginx.ingress.kubernetes.io/proxy-body-size: "0"
      nginx.ingress.kubernetes.io/proxy-connect-timeout: "600"
    ingress_tls_secret: controller-ingress-tls-secret
```

8.  Click **Save**.
  
  Note:
      These settings apply to the automation controller component managed by this Ansible Automation Platform instance. The operator automatically updates the ingress configuration for the controller.

    For more examples of Ansible Automation Platform custom resources, see [Red Hat Ansible Automation Platform custom resources](/documentation/en-us/red_hat_ansible_automation_platform/2.6/install-assembly_appendix_operator_crs#appendix-operator-crs_appendix-operator-crs "This appendix provides a reference for the Ansible Automation Platform custom resources for various deployment scenarios.")

### Results

After you have configured your automation controller ingress setting, OpenShift Container Platform updates the pods. This may take a few minutes.

You can view the progress by navigating to Workloads> (and then)Pods and locating the newly created instance.

Verify that the following operator pods provided by the Ansible Automation Platform Operator installation from automation controller are running:

| Operator manager controllers                                                                                                                                                                                                                                                                                                                               | Automation controller                                                                                                                                    | Automation hub                                                                                                                           | Event-Driven Ansible (EDA)                                                                                                                             |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| <br>The operator manager controllers for each of the three operators, include the following:<br>automation-controller-operator-controller-managerautomation-hub-operator-controller-managerresource-operator-controller-manageraap-gateway-operator-controller-manageransible-lightspeed-operator-controller-managereda-server-operator-controller-manager | <br>After deploying automation controller, you can see the addition of the following pods:<br>controllercontroller-postgrescontroller-webcontroller-task | <br>After deploying automation hub, you can see the addition of the following pods:<br>hub-apihub-contenthub-postgreshub-redishub-worker | <br>After deploying EDA, you can see the addition of the following pods:<br>eda-activation-workerda-apieda-default-workereda-event-streameda-scheduler |


Note:

A missing pod can indicate the need for a pull secret. Pull secrets are required for protected or private image registries. See [Using image pull secrets](https://docs.openshift.com/container-platform/4.11/openshift_images/managing_images/using-image-pull-secrets.html) for more information. You can diagnose this issue further by running `oc describe pod <pod-name>` to see if there is an ImagePullBackOff error on that pod.

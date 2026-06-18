+++
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-assembly_operator_customize_aap"
title = "Customize your Red Hat Ansible Automation Platform Operator - Red Hat Ansible Automation Platform 2.7"
template = "docs/aem-title.html"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-assembly_operator_install_operator/", "Install on OpenShift Container Platform"]]
category = "Install"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/install-assembly_operator_customize_aap/aem-page/install-assembly_operator_customize_aap.html"
last_crumb = "Customize your Red Hat Ansible Automation Platform Operator"
modified = "2026-06-05T07:48:10.594Z"
multi_page_path = ""
name = "Customize your Red Hat Ansible Automation Platform Operator"
oversized = "false"
page_slug = "install-assembly_operator_customize_aap"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/install-assembly_operator_customize_aap"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/install-assembly_operator_customize_aap/toc/toc.json"
type = "aem-page"
+++

# Customize your Red Hat Ansible Automation Platform Operator

Customize your deployment by setting configuration parameters in the parent **AnsibleAutomationPlatform** custom resource (CR). The operator automatically applies these settings to all nested platform components.

## View configuration parameters in the UI

You can discover the configuration parameters for your Ansible Automation Platform Operator by viewing its Custom Resource (CR). The parameters are listed in the YAML schema.

### About this task

### Procedure

1.  Log in to Red Hat OpenShift Container Platform.
2.  Navigate to Operators> (and then)Installed Operators.
3.  Select your Ansible Automation Platform Operator deployment.
4.  Go to the Ansible Automation Platform tab and click the name of your CR.
5.  Switch to the **YAML view** tab to view and edit the configuration. The available parameters are listed in the YAML schema. Note:
      If you cannot see the **Schema** panel, you might have closed or minimized the side bar. Click view sidebar to reopen it.

## View configuration parameters by using the CLI

The Ansible Automation Platform Operator manages multiple custom resources (CRs), each with its own configuration parameters. Use the `oc explain` command to discover all available configuration options for the `AnsibleAutomationPlatform` CR and its nested components.

### About this task

### Procedure

1.  To see all available configuration parameters for a top-level CR, run:
  

```
oc explain ansibleautomationplatform.spec
```

2.  To view component-specific configuration options nested under the Ansible Automation Platform CR, query them through the component section:
  

```
oc explain ansibleautomationplatform.spec.controller.postgres_configuration_secret
oc explain ansibleautomationplatform.spec.controller.route_tls_termination_mechanism
oc explain ansibleautomationplatform.spec.hub.storage_type
oc explain ansibleautomationplatform.spec.eda.automation_server_url
```

3.  To explore all nested fields for a specific component, use the `--recursive` flag:
  

```
oc explain ansibleautomationplatform.spec.controller --recursive
oc explain ansibleautomationplatform.spec.hub --recursive
oc explain ansibleautomationplatform.spec.eda --recursive
```
  
  Note:
  You can also query individual component CRs directly if needed:

```
oc explain automationcontroller.spec
oc explain automationhub.spec
oc explain eda.spec
```
    However, when configuring components through the Ansible Automation Platform CR (recommended approach), use the nested paths shown above.

## Configure component parameters

To define a parameter, such as the `resource_requirements` for automation controller, you add the configuration to the parent Ansible Automation Platform CR YAML. This ensures that the Ansible Automation Platform CR is the single source of truth for your deployment.

### About this task

Note:

The `image` and `image_version`, as well as the `{component}_image` and `{component}_image_version` parameters are intended for development or hotfix purposes only.

**Do not use these in production environments.** These settings bypass standard version management and can lead to configuration drift, inconsistent deployments, and difficulty troubleshooting issues.

### Procedure

1.  Log in to OpenShift Container Platform.
2.  Navigate to Operators> (and then)Installed Operators.
3.  Select your Ansible Automation Platform Operator deployment.
4.  Go to the Ansible Automation Platform tab and click the name of your CR.
5.  In the **YAML view** tab, locate the **spec** section.
6.  Add the `automationcontroller` parameter with the nested `resource_requirements` parameter and its value:
  

```
spec:
  database:
    resource_requirements:
      requests:
        cpu: 200m
        memory: 512Mi
    storage_requirements:
      requests:
        storage: 100Gi
```

7.  Click Save to apply the changes. The operator automatically applies this configuration to the automation controller component.

## Customize your resource requirements

Customize resource requirements for your Ansible Automation Platform components to optimize performance and resource allocation in your specific environment.

The following section provides a complete code block with the default resource requirements for each component. The main reasons for customizing your resource requirements include:

- Performance Tuning: Increase resource limits for components that perform heavy workloads.
- To comply with a `ResourceQuota` enforced by the cluster admin.
- Resource Constrained Environments: Decrease resource requests to conserve cluster resources in development or test environments.
- Environment Specifics: Align the resource allocation with the capacity of your OpenShift or Kubernetes cluster nodes.


You can use this reference as a starting point. Copy the full code block for your Ansible Automation Platform instance and modify the values for the components you want to change. This method helps ensure all default settings are applied correctly, reducing the risk of deployment errors.

Note:

When *adding* parameters, you can add it to the Ansible Automation Platform custom resource (CR) only and those parameters will work their way down to the nested CRs.

When *removing* parameters, you have to remove them both from the Ansible Automation Platform CR *and* the nested CR, for example, the **Automation Controller** CR.

```
# Example of defining custom resource requirements for all components
# This can be useful for clusters with a ResourceQuote in the AAP namespaceapiVersion: aap.ansible.com/v1alpha1
kind: AnsibleAutomationPlatform
metadata:
  name: aap
spec:

  # Platform
  api:
    replicas: 1
    resource_requirements:
      requests:
        cpu: 100m
        memory: 256Mi
      limits:
        cpu: 500m
        memory: 1000Mi
  redis:
    replicas: 1
    resource_requirements:
      requests:
        cpu: 100m
        memory: 256Mi
      limits:
        cpu: 500m
        memory: 500Mi
  database:
    resource_requirements:
      requests:
        cpu: 100m
        memory: 256Mi
      limits:
        cpu: 500m
        memory: 800Mi

  # Components
  controller:
    disabled: false
    uwsgi_processes: 2
    task_resource_requirements:
      requests:
        cpu: 100m
        memory: 150Mi
      limits:
        cpu: 1000m
        memory: 1200Mi
    web_resource_requirements:
      requests:
        cpu: 100m
        memory: 200Mi
      limits:
        cpu: 200m
        memory: 1600Mi
    ee_resource_requirements:
      requests:
        cpu: 100m
        memory: 64Mi
      limits:
        cpu: 1000m
        memory: 500Mi
    redis_resource_requirements:
      requests:
        cpu: 50m
        memory: 64Mi
      limits:
        cpu: 100m
        memory: 200Mi
    rsyslog_resource_requirements:
      requests:
        cpu: 100m
        memory: 128Mi
      limits:
        cpu: 500m
        memory: 250Mi
    init_container_resource_requirements:
      requests:
        cpu: 100m
        memory: 128Mi
      limits:
        cpu: 500m
        memory: 200Mi
  eda:
    disabled: false
    api:
      replicas: 1
      resource_requirements:
        requests:
          cpu: 50m
          memory: 350Mi
        limits:
          cpu: 500m
          memory: 400Mi
    ui:
      replicas: 1
      resource_requirements:
        requests:
          cpu: 25m
          memory: 64Mi
        limits:
          cpu: 500m
          memory: 150Mi
    scheduler:
      replicas: 1
      resource_requirements:
        requests:
          cpu: 50m
          memory: 200Mi
        limits:
          cpu: 500m
          memory: 250Mi
    worker:
      replicas: 2
      resource_requirements:
        requests:
          cpu: 25m
          memory: 200Mi
        limits:
          cpu: 250m
          memory: 250Mi
    default_worker:
      replicas: 1
      resource_requirements:
        requests:
          cpu: 25m
          memory: 200Mi
        limits:
          cpu: 500m
          memory: 400Mi
    activation_worker:
      replicas: 1
      resource_requirements:
        requests:
          cpu: 25m
          memory: 150Mi
        limits:
          cpu: 500m
          memory: 400Mi
    event_stream:
      replicas: 1
      resource_requirements:
        requests:
          cpu: 25m
          memory: 150Mi
        limits:
          cpu: 100m
          memory: 300Mi
  hub:
    disabled: false
    ## uncomment if using file storage for Content pod
    storage_type: file
    file_storage_storage_class: nfs-local-rwx  # replace with the rwx storage class for your cluster
    file_storage_size: 50Gi

    ## uncomment if using S3 storage for Content pod
    # storage_type: S3
    # object_storage_s3_secret: example-galaxy-object-storage

    ## uncomment if using Azure storage for Content pod
    # storage_type: azure
    # object_storage_azure_secret: azure-secret-name

    api:
      replicas: 1
      resource_requirements:
        requests:
          cpu: 150m
          memory: 256Mi
        limits:
          cpu: 800m
          memory: 500Mi
    content:
      replicas: 1
      resource_requirements:
        requests:
          cpu: 150m
          memory: 256Mi
        limits:
          cpu: 800m
          memory: 1200Mi
    worker:
      replicas: 1
      resource_requirements:
        requests:
          cpu: 150m
          memory: 256Mi
        limits:
          cpu: 800m
          memory: 400Mi
    web:
      replicas: 1
      resource_requirements:
        requests:
          cpu: 100m
          memory: 256Mi
        limits:
          cpu: 500m
          memory: 300Mi
    redis:
      replicas: 1
      resource_requirements:
        requests:
          cpu: 100m
          memory: 250Mi
        limits:
          cpu: 300m
          memory: 400Mi


  # lightspeed:
  #   disabled: true

# End state:
# * Controller deployed and named: myaap-controller
# * EDA deployed and named: myaap-eda
# * Hub deployed and named: myaap-hub
```

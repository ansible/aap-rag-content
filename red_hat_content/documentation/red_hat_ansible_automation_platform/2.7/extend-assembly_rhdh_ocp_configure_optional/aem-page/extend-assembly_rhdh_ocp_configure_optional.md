+++
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/extend-assembly_rhdh_ocp_configure_optional"
template = "docs/aem-title.html"
title = "Optional configuration - Red Hat Ansible Automation Platform 2.7"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/extend-assembly_rhdh_intro/", "Ansible plug-ins for Red Hat Developer Hub"]]
category = "Extend"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/extend-assembly_rhdh_ocp_configure_optional/aem-page/extend-assembly_rhdh_ocp_configure_optional.html"
last_crumb = "Optional configuration"
modified = "2026-07-30T17:12:56.473Z"
multi_page_path = ""
name = "Optional configuration"
oversized = "false"
page_slug = "extend-assembly_rhdh_ocp_configure_optional"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/extend-assembly_rhdh_ocp_configure_optional"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/extend-assembly_rhdh_ocp_configure_optional/toc/toc.json"
type = "aem-page"
+++

# Optional configuration

Enable optional integrations to enhance the user experience and functionality of the Ansible plug-ins.

## Configure OpenShift Dev Spaces

When OpenShift Dev Spaces is configured for the Ansible plug-ins, users can click a link from the catalog item view in Red Hat Developer Hub and edit their provisioned Ansible Git projects using Dev Spaces.

### Before you begin

- You have a Dev Spaces installation. For more details, see [Installing Dev Spaces](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/3.14/html-single/administration_guide/installing-devspaces).

### About this task

Note:

OpenShift Dev Spaces is a separate product and it is optional. The plug-ins will function without it.

It is a separate Red Hat product and is not included in the Ansible Automation Platform or Red Hat Developer Hub subscription.

If the OpenShift Dev Spaces link is not configured in the Ansible plug-ins, the **Go to OpenShift Dev Spaces dashboard** link in the **DEVELOP** section of the Ansible plug-ins landing page redirects users to the [Ansible development tools home page](https://www.redhat.com/en/technologies/management/ansible/development-tools).

### Procedure

1.  Edit your custom Red Hat Developer Hub config map, for example `app-config-rhdh`.
2.  Add the following code to your Red Hat Developer Hub `app-config-rhdh.yaml` file.

```
data:
  app-config-rhdh.yaml: |-
    ansible:
      devSpaces:
        baseUrl: >-
          https://<Your OpenShift Dev Spaces URL>
```

3.  Replace `<Your OpenShft Dev Spaces URL>` with your OpenShift Dev Spaces URL.
4.  In the OpenShift Developer UI, select the `Red Hat Developer Hub` pod.
5.  Open **Actions**.
6.  Click **Restart rollout**.

## Configure the private automation hub URL

Private automation hub provides a centralized, on-premise repository for certified Ansible collections, execution environments and any additional, vetted content provided by your organization.

### Before you begin

- You have a private automation hub instance. For more information, see [Manage your automation content in private automation hub](/documentation/en-us/red_hat_ansible_automation_platform/2.7/assembly_managing_collections_hub "As a content creator, you can use namespaces in automation hub to curate and manage collections.")

### About this task

If the private automation hub URL is not configured in the Ansible plug-ins, users are redirected to the [Red Hat Hybrid Cloud Console automation hub](https://console.redhat.com/ansible/automation-hub).

Note:

The private automation hub configuration is optional but recommended. The Ansible plug-ins will function without it.

### Procedure

1.  Edit your custom Red Hat Developer Hub config map, for example `app-config-rhdh`.
2.  Add the following code to your Red Hat Developer Hub `app-config-rhdh.yaml` file.

```
data:
  app-config-rhdh.yaml: |-
    ansible:
    ...
      automationHub:
        baseUrl: '<https://MyOwnPAHUrl>'
    ...
```

3.  Replace `<https://MyOwnPAHUrl/>` with your private automation hub URL.
4.  In the OpenShift Developer UI, select the `Red Hat Developer Hub` pod.
5.  Open **Actions**.
6.  Click **Restart rollout**.

## Customize Ansible Developer Tools server resources

Ansible Developer Tools sidecar container ships with default CPU and memory resource requests and limits. Customize these values if your namespace enforces a `LimitRange` with lower values or if you want to tune resources for your workload.

### About this task

The following table lists the default resource requests and limits for the `ansible-devtools-server` container in the Helm chart:

*Table 1. Default resource requests and limits*

| Resource type | CPU   | Memory |
| ------------- | ----- | ------ |
| Requests      | 1     | 1Gi    |
| Limits        | 2500m | 2.5Gi  |

Important:

If the target namespace has a `LimitRange` resource configured without default values, Kubernetes rejects any pod that does not specify resource requests and limits. The `ansible-devtools-server` container includes explicit defaults to pass `LimitRange` validation. If your `LimitRange` enforces values lower than the chart defaults, you must override the resources to match your namespace constraints.

The `ansible-devtools-server` runs as an `extraContainers` entry in the Helm chart. Due to Helm array replacement behavior, overriding a single field inside an array item requires duplicating the full container spec. You cannot set only the `resources` block. You must include the `command`, `image`, `name`, and `ports` fields as well.

### Procedure

1.  Log in to the OpenShift Container Platform web console.
2.  Open the Helm chart configuration for your portal deployment.

  - For a new deployment, select Ecosystem> (and then)Helm, click Create, and select **Helm Release**.
  - For an existing deployment, select Workloads> (and then)Deployments, click your portal deployment, and click the **YAML** tab.

3.  Switch to the YAML view and find the `extraContainers` section. Set your desired resource values:
  

```yaml
upstream:
  backstage:
    extraContainers:
      - command:
          - adt
          - server
        image: >-
          registry.redhat.io/ansible-automation-platform-2.7/ansible-dev-tools-rhel9:latest
        imagePullPolicy: IfNotPresent
        name: ansible-devtools-server
        ports:
          - containerPort: 8000
        resources:
          requests:
            cpu: 500m
            memory: 512Mi
          limits:
            cpu: 1250m
            memory: 1.25Gi
```

    Replace the `cpu` and `memory` values under `requests` and `limits` with values that match your namespace constraints.

4.  Apply the changes.

  - For a new deployment, click Create.
  - For an existing deployment, click Save. The pod restarts automatically with the updated resource values.

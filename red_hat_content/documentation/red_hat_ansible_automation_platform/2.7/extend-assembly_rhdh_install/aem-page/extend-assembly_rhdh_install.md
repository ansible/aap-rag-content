+++
title = "Install the Ansible plug-ins - Red Hat Ansible Automation Platform 2.7"
template = "docs/aem-title.html"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/extend-assembly_rhdh_install"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/extend-assembly_rhdh_intro/", "Ansible plug-ins for Red Hat Developer Hub"]]
category = "Extend"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/extend-assembly_rhdh_install/aem-page/extend-assembly_rhdh_install.html"
last_crumb = "Install the Ansible plug-ins"
modified = "2026-06-05T07:48:10.594Z"
multi_page_path = ""
name = "Install the Ansible plug-ins"
oversized = "false"
page_slug = "extend-assembly_rhdh_install"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/extend-assembly_rhdh_install"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/extend-assembly_rhdh_install/toc/toc.json"
type = "aem-page"
+++

# Install the Ansible plug-ins

Install the Ansible plug-ins for Red Hat Developer Hub on OpenShift Container Platform using OCI container delivery. Red Hat Developer Hub pulls the plug-ins directly from `registry.redhat.io` as OCI artifacts during startup.

## Create the registry authentication secret

Red Hat Developer Hub pulls the Ansible plug-ins directly from `registry.redhat.io` as OCI artifacts during startup. This requires a registry authentication secret in the same OpenShift Container Platform project as your Red Hat Developer Hub deployment.

### Procedure

1.  Log in to the container image registry:
  

```terminal
$ podman login --authfile auth.json registry.redhat.io
```
    To authenticate to multiple registries, run `podman login` for each registry. The `auth.json` file accumulates credentials for all registries you log in to.

2.  Create a secret from the `auth.json` file in the same OpenShift Container Platform project as your Red Hat Developer Hub deployment.
      For an Operator-based deployment:

```terminal
$ oc create secret generic dynamic-plugins-registry-auth \
  --from-file=auth.json=auth.json \
  -n <your_rhdh_namespace>
```
    For a Helm-based deployment:

```terminal
$ oc create secret generic <release_name>-dynamic-plugins-registry-auth \
  --from-file=auth.json=auth.json \
  -n <your_rhdh_namespace>
```
    Replace `<release_name>` with your Helm release name.

  Important:
      The secret name is fixed. The Red Hat Developer Hub Operator and Helm chart expect these exact names. You cannot use a custom name.

*Table 1. Secret names by deployment method*

    | Deployment method | Secret name                                    |
    | ----------------- | ---------------------------------------------- |
    | Operator          | `dynamic-plugins-registry-auth`                |
    | Helm chart        | `<release_name>-dynamic-plugins-registry-auth` |
  Note:
      For disconnected or restricted network environments, mirror the `automation-portal` OCI image to an internal registry and use OCI references pointing to that registry instead.

### Results

Verify that the secret exists in the project.

For an Operator-based deployment:

```terminal
$ oc get secret dynamic-plugins-registry-auth -n <your_rhdh_namespace>
```
For a Helm-based deployment:

```terminal
$ oc get secret <release_name>-dynamic-plugins-registry-auth -n <your_rhdh_namespace>
```

## Configure the dynamic plug-ins

After creating the registry authentication secret, add the Ansible plug-ins to your dynamic plug-ins configuration.

### Procedure

1.  Edit your dynamic plug-ins configuration and add the Ansible plug-ins using OCI references.
      **Operator installation**

    In the `data.dynamic-plugins.yaml.plugins` block, add the Ansible plug-ins:

```yaml
kind: ConfigMap
apiVersion: v1
metadata:
  name: dynamic-plugins-rhdh
data:
  dynamic-plugins.yaml: |
    includes:
      - dynamic-plugins.default.yaml
    plugins:
      - disabled: false
        package: >-
          oci://registry.redhat.io/ansible-automation-platform/automation-portal:<tag>!ansible-plugin-backstage-rhaap
        pluginConfig:
          dynamicPlugins:
            frontend:
              ansible.plugin-backstage-rhaap:
                appIcons:
                  - importName: AnsibleLogo
                    name: AnsibleLogo
                dynamicRoutes:
                  - importName: AnsiblePage
                    menuItem:
                      icon: AnsibleLogo
                      text: Ansible
                    path: /ansible
      - disabled: false
        package: >-
          oci://registry.redhat.io/ansible-automation-platform/automation-portal:<tag>!ansible-plugin-backstage-self-service
        pluginConfig:
          dynamicPlugins:
            frontend:
              ansible.plugin-backstage-self-service:
                scaffolderFieldExtensions:
                  - importName: AAPTokenFieldExtension
                  - importName: AAPResourcePickerExtension
      - disabled: false
        package: >-
          oci://registry.redhat.io/ansible-automation-platform/automation-portal:<tag>!ansible-backstage-plugin-catalog-backend-module-rhaap
        pluginConfig: {}
      - disabled: false
        package: >-
          oci://registry.redhat.io/ansible-automation-platform/automation-portal:<tag>!ansible-plugin-scaffolder-backend-module-backstage-rhaap
        pluginConfig:
          dynamicPlugins:
            backend:
              ansible.plugin-scaffolder-backend-module-backstage-rhaap:
```
    **Helm chart installation**

    Update the Helm chart configuration under the `plugins` section:

```yaml
global:
  # ...
  dynamic:
    # ...
    plugins:
      - disabled: false
        package: >-
          oci://registry.redhat.io/ansible-automation-platform/automation-portal:<tag>!ansible-plugin-backstage-rhaap
        pluginConfig:
          dynamicPlugins:
            frontend:
              ansible.plugin-backstage-rhaap:
                appIcons:
                  - importName: AnsibleLogo
                    name: AnsibleLogo
                dynamicRoutes:
                  - importName: AnsiblePage
                    menuItem:
                      icon: AnsibleLogo
                      text: Ansible
                    path: /ansible
      - disabled: false
        package: >-
          oci://registry.redhat.io/ansible-automation-platform/automation-portal:<tag>!ansible-plugin-backstage-self-service
        pluginConfig:
          dynamicPlugins:
            frontend:
              ansible.plugin-backstage-self-service:
                scaffolderFieldExtensions:
                  - importName: AAPTokenFieldExtension
                  - importName: AAPResourcePickerExtension
      - disabled: false
        package: >-
          oci://registry.redhat.io/ansible-automation-platform/automation-portal:<tag>!ansible-backstage-plugin-catalog-backend-module-rhaap
        pluginConfig: {}
      - disabled: false
        package: >-
          oci://registry.redhat.io/ansible-automation-platform/automation-portal:<tag>!ansible-plugin-scaffolder-backend-module-backstage-rhaap
        pluginConfig:
          dynamicPlugins:
            backend:
              ansible.plugin-scaffolder-backend-module-backstage-rhaap:
```

2.  Replace `<tag>` with the Ansible plug-ins image tag for your release (for example, `2.2`).
3.  Apply the changes. For Operator deployments, click **Save**. For Helm deployments, click **Upgrade**.

## Add the Ansible Developer Tools sidecar container

After the plug-ins load, add the Ansible Developer Tools container as a sidecar container to the Red Hat Developer Hub pod.

### About this task

Note:

The `ansible-dev-tools-rhel9` container image is hosted on `registry.redhat.io` and requires Red Hat Ansible Automation Platform subscription entitlements. If your OpenShift Container Platform cluster's global pull secret does not include AAP-entitled credentials, you must create an `imagePullSecrets` entry in the deployment patch. You can reuse the same `auth.json` credentials created for the dynamic plug-ins registry secret:

```terminal
$ oc create secret docker-registry rhdh-registry-pull-secret \
    --from-file=.dockerconfigjson=auth.json \
    -n <your_rhdh_namespace>
```
Then add the `imagePullSecrets` field to the deployment patch as shown in the examples below.

### Procedure

1.  Add the Ansible Developer Tools sidecar container to your deployment configuration.
      **Operator installation**

    Modify the Backstage custom resource to add a `containers` block in the `spec.deployment.patch.spec.template.spec` block:

```yaml
apiVersion: rhdh.redhat.com/v1alpha5
kind: Backstage
metadata:
  name: developer-hub
spec:
  deployment:
    patch:
      spec:
        template:
          spec:
            imagePullSecrets:
              - name: rhdh-registry-pull-secret
            containers:
              - command:
                  - adt
                  - server
                image: registry.redhat.io/ansible-automation-platform-2.7/ansible-dev-tools-rhel9:latest
                imagePullPolicy: Always
                ports:
                  - containerPort: 8000
                    protocol: TCP
```
    **Helm chart installation**

    Update the `extraContainers` section in the Helm chart YAML:

```yaml
upstream:
  backstage:
    # ...
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
    # ...
```
  Note:
      The image pull policy is `imagePullPolicy: IfNotPresent`. The image is pulled only if it does not already exist on the node. Update it to `imagePullPolicy: Always` if you always want to use the latest image.

2.  Apply the changes. For Operator deployments, click **Save**. For Helm deployments, click **Upgrade**.

## Verify the plug-in installation

After configuring the dynamic plug-ins and sidecar container, verify that the Ansible plug-ins installed successfully.

### Procedure

1.  In the `install-dynamic-plugin` container logs, search for the Ansible plug-ins.
      A successful installation shows:

```terminal
==> Successfully installed dynamic plugin oci://registry.redhat.io/ansible-automation-platform/automation-portal:<tag>!ansible-plugin-backstage-rhaap
==> Successfully installed dynamic plugin oci://registry.redhat.io/ansible-automation-platform/automation-portal:<tag>!ansible-plugin-backstage-self-service
==> Successfully installed dynamic plugin oci://registry.redhat.io/ansible-automation-platform/automation-portal:<tag>!ansible-backstage-plugin-catalog-backend-module-rhaap
==> Successfully installed dynamic plugin oci://registry.redhat.io/ansible-automation-platform/automation-portal:<tag>!ansible-plugin-scaffolder-backend-module-backstage-rhaap
```

2.  Verify that the Ansible plug-in is present in the navigation pane.
3.  Select **Administration** to view the installed plug-ins in the **Plugins** tab.

+++
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/extend-assembly_rhdh_full_examples"
template = "docs/aem-title.html"
title = "Full configuration examples - Red Hat Ansible Automation Platform 2.7"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/extend-assembly_rhdh_intro/", "Ansible plug-ins for Red Hat Developer Hub"]]
category = "Extend"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/extend-assembly_rhdh_full_examples/aem-page/extend-assembly_rhdh_full_examples.html"
last_crumb = "Full configuration examples"
modified = "2026-06-05T07:48:10.594Z"
multi_page_path = ""
name = "Full configuration examples"
oversized = "false"
page_slug = "extend-assembly_rhdh_full_examples"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/extend-assembly_rhdh_full_examples"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/extend-assembly_rhdh_full_examples/toc/toc.json"
type = "aem-page"
+++

# Full configuration examples

Review complete configuration examples for Ansible plug-ins for Red Hat Developer Hub deployments.

## Full app-config-rhdh ConfigMap example for Ansible plug-ins entries

This example details necessary settings like the creatorService URL, optional integrations for Ansible Automation Platform and OpenShift Dev Spaces, and the addition of Ansible software templates to the catalog.

```
kind: ConfigMap
...
metadata:
  name: app-config-rhdh
  ...
data:
  app-config-rhdh.yaml: |-
    ansible:
      creatorService:
        baseUrl: 127.0.0.1
        port: '8000'
      # Optional integrations
      rhaap:
        baseUrl: '<https://your-controller-url>'
        token: '<AAP Personal Access Token>'
        checkSSL: true
      devSpaces:
        baseUrl: '<https://MyDevSpacesURL>'
      automationHub:
        baseUrl: '<https://MyPrivateAutomationHubURL>'

    ...
    catalog:
      locations:
        - type: url
          target: https://github.com/ansible/ansible-rhdh-templates/blob/main/all.yaml
          rules:
            - allow: [Template]
    ...
```

## Full Operator Backstage CR example for Ansible plug-ins

This example shows the full Backstage custom resource configuration for an Operator-based deployment, including the ADT sidecar container and `imagePullSecrets`.

```yaml
apiVersion: rhdh.redhat.com/v1alpha5
kind: Backstage
metadata:
  name: developer-hub
  namespace: <your_rhdh_namespace>
spec:
  application:
    appConfig:
      configMaps:
      - name: app-config-rhdh
      mountPath: /opt/app-root/src
    dynamicPluginsConfigMapName: dynamic-plugins-rhdh
    extraEnvs:
      secrets:
      - name: <your_scm_credentials_secret>
      - name: <your_rhaap_credentials_secret>
    extraFiles:
      mountPath: /opt/app-root/src
      secrets:
      - key: private-key.pem
        name: <your_scm_credentials_secret>
    route:
      enabled: true
  database:
    enableLocalDb: true
  deployment:
    patch:
      spec:
        template:
          spec:
            imagePullSecrets:
              - name: rhdh-registry-pull-secret
            containers:
              - name: ansible-devtools-server
                command:
                  - adt
                  - server
                image: registry.redhat.io/ansible-automation-platform-2.7/ansible-dev-tools-rhel9:latest
                imagePullPolicy: Always
                ports:
                  - containerPort: 8000
                    protocol: TCP
```

## Full Helm chart config example for Ansible plug-ins

This example provides a full YAML configuration for the Helm chart using OCI container delivery.

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
upstream:
  backstage:
    # ...
    extraAppConfig:
      - configMapRef: app-config-rhdh
        filename: app-config-rhdh.yaml
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
```

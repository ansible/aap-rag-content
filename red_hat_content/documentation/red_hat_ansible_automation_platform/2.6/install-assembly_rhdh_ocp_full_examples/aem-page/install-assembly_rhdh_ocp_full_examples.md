+++
title = "Example ConfigMaps - Red Hat Ansible Automation Platform 2.6"
template = "docs/aem-title.html"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.6/install-assembly_rhdh_ocp_full_examples"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6", "2.6"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6/install-assembly_rhdh_intro/", "Install Ansible plug-ins for Red Hat Developer Hub"]]
category = "Install"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/install-assembly_rhdh_ocp_full_examples/aem-page/install-assembly_rhdh_ocp_full_examples.html"
last_crumb = "Example ConfigMaps"
modified = "2026-05-21T14:12:12.122Z"
multi_page_path = ""
name = "Example ConfigMaps"
oversized = "false"
page_slug = "install-assembly_rhdh_ocp_full_examples"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.6"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/install-assembly_rhdh_ocp_full_examples"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/install-assembly_rhdh_ocp_full_examples/toc/toc.json"
type = "aem-page"
+++

# Example ConfigMaps

The following examples demonstrate how the required and optional settings for the Ansible Dev Tools Server, Ansible Automation Platform, software templates, and other integrations are correctly formatted within their respective YAML files.

## app-config-rhdh ConfigMap example for Ansible plug-ins

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
        baseUrl: '<https://MyControllerUrl>'
        token: '<AAP Personal Access Token>'
        checkSSL: <true or false>
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

## Full Helm chart config example for Ansible plug-ins

This example provides a full YAML configuration for the Helm chart, illustrating the precise structure needed to integrate the Ansible plug-ins into the Red Hat Developer Hub installation.

Important:

This example uses the HTTP plug-in registry delivery method, which is deprecated and will be removed in a future release of Red Hat Ansible Automation Platform. For new installations, use OCI container delivery instead.

```
global:
  ...
  dynamic:
    ...
    plugins:
      - disabled: false
        integrity: <SHA512 Integrity key for ansible-plugin-backstage-rhaap plugin>
        package: 'http://plugin-registry:8080/ansible-plugin-backstage-rhaap-dynamic-x.y.z.tgz'
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
        integrity: <SHA512 Integrity key for ansible-plugin-scaffolder-backend-module-backstage-rhaap plugin>
        package: >-
          http://plugin-registry:8080/ansible-plugin-scaffolder-backend-module-backstage-rhaap-dynamic-x.y.z.tgz
        pluginConfig:
          dynamicPlugins:
            backend:
              ansible.plugin-scaffolder-backend-module-backstage-rhaap: null
...
upstream:
  backstage:
    ...
    extraAppConfig:
      - configMapRef: app-config-rhdh
        filename: app-config-rhdh.yaml
    extraContainers:
      - command:
          - adt
          - server
        image: >-
          registry.redhat.io/ansible-automation-platform-25/ansible-dev-tools-rhel8:latest
        imagePullPolicy: IfNotPresent
        name: ansible-devtools-server
        ports:
          - containerPort: 8000
...
```

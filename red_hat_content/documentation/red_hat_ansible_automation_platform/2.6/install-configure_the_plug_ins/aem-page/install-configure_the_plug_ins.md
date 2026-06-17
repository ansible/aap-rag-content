+++
title = "Configure the plug-ins - Red Hat Ansible Automation Platform 2.6"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.6/install-configure_the_plug_ins"
template = "docs/aem-title.html"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6", "2.6"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6/install-assembly_rhdh_intro/", "Install Ansible plug-ins for Red Hat Developer Hub"]]
category = "Install"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/install-configure_the_plug_ins/aem-page/install-configure_the_plug_ins.html"
last_crumb = "Configure the plug-ins"
modified = "2026-05-21T14:12:12.122Z"
multi_page_path = ""
name = "Configure the plug-ins"
oversized = "false"
page_slug = "install-configure_the_plug_ins"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.6"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/install-configure_the_plug_ins"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/install-configure_the_plug_ins/toc/toc.json"
type = "aem-page"
+++

# Configure the plug-ins

Configure Ansible plug-ins for Red Hat Developer Hub to customize how users access and create Ansible content. Configure the plug-ins to control access to software templates and enable optional integrations that enhance the development environment.

 Configuring the plug-ins helps you to:

- **Control access to templates**: Configure role-based access control to determine who can create projects from templates and who can view them.
- **Enable project provisioning**: Configure the Ansible development tools server and add software templates to enable playbook and collection project creation.
- **Enhance development workflows**: Configure optional integrations to extend functionality based on your environment needs.

## Add a custom ConfigMap

Create a custom Red Hat Developer Hub ConfigMap, typically named `app-config-rhdh`, to store custom application settings.

### Procedure

 Create a Red Hat Developer Hub ConfigMap following the procedure in the [Creating and using config maps](https://docs.redhat.com/en/documentation/openshift_container_platform/4.15/html-single/nodes/index#configmaps) section of the OpenShift Container Platform *Nodes* guide. The following examples use a custom ConfigMap named `app-config-rhdh`.

To edit your custom ConfigMap, log in to the OpenShift UI and navigate to Select Project ( developerHubProj )> (and then)ConfigMaps> (and then){developer-hub}-app-config> (and then)EditConfigMaps> (and then)app-config-rhdh.

## Configure the Ansible development tools Server

The `creatorService` URL is required for the Ansible plug-ins to provision new projects using the provided software templates.

### Procedure

1.  Edit your custom Red Hat Developer Hub config map, `app-config-rhdh`, that you created in [Adding a custom ConfigMap](/documentation/en-us/red_hat_ansible_automation_platform/2.6/install-configure_the_plug_ins#rhdh-add-custom-configmap "Create a custom Red Hat Developer Hub ConfigMap, typically named app-config-rhdh, to store custom application settings.").
2.  Add the following code to your Red Hat Developer Hub `app-config-rhdh.yaml` file.

```
kind: ConfigMap
apiVersion: v1
metadata:
  name: app-config-rhdh
...
data:
  app-config-rhdh.yaml: |-
    ansible:
      creatorService:
        baseUrl: 127.0.0.1
        port: '8000'
...
```

## Configure Ansible Automation Platform details

Connect Red Hat Developer Hub to your automation controller by configuring the Ansible Automation Platform details. This configuration uses a Personal Access Token (PAT) to authenticate the plug-ins, which allows them to interact with your automation environment.

### About this task

Note:

The Ansible plug-ins continue to function regardless of the Ansible Automation Platform subscription status.

### Procedure

1.  Create a Personal Access Token (PAT) with "read and write” scope in automation controller, following the [Applications](/documentation/en-us/red_hat_ansible_automation_platform/2.6/secure-assembly_gw_token_based_authentication#gw-token-based-authentication "Token-based authentication permits authentication of third-party tools and services with the platform through integrated OAuth 2 token support. Ansible Automation Platform utilizes both OAuth Tokens and Personal Access Tokens (PATs).") section of *Access management and authentication*.
2.  Edit your custom Red Hat Developer Hub config map, for example `app-config-rhdh`.
3.  Add your Ansible Automation Platform details to `app-config-rhdh.yaml`.   1.  Set the `baseURL` key with your automation controller URL.
  2.  Set the `token` key with the generated token value that you created in Step 1.
  3.  Set the `checkSSL` key to `true` or `false`. If `checkSSL` is set to `true`, the Ansible plug-ins verify whether the SSL certificate is valid.

```
data:
  app-config-rhdh.yaml: |
    ...
    ansible:
    ...
      rhaap:
        baseUrl: '<https://MyControllerUrl>'
        token: '<AAP Personal Access Token>'
        checkSSL: true
```
    Note:
            You are responsible for protecting your Red Hat Developer Hub installation from external and unauthorized access. Manage the backend authentication key like any other secret. Meet strong password requirements, do not expose it in any configuration files, and only inject it into configuration files as an environment variable.

## Add Ansible plug-ins software templates

Add Ansible Automation Platform software templates to your Red Hat Developer Hub instance so users can create new Ansible playbooks and collection projects based on Ansible best practices.

### Procedure

1.  Edit your custom Red Hat Developer Hub config map, for example `app-config-rhdh`.
2.  Add the following code to your Red Hat Developer Hub `app-config-rhdh.yaml` file.

```
data:
  app-config-rhdh.yaml: |
    catalog:
      ...
      locations:
        ...
        - type: url
          target: https://github.com/ansible/ansible-rhdh-templates/blob/main/all.yaml
          rules:
            - allow: [Template]
```

## Configure Role Based Access Control

Red Hat Developer Hub offers Role-based Access Control (RBAC) functionality. RBAC can then be applied to the Ansible plug-ins content.

### Procedure

 Assign the following roles:

- Members of the `admin:superUsers` group can select templates in the **Create** tab of the Ansible plug-ins to create playbook and collection projects.

- Members of the `admin:users` group can view templates in the **Create** tab of the Ansible plug-ins. The following example adds RBAC to Red Hat Developer Hub.



```
data:
  app-config-rhdh.yaml: |
    plugins:
    ...
    permission:
      enabled: true
      rbac:
        admin:
          users:
            - name: user:default/<user-scm-ida>
          superUsers:
            - name: user:default/<user-admin-idb>
```
     For more information about permission policies and managing RBAC, refer to the [*Authorization in Red Hat Developer Hub*](https://docs.redhat.com/en/documentation/red_hat_developer_hub/1.6/html-single/authorization_in_red_hat_developer_hub/index) guide for Red Hat Developer Hub.

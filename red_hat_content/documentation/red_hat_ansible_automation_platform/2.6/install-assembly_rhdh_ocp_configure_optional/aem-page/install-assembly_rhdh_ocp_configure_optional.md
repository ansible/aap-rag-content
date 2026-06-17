+++
template = "docs/aem-title.html"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.6/install-assembly_rhdh_ocp_configure_optional"
title = "Optional configurations - Red Hat Ansible Automation Platform 2.6"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6", "2.6"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6/install-assembly_rhdh_intro/", "Install Ansible plug-ins for Red Hat Developer Hub"]]
category = "Install"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/install-assembly_rhdh_ocp_configure_optional/aem-page/install-assembly_rhdh_ocp_configure_optional.html"
last_crumb = "Optional configurations"
modified = "2026-05-21T14:12:12.122Z"
multi_page_path = ""
name = "Optional configurations"
oversized = "false"
page_slug = "install-assembly_rhdh_ocp_configure_optional"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.6"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/install-assembly_rhdh_ocp_configure_optional"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/install-assembly_rhdh_ocp_configure_optional/toc/toc.json"
type = "aem-page"
+++

# Optional configurations

Enable Red Hat Developer Hub authentication and configure optional integrations, such as connecting to OpenShift Dev Spaces or specifying a private automation hub URL. While optional, these configurations enhance the user experience and functionality of the plug-ins.

## Enable Red Hat Developer Hub authentication

Enable Red Hat Developer Hub (RHDH) authentication to integrate with Source Control Management (SCM) systems. This capability is necessary for the plug-ins to create repositories.

### Procedure

 To enable Red Hat Developer Hub authentication refer to the [Enabling authentication in Red Hat Developer Hub](/documentation/en-us/red_hat_ansible_automation_platform/2.6/install-assembly_rhdh_ocp_configure_optional#rhdh-enable-rhdh-authentication "Enable Red Hat Developer Hub (RHDH) authentication to integrate with Source Control Management (SCM) systems. This capability is necessary for the plug-ins to create repositories.").

## Configure Ansible plug-ins optional integrations

The Ansible plug-ins provide integrations with Ansible Automation Platform and other optional Red Hat products.

### Procedure

 To edit your custom ConfigMap, log in to the OpenShift UI and navigate to Select Project ( developerHubProj )> (and then)ConfigMaps> (and then){developer-hub}-app-config-rhdh> (and then)app-config-rhdh.

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

- You have a private automation hub instance. For more information, see [Manage your automation content in private automation hub](/documentation/en-us/red_hat_ansible_automation_platform/2.6/assembly_managing_collections_hub "As a content creator, you can use namespaces in automation hub to curate and manage collections.")

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

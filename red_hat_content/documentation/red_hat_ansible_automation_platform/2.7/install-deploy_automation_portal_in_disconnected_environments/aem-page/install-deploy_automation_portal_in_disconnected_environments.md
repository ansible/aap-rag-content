+++
template = "docs/aem-title.html"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-deploy_automation_portal_in_disconnected_environments"
title = "Deploy automation portal in disconnected environments - Red Hat Ansible Automation Platform 2.7"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-install_automation_portal_on_openshift_container_platform/", "Install automation portal on OpenShift Container Platform"]]
category = "Install"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/install-deploy_automation_portal_in_disconnected_environments/aem-page/install-deploy_automation_portal_in_disconnected_environments.html"
last_crumb = "Deploy automation portal in disconnected environments"
latest = "true"
modified = "2026-10-06T15:21:13.207Z"
multi_page_path = ""
name = "Deploy automation portal in disconnected environments"
oversized = "false"
page_slug = "install-deploy_automation_portal_in_disconnected_environments"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/install-deploy_automation_portal_in_disconnected_environments"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/install-deploy_automation_portal_in_disconnected_environments/toc/toc.json"
type = "aem-page"
+++

# Deploy automation portal in disconnected environments

Deploy the automation portal operator in air-gapped or disconnected OpenShift environments by mirroring container images and operator artifacts to an internal registry.

## Before you begin

- An OpenShift Container Platform cluster with a configured mirror registry.
- A connected workstation with access to `registry.redhat.io` and `ghcr.io` for downloading images.
- The `oc` CLI installed and authenticated to both your OpenShift cluster and your mirror registry.
- AAP OAuth credentials prepared. See [Install the automation portal operator](/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-install_the_automation_portal_operator#install-portal-operator "Install the automation portal operator from the Software Catalog on OpenShift and deploy a portal instance by creating an AutomationPortal custom resource.") for the credentials Secret format.

Important:

The automation portal operator is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production.

## About this task

In disconnected environments, the operator and all container images must be available from an internal mirror registry. You mirror the required images from the Red Hat and GitHub container registries to your internal registry, then configure the `AutomationPortal` custom resource to use the mirrored locations.

## Procedure

1. From a connected workstation, mirror the required container images to your internal registry.
      The following images are required for a complete deployment:

    | Source image                                                                                                                 | Purpose                                                                  |
    | ---------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------ |
    | `registry.redhat.io/rhdh/rhdh-hub-rhel9:1.10`                                                                                | Base Red Hat Developer Hub container                                     |
    | `registry.redhat.io/rhel9/postgresql-15:latest`                                                                              | Local PostgreSQL database, managed by the Red Hat Developer Hub Operator |
    | `registry.redhat.io/ansible-automation-platform-27/ansible-dev-tools-rhel9:latest`                                           | DevTools sidecar                                                         |
    | `registry.redhat.io/ansible-automation-platform/automation-portal:2.2`                                                       | OCI plugins                                                              |
    | `ghcr.io/redhat-developer/rhdh-plugin-export-overlays/backstage-plugin-auth-backend-module-github-provider:bs_1.49.4__0.5.1` | GitHub auth module                                                       |
    | `ghcr.io/redhat-developer/rhdh-plugin-export-overlays/backstage-plugin-auth-backend-module-gitlab-provider:bs_1.49.4__0.4.1` | GitLab auth module                                                       |
  Note:
  The GitHub and GitLab authentication module images (the two `ghcr.io` entries) are required only if you enable GitHub or GitLab authentication or source control management (SCM) integration. If you do not use either integration, you can omit these two images from the mirror.
  

```terminal
$ oc image mirror \
  --preserve-digests \
  registry.redhat.io/rhdh/rhdh-hub-rhel9:1.10 \
  <mirror-registry>/rhdh/rhdh-hub-rhel9:1.10
```

    The `--preserve-digests` flag is required. The operator resolves images and OCI plugin artifacts by SHA digest. Without digest preservation, plugin installation fails because the mirror registry cannot match the expected digest. Repeat for each image in the table, replacing `<mirror-registry>` with your internal registry hostname.

2. If your mirror registry requires authentication, create a pull secret on the OpenShift cluster.
  

```terminal
$ oc create secret docker-registry registry-auth \
  --namespace automation-portal \
  --docker-server=<mirror-registry> \
  --docker-username='<username>' \
  --docker-password='<password>'
```

      Link the pull secret to the default service account:

  

```terminal
$ oc secrets link default registry-auth --for=pull -n automation-portal
```

3. Create the AAP credentials Secret in the target namespace.
      Follow the same procedure as a connected deployment. See [Install the automation portal operator](/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-install_the_automation_portal_operator#install-portal-operator "Install the automation portal operator from the Software Catalog on OpenShift and deploy a portal instance by creating an AutomationPortal custom resource."), step 2.

4. Create an `AutomationPortal` custom resource with mirror registry overrides.
      The following example configures all image references to use your internal mirror registry:

  

```yaml
apiVersion: automationportal.aap.redhat.com/v1alpha1
kind: AutomationPortal
metadata:
  name: portal
  namespace: automation-portal
spec:
  aap:
    checkSSL: false
    credentials:
      secretRef: secrets-rhaap-portal
  plugins:
    registry: mirror.internal.example.com
    ociPluginImage: mirror.internal.example.com/ansible-automation-platform/automation-portal
    ghcrRegistry: mirror.internal.example.com
  backstage:
    image:
      registry: mirror.internal.example.com
      repository: rhdh/rhdh-hub-rhel9
      tag: "1.10"
  devtools:
    image:
      registry: mirror.internal.example.com
      repository: ansible-automation-platform-27/ansible-dev-tools-rhel9
      tag: latest
```

      Replace `mirror.internal.example.com` with your internal registry hostname throughout the custom resource.

    The `ghcrRegistry` field redirects the GitHub and GitLab authentication plugin images — normally pulled from `ghcr.io` — to your internal mirror. These community plugin images are not part of the operator bundle's `relatedImages`, so catalog mirroring tools do not copy them automatically. Mirror them manually as shown in step 1, and set `ghcrRegistry` so the operator pulls them from your mirror.

  Important:
      Set `checkSSL: false` only if your mirror registry or AAP instance uses self-signed certificates. The default is `true`, which enforces SSL certificate validation. Keep `checkSSL: true` for production environments.

    In disconnected environments, the built-in Ansible scaffold templates cannot be retrieved from GitHub. Mirror the template YAML files to an internal HTTP server and set `spec.plugins.catalog.templateBaseURL` to the mirrored location.

5. Apply the custom resource.
  

```terminal
$ oc apply -f portal-airgapped.yaml -n automation-portal
```

6. Monitor the deployment status.
  

```terminal
$ oc get automationportal portal -n automation-portal -w
```

      Wait for `Phase: Running`. If the phase stays `Pending`, check the status conditions for image pull or registry connectivity errors. See [Troubleshoot your portal operator deployment](/documentation/en-us/red_hat_ansible_automation_platform/2.7/troubleshoot-troubleshoot_your_portal_operator_deployment#troubleshoot-portal-operator "Diagnose and resolve common issues when deploying or operating the automation portal operator on OpenShift, including status condition interpretation, log collection, and cleanup procedures.").

## Results

The automation portal is deployed in the disconnected environment using mirrored images. All operator and portal container images are served from your internal registry.

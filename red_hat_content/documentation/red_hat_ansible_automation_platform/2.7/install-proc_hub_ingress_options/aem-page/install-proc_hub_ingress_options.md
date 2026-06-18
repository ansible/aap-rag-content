+++
template = "docs/aem-title.html"
title = "Configure ingress options for automation hub - Red Hat Ansible Automation Platform 2.7"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-proc_hub_ingress_options"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-assembly_operator_install_operator/", "Install on OpenShift Container Platform"]]
category = "Install"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/install-proc_hub_ingress_options/aem-page/install-proc_hub_ingress_options.html"
last_crumb = "Configure ingress options for automation hub"
modified = "2026-06-05T07:48:10.594Z"
multi_page_path = ""
name = "Configure ingress options for automation hub"
oversized = "false"
page_slug = "install-proc_hub_ingress_options"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/install-proc_hub_ingress_options"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/install-proc_hub_ingress_options/toc/toc.json"
type = "aem-page"
+++

# Configure ingress options for automation hub

The Ansible Automation Platform Operator installation form allows you to further configure your automation hub operator ingress under **Advanced configuration**.

## About this task

## Procedure

1.  Log in to Red Hat OpenShift Container Platform.
2.  Navigate to Operators> (and then)Installed Operators.
3.  Select your Ansible Automation Platform Operator deployment.
4.  Select the **Ansible Automation Platform** tab.
5.  Click the ⋮ icon next to your Ansible Automation Platform instance and select **Edit AnsibleAutomationPlatform** .
6.  Click **YAML view** and locate the `spec.hub:` section..
7.  Configure the route options under the `hub:` section:
  

```
spec:
  hub:
    ingress_type: Ingress
    ingress_annotations: |
      nginx.ingress.kubernetes.io/proxy-body-size: "0"
      nginx.ingress.kubernetes.io/proxy-connect-timeout: "600"
    ingress_tls_secret: hub-ingress-tls-secret
```

8.  Click **Save**.
  
  Note:
      These settings apply to the automation hub component managed by this Ansible Automation Platform instance. The operator automatically updates the ingress configuration for the hub.

    For more examples of Ansible Automation Platform custom resources, see [Red Hat Ansible Automation Platform custom resources](/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-assembly_appendix_operator_crs#appendix-operator-crs_appendix-operator-crs "This appendix provides a reference for the Ansible Automation Platform custom resources for various deployment scenarios.")

9.  

## Results

After you have configured your automation hub ingress settings, OpenShift Container Platform updates the pods. This may take a few minutes.

You can view the progress by navigating to Workloads> (and then)Pods and locating the newly created instance.

Verify that the following operator pods provided by the Ansible Automation Platform Operator installation from automation hub are running:

| Operator manager controllers                                                                                                                                                                                                | Automation controller                                                                                                | Automation hub                                                                                                                    |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| <br>The operator manager controllers for each of the 3 operators, include the following:<br>automation-controller-operator-controller-managerautomation-hub-operator-controller-managerresource-operator-controller-manager | <br>After deploying automation controller, you will see the addition of these pods:<br>controllercontroller-postgres | <br>After deploying automation hub, you will see the addition of these pods:<br>hub-apihub-contenthub-postgreshub-redishub-worker |


Note:

A missing pod can indicate the need for a pull secret. Pull secrets are required for protected or private image registries. See [Using image pull secrets](https://docs.openshift.com/container-platform/4.11/openshift_images/managing_images/using-image-pull-secrets.html) for more information. You can diagnose this issue further by running `oc describe pod <pod-name>` to see if there is an ImagePullBackOff error on that pod.

+++
title = "Configure automation hub route options - Red Hat Ansible Automation Platform 2.6"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.6/install-proc_hub_route_options"
template = "docs/aem-title.html"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6", "2.6"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6/install-assembly_operator_install_operator/", "Install on OpenShift Container Platform"]]
category = "Install"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/install-proc_hub_route_options/aem-page/install-proc_hub_route_options.html"
last_crumb = "Configure automation hub route options"
modified = "2026-05-21T14:12:12.122Z"
multi_page_path = ""
name = "Configure automation hub route options"
oversized = "false"
page_slug = "install-proc_hub_route_options"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.6"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/install-proc_hub_route_options"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/install-proc_hub_route_options/toc/toc.json"
type = "aem-page"
+++

# Configure automation hub route options

The Red Hat Ansible Automation Platform operator installation form allows you to further configure your automation hub operator route options under **Advanced configuration**.

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
    ingress_type: Route
    route_host: hub.example.com  # Custom hostname for the route
    route_tls_termination_mechanism: Edge  # Options: Edge, Passthrough
    route_tls_secret: hub-tls-secret  # Optional: TLS credential secret
```

8.  Click **Save.**
  
  Note:
      Edge termination is recommended for most instances. After configuring your route, you can customize additional route settings by adding them to the `hub:` section in the Ansible Automation Platform custom resource.

    For more examples of Ansible Automation Platform custom resources, see [Red Hat Ansible Automation Platform custom resources](/documentation/en-us/red_hat_ansible_automation_platform/2.6/install-assembly_appendix_operator_crs#appendix-operator-crs_appendix-operator-crs "This appendix provides a reference for the Ansible Automation Platform custom resources for various deployment scenarios.") .

9.  
10.  

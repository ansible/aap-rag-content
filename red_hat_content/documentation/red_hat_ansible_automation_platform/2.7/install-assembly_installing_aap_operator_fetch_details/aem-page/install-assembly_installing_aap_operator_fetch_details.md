+++
title = "Access Ansible Automation Platform through the CLI - Red Hat Ansible Automation Platform 2.7"
template = "docs/aem-title.html"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-assembly_installing_aap_operator_fetch_details"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-assembly_operator_install_operator/", "Install on OpenShift Container Platform"]]
category = "Install"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/install-assembly_installing_aap_operator_fetch_details/aem-page/install-assembly_installing_aap_operator_fetch_details.html"
last_crumb = "Access Ansible Automation Platform through the CLI"
modified = "2026-06-05T07:48:10.594Z"
multi_page_path = ""
name = "Access Ansible Automation Platform through the CLI"
oversized = "false"
page_slug = "install-assembly_installing_aap_operator_fetch_details"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/install-assembly_installing_aap_operator_fetch_details"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/install-assembly_installing_aap_operator_fetch_details/toc/toc.json"
type = "aem-page"
+++

# Access Ansible Automation Platform through the CLI

You can use the OpenShift Container Platform CLI to fetch the web address and the password of the Automation controller that you created. To login to the platform gateway, you need the web address and the password.

## Fetch the platform gateway web address

A Red Hat OpenShift Container Platform route exposes a service at a host name, so that external clients can reach it by name. When you created the platform gateway instance, a route was created for it. The route inherits the name that you assigned to the platform gateway object in the YAML file.

### About this task

### Procedure

 Use the following command to fetch the routes:

```
oc get routes -n <platform_namespace>
```

### Results

You can see in the following example, the `example` platform gateway is running in the `ansible-automation-platform` namespace.

```
$ oc get routes -n ansible-automation-platform

NAME      HOST/PORT                                              PATH   SERVICES          PORT   TERMINATION     WILDCARD
example   example-ansible-automation-platform.apps-crc.testing          example-service   http   edge/Redirect   None
```
The address for the platform gateway instance is `example-ansible-automation-platform.apps-crc.testing`.

## Fetch the platform gateway password

The YAML block for the platform gateway instance in the `AnsibleAutomationPlatform` object assigns values to the *name* and *admin_user* keys.

### About this task

### Procedure

1.  Use these values in the following command to fetch the password for the platform gateway instance.

```
oc get secret/<your instance name>-<admin_user>-password -o yaml
```

2.  The default value for *admin_user* is `admin`. Modify the command if you changed the admin username in the `AnsibleAutomationPlatform` object. The following example retrieves the password for a platform gateway object called `example`:

```
oc get secret/example-admin-password -o yaml
```
    The base64 encoded password for the platform gateway instance is listed in the `metadata` field in the output:

```
$ oc get secret/example-admin-password -o yaml

    apiVersion: v1
data:
  password: ODzLODzLODzLODzLODzLODzLODzLODzLODzLODzLODzL
kind: Secret
metadata:
  labels:
    app.kubernetes.io/component: aap
    app.kubernetes.io/name: example
    app.kubernetes.io/operator-version: ""
    app.kubernetes.io/part-of: example
  name: example-admin-password
  namespace: ansible-automation-platform
```

## Decode the platform gateway password

After you have fetched your gateway password, you must decode it from base64.

### About this task

### Procedure

 Run the following command to decode your password from base64:

```
oc get secret/example-admin-password -o jsonpath={.data.password} | base64 --decode
```

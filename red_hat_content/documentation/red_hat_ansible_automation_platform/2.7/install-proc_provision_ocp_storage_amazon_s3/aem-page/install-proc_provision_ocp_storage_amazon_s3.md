+++
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-proc_provision_ocp_storage_amazon_s3"
title = "Configure object storage on Amazon S3 - Red Hat Ansible Automation Platform 2.7"
template = "docs/aem-title.html"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-assembly_operator_install_operator/", "Install on OpenShift Container Platform"]]
category = "Install"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/install-proc_provision_ocp_storage_amazon_s3/aem-page/install-proc_provision_ocp_storage_amazon_s3.html"
last_crumb = "Configure object storage on Amazon S3"
modified = "2026-06-05T07:48:10.594Z"
multi_page_path = ""
name = "Configure object storage on Amazon S3"
oversized = "false"
page_slug = "install-proc_provision_ocp_storage_amazon_s3"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/install-proc_provision_ocp_storage_amazon_s3"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/install-proc_provision_ocp_storage_amazon_s3/toc/toc.json"
type = "aem-page"
+++

# Configure object storage on Amazon S3

Red Hat supports Amazon Simple Storage Service (S3) for automation hub. You can configure it when deploying the `AnsibleAutomationPlatform` custom resource (CR), or you can configure it for an existing instance.

## Before you begin

- Create an Amazon S3 bucket to store the objects.
- Note the name of the S3 bucket.

## About this task

## Procedure

1.  Create a Kubernetes secret containing the AWS credentials and connection details, and the name of your Amazon S3 bucket. The following example creates a secret called `test-s3`:
  

```yaml
$ oc -n $HUB_NAMESPACE apply -f- <<EOF
apiVersion: v1
kind: Secret
metadata:
  name: 'test-s3'
stringData:
  s3-access-key-id: $S3_ACCESS_KEY_ID
  s3-secret-access-key: $S3_SECRET_ACCESS_KEY
  s3-bucket-name: $S3_BUCKET_NAME
  s3-region: $S3_REGION
EOF
```

2.  Add the secret to the Ansible Automation Platform custom resource (CR) under the `hub` section in the `spec`:
  

```yaml
apiVersion: aap.ansible.com/v1alpha1
kind: AnsibleAutomationPlatform
metadata:
  name: myaap
spec:
  hub:
    storage_type: S3
    object_storage_s3_secret: test-s3
```
  
  Note:
      If you have an existing automation hub instance, specify its name using `hub.name: existing-hub-name` to apply these settings to the existing instance.

    For more examples of Ansible Automation Platform custom resources, see [Red Hat Ansible Automation Platform custom resources](/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-assembly_appendix_operator_crs#appendix-operator-crs_appendix-operator-crs "This appendix provides a reference for the Ansible Automation Platform custom resources for various deployment scenarios.")

3.  If you are applying this secret to an existing instance, restart the API pods for the change to take effect. `<hub-name>` is the name of your hub instance.

```bash
$ oc -n $HUB_NAMESPACE delete pod -l app.kubernetes.io/name=<hub-name>-api
```

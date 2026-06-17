+++
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.6/observe-ref_supported_storage"
title = "Specify where to store consumption-based reports - Red Hat Ansible Automation Platform 2.6"
template = "docs/aem-title.html"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6", "2.6"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6/observe-assembly_metrics_utility/", "Generate consumption-based billing reports with the metrics-utility"]]
category = "Observe"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/observe-ref_supported_storage/aem-page/observe-ref_supported_storage.html"
last_crumb = "Specify where to store consumption-based reports"
modified = "2026-05-21T14:12:12.122Z"
multi_page_path = ""
name = "Specify where to store consumption-based reports"
oversized = "false"
page_slug = "observe-ref_supported_storage"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.6"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/observe-ref_supported_storage"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/observe-ref_supported_storage/toc/toc.json"
type = "aem-page"
+++

# Specify where to store consumption-based reports

Supported storage is available for storing the raw data obtained by using the `metrics-utility gather_automation_controller_billing_data` command and storing the generated reports obtained by using the `metrics-utility build_report` command.

Apply the environment variables to this storage based on your Ansible Automation Platform installation.

## Local disk

For an installation of Ansible Automation Platform on Red Hat Enterprise Linux, the default storage option is a local disk. Using an OpenShift deployment of OpenShift Container Platform, default storage is a path inside the attached Persistent Volume Claim.

### Procedure

 Set the environment variables for your target directory and your local disk path.

```
# Set needed ENV VARs for gathering data and generating reports
export METRICS_UTILITY_SHIP_TARGET=directory
# Your path on the local disk
export METRICS_UTILITY_SHIP_PATH=/path_to_data_and_reports/...
```

## Object storage with S3 interface

To use object storage with S3 interface, for example, with AWS S3, Ceph Object storage, or Minio, you must define environment variables for data gathering and report building commands and cronjobs.

### Procedure

 Set the environment variables for your S3 object storage path, name, endpoint, region, access key, and secret key.

```
################
export METRICS_UTILITY_SHIP_TARGET=s3
# Your path in the object storage
export METRICS_UTILITY_SHIP_PATH=path_to_data_and_reports/...

################
# Define S3 config
export METRICS_UTILITY_BUCKET_NAME=metricsutilitys3
export METRICS_UTILITY_BUCKET_ENDPOINT="https://s3.us-east-1.amazonaws.com"
# For AWS S3, define also a region
export METRICS_UTILITY_BUCKET_REGION="us-east-1"

################
# Define S3 credentials
export METRICS_UTILITY_BUCKET_ACCESS_KEY=<access_key>
export METRICS_UTILITY_BUCKET_SECRET_KEY=<secret_key>
```

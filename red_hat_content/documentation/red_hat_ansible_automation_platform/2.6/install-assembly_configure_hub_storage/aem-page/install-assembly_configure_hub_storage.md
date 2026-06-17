+++
title = "Configure storage for automation hub - Red Hat Ansible Automation Platform 2.6"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.6/install-assembly_configure_hub_storage"
template = "docs/aem-title.html"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6", "2.6"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6/install-con_aap_containerized_installation_intro/", "Install containerized Ansible Automation Platform"]]
category = "Install"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/install-assembly_configure_hub_storage/aem-page/install-assembly_configure_hub_storage.html"
last_crumb = "Configure storage for automation hub"
modified = "2026-05-21T14:12:12.122Z"
multi_page_path = ""
name = "Configure storage for automation hub"
oversized = "false"
page_slug = "install-assembly_configure_hub_storage"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.6"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/install-assembly_configure_hub_storage"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/install-assembly_configure_hub_storage/toc/toc.json"
type = "aem-page"
+++

# Configure storage for automation hub

Configure storage backends for automation hub to store automation content by using Amazon S3, Azure Blob Storage, or Network File System (NFS).

## Configure Amazon S3 storage for automation hub

Amazon S3 storage is a type of object storage that is supported in containerized installations. When using an AWS S3 storage backend, set `hub_storage_backend` to `s3`. The AWS S3 bucket needs to exist before running the installation program.

### Procedure

1.  Ensure your AWS S3 bucket exists before proceeding with the installation.
2.  Add the following variables to your inventory file under the `[all:vars]` group to configure S3 storage:
  

```
[all:vars]
hub_storage_backend=s3
hub_s3_access_key=<access_key>
hub_s3_secret_key=<secret_key>
hub_s3_bucket_name=<bucket_name>
```

3.  Optional: You can pass extra parameters to the AWS S3 storage backend by using the `hub_s3_extra_settings` variable. For example:
  

```
hub_s3_extra_settings={'AWS_S3_REGION_NAME': 'eu-south-1', 'AWS_S3_ENDPOINT_URL': 'https://endpoint'}
```

## Configure Azure Blob Storage for automation hub

Azure Blob storage is a type of object storage that is supported in containerized installations. When using an Azure blob storage backend, set `hub_storage_backend` to `azure`. The Azure container needs to exist before running the installation program.

### Procedure

1.  Ensure your Azure container exists before proceeding with the installation.
2.  Add the following variables to your inventory file under the `[all:vars]` group to configure Azure Blob storage:
  

```
[all:vars]
hub_storage_backend=azure
hub_azure_account_key=<account_key>
hub_azure_account_name=<account_name>
hub_azure_container=<container_name>
```

3.  Optional: You can pass extra parameters to the Azure Blob storage backend by using the `hub_azure_extra_settings` variable. For example:
  

```
hub_azure_extra_settings={'AZURE_LOCATION': 'foo', 'AZURE_SSL': True, 'AZURE_URL_EXPIRATION_SECS': 60}
```

## Configure Network File System (NFS) storage for automation hub

NFS is a type of shared storage that is supported in containerized installations. Shared storage is required when installing more than one instance of automation hub with a `file` storage backend. When installing a single instance of the automation hub, shared storage is optional.

### Procedure

1.  To configure shared storage for automation hub, set the `hub_shared_data_path` variable in your inventory file:
  

```yaml
hub_shared_data_path=<path_to_nfs_share>
```
    The value must match the format `host:dir`, for example `nfs-server.example.com:/exports/hub`.

2.  (Optional) To change the mount options for your NFS share, use the `hub_shared_data_mount_opts` variable. The default value is `rw,sync,hard`.

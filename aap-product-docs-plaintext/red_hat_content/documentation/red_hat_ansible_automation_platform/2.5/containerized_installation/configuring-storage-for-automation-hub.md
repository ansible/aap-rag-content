# 2. Ansible Automation Platform containerized installation
## 2.7. Advanced configuration options
### 2.7.3. Configuring storage for automation hub




Configure storage backends for automation hub including Amazon S3, Azure Blob Storage, and Network File System (NFS) storage.

#### 2.7.3.1. Configuring Amazon S3 storage for automation hub




Amazon S3 storage is a type of object storage that is supported in containerized installations. When using an AWS S3 storage backend, set `hub_storage_backend` to `s3` . The AWS S3 bucket needs to exist before running the installation program.

**Procedure**

1. Ensure your AWS S3 bucket exists before proceeding with the installation.
1. Add the following variables to your inventory file under the `    [all:vars]` group to configure S3 storage:


-  `        hub_s3_access_key`
-  `        hub_s3_secret_key`
-  `        hub_s3_bucket_name`
-  `        hub_s3_extra_settings`

You can pass extra parameters through an Ansible `        hub_s3_extra_settings` dictionary. For example:


```
hub_s3_extra_settings:          AWS_S3_MAX_MEMORY_SIZE: 4096          AWS_S3_REGION_NAME: eu-central-1          AWS_S3_USE_SSL: True
```





**Additional resources**

- For more information about the list of parameters, see [django-storages documentation - Amazon S3](https://django-storages.readthedocs.io/en/latest/backends/amazon-S3.html#settings) .


#### 2.7.3.2. Configuring Azure Blob Storage for automation hub




Azure Blob storage is a type of object storage that is supported in containerized installations. When using an Azure blob storage backend, set `hub_storage_backend` to `azure` . The Azure container needs to exist before running the installation program.

**Procedure**

1. Ensure your Azure container exists before proceeding with the installation.
1. Add the following variables to your inventory file under the `    [all:vars]` group to configure Azure Blob storage:


-  `        hub_azure_account_key`
-  `        hub_azure_account_name`
-  `        hub_azure_container`
-  `        hub_azure_extra_settings`

You can pass extra parameters through an Ansible `        hub_azure_extra_settings` dictionary. For example:


```
hub_azure_extra_settings:          AZURE_LOCATION: foo          AZURE_SSL: True          AZURE_URL_EXPIRATION_SECS: 60
```





**Additional resources**

- For more information about the list of parameters, see [django-storages documentation - Azure Storage](https://django-storages.readthedocs.io/en/latest/backends/azure.html#settings) .


#### 2.7.3.3. Configuring Network File System (NFS) storage for automation hub




NFS is a type of shared storage that is supported in containerized installations. Shared storage is required when installing more than one instance of automation hub with a `file` storage backend. When installing a single instance of the automation hub, shared storage is optional.

**Procedure**

1. To configure shared storage for automation hub, set the `    hub_shared_data_path` variable in your inventory file:


```
hub_shared_data_path=&lt;path_to_nfs_share&gt;
```

The value must match the format `    host:dir` , for example `    nfs-server.example.com:/exports/hub` .


1. (Optional) To change the mount options for your NFS share, use the `    hub_shared_data_mount_opts` variable. The default value is `    rw,sync,hard` .



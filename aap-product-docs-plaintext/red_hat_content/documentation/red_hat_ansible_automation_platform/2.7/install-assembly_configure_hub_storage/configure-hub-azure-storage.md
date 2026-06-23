# Configure storage for automation hub
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


# 5. Advanced containerized deployment
## 5.3. Configuring storage for automation hub
### 5.3.2. Configuring Azure Blob Storage for automation hub




Azure Blob storage is a type of object storage that is supported in containerized installations. When using an Azure blob storage backend, set `hub_storage_backend` to `azure` . The Azure container needs to exist before running the installation program.

**Procedure**

1. Ensure your Azure container exists before proceeding with the installation.
1. Add the following variables to your inventory file under the `    [all:vars]` group to configure Azure Blob storage:


```
[all:vars]    hub_storage_backend=azure    hub_azure_account_key=&lt;account_key&gt;    hub_azure_account_name=&lt;account_name&gt;    hub_azure_container=&lt;container_name&gt;
```


1. Optional: You can pass extra parameters to the Azure Blob storage backend by using the `    hub_azure_extra_settings` variable. For example:


```
hub_azure_extra_settings={'AZURE_LOCATION': 'foo', 'AZURE_SSL': True, 'AZURE_URL_EXPIRATION_SECS': 60}
```




**Additional resources**

-  [django-storages documentation - Azure Storage](https://django-storages.readthedocs.io/en/latest/backends/azure.html#settings)



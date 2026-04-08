# 5. Advanced containerized deployment
## 5.3. Configuring storage for automation hub
### 5.3.1. Configuring Amazon S3 storage for automation hub




Amazon S3 storage is a type of object storage that is supported in containerized installations. When using an AWS S3 storage backend, set `hub_storage_backend` to `s3` . The AWS S3 bucket needs to exist before running the installation program.

**Procedure**

1. Ensure your AWS S3 bucket exists before proceeding with the installation.
1. Add the following variables to your inventory file under the `    [all:vars]` group to configure S3 storage:


```
[all:vars]    hub_storage_backend=s3    hub_s3_access_key=&lt;access_key&gt;    hub_s3_secret_key=&lt;secret_key&gt;    hub_s3_bucket_name=&lt;bucket_name&gt;
```


1. Optional: You can pass extra parameters to the AWS S3 storage backend by using the `    hub_s3_extra_settings` variable. For example:


```
hub_s3_extra_settings={'AWS_S3_REGION_NAME': 'eu-south-1', 'AWS_S3_ENDPOINT_URL': 'https://endpoint'}
```




**Additional resources**

-  [django-storages documentation - Amazon S3](https://django-storages.readthedocs.io/en/latest/backends/amazon-S3.html#settings)



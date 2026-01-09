# 6. Job templates
## 6.16. OpenStack
### 6.16.3. Azure




Automation controller includes built-in support for managing Microsoft Azure cloud resources.

Azure cloud credentials exist as the following environment variables during playbook execution (in the job template, select the cloud credential needed for your setup):

-  `    AZURE_SUBSCRIPTION_ID`
-  `    AZURE_CERT_PATH`


Each Azure module uses these credentials when run using automation controller without having to set the `subscription_id` or `management_cert_path` module options.


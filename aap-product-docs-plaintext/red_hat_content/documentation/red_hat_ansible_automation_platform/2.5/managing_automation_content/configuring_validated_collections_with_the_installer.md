# 1. Red Hat Certified, validated, and Ansible Galaxy content in automation hub
## 1.4. Ansible validated content
### 1.4.1. Configuring validated collections with the installer




When you download and run the RPM bundle installer, certified and validated collections are automatically uploaded. Certified collections are uploaded into the `rh-certified` repository. Validated collections are uploaded into the `validated` repository.

You can change the default configuration by using two variables:

-  `    automationhub_seed_collections` is a boolean that defines whether or not preloading is enabled.
-  `    automationhub_collection_seed_repository` is a variable that enables you to specify the type of content to upload when it is set to `    true` . Possible values are `    certified` or `    validated` . If this variable is missing, both content sets will be uploaded.


Note
Changing the default configuration may require further platform configuration changes for other content you may use.




# 1. Red Hat Certified, validated, and Ansible Galaxy content in automation hub
## 1.1. Configuring Ansible automation hub remote repositories to synchronize content
### 1.1.8. Creating a requirements file




Use a requirements file to add collections to your automation hub. Requirements files are in YAML format and list the collections that you want to install in your automation hub.

A standard `requirements.yml` file contains the following parameters:

-  `    name` : the name of the collection formatted as `    &lt;namespace&gt;.&lt;collection_name&gt;`
-  `    version` : the collection version number


**Procedure**

- Create your requirements file.

In YAML format, collection information in your requirements file should look like this:


```
collections:     name: namespace.collection_name     version: 1.0.0
```




Be sure to specify the collection version number, otherwise you will sync all collection versions. Syncing all versions can require more space than expected.


**Next step**

To sync the collections in your requirements file, follow the steps in [Syncing Ansible content collections](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/managing_automation_content/managing-cert-valid-content#proc-create-synclist) .



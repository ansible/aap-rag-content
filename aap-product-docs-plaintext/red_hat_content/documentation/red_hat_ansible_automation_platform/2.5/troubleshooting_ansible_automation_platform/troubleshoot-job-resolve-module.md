# 6. Jobs
## 6.1. Issue - Jobs are failing with “ERROR! couldn’t resolve module/action” error message




Jobs are failing with the error message “ERROR! couldn’t resolve module/action 'module name'. This often indicates a misspelling, missing collection, or incorrect module path”.

This error can happen when the collection associated with the module is missing from the execution environment.

The recommended resolution is to create a custom execution environment and add the required collections inside of that execution environment. For more information about creating an execution environment, see [Using Ansible Builder](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/creating_and_using_execution_environments/assembly-using-builder) in _Creating and using execution environments_ .

Alternatively, you can complete the following steps:

**Procedure**

1. Create a `    collections` folder inside of the project repository.
1. Add a `    requirements.yml` file inside of the `    collections` folder and add the collection:


```
collections:    -<span class="emphasis"><em><span class="Role ARG Spec Role ARG Spec">&lt;collection_name&gt;</span></em></span>
```





# 3. Manage containers in private automation hub
## 3.3. Populating your private automation hub container registry
### 3.3.2. Tagging execution environments for use in automation hub




After you pull execution environments from a registry, tag them for use in your private automation hub remote registry.

**Prerequisites**

- You have pulled an execution environment from an external registry.
- You have the FQDN or IP address of the automation hub instance.


**Procedure**

- Tag a local execution environment with the automation hub container repository:


```
$ podman tag registry.redhat.io/<span class="emphasis"><em><span class="Role ARG Spec Role ARG Spec">&lt;ee_name&gt;</span></em></span>:<span class="emphasis"><em><span class="Role ARG Spec Role ARG Spec">&lt;tag&gt;</span></em></span><span class="emphasis"><em><span class="Role ARG Spec Role ARG Spec">&lt;automation_hub_hostname&gt;</span></em></span>/<span class="emphasis"><em><span class="Role ARG Spec Role ARG Spec">&lt;ee_name&gt;</span></em></span>
```




**Verification**

1. List the images in local storage:


```
$ podman images
```


1. Verify that the execution environment you recently tagged with your automation hub information is contained in the list.



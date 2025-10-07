# 3. Manage containers in private automation hub
## 3.3. Populating your private automation hub container registry
### 3.3.3. Pushing an execution environment to private automation hub




You can push tagged execution environments to private automation hub to create new containers and populate the remote registry.

**Prerequisites**

- You have permissions to create new containers.
- You have the FQDN or IP address of the Ansible Automation Platform instance.


**Procedure**

1. Log in to Podman using your Ansible Automation Platform location and credentials:


```
$ podman login -u=<span class="emphasis"><em><span class="Role ARG Spec Role ARG Spec">&lt;username&gt;</span></em></span>-p=<span class="emphasis"><em><span class="Role ARG Spec Role ARG Spec">&lt;password&gt;</span></em></span><span class="emphasis"><em><span class="Role ARG Spec Role ARG Spec">&lt;aap_url&gt;</span></em></span>
```

Warning
Let Podman prompt you for your password when you log in. Entering your password at the same time as your username can expose your password to the shell history.




1. Push your execution environment to your automation hub remote registry:


```
$ podman push<span class="emphasis"><em><span class="Role ARG Spec Role ARG Spec">&lt;automation_hub_url&gt;</span></em></span>/<span class="emphasis"><em><span class="Role ARG Spec Role ARG Spec">&lt;ee_name&gt;</span></em></span>
```




**Troubleshooting**

The `push` operation re-compresses image layers during the upload, which is not guaranteed to be reproducible and is client-implementation dependent. This may lead to image-layer digest changes and a failed push operation, resulting in `Error: Copying this image requires changing layer representation, which is not possible (image is signed or the destination specifies a digest)` .


**Verification**

1. Log in to your Ansible Automation Platform.
1. Navigate toAutomation Content→Execution Environments.
1. Locate the container in the container repository list.



# 5. Publishing an automation execution environment
## 5.1. Customizing an existing automation execution environments image




Ansible Controller includes the following default execution environments:

-  `    Minimal` - `    ansible-automation-platform-25` Includes the latest Ansible-core 2.16 release along with Ansible Runner, but does not include collections or other content. Ansible-automation-platform-24 Includes the Ansible-core 2.15 release along with Ansible Runner, but does not include collections or other content.

While supported execution environments cover many automation prerequisites, minimal execution-environments are the recommended basis for your own custom images, to keep full control over dependencies and their versions.


-  `    EE Supported` - Minimal, plus all Red Hat-supported collections and dependencies


While these environments cover many automation use cases, you can add additional items to customize these containers for your specific needs. The following procedure adds the `kubernetes.core` collection to the `ee-minimal` default image:

**Procedure**

1. Log in to `    registry.redhat.io` using Podman:


```
$ podman login -u="[username]" -p="[token/hash]" registry.redhat.io
```


1. Ensure that you can pull the required automation execution environment base image:


```
podman pull registry.redhat.io/ansible-automation-platform-24/ee-minimal-rhel8:latest
```


1. Configure your Ansible Builder files to specify the required base image and any additional content to add to the new execution environment image.


1. For example, to add the [Kubernetes Core Collection from Galaxy](https://galaxy.ansible.com/kubernetes/core) to the image, use the Galaxy entry:


```
collections:          - kubernetes.core
```


1. For more information about definition files and their content, see the [Breakdown of definition file content](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/creating_and_using_execution_environments/index#con-definition-file-breakdown) section.

1. In the execution environment definition file, specify the original `    ee-minimal` container’s URL and tag in the `    EE_BASE_IMAGE` field. In doing so, your final `    execution-environment.yml` file appears similar to the following:


<span id="idm139645553189760"></span>
**Example 5.1. A customized `    execution-environment.yml` file**


```
version: 3        images:      base_image: 'registry.redhat.io/ansible-automation-platform-25/ee-minimal-rhel9:latest'        dependencies:      galaxy:        collections:          - kubernetes.core
```




Note
Since this example uses the community version of `    kubernetes.core` and not a certified collection from automation hub, we do not need to create an `    ansible.cfg` file or reference that in our definition file.




1. Build the new execution environment image by using the following command:


```
$ ansible-builder build -t<span class="emphasis"><em><span class="Role ARG Spec Role ARG Spec">[username]</span></em></span>/<span class="emphasis"><em><span class="Role ARG Spec Role ARG Spec">new-ee</span></em></span>
```

where `    [username]` specifies your username, and `    new-ee` specifies the name of your new container image.

Note
If you do not use `    -t` with `    build` , an image called `    ansible-execution-env` is created and loaded into the local container registry.




- Use the `        podman images` command to confirm that your new container image is in that list:

The following shows the output of a 'podman images' command with the image `        new-ee` .


```
REPOSITORY          TAG     IMAGE ID      CREATED        SIZE        localhost/new-ee    latest  f5509587efbb  3 minutes ago  769 MB
```



1. Verify that the collection is installed:


```
$ podman run [username]/new-ee ansible-doc -l kubernetes.core
```


1. Tag the image for use in your automation hub:


```
$ podman tag [username]/new-ee [automation-hub-IP-address]/[username]/new-ee
```


1. Log in to your automation hub using Podman:

Note
You must have `    admin` or appropriate container repository permissions for automation hub to push a container. For more information, see [Manage containers in private automation hub](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/managing_automation_content/index#managing-containers-hub) .




```
$ podman login -u="[username]" -p="[token/hash]" [automation-hub-IP-address]
```


1. Push your image to the container registry in automation hub:


```
$ podman push [automation-hub-IP-address]/[username]/new-ee
```


1. Pull your new image into your automation controller instance:


1. Go to automation controller.
1. From the navigation panel, selectAutomation Execution→Infrastructure→Execution Environments.
1. ClickAdd.
1. Enter the appropriate information then clickSaveto pull in the new image.

Note
If your instance of automation hub is password or token protected, ensure that you have the appropriate container registry credential set up.







**Additional resources**

For more details on customizing execution environments based on common scenarios, see the following topics in the _Ansible Builder Documentation_ :


-  [Copying arbitratory files to an execution environment](https://ansible.readthedocs.io/projects/builder/en/latest/scenario_guides/scenario_copy/)
-  [Building execution environments with environment variables](https://ansible.readthedocs.io/projects/builder/en/latest/scenario_guides/scenario_using_env/)
-  [Building execution environments with environment variables and ansible.cfg](https://ansible.readthedocs.io/projects/builder/en/latest/scenario_guides/scenario_custom/)



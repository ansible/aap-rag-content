# 4. Publishing an automation execution environment
## 4.1. Customizing an existing automation execution environments image

You can customize existing Automation controller provided default automation execution environments by adding content specific to your needs. Automation controller includes the following default automation execution environments.

- `Minimal` - `ansible-automation-platform-26` Includes the latest Ansible-core 2.19 release along with Ansible Runner, but does not include collections or other content.

While supported execution environments cover many automation prerequisites, minimal execution-environments are the recommended basis for your own custom images, to keep full control over dependencies and their versions.

- `EE Supported` - Minimal, plus all Red Hat-supported collections and dependencies

While these environments cover many automation use cases, you can add additional items to customize these containers for your specific needs. The following procedure adds the `kubernetes.core` collection to the `ee-minimal` default image:

**Procedure**

1. Log in to `registry.redhat.io` using Podman:

$ podman login -u="[username]" -p="[token/hash]" registry.redhat.io

2. Ensure that you can pull the required automation execution environment base image:

podman pull registry.redhat.io/ansible-automation-platform-26/ee-minimal-rhel8:latest

3. Configure your Ansible Builder files to specify the required base image and any additional content to add to the new execution environment image.


1. For example, to add the [Kubernetes Core Collection from Galaxy](https://galaxy.ansible.com/kubernetes/core) to the image, use the Galaxy entry:

collections:
- kubernetes.core

2. For more information about definition files and their content, see the [Breakdown of definition file content](#con-definition-file-breakdown "2.7.&nbsp;Breakdown of definition file content") section.

4. In the execution environment definition file, specify the original `ee-minimal` container’s URL and tag in the `EE_BASE_IMAGE` field. In doing so, your final `execution-environment.yml` file looks similar to the following:

version: 3

images:
base_image:
name: 'registry.redhat.io/ansible-automation-platform-25/ee-minimal-rhel9:latest'

dependencies:
galaxy:
collections:
- kubernetes.core


Note
Since this example uses the community version of `kubernetes.core` and not a certified collection from automation hub, we do not need to create an `ansible.cfg` file or reference that in our definition file.

5. Build the new execution environment image by using the following command:

$ ansible-builder build -t [username]/new-ee

where `[username]` specifies your username, and `new-ee` specifies the name of your new container image.


Note
If you do not use `-t` with `build`, an image called `ansible-execution-env` is created and loaded into the local container registry.


- Use the `podman images` command to confirm that your new container image is in that list:

The following shows the output of a `podman images` command with the image `new-ee`.

REPOSITORY          TAG     IMAGE ID      CREATED        SIZE
localhost/new-ee    latest  f5509587efbb  3 minutes ago  769 MB

6. Verify that the collection is installed:

$ podman run [username]/new-ee ansible-doc -l kubernetes.core

7. Tag the image for use in your automation hub:

$ podman tag [username]/new-ee [automation-hub-IP-address]/[username]/new-ee

8. Log in to your automation hub using Podman:


Note
You must have `admin` or appropriate container repository permissions for automation hub to push a container. For more information, see [Manage containers in private automation hub](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/managing_automation_content/index#managing-containers-hub).

$ podman login -u="[username]" -p="[token/hash]" [automation-hub-IP-address]

9. Push your image to the container registry in automation hub:

$ podman push [automation-hub-IP-address]/[username]/new-ee

10. Pull your new image into your automation controller instance:


1. Go to automation controller.

2. From the navigation panel, select Automation Execution → Infrastructure → Execution Environments.

3. Click Add.

4. Enter the appropriate information then click Save to pull in the new image.


Note
If your instance of automation hub is password or token protected, ensure that you have the appropriate container registry credential set up.

**Additional resources**

- [Copying arbitratory files to an execution environment](https://ansible.readthedocs.io/projects/builder/en/latest/scenario_guides/scenario_copy/)
- [Building execution environments with environment variables](https://ansible.readthedocs.io/projects/builder/en/latest/scenario_guides/scenario_using_env/)
- [Building execution environments with environment variables and `ansible.cfg`](https://ansible.readthedocs.io/projects/builder/en/latest/scenario_guides/scenario_custom/)


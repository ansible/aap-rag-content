# 2. Using Ansible Builder
## 2.4. Building a definition file




You can use Ansible Builder to create an execution environment. Building a new execution environment involves a definition that specifies which content you want to include in your execution environment, such as collections, Python requirements, and system-level packages.

After you install Ansible Builder, you can create a definition file that Ansible Builder uses to create your automation execution environment image. Ansible Builder makes an automation execution environment image by reading and validating your definition file, then creating a `Containerfile` , and finally passing the `Containerfile` to Podman, which then packages and creates your automation execution environment image. The definition file that you create must be in `YAML` format, with a `.yaml` or `.yml extension` , and contain different sections. The default definition filename, if not provided, is `execution-environment.yml` . For more information on the parts of a definition file, see [Breakdown of definition file content](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html-single/creating_and_using_execution_environments/index#con-definition-file-breakdown) .

The following is an example of a version 3 definition file. Each definition file must specify the major version number of the Ansible Builder feature set it uses. If not specified, Ansible Builder defaults to version 1, making most new features and definition keywords unavailable.

```
version: 3

build_arg_defaults:
ANSIBLE_GALAXY_CLI_COLLECTION_OPTS: '--pre'

dependencies:
galaxy: requirements.yml
python:
- six
- psutil
system: bindep.txt

images:
base_image:
name: registry.redhat.io/ansible-automation-platform-24/ee-minimal-rhel9:latest

# Custom package manager path for the RHEL based images
options:
package_manager_path: /usr/bin/microdnf

additional_build_steps:
prepend_base:
- RUN echo This is a prepend base command!

prepend_galaxy:
# Environment variables used for Galaxy client configurations
- ENV ANSIBLE_GALAXY_SERVER_LIST=automation_hub
- ENV ANSIBLE_GALAXY_SERVER_AUTOMATION_HUB_URL=https://console.redhat.com/api/automation-hub/content/xxxxxxx-synclist/
- ENV ANSIBLE_GALAXY_SERVER_AUTOMATION_HUB_AUTH_URL=https://sso.redhat.com/auth/realms/redhat-external/protocol/openid-connect/token
# define a custom build arg env passthru - we still also have to pass
# `--build-arg ANSIBLE_GALAXY_SERVER_AUTOMATION_HUB_TOKEN` to get it to pick it up from the env
- ARG ANSIBLE_GALAXY_SERVER_AUTOMATION_HUB_TOKEN

prepend_final: |
RUN whoami
RUN cat /etc/os-release
append_final:
- RUN echo This is a post-install command!
- RUN ls -la /etc
```

-  `    build_arg_defaults` : Lists default values for build arguments.
-  `    dependencies` : Specifies the location of various requirements files.
-  `    images` : Specifies the base image to be used. Red Hat support is only provided for the redhat.registry.io base image.
-  `    options` : Specifies options that can affect builder runtime functionality.
-  `    additional_build_steps` : Commands for additional custom build steps.


**Additional resources**

-  [Breakdown of definition file content](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html-single/creating_and_using_execution_environments/index#con-definition-file-breakdown)
-  [Ansible Builder Porting Guide](https://ansible.readthedocs.io/projects/builder/en/latest/porting_guides/porting_guide/)



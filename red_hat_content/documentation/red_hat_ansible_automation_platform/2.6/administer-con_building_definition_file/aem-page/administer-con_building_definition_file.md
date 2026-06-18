+++
template = "docs/aem-title.html"
title = "Build a definition file - Red Hat Ansible Automation Platform 2.6"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.6/administer-con_building_definition_file"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6", "2.6"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6/administer-define__create__and_build_execution_environments/", "Define, create, and build execution environments"]]
category = "Administer"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/administer-con_building_definition_file/aem-page/administer-con_building_definition_file.html"
last_crumb = "Build a definition file"
modified = "2026-05-21T14:12:12.122Z"
multi_page_path = ""
name = "Build a definition file"
oversized = "false"
page_slug = "administer-con_building_definition_file"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.6"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/administer-con_building_definition_file"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/administer-con_building_definition_file/toc/toc.json"
type = "aem-page"
+++

# Build a definition file

You can use Ansible Builder to create an execution environment. Building a new execution environment involves a definition that specifies which content you want to include in your execution environment, such as collections, Python requirements, and system-level packages.

After you install Ansible Builder, you can create a definition file that Ansible Builder uses to create your automation execution environment image. Ansible Builder makes an automation execution environment image by reading and validating your definition file, then creating a `Containerfile`, and finally passing the `Containerfile` to Podman, which then packages and creates your automation execution environment image. The definition file that you create must be in `YAML` format, with a `.yaml` or `.yml extension`, and contain different sections. The default definition filename, if not provided, is `execution-environment.yml`. For more information on the parts of a definition file, see *Breakdown of definition file content*.

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
    name: registry.redhat.io/ansible-automation-platform-26/ee-minimal-rhel9:latest

# Custom package manager path for the RHEL based images
options:
  package_manager_path: /usr/bin/microdnf

additional_build_steps:
  prepend_base:
    - RUN echo This is a prepend base command!

  prepend_galaxy:
    # Environment variables used for Galaxy client configurations
    - ENV ANSIBLE_GALAXY_SERVER_LIST=automation_hub
    - ENV ANSIBLE_GALAXY_SERVER_AUTOMATION_HUB_URL=https://console.redhat.com/api/automation-hub/content/published/
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


- `build_arg_defaults`: Lists default values for build arguments.
- `dependencies`: Specifies the location of various requirements files.
- `images`: Specifies the base image to be used. Red Hat support is only provided for the redhat.registry.io base image.
- `options`: Specifies options that can affect builder runtime functionality.
- `additional_build_steps`: Commands for additional custom build steps.

## Definition dependencies

You can include dependencies that must be installed into the final image in the dependencies section of your definition file.

To avoid issues with your automation execution environment image, make sure that the entries for Galaxy, Python, and system point to a valid requirements file, or are valid content for their file types.

## Galaxy

The `galaxy` entry points to a valid requirements file or includes inline content for the `ansible-galaxy collection install -r …​` command.

The entry `requirements.yml` can be a relative path from the directory of the automation execution environment definition’s folder, or an absolute path.

The content might look like the following:

```
collections:
  - community.aws
  - kubernetes.core
```

## Python

The `python` entry in the definition file points to a valid requirements file or to an inline list of Python requirements in PEP508 format for the `pip install -r …​` command.

The entry `requirements.txt` is a file that installs extra Python requirements on top of what the Collections already list as their Python dependencies. It might be listed as a relative path from the directory of the automation execution environment definition’s folder, or an absolute path. The contents of a `requirements.txt` file should be formatted as the following example, similar to the standard output from a `pip freeze` command.

The content might look like the following:

```
boto>=2.49.0
botocore>=1.12.249
pytz
python-dateutil>=2.7.0
awxkit
packaging
requests>=2.4.2
xmltodict
azure-cli-core==2.11.1
openshift>=0.6.2
requests-oauthlib
openstacksdk>=0.13
ovirt-engine-sdk-python>=4.4.10
```

## System

The `system` entry in the definition points to a bindep requirements file or to an inline list of bindep entries, which install system-level dependencies that are outside of what the collections already include as their dependencies.

The `system` entry can be listed as a relative path from the directory of the automation execution environment definition’s folder, or as an absolute path. At a minimum, the collections must specify necessary requirements for `[platform:rpm]`.

To demonstrate this, the following is an example `bindep.txt` file that adds the `libxml2` and `subversion` packages to a container.

The content might look like the following:

```
libxml2-devel [platform:rpm]
subversion [platform:rpm]
```
Entries from multiple collections are combined into a single file. This is processed by `bindep` and then passed to `dnf`. Only requirements with no profiles or no runtime requirements will be installed to the image.

## Images

The `images` section of the definition file identifies the base image. Verification of signed container images is supported with the `podman` container runtime.

The following table shows a list of values that you can use in `images`:

| Value             | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| ----------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <br> `base_image` | <br>Specifies the parent image for the automation execution environment which enables a new image to be built that is based on an existing image. This is typically a supported execution environment base image such as *ee-minimal* or *ee-supported*, but it can also be an execution environment image that you have created and want to customize further.<br>A `name` key is required for the container image to use. Specify the `signature _original_name` key if the image is mirrored within your repository, but is signed with the image’s original signature key. Image names must contain a tag, such as `:latest`.<br>The default image is `registry.redhat.io/ansible-automation-platform-24/ee-minimal-rhel8:latest`. |

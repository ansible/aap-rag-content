# Execution environment setup reference

Review this reference information to better understand the definition of an execution environment.

You define the content of your execution environment in a YAML file. By default, this file is called `execution_environment.yml`. This file tells Ansible Builder how to create the build instruction file (Containerfile for Podman, Dockerfile for Docker) and build context for your container image.

Note:

The definition schema for Ansible Builder 3.x is documented here. If you are running an older version of Ansible Builder, you need an older schema version. We recommend using version 3, which offers substantially more configurable options and functionality than previous versions.

## Execution environment definition example

You must create a definition file to build an image for an execution environment. The file is in YAML format.

You must specify the version of Ansible Builder in the definition file. The default version is 1.

The following definition file is using Ansible Builder version 3:

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
name: registry.redhat.io/ansible-automation-platform-24/ee-minimal-rhel8:latest
additional_build_files:
- src: files/ansible.cfg
dest: configs
additional_build_steps:
prepend_galaxy:
- ADD _build/configs/ansible.cfg /home/runner/.ansible.cfg
prepend_final: |
RUN whoami
RUN cat /etc/os-release
append_final:
- RUN echo This is a post-install command!
- RUN ls -la /etc
```

## Configuration options

When defining a custom execution environment for use with automation controller, you can specify various configuration options in the definition file used by Ansible Builder to build the EE image.

Use the following configuration YAML keys in your definition file.

The Ansible Builder 3.x execution environment definition file accepts seven top-level sections:

- [Additional_build_files](/documentation/en-us/red_hat_ansible_automation_platform/2.6/administer-assembly_controller_ee_setup_reference#ref-controller-additional-build-files "Various build steps can require additional files to be present in the build context directory. These files can be specified using the additional_build_files configuration item in the controller_settings section of the controller_configuration.yml file.")
- [Additional_build_steps](/documentation/en-us/red_hat_ansible_automation_platform/2.6/administer-assembly_controller_ee_setup_reference#ref-controller-additional-build-steps "The build steps specify custom build commands for any build phase. These commands are inserted directly into the build instruction file for the container runtime, for example, Containerfile or Dockerfile. The commands must conform to any rules required by the containerization tool.")
- [build_arg_defaults](/documentation/en-us/red_hat_ansible_automation_platform/2.6/administer-assembly_controller_ee_setup_reference#ref-controller-build-arg-defaults "This specifies the default values for build arguments as a dictionary.")
- [Dependencies](/documentation/en-us/red_hat_ansible_automation_platform/2.6/administer-assembly_controller_ee_setup_reference#ref-controller-dependencies "Specifies dependencies to install into the final image, including ansible-core, ansible-runner, Python packages, system packages, and collections.")
- [Images](/documentation/en-us/red_hat_ansible_automation_platform/2.6/administer-assembly_controller_ee_setup_reference#ref-controller-images "Use the images dictionary to define container images for your execution environment. Each key represents a unique image name, while the corresponding value is a dictionary defining that image's properties.")
* [Image verification](/documentation/en-us/red_hat_ansible_automation_platform/2.6/administer-assembly_controller_ee_setup_reference#ref-controller-image-verification "You can verify signed container images if you are using the podman container runtime.")
- [Options](/documentation/en-us/red_hat_ansible_automation_platform/2.6/administer-assembly_controller_ee_setup_reference#ref-controller-config-options "A dictionary of keywords or options that can affect the runtime functionality Ansible Builder.")
- [Version](/documentation/en-us/red_hat_ansible_automation_platform/2.6/administer-assembly_controller_ee_setup_reference#ref-controller-config-version "An integer value that sets the schema version of the execution environment definition file.")




## Additional_build_files

Various build steps can require additional files to be present in the build context directory. These files can be specified using the `additional_build_files` configuration item in the `controller_settings` section of the `controller_configuration.yml` file.

The build files specify what are to be added to the build context directory. These can then be referenced or copied by `additional_build_steps` during any build stage.

The format is a list of dictionary values, each with a `src` and `dest` key and value.

Each list item must be a dictionary containing the following required keys:

| <br> **src**  | <br>Specifies the source files to copy into the build context directory.<br>This can be an absolute path, for example, `/home/user/.ansible.cfg`, or a path that is relative to the file. Relative paths can be a glob expression matching one or more files, for example, `files/\*.cfg`. Note that an absolute path must not include a regular expression. If `src` is a directory, the entire contents of that directory are copied to `dest`.                                                                                                                         |
| ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <br> **dest** | <br>Specifies a subdirectory path underneath the `_build` subdirectory of the build context directory that contains the source files, for example, `files/configs`.<br>This cannot be an absolute path or contain `..` within the path. This directory is created for you if it does not exist.  Note:   <br>When using an `ansible.cfg` file to pass a token and other settings for a private account to an automation hub server, listing the configuration file path here as a string enables it to be included as a build argument in the initial phase of the build. |

## Additional_build_steps

The build steps specify custom build commands for any build phase. These commands are inserted directly into the build instruction file for the container runtime, for example, Containerfile or Dockerfile. The commands must conform to any rules required by the containerization tool.

You can add build steps before or after any stage of the image creation process. For example, if you need `git` to be installed before you install your dependencies, you can add a build step at the end of the base build stage.

The following are the valid keys. Each supports either a multi-line string, or a list of strings.

| <br> **append\_base**     | <br>Commands to insert after building of the base image.     |
| ------------------------- | ------------------------------------------------------------ |
| <br> **append\_builder**  | <br>Commands to insert after building of the builder image.  |
| <br> **append\_final**    | <br>Commands to insert after building of the final image.    |
| <br> **append\_galaxy**   | <br>Commands to insert after building of the galaxy image.   |
| <br> **prepend\_base**    | <br>Commands to insert before building of the base image.    |
| <br> **prepend\_builder** | <br>Commands to insert before building of the builder image. |
| <br> **prepend\_final**   | <br>Commands to insert before building of the final image.   |
| <br> **prepend\_galaxy**  | <br>Commands to insert before building of the galaxy image.  |

## build_arg_defaults

This specifies the default values for build arguments as a dictionary.

This is an alternative to using the `--build-arg` CLI flag.

Ansible Builder uses the following build arguments:

| <br> **ANSIBLE\_GALAXY\_CLI\_COLLECTION\_OPTS** | <br>Enables the user to pass the `-pre` flag and other flags to enable the installation of pre-release collections.                                                                                                                                                                                                                                                  |
| ----------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <br> **ANSIBLE\_GALAXY\_CLI\_ROLE\_OPTS**       | <br>This enables the user to pass any flags, such as `--no-deps`, to the role installation.                                                                                                                                                                                                                                                                          |
| <br> **PKGMGR\_PRESERVE\_CACHE**                | <br>This controls how often the package manager cache is cleared during the image build process.<br>If this value is not set, which is the default, the cache is cleared frequently. If the value is `always`, the cache is never cleared. Any other value forces the cache to be cleared only after the system dependencies are installed in the final build stage. |


Ansible Builder hard-codes values given inside of `build_arg_defaults` into the build instruction file, so they persist if you run your container build manually.

If you specify the same variable in the definition and at the command line with the CLI `build-arg` flag, the CLI value overrides the value in the definition.

## Dependencies

Specifies dependencies to install into the final image, including `ansible-core`, `ansible-runner`, Python packages, system packages, and collections.

Ansible Builder automatically installs dependencies for any Ansible collections you install.

In general, you can use standard syntax to constrain package versions. Use the same syntax you would pass to `dnf`, `pip`, `ansible-galaxy`, or any other package management utility. You can also define your packages or collections in separate files and reference those files in the `dependencies` section of your definition file.

The following keys are valid:

| <br> **ansible\_core**       | <br>The version of the `ansible-core` Python package to be installed.<br>This value is a dictionary with a single key, `package_pip`. The `package_pip` value is passed directly to pip for installation and can be in any format that pip supports. The following are some example values:   ``` ansible_core:     package_pip: ansible-core ansible_core:     package_pip: ansible-core==2.14.3 ansible_core:     package_pip: https://github.com/example_user/ansible/archive/refs/heads/ansible.tar.gz ```                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| ---------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <br> **ansible\_runner**     | <br>The version of the Ansible Runner Python package to be installed.<br>This value is a dictionary with a single key, `package_pip`. The `package_pip` value is passed directly to pip for installation and can be in any format that pip supports. The following are some example values:   ``` ansible_runner:     package_pip: ansible-runner ansible_runner:     package_pip: ansible-runner==2.3.2 ansible_runner:     package_pip: https://github.com/example_user/ansible-runner/archive/refs/heads/ansible-runner.tar.gz ```                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| <br> **galaxy**              | <br>Collections to be installed from Ansible Galaxy.<br>This can be a filename, a dictionary, or a multi-line string representation of an Ansible Galaxy `requirements.yml` file.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| <br> **python**              | <br>The Python installation requirements.<br>This can be a filename, or a list of requirements. Ansible Builder combines all the Python requirements files from all collections into a single file by using the `requirements-parser` library.<br>This library supports complex syntax, including references to other files. If many collections require the same *package name*, Ansible Builder combines them into a single entry and combines the constraints.<br>Ansible Builder excludes some packages in the combined file of Python dependencies even if a collection lists them as dependencies. These include test packages and packages that provide Ansible itself. The full list can is available under `EXCLUDE_REQUIREMENTS` in `src/ansible_builder/_target_scripts/introspect.py`.<br>If you need to include one of these excluded package names, use the `--user-pip` option of the `introspect` command to list it in the user requirements file.<br>Packages supplied this way are not processed against the list of excluded Python packages. |
| <br> **python\_interpreter** | <br>A dictionary that defines the Python system package name to be installed by dnf (`package_system`) or a path to the Python interpreter to be used (`python_path)`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| <br> **system**              | <br>The system packages to be installed, in bindep format. This can be a filename or a list of requirements.<br>For more information about bindep, see the [OpenDev documentation](https://docs.opendev.org/opendev/bindep/latest/readme.html).<br>For system packages, use the `bindep` format to specify cross-platform requirements, so they can be installed by whichever package management system the execution environment uses. Collections must specify necessary requirements for `[platform:rpm]`. Ansible Builder combines system package entries from multiple collections into a single file. Only requirements with no profiles (runtime requirements) are installed to the image. Entries from many collections that are duplicates of each other can be consolidated in the combined file.                                                                                                                                                                                                                                                       |


The following example uses filenames that contain the various dependencies:

```
dependencies:
python: requirements.txt
system: bindep.txt
galaxy: requirements.yml
ansible_core:
package_pip: ansible-core==2.14.2
ansible_runner:
package_pip: ansible-runner==2.3.1
python_interpreter:
package_system: "python310"
python_path: "/usr/bin/python3.10"
```
This example uses inline values:

```
dependencies:
python:
- pywinrm
system:
- iputils [platform:rpm]
galaxy:
collections:
- name: community.windows
- name: ansible.utils
version: 2.10.1
ansible_core:
package_pip: ansible-core==2.14.2
ansible_runner:
package_pip: ansible-runner==2.3.1
python_interpreter:
package_system: "python310"
python_path: "/usr/bin/python3.10"
```


Note:

If any of these dependency files (`requirements.txt, bindep.txt, and requirements.yml`) are in the `build_ignore` of the collection, the build fails.

Collection maintainers can verify that ansible-builder recognizes the requirements they expect by using the `introspect` command:

```
ansible-builder introspect --sanitize ~/.ansible/collections/
```

The `--sanitize` option reviews all of the collection requirements and removes duplicates. It also removes any Python requirements that are normally excluded (see **python** dependencies).

Use the `-v3` option to `introspect` to see logging messages about requirements that are being excluded.

## Images

Use the **images** dictionary to define container images for your execution environment. Each key represents a unique image name, while the corresponding value is a dictionary defining that image's properties.

At a minimum you must specify a source, image, and tag for the base image. The base image provides the operating system and can also provide some packages. Use the standard `host/namespace/container:tag` syntax to specify images. You can use Podman or Docker shortcut syntax instead, but the full definition is more reliable and portable.

Valid keys for this section are:

| <br> **base\_image** | <br>A dictionary defining the parent image for the execution environment.<br>A `name` key must be supplied with the container image to use. Use the `signature_original_name` key if the image is mirrored within your repository, but signed with the original image’s signature key. |
| -------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

## Image verification

You can verify signed container images if you are using the `podman` container runtime.

Set the `container-policy` CLI option to control how this data is used in relation to a Podman `policy.json` file for container image signature validation.

- **`ignore_all`** policy: Generate a `policy.json` file in the build `context directory <context>` where no signature validation is performed.
- **`system`** policy: Signature validation is performed using pre-existing `policy.json` files in standard system locations. `ansible-builder` assumes no responsibility for the content within these files, and the user has complete control over the content.
- **`signature_required`** policy: `ansible-builder` uses the container image definitions to generate a `policy.json` file in the build `context directory <context>` that is used during the build to validate the images.

## Options

A dictionary of keywords or options that can affect the runtime functionality Ansible Builder.

Valid keys for this section are:

- **container_init**: A dictionary with keys that allow for customization of the container `ENTRYPOINT` and `CMD` directives (and related behaviors). Customizing these behaviors is an advanced task, and can result failures that are difficult to debug. Because the provided defaults control several intertwined behaviors, overriding any value skips all remaining defaults in this dictionary. Valid keys are:

* **cmd**: Literal value for the `CMD` Containerfile directive. The default value is `["bash"]`.
* **entrypoint**: Literal value for the `ENTRYPOINT` Containerfile directive. The default entrypoint behavior handles signal propagation to subprocesses, and attempting to ensure at runtime that the container user has a proper environment with a valid writeable home directory, represented in `/etc/passwd`, with the `HOME` environment variable set to match. The default entrypoint script can emit warnings to `stderr` in cases where it is unable to suitably adjust the user runtime environment. This behavior can be ignored or elevated to an unrecoverable error; consult the source for the `entrypoint` target script for more details.
* **package_pip**: Package to install with pip for entrypoint support. This package is installed in the final build image.

- **package_manager_path**: string with the path to the package manager (dnf or microdnf) to use. This value is used to install packages.

- **skip_ansible_check**: This boolean value controls whether or not the check for an installation of Ansible and Ansible Runner is performed on the final image. Set this value to `True` to not perform this check.

The default is `False`.

- **relax_passwd_permissions**: This boolean value controls whether the `root` group (GID 0) is explicitly granted write permission to `/etc/passwd` in the final container image. The default entrypoint script can attempt to update `/etc/passwd` under some container runtimes with dynamically created users to ensure a fully-functional POSIX user environment and home directory. Disabling this capability can cause failures of software features that require users to be listed in `/etc/passwd` with a valid and writeable home directory, for example, `async` in ansible-core, and the `~username` shell expansion. The default is `True`.

- **workdir**: Default current working directory for new processes started under the final container image. Some container runtimes also use this value as `HOME` for dynamically-created users in the `root` (GID 0) group. When this value is specified, if the directory does not already exist, it is created, set to `root` group ownership, and `rwx` group permissions are recursively applied to it. The default value is `/runner`.

- **user**: This sets the username or UID to use as the default user for the final container image. The default value is `1000`.

**Example**

```
options:
container_init:
package_pip: dumb-init>=1.2.5
entrypoint: '["dumb-init"]'
cmd: '["csh"]'
package_manager_path: /usr/bin/microdnf
relax_password_permissions: false
skip_ansible_check: true
workdir: /myworkdir
user: bob
```

## Version

An integer value that sets the schema version of the execution environment definition file.

Defaults to `1`.

The value must be `3` if you are using Ansible Builder 3.x.

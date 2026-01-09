# 2. Using Ansible Builder
## 2.7. Breakdown of definition file content
### 2.7.1. Build arguments




The `build_arg_defaults` section of the definition file is a dictionary whose keys can provide default values for arguments to Ansible Builder.

The following table lists values that can be used in `build_arg_defaults` :

| Value | Description |
| --- | --- |
|  `ANSIBLE_GALAXY_CLI_COLLECTION_OPTS` | Passes arbitrary arguments to the ansible-galaxy CLI during the collection installation phase.

For example, the `-pre` flag to enable the installation of pre-release collections, or `-c` to disable verification of the server’s SSL/TLS certificate. |
|  `ANSIBLE_GALAXY_CLI_ROLE_OPTS` | Passes any flags, such as `-no-deps` , to the role installation. |


Note
It is generally easier (especially in a pipeline context) to customize the base image into a custom base image using Podman first, and then call `ansible-builder` on this custom image.



The values given inside `build_arg_defaults` will be hard-coded into the `Containerfile` , so these values will persist if `podman build` is called manually.

Note
If you specify the same variable in the CLI `--build-arg` flag, the CLI value takes higher precedence.




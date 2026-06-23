# Execution environment setup reference
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


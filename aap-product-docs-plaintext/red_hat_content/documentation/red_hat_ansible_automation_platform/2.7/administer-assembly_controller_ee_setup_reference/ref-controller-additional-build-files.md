# Execution environment setup reference
## Additional_build_files

Various build steps can require additional files to be present in the build context directory. These files can be specified using the `additional_build_files` configuration item in the `controller_settings` section of the `controller_configuration.yml` file.

The build files specify what are to be added to the build context directory. These can then be referenced or copied by `additional_build_steps` during any build stage.

The format is a list of dictionary values, each with a `src` and `dest` key and value.

Each list item must be a dictionary containing the following required keys:

| <br> **src**  | <br>Specifies the source files to copy into the build context directory.<br>This can be an absolute path, for example, `/home/user/.ansible.cfg`, or a path that is relative to the file. Relative paths can be a glob expression matching one or more files, for example, `files/\*.cfg`. Note that an absolute path must not include a regular expression. If `src` is a directory, the entire contents of that directory are copied to `dest`.                                                                                                                         |
| ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <br> **dest** | <br>Specifies a subdirectory path underneath the `_build` subdirectory of the build context directory that contains the source files, for example, `files/configs`.<br>This cannot be an absolute path or contain `..` within the path. This directory is created for you if it does not exist.  Note:   <br>When using an `ansible.cfg` file to pass a token and other settings for a private account to an automation hub server, listing the configuration file path here as a string enables it to be included as a build argument in the initial phase of the build. |


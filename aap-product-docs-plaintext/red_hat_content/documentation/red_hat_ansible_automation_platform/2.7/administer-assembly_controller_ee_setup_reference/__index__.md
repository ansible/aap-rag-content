# Execution environment setup reference

Review this reference information to better understand the definition of an execution environment.

You define the content of your execution environment in a YAML file. By default, this file is called `execution_environment.yml`. This file tells Ansible Builder how to create the build instruction file (Containerfile for Podman, Dockerfile for Docker) and build context for your container image.

Note:

The definition schema for Ansible Builder 3.x is documented here. If you are running an older version of Ansible Builder, you need an older schema version. We recommend using version 3, which offers substantially more configurable options and functionality than previous versions.


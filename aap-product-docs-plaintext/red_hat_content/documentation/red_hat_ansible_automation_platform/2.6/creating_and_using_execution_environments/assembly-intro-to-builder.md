# Chapter 1. Introduction to automation execution environments




Using Ansible content that depends on non-default dependencies can be complicated because the packages must be installed on each node, interact with other software installed on the host system, and be kept in sync.

You must use the same environment during development, testing and in production. Red Hat provides execution environments for this purpose.

Automation execution environments help simplify this process and you can easily create them with Ansible Builder.

**Builder** Builder is a command line tool that makes it easy to build, test, and publish container images for use as Ansible execution environments.

Ansible provides an [Execution Environment Utilities Collection](https://github.com/redhat-cop/ee_utilities) , `infra.ee_utilities` . Red Hat provides execution environments for this purpose. This is a collection of roles for creating and managing images, or migrating from the older Tower virtualenvs to execution environment. Using this collection, you can automate the preparation and maintenance of Ansible execution environments.


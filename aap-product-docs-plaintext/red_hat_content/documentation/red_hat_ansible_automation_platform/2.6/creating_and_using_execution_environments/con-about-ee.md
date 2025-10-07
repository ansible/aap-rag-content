# 2. Builder
## 2.1. About automation execution environments




All automation in Red Hat Ansible Automation Platform runs on container images called automation execution environments. Automation execution environments create a common language for communicating automation dependencies, and offer a standard way to build and distribute the automation environment.

Red Hat provides supported execution environments for you to use in the [Red Hat ecosystem catalog](https://catalog.redhat.com/search?gs&q=execution%20environments&searchType=containers) .

An automation execution environment should contain the following:

- Ansible Core 2.16 or later
- Python 3.11 or later
- Ansible Runner
- Ansible content collections and their dependencies
- System dependencies



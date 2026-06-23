# Automate nodes that comply with security profiles
## Fapolicyd on managed RHEL nodes

Ansible jobs on RHEL nodes often fail if the `fapolicyd` service is enabled. This occurs because the service prevents the execution of Python code copied to the node during task processing.

To prevent this issue from occurring, use one of the following methods:

- Option 1: Set the fapolicyd service to permissive mode
- Option 2: Create custom fapolicyd rules


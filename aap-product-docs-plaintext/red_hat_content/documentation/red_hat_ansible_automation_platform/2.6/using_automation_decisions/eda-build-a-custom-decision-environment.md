# 5. Decision environments
## 5.3. Building a custom decision environment for Event-Driven Ansible




Customize a decision environment container image to ensure your rulebook activations run with the precise, custom-maintained collections and dependencies they require.

**Prerequisites**

- Ansible Automation Platform > = 2.5
- Event-Driven Ansible
- Ansible Builder > = 3.0


Important
- Use the correct Event-Driven Ansible controller decision environment in Ansible Automation Platform to prevent rulebook activation failure.


- If you want to connect Event-Driven Ansible controller to Ansible Automation Platform 2.4, you must use `        registry.redhat.io/ansible-automation-platform-24/de-minimal-rhel9:latest` (recommended) or `        registry.redhat.io/ansible-automation-platform-24/de-minimal-rhel8:latest`
- If you want to connect Event-Driven Ansible controller to Ansible Automation Platform 2.5, you must use `        registry.redhat.io/ansible-automation-platform-25/de-minimal-rhel9:latest` (recommended) or `        registry.redhat.io/ansible-automation-platform-25/de-minimal-rhel8:latest`
- If you want to connect Event-Driven Ansible controller to Ansible Automation Platform 2.6, you must use `        registry.redhat.io/ansible-automation-platform-26/de-minimal-rhel9:latest`





**Procedure**

1. Use `    de-minimal` as the base image with Ansible Builder to build your custom decision environments. This image is built from a base image provided by Red Hat at [Ansible Automation Platform minimal decision environment](https://catalog.redhat.com/software/containers/ansible-automation-platform-26/de-minimal-rhel9/6449633cfb26ed69bfc5d755) .

The following is an example of the Ansible Builder definition file that uses `    de-minimal` as a base image to build a custom decision environment with the ansible.eda collection:


```
version: 3        images:      base_image:        name: 'registry.redhat.io/ansible-automation-platform-26/de-minimal-rhel9:latest'        dependencies:      galaxy:        collections:          - ansible.eda      python_interpreter:        package_system: "python3.12"        options:      package_manager_path: /usr/bin/microdnf
```


1. Optional: If you need other Python packages or RPMs, add the following to a single definition file:


```
version: 3        images:      base_image:        name: 'registry.redhat.io/ansible-automation-platform-26/de-minimal-rhel9:latest'        dependencies:      galaxy:        collections:          - ansible.eda      python:        - six        - psutil      system:        - iputils [platform:rpm]      python_interpreter:        package_system: "python3.12"        options:      package_manager_path: /usr/bin/microdnf
```





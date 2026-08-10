# Create runtime environments for event-driven automation
## Build a custom decision environment for Event-Driven Ansible

Customize a decision environment container image to ensure your rulebook activations run with the precise, custom-maintained collections and dependencies they require.

### Before you begin

- Ansible Automation Platform > = 2.5
- Event-Driven Ansible
- Ansible Builder > = 3.0

Important:

Use the `de-minimal` decision environment image that matches your version of Ansible Automation Platform to prevent rulebook activation failure. Use `registry.redhat.io/<platform-version>/de-minimal-rhel<rhel-version>:latest`.

### Procedure

1.  Use `de-minimal` as the base image with Ansible Builder to build your custom decision environments. This image is built from a base image provided by Red Hat at [Ansible Automation Platform minimal decision environment](https://catalog.redhat.com/en/search?q=de-minimal&searchType=Containers). Important:
The `ansible.eda` collection is already installed in the `de-minimal `base image. To prevent Ansible Builder from attempting to reinstall it, add `ansible.eda` to the `exclude.all_from_collections` list as shown in the following examples.

The following is an example of the Ansible Builder definition file that uses `de-minimal` as a base image to build a custom decision environment with the ansible.eda collection:

Note:
Replace `<platform-version>` with the namespace for your version of Ansible Automation Platform. Replace `<rhel-version>` with your Red Hat Enterprise Linux version

```
version: 3

images:
base_image:
name: 'registry.redhat.io/<platform-version>/de-minimal-rhel<rhel-version>:latest'

dependencies:
galaxy:
collections:
- name: servicenow.itsm
python_interpreter:
package_system: "python3.12"
exclude:
all_from_collections:
# ansible.eda is already installed in de-minimal
- ansible.eda

options:
package_manager_path: /usr/bin/microdnf
```

2.  Optional: If you need other Python packages or RPMs, add the following to a single definition file:

Note:
Replace `<platform-version>` with the namespace for your version of Ansible Automation Platform. Replace `<rhel-version>` with your Red Hat Enterprise Linux version

```
version: 3

images:
base_image:
name: 'registry.redhat.io/<platform-version>/de-minimal-rhel<rhel-version>:latest'

dependencies:
galaxy:
collections:
- name: servicenow.itsm
python:
- six
- psutil
python_interpreter:
package_system: "python3.12"
exclude:
all_from_collections:
# ansible.eda is already installed in de-minimal
- ansible.eda

options:
package_manager_path: /usr/bin/microdnf
```


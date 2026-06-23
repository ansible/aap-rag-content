# Execution environment setup reference
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


# Browse collections in a text-based format

As a content creator, you can browse your Ansible collections with automation content navigator and interactively delve into each collection developed locally or within Automation execution environments.

## Automation content navigator collections display

Understand the information displayed by Automation content navigator about your collections, such as shadowing, type, and path. This overview helps you verify the collection source and search priority.

Automation content navigator displays information about your collections with the following details for each collection:

SHADOWED
Indicates that an additional copy of the collection is higher in the search order, and playbooks prefer that collection.

TYPE
Shows if the collection is contained within an automation execution environment or volume mounted on onto the automation execution environment as a `bind_mount`.

PATH
Reflects the collections location within the automation execution environment or local file system based on the collection TYPE field.


![Automation content navigator collections display](/webassets/aem/red_hat_ansible_automation_platform/2.7/images/navigator-collections-shadow.png)

## Browse collections from automation content navigator

You can browse Ansible collections with the automation content navigator text-based user interface in interactive mode and delve into each collection. automation content navigator shows collections within the current project directory and those available in the automation execution environments

### Before you begin

- A locally accessible collection or installed automation execution environments.

### Procedure

1.  Start automation content navigator


```
$ ansible-navigator
```

2.  Browse the collection. Alternately, you can type `ansible-navigator collections` to directly browse the collections.

```
$ :collections
```

![A list of Ansible collections shown in the automation content navigator](/webassets/aem/red_hat_ansible_automation_platform/2.7/images/navigator-collection-list.png)

3.  Type the number of the collection you want to explore.

```
:4
```

![A collection shown in the automation content navigator](/webassets/aem/red_hat_ansible_automation_platform/2.7/images/navigator-plugin-list.png)

4.  Type the number corresponding to the module you want to delve into.

```
ANSIBLE.UTILS.IP_ADDRESS: Test if something in an IP address
0│---
1│additional_information: {}
2│collection_info:
3│  authors:
4│  - Ansible Community
5│  dependencies: {}
6│  description: Ansible Collection with utilities to ease the management, manipulation,
7│    and validation of data within a playbook
8│  documentation: null
9│  homepage: null
10│  issues: null
11│  license: []
12│  license_file: LICENSE
13│  name: ansible.utils
14│  namespace: ansible
15│  path:/usr/share/ansible/collections/ansible_collections/ansible/utils/
16│  readme: README.md
<... output truncated...>
```

5.  Optional: jump to the documentation examples for this module.

```
:{{ examples }}

0│
1│
2│#### Simple examples
3│
4│- name: Check if 10.1.1.1 is a valid IP address
5│  ansible.builtin.set_fact:
6│    data: "{{ '10.1.1.1' is ansible.utils.ip_address }}"
7│
8│# TASK [Check if 10.1.1.1 is a valid IP address] *********************
9│# ok: [localhost] => {
10│#     "ansible_facts": {
11│#         "data": true
12│#     },
13│#     "changed": false
14│# }
15│
```

6.  Optional: open the example in your editor to copy it into a playbook.

```
:open
```

![Documentation example shown in the editing tool](/webassets/aem/red_hat_ansible_automation_platform/2.7/images/navigator-vscode-example.png)

### Results

- Browse the collection list.
![Collection list](/webassets/aem/red_hat_ansible_automation_platform/2.7/images/navigator-collection-list.png)

## Review collection and plugin documentation

You can review Ansible documentation for collections and plugins with the automation content navigator text-based user interface in interactive mode. automation content navigator shows collections within the current project directory and those available in the automation execution environments

### Before you begin

- A locally accessible collection or installed automation execution environments.

### Procedure

1.  Start automation content navigator


```
$ ansible-navigator
```

2.  Review the module you are interested in. Alternately, you can type `ansible-navigator doc` to access the documentation.

```
:doc ansible.utils.ip_address
```

```
ANSIBLE.UTILS.IP_ADDRESS: Test if something in an IP address
0│---
1│additional_information: {}
2│collection_info:
3│  authors:
4│  - Ansible Community
5│  dependencies: {}
6│  description: Ansible Collection with utilities to ease the management, manipulation,
7│    and validation of data within a playbook
8│  documentation: null
9│  homepage: null
10│  issues: null
11│  license: []
12│  license_file: LICENSE
13│  name: ansible.utils
14│  namespace: ansible
15│  path:/usr/share/ansible/collections/ansible_collections/ansible/utils/
16│  readme: README.md
<... output truncated...>
```

3.  Jump to the documentation examples for this module.

```
:{{ examples }}

0│
1│
2│#### Simple examples
3│
4│- name: Check if 10.1.1.1 is a valid IP address
5│  ansible.builtin.set_fact:
6│    data: "{{ '10.1.1.1' is ansible.utils.ip_address }}"
7│
8│# TASK [Check if 10.1.1.1 is a valid IP address] *********************
9│# ok: [localhost] => {
10│#     "ansible_facts": {
11│#         "data": true
12│#     },
13│#     "changed": false
14│# }
15│
```

4.  Optional: open the example in your editor to copy it into a playbook.

```
:open
```

![Documentation example in editor](/webassets/aem/red_hat_ansible_automation_platform/2.7/images/navigator-vscode-example.png)
See [Automation content navigator general settings](/documentation/en-us/red_hat_ansible_automation_platform/2.7/develop-assembly_settings_navigator#ref-navigator-general-settings "The following table describes each general parameter and setting options for automation content navigator.") for details on how to set up your editor.

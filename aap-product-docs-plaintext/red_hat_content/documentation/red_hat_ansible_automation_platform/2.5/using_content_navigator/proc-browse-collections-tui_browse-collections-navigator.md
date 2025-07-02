# 5. Browsing collections with automation content navigator
## 5.2. Browsing collections from automation content navigator




You can browse Ansible collections with the automation content navigator text-based user interface in interactive mode and delve into each collection. automation content navigator shows collections within the current project directory and those available in the automation execution environments

**Prerequisites**

- A locally accessible collection or installed automation execution environments.


**Procedure**

1. Start automation content navigator


```
$ ansible-navigator
```


1. Browse the collection. Alternately, you can type `    ansible-navigator collections` to directly browse the collections.


```
$ :collections
```

![A list of Ansible collections shown in the automation content navigator](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.5-Using_content_navigator-en-US/images/a7b4611efdde018154c3717444581117/navigator-collection-list.png)



1. Type the number of the collection you want to explore.


```
:4
```

![A collection shown in the automation content navigator](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.5-Using_content_navigator-en-US/images/11c84eb67977b58176f1ce30a5aa168e/navigator-plugin-list.png)



1. Type the number corresponding to the module you want to delve into.


```
ANSIBLE.UTILS.IP_ADDRESS: Test if something in an IP address     0│---     1│additional_information: {}     2│collection_info:     3│  authors:     4│  - Ansible Community     5│  dependencies: {}     6│  description: Ansible Collection with utilities to ease the management, manipulation,     7│    and validation of data within a playbook     8│  documentation: null     9│  homepage: null    10│  issues: null    11│  license: []    12│  license_file: LICENSE    13│  name: ansible.utils    14│  namespace: ansible    15│  path:/usr/share/ansible/collections/ansible_collections/ansible/utils/    16│  readme: README.md    &lt;... output truncated...&gt;
```


1. Optional: jump to the documentation examples for this module.


```
:{{ examples }}        0│    1│    2│#### Simple examples    3│    4│- name: Check if 10.1.1.1 is a valid IP address    5│  ansible.builtin.set_fact:    6│    data: "{{ '10.1.1.1' is ansible.utils.ip_address }}"    7│    8│# TASK [Check if 10.1.1.1 is a valid IP address] *********************    9│# ok: [localhost] =&gt; {    10│#     "ansible_facts": {    11│#         "data": true    12│#     },    13│#     "changed": false    14│# }    15│
```


1. Optional: open the example in your editor to copy it into a playbook.


```
:open
```

![Documentation example shown in the editing tool](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.5-Using_content_navigator-en-US/images/3405ec63edee7bec61c21f0bc6ba5e57/navigator-vscode-example.png)





**Verification**

- Browse the collection list.

![Collection list](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.5-Using_content_navigator-en-US/images/a7b4611efdde018154c3717444581117/navigator-collection-list.png)






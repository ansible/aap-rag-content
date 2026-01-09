# 3. Getting started as an automation developer
## 3.5. Bundle automation content with roles
### 3.5.1. Creating a role




Create an Ansible role by using the `ansible-galaxy` CLI tool to build reusable automation components.

The Ansible Automation Platform bundle includes the Ansible Galaxy CLI tool. Access role-specific commands from the `role` subcommand:

```
ansible-galaxy role init &lt;role_name&gt;
```

Standalone roles outside of Collections are supported. Create new roles inside a Collection to take advantage of the features Ansible Automation Platform has to offer.

**Procedure**

1. In a terminal, navigate to the `    roles` directory inside a collection.
1. Create a role called `    my_role` inside the collection:


```
$ ansible-galaxy role init my_role
```

The collection now includes a role named `    my_role` inside the `    roles` directory, as you can see in this example:


```
~/.ansible/collections/ansible_collections/&lt;my_namespace&gt;/&lt;my_collection_name&gt;        ...        └── roles/            └── my_role/                ├── .travis.yml                ├── README.md                ├── defaults/                │   └── main.yml                ├── files/                ├── handlers/                │   └── main.yml                ├── meta/                │   └── main.yml                ├── tasks/                │   └── main.yml                ├── templates/                ├── tests/                │   ├── inventory                │   └── test.yml                └── vars/                    └── main.yml
```


1. A custom role skeleton directory can be supplied by using the `    --role-skeleton` argument. This allows organizations to create standardized templates for new roles to suit their needs.


```
$ ansible-galaxy role init my_role --role-skeleton ~/role_skeleton
```

This creates a role named `    my_role` by copying the contents of `    ~/role_skeleton` into `    my_role` . The contents of `    role_skeleton` can be any files or folders that are valid inside a role directory.





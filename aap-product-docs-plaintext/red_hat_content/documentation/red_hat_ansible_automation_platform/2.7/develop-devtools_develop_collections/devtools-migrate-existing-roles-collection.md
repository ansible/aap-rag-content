# Package and distribute automation content with collections
## Understand collections for distributing roles
### Migrate existing roles to your collection

Migrate existing standalone roles into the `roles/` directory of your new collection. You must rename roles to remove hyphens and update playbooks to use the fully qualified collection name.

#### About this task

```
my_role
├── README.md
├── defaults
│   └── main.yml
├── files
├── handlers
│   └── main.yml
├── meta
│   └── main.yml
├── tasks
│   └── main.yml
├── templates
├── tests
│   ├── inventory
│   └── test.yml
└── vars
└── main.yml
```
An Ansible role has a defined directory structure with seven main standard directories. Each role must must include at least one of these directories. You can omit any directories the role does not use. Each directory contains a `main.yml` file.

#### Procedure

1.  If necessary, rename the directory that contains your role to reflect its content, for example, `acl_config` or `tacacs`. Roles in collections cannot have hyphens in their names. Use the underscore character (`_`) instead.

2.  Copy the roles directories from your standalone role into the `roles/` directory in your collection. For example, in a collection called `myapp_network`, add your roles to the `myapp_network/roles/` directory.

3.  Copy any plug-ins from your standalone roles into the `plugins directory/` for your new collection. The collection directory structure resembles the following.

```
company_namespace
└── myapp_network
├── ...
├── galaxy.yml
├── docs
├── extensions
├── meta
├── plugins
├── roles
│   ├── acl_config
│   │   ├── README.md
│   │   ├── defaults
│   │   ├── files
│   │   ├── handlers
│   │   ├── meta
│   │   ├── tasks
│   │   ├── templates
│   │   ├── tests
│   │   └── vars
│   └── tacacs
│       ├── README.md
│       ├── default
│       ├── files
│       ├── handlers
│       ├── meta
│       ├── tasks
│       ├── templates
│       ├── tests
│       └── vars
│   ├── run
├── ...
├── tests
└── vars
```
The `run` role is a default role directory that is created when you scaffold the collection.

4.  Update your playbooks to use the fully qualified collection name (FQDN) for your new roles in your collection. Note:
Not every standalone role will seamlessly integrate into your collection without modification of the code. For example, if a third-party standalone role from Galaxy that contains a plug-in uses the `module_utils/` directory, then the plug-in itself has import statements.


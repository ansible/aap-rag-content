# Package and distribute automation content with collections

Collections are a distribution format for Ansible content that can include playbooks, roles, modules, and plugins. Red Hat provides Ansible Content Collections on Ansible automation hub that contain both Red Hat Ansible Certified Content and Ansible validated content.

If you have installed private automation hub, you can create collections for your organization and push them to private automation hub so that you can use them in job templates in Ansible Automation Platform. You can use collections to package and distribute plug-ins. These plug-ins are written in Python.

You can also create collections to package and distribute Ansible roles, which are expressed in YAML. You can also include playbooks and custom plug-ins that are required for these roles in the collection. Typically, collections of roles are distributed for use within your organization.

## Understand collections for distributing roles

An Ansible role is a self-contained unit of Ansible automation content that groups related tasks and associated variables, files, handlers, and other assets in a defined directory structure.

You can run Ansible roles in one or more plays, and reuse them across playbooks. Invoking roles instead of tasks simplifies playbooks. You can migrate existing standalone roles into collections, and push them to private automation hub to share them with other users in your organization. Distributing roles in this way is a typical way to use collections.

With Ansible collections, you can store and distribute multiple roles in a single unit of reusable automation. Inside a collection, you can share custom plug-ins across all roles in the collection instead of duplicating them in each role.

You must move roles into collections if you want to use them in Ansible Automation Platform.

You can add existing standalone roles to a collection, or add new roles to it. Push the collection to source control and configure credentials for the repository in Ansible Automation Platform.

### Plan your collection

Organize smaller bundles of curated automation into separate collections for specific functions, rather than creating one big general collection for all of your roles.

For example, you could store roles that manage the networking for an internal system called `myapp` in a `company_namespace.myapp_network` collection, and store roles that manage and deploy networking in AWS in a collection called `company_namespace.aws_net`.

### Prerequisites

You must install and configure the essential software and accounts listed in this section before you proceed.

- VS Code and the Ansible extension
- Microsoft Dev Containers extension in VS Code
- Ansible development tools
- A containerization platform, for example Podman, Podman Desktop, Docker, or Docker Desktop
- A Red Hat account and log in access to the Red Hat container registry at registry.redhat.io. For information about logging in to registry.redhat.io, see Authenticating with the Red Hat container registry.

### Generate the collection structure for roles

Scaffold a collection using the Ansible extension in VS Code. This process creates the necessary directory structure for packaging and distributing your roles and plug-ins.

#### About this task

#### Procedure

1.  Open VS Code.
2.  Navigate to the directory where you want to create your roles collection.
3.  Click the Ansible icon in the VS Code activity bar to open the Ansible extension.
4.  Select **Get started** in the **Ansible content creator** section. The **Ansible content creator** tab opens.

5.  In the **Create** section, click **Ansible collection project**. The **Create new Ansible project** tab opens.

6.  In the form in the **Create Ansible project** tab, enter the following:

- **Namespace**: Enter a name for your namespace, for example `company_namespace`.

- **Collection**: Enter a name for your collection, for example, `myapp_network`.

- **Init path**: Enter the path to the directory where you want to scaffold your new collection. If you enter an existing directory name, the scaffolding process overwrites the contents of that directory. The scaffold process only allows you to use an existing directory if you enable the Force option.

* If you are using the containerized version of Ansible development tools, the destination directory path is relative to the container, not a path in your local system. To discover the current directory name in the container, run the pwd command in a terminal in VS Code. If the current directory in the container is `workspaces`, enter `workspaces/<current_project>/collections`.
* If you are using a locally installed version of Ansible Dev tools, enter the full path to the directory, for example `/user/<username>/path/to/<collection_directory>`.

7.  Click Create.

#### Results

The following message appears in the **Logs** pane of the **Create Ansible collection** tab.

```
--------------------- ansible-creator logs ---------------------

Note: collection company_namespace.myapp_network created at /path/to/collections/directory
```
The following directories and files are created in your `collections/` directory:

```
├── .devcontainer
├── .github
├── .gitignore
├── .isort.cfg
├── .pre-commit-config.yaml
├── .prettierignore
├── .vscode
├── CHANGELOG.rst
├── CODE_OF_CONDUCT.md
├── CONTRIBUTING
├── LICENSE
├── MAINTAINERS
├── README.md
├── changelogs
├── devfile.yaml
├── docs
├── extensions
├── galaxy.yml
├── meta
├── plugins
├── pyproject.toml
├── requirements.txt
├── roles
├── test-requirements.txt
├── tests
└── tox-ansible.ini
```

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

### Create a new role in your collection

Create a new Ansible role within your collection by copying the default role directory.

#### About this task

#### Procedure

1.  To create a new role, copy the default `run` role directory that was scaffolded when you created the collection.
2.  Define the tasks that you want your role to perform in the `tasks/main.yml` file. If you are creating a role to reuse tasks in an existing playbook, copy the content in the tasks block of your playbook YAML file. Remove the whitespace to the left of the tasks. Use `ansible-lint` in VS Code to check your YAML code.
3.  If your role depends on another role, add the dependency in the `meta/main.yml` file.

### Add documentation for your roles collection

It is important to provide documentation for your roles and roles collection, so that other users understand what your roles do and how to use them.

#### About this task

#### Procedure

1.  To add documentation for a role, navigate to the role directory.
2.  Open the `README.md` file in an editor. This file was added in the role directory when you scaffolded your collection directory.
3.  Provide the following information in the `README.md` files for every role in your collection:

- Role description: A brief summary of what the role does

- Requirements: List the collections, libraries, and required installations

- Dependencies

- Role variables: Provide the following information about the variables your role uses.     * Description
* Defaults
* Example values
* Required variables

- Example playbook: Show an example of a playbook that uses your role. Use comments in the playbook to help users understand where to set variables. The `README.md` file in [`controller_configuration.ad_hoc_command_cancel`](https://github.com/redhat-cop/controller_configuration/tree/devel/roles/ad_hoc_command_cancel) is an example of a role with standard documentation.

4.  To add documentation for your roles collection, navigate to the collection directory.
5.  In the `README.md` file for your collection, provide the following information:

- Collection description: Describe what the collection does.
- Requirements: List required collections.
- List the roles as a component of the collection.
- Using the collection: Describe how to run the components of the collection.
- Add a troubleshooting section.
- Versioning: Describe the release cycle of your collection.

### Publish your collection in private automation hub

Publish your collection by packaging it into a tarball and uploading it to a namespace in private automation hub. This makes the collection available for internal use in Ansible Automation Platform projects.

#### Before you begin

- Package your collection into a tarball.
- Format your collection file name as follows `<my_namespace-my_collection-x.y.z.tar.gz>`.For example, `company_namespace-myapp_network-2.0.0.tar.gz`

#### Procedure

1.  Create a namespace for your collection in private automation hub. See [Creating a namespace](/documentation/en-us/red_hat_ansible_automation_platform/2.7/administer-assembly_working_with_namespaces#proc-create-namespace "Create a namespace to organize collections that your content developers upload to automation hub.") .
2.  Optional: Add information to your namespace. See [Adding additional information and resources to a namespace](/documentation/en-us/red_hat_ansible_automation_platform/2.7/administer-assembly_working_with_namespaces#proc-edit-namespace "Edit the information associated with the namespace and provide resources for your users to accompany collections included in the namespace.") in *Managing automation content* .
3.  Upload your roles collections tarballs to your namespace. See [Uploading collections to your namespaces](/documentation/en-us/red_hat_ansible_automation_platform/2.7/administer-assembly_working_with_namespaces#proc-uploading-collections "Upload internally-developed collections in tar.gz file format to your private automation hub namespace for review and approval by an automation hub administrator.") in *Managing automation content* .
4.  Approve your collection for internal publication. See [Uploading collections to your namespaces](/documentation/en-us/red_hat_ansible_automation_platform/2.7/administer-assembly_managing_private_collections#proc-approve-collection "You can approve collections uploaded to individual namespaces for internal publication and use.") in *Managing automation content*.

#### Use your collection in projects in Red Hat Ansible Automation Platform

To use your collection in automation controller projects, add the collection to a custom execution environment. Then tag the new image and push it to private automation hub.

##### About this task

The following procedure describes the workflow to add a collection to an execution environment. Refer to [Customizing an existing automation executions environment image](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/creating_and_using_execution_environments/assembly-publishing-exec-env#proc-customize-ee-image) for the commands to execute these steps.

##### Procedure

1.  You can pull an execution environment base image from automation hub, or you can add your collection to your own custom execution environment.
2.  Add the collections that you want to include in the execution environment.
3.  Build the new execution environment.
4.  Verify that the collections are in the execution environment.
5.  Tag the image and push it to private automation hub.
6.  Pull your new image into your automation controller instance.
7.  The playbooks that use the roles in your collection must use the fully qualified domain name (FQDN) for the roles.

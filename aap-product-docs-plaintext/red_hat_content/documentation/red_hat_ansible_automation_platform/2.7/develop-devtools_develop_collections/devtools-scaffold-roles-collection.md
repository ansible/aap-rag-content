# Package and distribute automation content with collections
## Understand collections for distributing roles
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


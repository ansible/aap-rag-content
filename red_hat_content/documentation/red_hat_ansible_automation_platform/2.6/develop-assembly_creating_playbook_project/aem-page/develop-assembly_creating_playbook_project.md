+++
title = "Auto-generate the structure and files for your automation project - Red Hat Ansible Automation Platform 2.6"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.6/develop-assembly_creating_playbook_project"
template = "docs/aem-title.html"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6", "2.6"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6/develop-assembly_devtools_intro/", "Create, test, and deploy automation content with ansible-dev-tools"]]
category = "Develop"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/develop-assembly_creating_playbook_project/aem-page/develop-assembly_creating_playbook_project.html"
last_crumb = "Auto-generate the structure and files for your automation project"
modified = "2026-05-21T14:12:12.122Z"
multi_page_path = ""
name = "Auto-generate the structure and files for your automation project"
oversized = "false"
page_slug = "develop-assembly_creating_playbook_project"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.6"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/develop-assembly_creating_playbook_project"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/develop-assembly_creating_playbook_project/toc/toc.json"
type = "aem-page"
+++

# Auto-generate the structure and files for your automation project

Use the Ansible Automation Platform VS Code extension to scaffold a new Ansible playbook project. This process creates the necessary directory structure and configuration files, preparing your environment for playbook development.

## Scaffold a playbook project

The following steps describe the process for scaffolding a new playbook project with the Ansible VS Code extension.

### Before you begin

- You have installed Ansible development tools.
- You have installed and opened the Ansible VS Code extension.
- You have identified a directory where you want to save the project.

### Procedure

1.  Open VS Code.
2.  Click the Ansible icon in the VS Code activity bar to open the Ansible extension.
3.  Select **Get started** in the **Ansible content creator** section. The **Ansible content creator** tab opens.

4.  In the **Create** section, click **Ansible playbook project**. The **Create Ansible project** tab opens.

5.  In the form in the **Create Ansible project** tab, enter the following:

  - **Destination directory**: Enter the path to the directory where you want to scaffold your new playbook project. Note:
            If you enter an existing directory name, the scaffolding process overwrites the contents of that directory. The scaffold process only allows you to use an existing directory if you enable the `Force` option.

    * If you are using the containerized version of Ansible Dev tools, the destination directory path is relative to the container, not a path in your local system. To discover the current directory name in the container, run the `pwd` command in a terminal in VS Code. If the current directory in the container is `workspaces`, enter `workspaces/<destination_directory_name>`.
    * If you are using a locally installed version of Ansible Dev tools, enter the full path to the directory, for example `/user/<username>/projects/<destination_directory_name>`.

  - **SCM organization and SCM project**: Enter a name for the directory and subdirectory where you can store roles that you create for your playbooks.

6.  Enter a name for the directory where you want to scaffold your new playbook project.

### Results

After the project directory has been created, the following message appears in the **Logs** pane of the **Create Ansible Project** tab. In this example, the destination directory name is `destination_directory_name`.

```
------------------ ansible-creator logs ------------------
    Note: ansible project created at /Users/username/test_project
```
The following directories and files are created in your project directory:

```
$ tree -a -L 5 .
├── .devcontainer
│   ├── devcontainer.json
│   ├── docker
│   │   └── devcontainer.json
│   └── podman
│       └── devcontainer.json
├── .gitignore
├── README.md
├── ansible-navigator.yml
├── ansible.cfg
├── collections
│   ├── ansible_collections
│   │   └── scm_organization_name
│   │       └── scm_project_name
│   └── requirements.yml
├── devfile.yaml
├── inventory
│   ├── group_vars
│   │   ├── all.yml
│   │   └── web_servers.yml
│   ├── host_vars
│   │   ├── server1.yml
│   │   ├── server2.yml
│   │   ├── server3.yml
│   │   ├── switch1.yml
│   │   └── switch2.yml
│   └── hosts.yml
├── linux_playbook.yml
├── network_playbook.yml
└── site.yml
```

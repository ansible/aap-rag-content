+++
title = "Create and launch an Ansible development workspace - Red Hat Ansible Automation Platform 2.7"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/develop-assembly_workspaces_create_launch"
template = "docs/aem-title.html"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/develop-assembly_workspaces_create_launch/", "Create and launch an Ansible development workspace"]]
category = "Develop"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/develop-assembly_workspaces_create_launch/aem-page/develop-assembly_workspaces_create_launch.html"
last_crumb = "Create and launch an Ansible development workspace"
modified = "2026-06-05T07:48:10.594Z"
multi_page_path = ""
name = "Create and launch an Ansible development workspace"
oversized = "false"
page_slug = "develop-assembly_workspaces_create_launch"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/develop-assembly_workspaces_create_launch"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/develop-assembly_workspaces_create_launch/toc/toc.json"
type = "aem-page"
+++

# Create and launch an Ansible development workspace

An administrator installs Red Hat OpenShift Dev Spaces. After installation, developers can use the provided OpenShift Dev Spaces dashboard to create Ansible development workspaces that include a web-based version of VS Code.

## Authentication

Ansible dev spaces must be able to authenticate with your Git provider.

- If your organization has integrated Git OAuth authentication with Ansible dev spaces, you do not need to configure authentication between OpenShift Dev Spaces and your Git provider.
- If your organization has not set up OAuth authentication, you must generate personal access tokens for authentication between OpenShift Dev Spaces and your Git provider.

## Configure Git personal access token authentication

You must create a personal access token (PAT) in your Git provider, and add it to OpenShift Dev Spaces to enable access to your repositories from your Ansible development workspace.

### About this task

### Procedure

1.  Create a personal access token in your Git provider and save it.

  - See [Managing your personal access tokens](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens) in the GitHub documentation.
  - See [Personal access tokens](https://docs.gitlab.com/user/profile/personal_access_tokens) in the Gitlab documentation.

2.  In a browser, navigate to the OpenShift Dev Spaces dashboard provided by your administrator, and log in.
3.  Expand the dropdown menu under your login name and select **User Preferences**.
4.  Select **Personal Access Tokens**.
5.  Click **+Add Token**.
6.  Complete the **Add Personal Access Token** form:

  - **Token Name**: Enter a name for your token
  - **Token**: Enter your personal access token for your Git repository.

7.  Click **Add** to save the personal access token.

## Create a Git repository for an Ansible development workspace

To launch an Ansible development workspace, you must provide a link to a Git repository that defines the development environment. The repository also stores the automation content you create in Ansible dev spaces.

### About this task

### Procedure

1.  If your administrator provides an example repository for your team, fork the repository to create your own copy.
2.  If you do not have access to an example repository, you must create your own repository.
  1.  Create a directory for your new repository and use `git init` to initialize it as a Git repository.
  2.  Add a `devfile.yaml` file to the repository to define the Ansible dev spaces image that you want to use for your Ansible development workspace. See Creating a devfile for Ansible development workspaces.
  3.  Add a `.code-workspace` file to the repository to specify the VS Code extensions for your Ansible development workspace. See Creating a `.code-workspace` file for Ansible development workspaces.

## Create a devfile for an Ansible development workspace

To ensure your Ansible development workspace launches with the correct Ansible dev spaces image, you must add a `devfile` to your git repository. A `devfile` is a YAML file that defines the development environment for a project in Red Hat OpenShift Dev Spaces.

### About this task

### Procedure

1.  In your Git repository for your Ansible development workspace, create a new file named `devfile.yaml`.
2.  Copy and paste the following sample code into the `devfile.yaml` file:
  

```
schemaVersion: 2.3.0
attributes:
  controller.devfile.io/storage-type: per-workspace
metadata:
  name: ansible-devspaces
components:
  - name: dev-tools
    container:
      image: registry.redhat.io/ansible-automation-platform-27/ansible-devspaces-rhel9:latest
      cpuLimit: 4000m
      cpuRequest: 250m
      memoryRequest: 128Mi
      memoryLimit: 8Gi
      env:
        - name: HOME
          value: "/projects"
        - name: VSCODE_DEFAULT_WORKSPACE
          value: "/projects/ansible-devspaces/.code-workspace"
        - name: "ADT_CONTAINER_ENGINE"
          value: "podman"
```
    The environment variables configure the following:

  - `HOME`: Sets the home directory for the container.
  - `VSCODE_DEFAULT_WORKSPACE`: Points VS Code to the `.code-workspace` configuration file.
  - `ADT_CONTAINER_ENGINE`: Enables podman for container-in-container operations, including execution environments.

3. **Optional:** If you cannot pull images from the Red Hat Container Catalog (RHCC), modify the `image` value to point to your organization's internal registry.
4.  Add the `devfile.yaml` file to your Git repository and push the changes.

## Create a code-workspace file for an Ansible development workspace

To configure VS Code extensions that are included in your Ansible development workspace, you must add a `.code-workspace` JSON file to your git repository.

### About this task

### Procedure

1.  In your Git repository for your Ansible development workspace, create a new file named `.code-workspace`.
2.  Copy and paste the following sample code into the `.code-workspace` file:
  

```
{
    "settings": {
        "ansible.lightspeed.suggestions.enabled": true,
        "ansible.lightspeed.enabled": true,
        "ansible.ansible.useFullyQualifiedCollectionNames": true,
        "ansible.validation.enabled": true,
        "ansible.validation.lint.enabled": true,
        "files.trimTrailingWhitespace": true,
        "files.trimFinalNewlines": true,
        "files.insertFinalNewline": true,
        "ansible.validation.lint.arguments": "--profile production --offline",
        "openshiftToolkit.showWelcomePage": false,
        "editor.wordWrap": "on",
        "files.autoSave": "off"
    },
    "folders": [
        {
            "name": "ansible-devspaces",
            "path": "/projects/ansible-devspaces"
        }
    ],
    "extensions": {
        "recommendations": [
            "redhat.ansible",
            "redhat.vscode-yaml",
            "redhat.vscode-openshift-connector",
            "ms-python.python"
        ]
    }
}
```

3.  If you want to add extra extensions to your Ansible development workspace, add them in the `extensions.recommendations` section of the file.
4.  Add the `.code-workspace` file to your Git repository and push the changes.

## Launch an Ansible dev spaces workspace

Launch your Ansible development workspace by providing the URL for your prepared Git repository in the OpenShift Dev Spaces dashboard. This opens your VS Code environment in a browser.

### Before you begin

- Your administrator has provided a URL for a OpenShift Dev Spaces dashboard.
- You have prepared a git repository that contains the `devfile.yaml` and `.code-workspace` files that define the Ansible development workspace configuration.

### About this task

### Procedure

1.  In a browser, navigate to the OpenShift Dev Spaces dashboard and log in.
2.  Select **Create Workspace** in the navigation pane.
3.  In the **Import from Git** field of the **Create Workspace** form, enter the URL for the Git repository that contains your `devfile.yaml` and `.code-workspace` files.
4.  Click **Create & Open**.
5.  OpenShift Dev Spaces displays the progress for the provisioning process of your Ansible development workspace.  
![Workspace provisioning progress](/webassets/aem/red_hat_ansible_automation_platform/2.7/images/devtools-workspaces-provisioning.png)  
      After the Ansible development workspace launches, a VS Code environment opens in your browser.

6.  To open a terminal for executing commands and viewing `ansible-lint` suggestions in VS Code, click the main menu icon in the **Activity** bar and select Terminal> (and then)New Terminal.
      For more information about working in a VS Code terminal, see [Getting started with the terminal](https://code.visualstudio.com/docs/terminal/getting-started) in the VS Code documentation.

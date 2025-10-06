# 3. Creating and launching an Ansible development workspace
## 3.2. Creating a Git repository for an Ansible development workspace




To launch an Ansible development workspace, you must provide a link to a Git repository that defines the development environment. The repository also stores the automation content you create in Ansible dev spaces.

1. If your administrator provides an example repository for your team, fork the repository to create your own copy.
1. If you do not have access to an example repository, you must create your own repository.


1. Create a directory for your new repository and use `        git init` to initialize it as a Git repository.
1. Add a `        devfile.yaml` file to the repository to define the Ansible dev spaces image that you want to use for your Ansible development workspace. See Creating a devfile for Ansible development workspaces.
1. Add a `        .code-workspace` file to the repository to specify the VS Code extensions for your Ansible development workspace. See Creating a `        .code-workspace` file for Ansible development workspaces.




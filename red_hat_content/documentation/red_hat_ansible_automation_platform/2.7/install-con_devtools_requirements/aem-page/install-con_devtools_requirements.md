+++
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-con_devtools_requirements"
template = "docs/aem-title.html"
title = "Requirements - Red Hat Ansible Automation Platform 2.7"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-assembly_devtools_install/", "Install Ansible development tools"]]
category = "Install"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/install-con_devtools_requirements/aem-page/install-con_devtools_requirements.html"
last_crumb = "Requirements"
modified = "2026-06-05T07:48:10.594Z"
multi_page_path = ""
name = "Requirements"
oversized = "false"
page_slug = "install-con_devtools_requirements"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/install-con_devtools_requirements"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/install-con_devtools_requirements/toc/toc.json"
type = "aem-page"
+++

# Requirements

To install and use Ansible development tools, you must meet the following requirements. Extra requirements for Windows installations and containerized installations are indicated in the procedures.

- Python 3.10 or later.
- VS Code (Visual Studio Code) with the Ansible extension added.
- For containerized installations, the Microsoft Dev Containers VS Code extension.
- A containerization platform, for example Podman, Podman Desktop, Docker, or Docker Desktop. Note:
      The installation procedure for Ansible development tools on Windows covers the use of Podman Desktop only.

- You have a Red Hat account and you can log in to the Red Hat container registry at `registry.redhat.io`.

## Requirements for Ansible development tools on Windows

If you are installing Ansible development tools on a container in VS Code on Windows, there are extra requirements:

### Before you begin

- Windows Subsystem for Linux(WSL2)
- Podman Desktop

### Procedure

1.  Install WSL2 without a distribution:
  

```
$ wsl --install --no-distribution
```

2.  Use `cgroupsv2` by disabling `cgroupsv1` for WSL2:
      Edit the `%USERPROFILE%/wsl.conf` file and add the following lines to force `cgroupv2` usage:

```
[wsl2]
kernelCommandLine = cgroup_no_v1="all"
```

3.  Install Podman Desktop. Follow the instructions in [Installing Podman Desktop and Podman on Windows](https://podman-desktop.io/docs/installation/windows-install) in the Podman Desktop documentation. You do not need to change the default settings in the set-up wizard.

4.  Ensure the podman machine is using `cgroupsv2`:
  

```
$ podman info | findstr cgroup
```

5.  Test Podman Desktop:
  

```
$ podman run hello
```

6.  Configure the settings for Podman Desktop. Add a `%USERPROFILE%\bin\docker.bat` file with the following content:
  

```
@echo off
podman %*
```
    This avoids having to install Docker as required by the VS Code `Dev Container` extension.

7.  Add the `%USERPROFILE%\bin` directory to the `PATH`:
  1.  Select **Settings** and search for "Edit environment variables for your account" to display all of the user environment variables.
  2.  Highlight "Path" in the top user variables box, click Edit and add the path.
  3.  Click Save to set the path for any new console that you open.

## Authenticate with the Red Hat container registry

All container images available through the Red Hat container catalog are hosted on an image registry, `registry.redhat.io`. The registry requires authentication for access to images.

### Before you begin

- You have a Red Hat login. It is the same account that you use to log in to the Red Hat Customer Portal (access.redhat.com) and manage your Red Hat subscriptions.

### About this task

Note:

If you are planning to install the Ansible development tools on a container inside VS Code, you must log in to `registry.redhat.io` before launching VS Code so that VS Code can pull the `devtools` container from `registry.redhat.io`.

If you are running Ansible development tools on a container inside VS Code and you want to pull execution environments or the `devcontainer` to use as an execution environment, you must log in from a terminal prompt within the `devcontainer` from a terminal inside VS Code.

### Procedure

1.  Check whether you are already logged in to the `registry.redhat.io` registry:
  

```
$ podman login --get-login registry.redhat.io
```
    The command output displays your Red Hat login if you are logged in to `registry.redhat.io`.

2.  If you are not logged in to `registry.redhat.io`, use the `podman login` command with your credentials to access content on the registry.

```
$ podman login registry.redhat.io
Username: my_redhat_username
Password: ***********
```

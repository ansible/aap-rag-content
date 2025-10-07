# 2. Installing Ansible development tools
## 2.1. Requirements
### 2.1.1. Requirements for Ansible development tools on Windows




If you are installing Ansible development tools on a container in VS Code on Windows, there are extra requirements:

- Windows Subsystem for Linux(WSL2)
- Podman Desktop


**Procedure**

1. Install WSL2 without a distribution:


```
$ wsl --install --no-distribution
```


1. Use `    cgroupsv2` by disabling `    cgroupsv1` for WSL2:

Edit the `    %USERPROFILE%/wsl.conf` file and add the following lines to force `    cgroupv2` usage:


```
[wsl2]    kernelCommandLine = cgroup_no_v1="all"
```


1. Install Podman Desktop. Follow the instructions in [Installing Podman Desktop and Podman on Windows](https://podman-desktop.io/docs/installation/windows-install) in the Podman Desktop documentation.

You do not need to change the default settings in the set-up wizard.


1. Ensure the podman machine is using `    cgroupsv2` :


```
$ podman info | findstr cgroup
```


1. Test Podman Desktop:


```
$ podman run hello
```


1. Configure the settings for Podman Desktop. Add a `    %USERPROFILE%\bin\docker.bat` file with the following content:


```
@echo off    podman %*
```

This avoids having to install Docker as required by the VS Code `    Dev Container` extension.


1. Add the `    %USERPROFILE%\bin` directory to the `    PATH` :


1. Select **Settings** and search for "Edit environment variables for your account" to display all of the user environment variables.
1. Highlight "Path" in the top user variables box, clickEditand add the path.
1. ClickSaveto set the path for any new console that you open.




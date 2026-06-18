# Install Ansible development tools from an RPM package

Ansible development tools are available as an RPM package for Red Hat Enterprise Linux. Install the tools on your local RHEL system using a package manager.

## Before you begin

- You have installed a supported version of Red Hat Enterprise Linux.
- You have registered your system with Red Hat Subscription Manager.
- You have installed a containerization platform, for example Podman or Docker.

## Procedure

1.  Run the following command to check whether Simple Content Access (SCA) is enabled:


```shell
$ sudo subscription-manager status
```
If Simple Content Access is enabled, the output contains the following message:

```
Content Access Mode is set to Simple Content Access.
```
1.  If Simple Content Access is not enabled, attach the Red Hat Ansible Automation Platform SKU:


```shell
$ sudo subscription-manager attach --pool=<sku-pool-id>
```

2.  Install Ansible development tools with the following command:


```shell
$ sudo dnf install
--enablerepo=ansible-automation-platform-*aap-version*-for-rhel-*rhel-version*-x86_64-rpms ansible-dev-tools
```
Replace *aap-version* with your Ansible Automation Platform version and *rhel-version* with your Red Hat Enterprise Linux major version.

## Results

1. Verify that the Ansible development tools have been installed:

```shell
$ rpm -aq | grep ansible-dev-tools
```
If the installation was successful, the output shows the `ansible-dev-tools` package and its version number, for example:



```
ansible-dev-tools-25.8.3-1.el9ap.noarch
```

2. On successful installation, you can view the help documentation for the `ansible-creator` utility:

```
$ ansible-creator --help

usage: ansible-creator [-h] [--version] command ...

The fastest way to generate all your ansible content.

Positional arguments:
command
add           Add resources to an existing Ansible project.
init          Initialize a new Ansible project.

Options:
--version      Print ansible-creator version and exit.
-h     --help  Show this help message and exit
```

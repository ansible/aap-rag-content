# Upgrade your RPM deployment of Ansible Automation Platform

You can upgrade your Ansible Automation Platform installation using the supported upgrade paths. Review the available upgrade paths and required steps to ensure a successful upgrade of your Ansible Automation Platform environment.

Before beginning your upgrade, review the prerequisites and upgrade planning sections of this guide.

Ansible Automation Platform supports upgrades from the two most recent minor releases. Check the release notes for your target version to confirm which upgrade paths are supported.

| <br>Supported upgrade path                      | <br>Steps to upgrade                                                                                                                                                                                                                                                                                                                                                                                                                     |
| ----------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <br>From the immediately previous minor release | Back up your Ansible Automation Platform instance.Download the installation package for your target version.Set up your inventory file to match your installation environment.Run the installation program over your current Ansible Automation Platform instance.                                                                                                                                                                       |
| <br>From two minor releases back                | Back up your Ansible Automation Platform instance.Download the installation package for your target version.Set up your inventory file to match your installation environment.Check the release notes for any component-specific upgrade restrictions. Some components might require additional steps, such as removing a database before upgrading.Run the installation program over your current Ansible Automation Platform instance. |
| <br>Mixed-version environments                  | <br>If your environment includes components at different minor versions, upgrade the older components first so that all services reach the same target version. Use the inventory file to specify only the components you are upgrading in each pass.<br>After all components are at the same version, run a final upgrade on all services together.                                                                                     |


Important:

Not all components support upgrades that skip a minor release. Check the release notes for your target version to identify any components that require removal and reinstallation rather than a direct upgrade.

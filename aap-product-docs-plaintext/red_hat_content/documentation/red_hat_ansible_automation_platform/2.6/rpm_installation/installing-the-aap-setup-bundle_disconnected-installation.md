# 6. Disconnected installation
## 6.5. Downloading and installing the Ansible Automation Platform setup bundle

Choose the setup bundle to download Ansible Automation Platform for disconnected installations. This bundle includes the RPM content for Ansible Automation Platform and the default execution environment images that will be uploaded to your private automation hub during the installation process.

**Procedure**

1. Download the Ansible Automation Platform setup bundle package by navigating to the [Red Hat Ansible Automation Platform download](https://access.redhat.com/downloads/content/480/ver=2.6/rhel---9/2.6/x86_64/product-software) page and clicking Download Now for the Ansible Automation Platform 2.6 Setup Bundle.

2. On control node, untar the bundle:

$ tar xvf \
ansible-automation-platform-setup-bundle-2.6-1.tar.gz
$ cd ansible-automation-platform-setup-bundle-2.6-1

3. Edit the inventory file to include variables based on your host names and desired password values.

**Additional resources**

- [3.2 Inventory file examples base on installation scenarios](#con-install-scenario-examples "4.3.&nbsp;Inventory file examples based on installation scenarios")


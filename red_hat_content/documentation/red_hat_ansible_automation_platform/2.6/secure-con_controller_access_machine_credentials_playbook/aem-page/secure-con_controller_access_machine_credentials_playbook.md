+++
template = "docs/aem-title.html"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.6/secure-con_controller_access_machine_credentials_playbook"
title = "Access machine credentials in an ansible playbook - Red Hat Ansible Automation Platform 2.6"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6", "2.6"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6/secure-assembly_controller_credentials/", "Configure credentials to authenticate remote systems and services"]]
category = "Secure"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/secure-con_controller_access_machine_credentials_playbook/aem-page/secure-con_controller_access_machine_credentials_playbook.html"
last_crumb = "Access machine credentials in an ansible playbook"
modified = "2026-05-21T14:12:12.122Z"
multi_page_path = ""
name = "Access machine credentials in an ansible playbook"
oversized = "false"
page_slug = "secure-con_controller_access_machine_credentials_playbook"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.6"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/secure-con_controller_access_machine_credentials_playbook"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/secure-con_controller_access_machine_credentials_playbook/toc/toc.json"
type = "aem-page"
+++

# Access machine credentials in an ansible playbook

You can get username and password from Ansible facts:

```
vars:
  machine:
    username: '{{ ansible_user }}'
    password: '{{ ansible_password }}'
```

## Machine credential type

Machine credentials enable automation controller to call Ansible on hosts under your management.

You can specify the SSH username, optionally give a password, an SSH key, a key password, or have automation controller prompt the user for their password at deployment time. They define SSH and user-level privilege escalation access for playbooks, and are used when submitting jobs to run playbooks on a remote host.

The following network connections use **Machine** as the credential type: `httpapi`, `netconf`, and `network_cli`

Machine and SSH credentials do not use environment variables. They pass the username through the ansible `-u` flag, and interactively write the SSH password when the underlying SSH client prompts for it.

Machine credentials require the following inputs:

- **Username**: The username to use for SSH authentication.
- **Password**: The password to use for SSH authentication. This password is stored encrypted in the database, if entered. Alternatively, you can configure automation controller to ask the user for the password at launch time by selecting **Prompt on launch**. In these cases, a dialog opens when the job is launched, promoting the user to enter the password and password confirmation.
- **SSH Private Key**: Copy or drag-and-drop the SSH private key for the machine credential.
- **Private Key Passphrase**: If the SSH Private Key used is protected by a password, you can configure a Key Passphrase for the private key. This password is stored encrypted in the database, if entered. You can also configure automation controller to ask the user for the key passphrase at launch time by selecting **Prompt on launch**. In these cases, a dialog opens when the job is launched, prompting the user to enter the key passphrase and key passphrase confirmation.
- **Privilege Escalation Method**: Specifies the type of escalation privilege to assign to specific users. This is the same as specifying the `--become-method=BECOME_METHOD` parameter, where `BECOME_METHOD` is any of the existing methods, or a custom method you have written. Begin entering the name of the method, and the appropriate name auto-populates.   * **empty selection**: If a task or play has `become` set to `yes` and is used with an empty selection, then it will default to `sudo`.
  * **sudo**: Performs single commands with superuser (root user) privileges.
  * **su**: Switches to the superuser (root user) account (or to other user accounts).
  * **pbrun**: Requests that an application or command be run in a controlled account and provides for advanced root privilege delegation and keylogging.
  * **pfexec**: Executes commands with predefined process attributes, such as specific user or group IDs.
  * **dzdo**: An enhanced version of sudo that uses RBAC information in Centrify’s Active Directory service. For more information, see Centrify’s [site on DZDO](https://docs.delinea.com/online-help/server-suite/reports-events/events/server-suite/dzdo.htm).
  * **pmrun**: Requests that an application is run in a controlled account. See [Privilege Manager for Unix 6.0](https://support.oneidentity.com/privilege-manager-for-unix/7.2.3/technical-documents).
  * **runas**: Enables you to run as the current user.
  * **enable**: Switches to elevated permissions on a network device.
  * **doas**: Enables your remote/login user to run commands as another user through the *doas* ("Do as user") utility.
  * **ksu**: Enables your remote/login user to run commands as another user through Kerberos access.
  * **machinectl**: Enables you to manage containers through the `systemd` machine manager.
  * **sesu**: Enables your remote/login user to run commands as another user through the CA Privileged Access Manager.


- **Privilege Escalation Username**: You see this field only if you selected an option for privilege escalation. Enter the username to use with escalation privileges on the remote system.
- **Privilege Escalation Password**: You see this field only if you selected an option for privilege escalation. Enter the password to use to authenticate the user through the selected privilege escalation type on the remote system. This password is stored encrypted in the database. You can also configure automation controller to ask the user for the password at launch time by selecting **Prompt on launch**. In these cases, a dialog opens when the job is launched, promoting the user to enter the password and password confirmation.


 Note:

You must use sudo password must in combination with SSH passwords or SSH Private Keys, because automation controller must first establish an authenticated SSH connection with the host before invoking `sudo` to change to the sudo user.

 Warning:

Credentials that are used in scheduled jobs must not be configured as **Prompt on launch**.

## Using Machine and Network credentials together

You can assign both Machine and Network credentials to a single job template to manage network devices that require multi-hop SSH access, such as connecting through a jumphost.

### About this task

When you assign multiple credential types to a job template, {ControllerName} injects each credential into the job environment differently:

- **Machine credentials** set the SSH username, password, and key used by Ansible Automation Platform to connect to hosts. These values are passed through the `ansible -u` flag and SSH authentication.
- **Network credentials** set the `ANSIBLE_NET_USERNAME` and `ANSIBLE_NET_PASSWORD` environment variables, which Ansible Automation Platform networking modules use to authenticate to network devices.


 Note:

The credential type must match the connection type used by the network device:

- For `local` connections using `provider`, use the **Network** credential type
- For `httpapi`, `netconf`, and `network_cli` connections, use the **Machine** credential type, not the Network credential type.

**Prerequisites**

- You have created a Machine credential for the jumphost or bastion host.
- You have created a Network credential for the target network device (if using `local` connection with `provider`), or a second Machine credential (if using `network_cli`, `netconf`, or `httpapi`).
- Your inventory is configured with appropriate connection variables, such as `ansible_ssh_common_args` for ProxyCommand settings

### Procedure

1.  From the navigation panel, select Automation execution> (and then)Templates.
2.  Create or edit a job template.
3.  In the **Credentials** field, select the ![Search icon](/webassets/aem/red_hat_ansible_automation_platform/2.6/images/search.png) icon.
4.  Add the **Machine** credential for the jumphost.
5.  Add the **Network** credential for the network device (or a second Machine credential, depending on your connection type).
6.  Configure your inventory or playbook variables with the appropriate SSH proxy settings. For example, to use a jumphost with ProxyCommand:
   `ansible_ssh_common_args: '-o ProxyCommand="ssh -W %h:%p -q user@gateway.example.com"`

7.  Click Save and then Launch template.

### What to do next

**Verification**

Review the job output to confirm that both credentials were injected and the playbook successfully authenticated to the target network devices through the jumphost.

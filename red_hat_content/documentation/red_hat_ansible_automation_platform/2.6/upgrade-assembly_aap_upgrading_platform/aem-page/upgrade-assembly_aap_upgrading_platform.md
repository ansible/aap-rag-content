+++
title = "Upgrade Ansible Automation Platform - Red Hat Ansible Automation Platform 2.6"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.6/upgrade-assembly_aap_upgrading_platform"
template = "docs/aem-title.html"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6", "2.6"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6/upgrade-ansible_automation_platform_upgrade/", "Upgrade your RPM deployment of Ansible Automation Platform"]]
category = "Upgrade"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/upgrade-assembly_aap_upgrading_platform/aem-page/upgrade-assembly_aap_upgrading_platform.html"
last_crumb = "Upgrade Ansible Automation Platform"
modified = "2026-05-21T14:12:12.122Z"
multi_page_path = ""
name = "Upgrade Ansible Automation Platform"
oversized = "false"
page_slug = "upgrade-assembly_aap_upgrading_platform"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.6"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/upgrade-assembly_aap_upgrading_platform"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/upgrade-assembly_aap_upgrading_platform/toc/toc.json"
type = "aem-page"
+++

# Upgrade Ansible Automation Platform

To upgrade your deployment of Ansible Automation Platform, review the planning requirements to ensure a successful upgrade. You can then download the desired version of the installation program, configure the inventory file to reflect your environment, and then run the installation program.

Important:

The automation controller API remains available for backward compatibility; however, you must use the platform gateway API for managing organizations, teams, and users. Using the legacy API introduces a delay of up to 15 minutes before changes are synchronized to all components, including Event-Driven Ansible controller.

## System requirements

Before you begin the upgrade process, review the following considerations to plan and prepare your Ansible Automation Platform deployment.

Warning:

To upgrade to Ansible Automation Platform 2.7, you must be running a containerized or OpenShift Container Platform deployment. RPM-based deployments are not supported as an upgrade path to 2.7. If you are running an RPM-based deployment, migrate to a containerized or OpenShift Container Platform deployment before you upgrade.

### Ansible Automation Platform requirements

- Verify that you have a valid subscription before upgrading from a previous version of Ansible Automation Platform. Existing subscriptions are carried over during the upgrade process.
- Review *Plan your upgrade to Ansible Automation Platform 2.6* to understand the upgrade requirements and scenarios, and *Choose a deployment method and topology* for the RPM topologies and infrastructure.   * Inspect all existing SAML authenticators in your automation controller environment before upgrading from Ansible Automation Platform 2.4 to 2.6. Encrypted private keys for SAML configurations are not supported in Ansible Automation Platform 2.6.
- Ensure that you are on Ansible Automation Platform 2.4 or 2.5 before upgrading to 2.6. You can only upgrade from Ansible Automation Platform 2.4 or 2.5 to 2.6.
- Upgrade to the latest version of Ansible Automation Platform 2.4 or 2.5 before upgrading to Red Hat Ansible Automation Platform 2.6. Important:

  * When upgrading from Ansible Automation Platform 2.4 to 2.6, the API endpoints for the automation controller, automation hub, and Event-Driven Ansible controller are all available for use. These APIs are being deprecated and will be disabled in an upcoming release. This grace period is to allow for migration to the new APIs put in place with the platform gateway.
  * If you upgraded from Ansible Automation Platform 2.4 to 2.5, you must migrate your authentication methods and users before upgrading to 2.6 as that legacy authenticator functionality was removed.

- Back up your Ansible Automation Platform environment before upgrading in case any issues occur.
- Capture your inventory or instance group details before upgrading.
- Review the platform gateway requirements:
  * Ansible Automation Platform 2.4 to 2.6 upgrades include the platform gateway. Ensure you review the 2.6 Network ports and protocols diagram for architectural changes.

  * Platform gateway has a number of associated inventory file variables, some of which are required.

  * When upgrading from Ansible Automation Platform 2.4 to 2.6, connections to the platform gateway URL might fail on the platform gateway UI if you are using the automation controller behind a load balancer. The following error message is displayed: `Error connecting to Controller API`         To resolve this issue, for each automation controller host, add the platform gateway URL as a trusted source in the `CSRF_TRUSTED_ORIGIN` setting in the **settings.py** file for each automation controller host. You must then restart each automation controller host so that the URL changes are implemented.

- Review the centralized redis instance offered by Ansible Automation Platform for both standalone and clustered topologies.   * Ansible Automation Platform 2.6 offers a centralized Redis instance in both standalone and clustered topologies.
  * 6 VMs are required for a Redis high availability (HA) compatible deployment. Redis can be colocated on each Ansible Automation Platform component VM except for automation controller, execution nodes, or the PostgreSQL database.
  * External Redis is not supported for RPM-based deployments of Ansible Automation Platform.
- Limitation:
  * Upgrade of Event-Driven Ansible 2.5 to 2.6 is supported, but upgrade from Event-Driven Ansible 2.4 to 2.6 is not supported. Database migrations between Event-Driven Ansible 2.4 and Event-Driven Ansible 2.6 are not compatible. If you are upgrading from Ansible Automation Platform 2.4 to 2.6 and you deployed Event-Driven Ansible, you must first remove the Event-Driven Ansible 2.4 database and then upgrade your platform to 2.6.

### System requirements

| Type                 | Description                                                                                                                            | Notes                                                                                                                                                                                                                                                                                       |
| -------------------- | -------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <br>Subscription     | <br>Valid Red Hat Ansible Automation Platform subscription                                                                             |                                                                                                                                                                                                                                                                                             |
| <br>Operating system | <br>Red Hat Enterprise Linux 9.4 or later minor versions of Red Hat Enterprise Linux 9                                                 | <br>Red Hat Ansible Automation Platform are also supported on OpenShift.                                                                                                                                                                                                                    |
| <br>CPU architecture | <br>x86\_64, AArch64, s390x (IBM Z), ppc64le (IBM Power)                                                                               |                                                                                                                                                                                                                                                                                             |
| <br>Ansible-core     | <br>Ansible-core version 2.16 or later                                                                                                 | <br>Ansible Automation Platform uses the system-wide ansible-core package to install the platform, but uses ansible-core 2.16 for both its control plane and built-in execution environments.                                                                                               |
| <br>Browser          | <br>A currently supported version of Mozilla Firefox or Google Chrome.                                                                 |                                                                                                                                                                                                                                                                                             |
| <br>Database         | For Ansible Automation Platform managed databases: PostgreSQL 15.For customer provided (external) databases: PostgreSQL 15, 16, or 17. | External (customer supported) databases require International Components for Unicode (ICU) support.External databases using PostgreSQL 16 or 17 must rely on external backup and restore processes. Backup and restore functionality is dependent on utilities provided with PostgreSQL 15. |

### Database requirements

- Ansible Automation Platform can work with two varieties of database:
  * Database installed with Ansible Automation Platform - This database consists of a PostgreSQL installation done as part of an Ansible Automation Platform installation using PostgreSQL packages provided by Red Hat.
  * Customer provided or configured database - This is an external database that is provided by the customer, whether on bare metal, virtual machine, container, or cloud hosted service. Ansible Automation Platform requires customer provided (external) database to have ICU support.
- PostgreSQL user passwords are hashed with SCRAM-SHA-256 secure hashing algorithm before storing in the database.
- Ensure that you back up your Ansible Automation Platform environment before upgrading in case any issues occur.

### User privileges

- Ensure a dedicated non-root user is configured on the Red Hat Enterprise Linux host.   * This user requires sudo or other Ansible supported privilege escalation (sudo is recommended) to perform administrative tasks during the installation.
  * This user is responsible for the installation of RPM Ansible Automation Platform.
  * You can obtain root access either through the sudo command, or through privilege escalation. You can de-escalate privileges from root to users such as AWX, PostgreSQL, Event-Driven Ansible, or Pulp.
  * An NTP client is configured on each node.

## Back up your Ansible Automation Platform instance

Back up an Ansible Automation Platform instance by running the `setup.sh` script with the `backup_dest` flag. You can also enable the compression flags `use_archive_compression` and `use_db_compression` to reduce the size of the backup artifacts.

### Procedure

1.  Navigate to your Ansible Automation Platform installation directory.
2.  Run the `./setup.sh` script following the example below:
  

```
$ ./setup.sh -e 'backup_dest=/ansible/mybackup' -e
'use_archive_compression=true' 'use_db_compression=true @credentials.yml -b
```
    Where:

  - `backup_dest`: Specifies a directory to save your backup to.

  - `use_archive_compression=true` and `use_db_compression=true`: Compresses the backup artifacts before they are sent to the host running the backup operation. You can use the following variables to customize the compression:

    * For global control of compression for filesystem related backup files: `use_archive_compression=true`

    * For component-level control of compression for filesystem related backup files: `<componentName>_use_archive_compression`             For example:

      + `automationgateway_use_archive_compression=true`
      + `automationcontroller_use_archive_compression=true`
      + `automationhub_use_archive_compression=true`
      + `automationedacontroller_use_archive_compression=true`

    * For global control of compression for database related backup files: `use_db_compression=true`

    * For component-level control of compression for database related backup files: `<componentName>_use_db_compression=true`             For example:

      + `automationgateway_use_db_compression=true`
      + `automationcontroller_use_db_compression=true`
      + `automationhub_use_db_compression=true`
      + `automationedacontroller_use_db_compression=true`

### Results

After a successful backup, a backup file is created at `/ansible/mybackup/automation-platform-backup-<date/time>.tar.gz`.

## Install with internet access

Choose the Red Hat Ansible Automation Platform installation program if your Red Hat Enterprise Linux environment is connected to the internet. Installing with internet access retrieves the latest required repositories, packages, and dependencies.

### About this task

Choose one of the following ways to set up your Ansible Automation Platform installation program.

### Procedure

-   **Tarball install**   1.  Navigate to the [Red Hat Ansible Automation Platform download](https://access.redhat.com/downloads/content/480/ver=2.6/rhel---9/2.6/x86_64/product-software) page.
  2.  In the **Product software** tab, click Download Now for the **Ansible Automation Platform <latest-version> Setup**.
  3.  Extract the files:
  

```
$ tar xvzf ansible-automation-platform-setup-<latest-version>.tar.gz
```

-   **RPM install**   1.  Install the Ansible Automation Platform Installer Package. v.2.6 for RHEL 9 for x86-64:

```
$ sudo dnf install --enablerepo=ansible-automation-platform-2.6-for-rhel-9-x86_64-rpms ansible-automation-platform-installer
```
    Note:
            `dnf install` enables the repo as the repo is disabled by default.

        When you use the RPM installer, the files are placed under the `/opt/ansible-automation-platform/installer` directory.

## Install without internet access

Use the Ansible Automation Platform Bundle installation program for offline environments or to avoid installing dependencies from online repositories. RHEL repository access is still required; all other data is in the archive.

### Procedure

1.  Navigate to the [Red Hat Ansible Automation Platform download](https://access.redhat.com/downloads/content/480/ver=2.6/rhel---9/2.6/x86_64/product-software) page.
2.  In the **Product software** tab, click Download Now for the **Ansible Automation Platform <latest-version> Setup Bundle**.
3.  Extract the files:
  

```
$ tar xvzf ansible-automation-platform-setup-bundle-<latest-version>.tar.gz
```

## Set up the inventory file

Before upgrading your Red Hat Ansible Automation Platform installation, edit the `inventory` file to match your required configuration. You can keep the same parameters from your existing deployment or you can update the parameters to match any changes to your environment.

### About this task

You can find sample inventory files in the [Test topologies](https://github.com/ansible/test-topologies/) GitHub repository, or in [Choose a deployment method and topology](/documentation/en-us/red_hat_ansible_automation_platform/2.6/plan-assembly_overview_tested_deployment_models "Red Hat tests Ansible Automation Platform with a defined set of topologies to give you opinionated deployment options. Deploy all components of Ansible Automation Platform so that all features and capabilities are available for use without the need to take further action.").

### Procedure

1.  Navigate to the installation program directory.

Bundled installer
```
$ cd ansible-automation-platform-setup-bundle-2.6-4-x86_64
```

Online installer
```
$ cd ansible-automation-platform-setup-2.6-4
```

2.  Open the `inventory` file for editing.
3.  Modify the `inventory` file to provision new nodes, deprovision nodes or groups, and import or generate automation hub API tokens. You can use the same `inventory` file from an existing Ansible Automation Platform installation if there are no changes to the environment.

  Note:
      Provide a reachable IP address or fully qualified domain name (FQDN) for all hosts to ensure that users can synchronize and install content from Ansible automation hub from a different node. Do not use `localhost`. If `localhost` is used, the upgrade will be stopped as part of preflight checks.

4.  Provision new nodes in a cluster, by adding new nodes alongside existing nodes in the `inventory` file as follows:
  

```ini
[automationcontroller]
clusternode1.example.com
clusternode2.example.com
clusternode3.example.com

    [all:vars]
admin_password='password'

    pg_host='<host_name>'

    pg_database='<database_name>'
pg_username='<your_username>'
pg_password='<your_password>'
```

## Remove the 2.4 database for Event-Driven Ansible

Ansible Automation Platform 2.6 supports upgrades from Ansible Automation Platform 2.4 environments for all components, except for Event-Driven Ansible. Database migrations between Event-Driven Ansible 2.4 and Event-Driven Ansible 2.6 are not compatible.

### About this task

If you are upgrading from Ansible Automation Platform 2.4 to 2.6, you must first remove the Event-Driven Ansible 2.4 database. A new Event-Driven Ansible 2.6 database gets created automatically after the upgrade. You can then reconnect Automation Decisions (Event-Driven Ansible controller) to Automation Execution (automation controller) to run rulebook activations.

Note:

When upgrading from Ansible Automation Platform 2.5 to 2.6, the Event-driven Ansible component will be updated automatically. You are not required to delete the existing Event-Driven Ansible 2.5 database before upgrading your platform to 2.6.

### Procedure

1.  Shut down the old Event-Driven Ansible 2.4 host.
2.  Log in to your database host with a user that has superuser privileges.  `# psql -h <hostname> -U <username>`

3.  When prompted, enter your password.
4.  Delete the existing Event-Driven Ansible 2.4 database by using the following command:
       `DROP DATABASE automationedacontroller`

5.  When prompted, reenter your password.

### What to do next

1. [Run the Ansible Automation Platform installer setup script](/documentation/en-us/red_hat_ansible_automation_platform/2.6/upgrade-assembly_aap_upgrading_platform#proc-running-setup-script-for-updates "Execute the Red Hat Ansible Automation Platform installer setup script after configuring your inventory file. This action initiates the installation or update process, applying all your custom settings to deploy the platform successfully.").
2. After the upgrade is completed, reconnect Automation Decisions (Event-Driven Ansible controller) to Automation Execution (automation controller) to run rulebook activations successfully.

## Run the installer setup script and verify platform accounts

Execute the Red Hat Ansible Automation Platform installer setup script after configuring your `inventory` file. This action initiates the installation or update process, applying all your custom settings to deploy the platform successfully.

### Procedure

 Run the `setup.sh` script:

```
$ ./setup.sh
```

### Results

The installation will begin.

### Verify user migration

During the upgrade to Ansible Automation Platform 2.6, controller user accounts are converted into platform user accounts. Controller administrators retain their administrative privileges, but they are converted into platform administrator privileges.

#### About this task

Other controller accounts become platform users, and their existing permissions are mapped over appropriately after an initial password reset. Users with existing accounts associated with other components (like private automation hub and Event-Driven Ansible) must have their passwords reset by their administrator before they can log in.

Authenticator configurations are automatically migrated. SSO and LDAP accounts do not require any manual migration steps, including password resets, with the exception of accounts that use a certificate from the trust store. See [Configuring authentication in the Ansible Automation Platform](/documentation/en-us/red_hat_ansible_automation_platform/2.6/upgrade-con_aap_upgrade_overview#con-upgrade-improvements-overview "Ansible Automation Platform 2.6 includes changes that improve the overall platform upgrade experience.") for more information on migrating authentication configurations that use a custom certificate.

After your upgrade to Ansible Automation Platform 2.6 is complete, verify that you can log in to the upgraded platform.

#### Procedure

-  If you have a controller account that has been converted to a platform gateway account for Ansible Automation Platform 2.6:

  * Log into your upgraded platform instance with your controller credentials.

-  If you have a component-level account (such as an account associated with private automation hub or Event-Driven Ansible):

  * Request a password reset from your administrator and log into the upgraded platform with your new password.

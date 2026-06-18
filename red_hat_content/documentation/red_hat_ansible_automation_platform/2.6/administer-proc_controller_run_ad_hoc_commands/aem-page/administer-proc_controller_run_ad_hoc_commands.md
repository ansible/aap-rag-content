+++
title = "Run ad hoc commands against a host in an inventory - Red Hat Ansible Automation Platform 2.6"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.6/administer-proc_controller_run_ad_hoc_commands"
template = "docs/aem-title.html"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6", "2.6"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6/administer-assembly_controller_inventories/", "Define automation target hosts in your inventory files"]]
category = "Administer"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/administer-proc_controller_run_ad_hoc_commands/aem-page/administer-proc_controller_run_ad_hoc_commands.html"
last_crumb = "Run ad hoc commands against a host in an inventory"
modified = "2026-05-21T14:12:12.122Z"
multi_page_path = ""
name = "Run ad hoc commands against a host in an inventory"
oversized = "false"
page_slug = "administer-proc_controller_run_ad_hoc_commands"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.6"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/administer-proc_controller_run_ad_hoc_commands"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/administer-proc_controller_run_ad_hoc_commands/toc/toc.json"
type = "aem-page"
+++

# Run ad hoc commands against a host in an inventory

Learn how to run ad hoc commands against hosts in an inventory.

## About this task

*Ad hoc* refers to using Ansible to perform a quick command, using /usr/bin/ansible, rather than the orchestration language, which is /usr/bin/ansible-playbook. An example of an ad hoc command might be rebooting 50 machines in your infrastructure. Anything you can do ad hoc can be accomplished by writing a playbook. Playbooks can also glue many other operations together.

## Procedure

1.  From the navigation panel, select Automation Execution> (and then)Infrastructure> (and then)Inventories.
2.  Select the inventory name you want to run an ad hoc command with.
3.  Select an inventory source from the **Hosts** or **Groups** tab. The inventory source can be a single group or host, a selection of many hosts, or a selection of many groups.
4.  Click Run Command. The Run command window opens.
5.  Enter the following information:

  - **Module**: Select one of the modules that the supports running commands against.
      | command  | apt\_repository | mount     | win\_service |
      | -------- | --------------- | --------- | ------------ |
      | shell    | apt\_rpm        | ping      | win\_updates |
      | yum      | service         | SELinux   | win\_group   |
      | apt      | group           | setup     | win\_user    |
      | apt\_key | user            | win\_ping | win\_user    |

  - **Arguments**: Provide arguments to be used with the module you selected.
  - **Limit**: Enter the limit used to target hosts in the inventory. To target all hosts in the inventory enter `all` or `*`, or leave the field blank. This is automatically populated with whatever was selected in the previous view before clicking the launch button.
  - **Machine Credential**: Select the credential to use when accessing the remote hosts to run the command. Choose the credential containing the username and SSH key or password that Ansible needs to log in to the remote hosts.
  - **Verbosity**: Select a verbosity level for the standard output.
  - **Forks**: If needed, select the number of parallel or simultaneous processes to use while executing the command.
  - **Show Changes**: Select to enable the display of Ansible changes in the standard output. The default is OFF.
  - **Enable Privilege Escalation**: If enabled, the playbook is run with administrator privileges. This is the equivalent of passing the `--become` option to the `ansible` command.
  - **Extra Variables**: Provide extra command line variables to be applied when running this inventory. Enter variables using either JSON or YAML syntax. Use the radio button to toggle between the two.

6.  Click Next to select the execution environment you want the ad hoc command to be run against.
7.  Click Next to select the credential you want to use.
8.  Click Launch. The results display in the **Output** tab of the module’s job window.

## Configure notifications for the source

After you create a source for an inventory in automation controller, you can configure notifications for that source.

### Procedure

1.  From the navigation panel, select Automation Execution> (and then)Infrastructure> (and then)Inventories.
2.  Select the inventory name you want to configure notifications for.
3.  In the inventory **Details** page, select the **Notifications** tab. Note:
      The **Notifications** tab is only present when you have saved the newly-created source.

4.  If notifications are already set up, use the toggles to enable or disable the notifications to use with your particular source. For more information, see [Enable and Disable Notifications](/documentation/en-us/red_hat_ansible_automation_platform/2.6/observe-con_controller_configure_hostname_notifications#controller-enable-disable-notifications "You can set up notifications to notify you when a specific job starts, and on the success or failure at the end of the job run. Note the following behaviors:").
5.  If you have not set up notifications, see [Notifiers](/documentation/en-us/red_hat_ansible_automation_platform/2.6/observe-assembly_ug_controller_notifications#controller-notifications "A Notification Type such as Email, Slack or a Webhook, is an instance of a Notification Template, and has a name, description and configuration defined in the Notification template.") for more information.
6.  Review your entries and selections.
7.  Click Save.

### What to do next

When you define a source, it is displayed in the list of sources associated with the inventory. From the **Sources** tab you can perform a sync on a single source, or sync all of them at once. You can also perform additional actions such as scheduling a sync process, and edit or delete the source.

## View completed jobs

You can view completed jobs in automation controller by navigating to the **Jobs** tab in the navigation panel.

If you use an inventory to run a job, you can view details about those jobs in the **Jobs** tab of the inventory and click **Expanded** to view details about each job.

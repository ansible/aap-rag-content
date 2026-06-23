# Add a source to an inventory
## Source from a project’s source control management

An inventory that is sourced from a project means that it uses the SCM type from the project it is tied to. For example, if the project’s source is from GitHub, then the inventory uses the same source.

### About this task

Use the following procedure to configure a project-sourced inventory:

### Procedure

1.  From the navigation panel, select Automation Execution> (and then)Infrastructure> (and then)Inventories.
2.  Select the inventory name you want a source to and click the **Sources** tab.
3.  Click Create source.
4.  In the **Create source** page, select **Sourced from a Project** from the **Source** list.
5.  Enter the following details in the additional fields:

- Optional: **Source control branch/tag/commit**: Enter the SCM branch, tags, commit hashes, arbitrary refs, or revision number (if applicable) from the source control (Git or Subversion) to checkout. This field only displays if the sourced project has the **Allow branch override** option checked. For further information, see [SSCM Types - Configuring playbooks to use Git and Subversion](/documentation/en-us/red_hat_ansible_automation_platform/2.7/develop-ref_projects_manage_playbooks_with_source_control#proc-scm-git-subversion "Configure automation controller projects to synchronize Ansible playbooks directly from Git and Subversion. Integrating with Source Control Management supports collaboration and helps ensure you always deploy the latest automation code.").

![Allow branch override](/webassets/aem/red_hat_ansible_automation_platform/2.7/images/projects-create-scm-project-branch-override-checked.png)

Some commit hashes and refs might not be available unless you also give a custom refspec in the next field. If left blank, the default is HEAD which is the last checked out Branch/Tag/Commit for this project.

- Optional: **Credential**: Specify the credential to use for this source.

- **Project** (required): Pre-populates with a default project, otherwise, specify the project this inventory is using as its source. Click the ![Search](/webassets/aem/red_hat_ansible_automation_platform/2.7/images/search.png) icon to choose from a list of projects. If the list is extensive, use the search to narrow the options.

- **Inventory file** (required): Select an inventory file associated with the sourced project. If not already populated, you can type it into the text field within the menu to filter extraneous file types. In addition to a flat file inventory, you can point to a directory or an inventory script. ![image](/webassets/aem/red_hat_ansible_automation_platform/2.7/images/inventories-create-source-sourced-from-project-filter.png)

6.  Optional: You can specify the verbosity, host filter, enabled variable/value, and update options as described in [Adding a source](/documentation/en-us/red_hat_ansible_automation_platform/2.7/administer-proc_controller_add_source#proc-controller-add-source "Use the following procedure to add a source to an inventory. When you add a source to an inventory, the system creates a new group for that source.").
7.  Optional: To pass to the custom inventory script, you can set environment variables in the **Source variables** field. You can also place inventory scripts in source control and then run it from a project. For more information, see [Inventory File Importing](/documentation/en-us/red_hat_ansible_automation_platform/2.7/administer-assembly_inventory_file_importing#assembly-inventory-file-importing "With automation controller you can select an inventory file from source control, rather than creating one from scratch.").

If you are executing a custom inventory script from SCM, ensure that you set the execution bit (`chmod +x`) for the script in your upstream source control.

If you do not, automation controller throws a `[Error 13] Permission denied` error on execution.


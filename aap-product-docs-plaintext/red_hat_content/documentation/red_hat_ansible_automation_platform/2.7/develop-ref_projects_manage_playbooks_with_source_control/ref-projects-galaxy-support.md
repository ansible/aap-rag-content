# Configure playbooks to use source control management (SCM) systems
## Reuse prebuilt automation by referencing roles

At the end of a project update, automation controller searches for the `requirements.yml` file in the `roles` directory, located at `<project-top-level-directory>/roles/requirements.yml`.

If this file is found, the following command automatically runs:

```
ansible-galaxy role install -r roles/requirements.yml -p <project-specific cache location>/requirements_roles -vvv
```
This file enables you to reference Ansible Galaxy roles or roles within other repositories which can be checked out in conjunction with your own project. The addition of Ansible Galaxy access eliminates the need to create git submodules to achieve this result. Given that SCM projects, along with roles or collections, are pulled into and executed from a private job environment, a `<private job directory>` specific to the project within `/tmp` is created by default.

The cache directory is a subdirectory inside the global projects folder. You can copy the content from the cache location to `<job private directory>/requirements_roles`.

By default, automation controller has a system-wide setting that enables you to dynamically download roles from the `roles/requirements.yml` file for SCM projects. You can turn off this setting in the **Job Settings** screen from the navigation panel Settings> (and then)Automation Execution> (and then)Job, by unchecking the **Enable Role Download** box.

Whenever a project synchronization runs, automation controller determines if the project source and any roles from Galaxy or Collections are out of date with the project. Project updates download the roles inside the update.

If jobs need to pick up a change made to an upstream role, updating the project ensures that this happens. A change to the role means that a new commit was pushed to the *provision-role* source control.

To make this change take effect in a job, you do not have to push a new commit to the *playbooks* repository. You must update the project, which downloads roles to a local cache.

For instance, say you have two git repositories in source control. The first one is *playbooks* and the project in automation controller points to this URL. The second one is *provision-role* and it is referenced by the `roles/requirements.yml` file inside of the *playbooks* git repository.

Jobs download the most recent roles before every job run. Roles and collections are locally cached for performance reasons. You must select **Update revision on launch** in the project **Options** to ensure that the upstream role is re-downloaded before each job run:

![update-on-launch](/webassets/aem/red_hat_ansible_automation_platform/2.7/images/projects-scm-update-options-update-on-launch-checked.png)

The update happens much earlier in the process than the sync, so this identifies errors and details faster and in a more logical location.

If there are any directories that must be specifically exposed, you can specify those in the **Job Settings** screen from the navigation panel Settings> (and then)Automation Execution> (and then)Job, in **Paths to expose to isolated Jobs**. You can also update the following entry in the settings file:

```
AWX_ISOLATION_SHOW_PATHS = ['/list/of/', '/paths']
```


Note:

If your playbooks need to use keys or settings defined in `AWX_ISOLATION_SHOW_PATHS`, you must add `AWX_ISOLATION_SHOW_PATHS` to `/var/lib/awx/.ssh`.

If you made changes in the settings file, be sure to restart services with the `automation-controller-service restart` command after your changes have been saved.

In the UI, you can configure these settings in the **Jobs Settings** window.

![Configure jobs](/webassets/aem/red_hat_ansible_automation_platform/2.7/images/configure-controller-jobs-path-to-expose.png)

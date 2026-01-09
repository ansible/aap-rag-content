# 11. Projects
## 11.5. Collections support




Automation controller supports project-specific Ansible collections in job runs.

If you specify a collections requirements file in the SCM at `collections/requirements.yml` , automation controller installs collections in that file in the implicit project synchronization before a job run.

Automation controller has a system-wide setting that enables collections to be dynamically downloaded from the `collections/requirements.yml` file for SCM projects. You can turn off this setting in the **Job Settings** screen from the navigation panelSettings→Automation Execution→Job, by unchecking the **Enable Collection(s) Download** box.

Roles and collections are locally cached for performance reasons, and you select **Update revision on launch** in the project **Options** to ensure this:

Note
If you also have collections installed in your execution environment, the collections specified in the project’s `requirements.yml` file will take precedence when running a job. This precedence applies regardless of the version of the collection. For example, if the collection specified in `requirements.yml` is older than the collection within the execution environment, the collection specified in `requirements.yml` is used.



